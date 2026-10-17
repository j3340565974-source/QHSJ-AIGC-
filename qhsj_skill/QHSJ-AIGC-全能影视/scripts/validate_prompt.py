#!/usr/bin/env python3
"""QHSJ AIGC 全能影视 提示词校验器。

校验结果是辅助诊断，不替代目标模型实测；同一实例重复运行结果保持幂等。
用法：python scripts/validate_prompt.py prompt.txt --type video [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

VALID_TYPES = {"video", "image"}


class PromptValidator:
    VAGUE_WORDS = [
        "高级感", "电影感", "氛围感", "质感", "唯美", "震撼", "精致", "完美",
        "绝美", "好看", "漂亮", "大气", "高端", "奢华", "时尚", "潮流", "经典",
    ]
    EMOTION_WORDS = [
        "开心", "悲伤", "愤怒", "恐惧", "惊讶", "厌恶", "快乐", "难过", "生气",
        "害怕", "紧张", "放松", "激动", "平静", "兴奋", "沮丧", "骄傲", "羞愧",
        "绝望", "痛苦", "焦虑", "冷漠", "委屈", "心虚", "不安",
    ]
    SUBJECT_PATTERNS = [
        r"\b(?:a|an|the)\s+(?:young\s+)?(?:man|woman|person|child|girl|boy|character|robot|creature|soldier|nurse|detective)\b",
        r"(?:一个|一名|一位|人物|主角|男人|女人|男孩|女孩|少年|少女|老人|孩子|机器人|怪物|士兵|护士|侦探|猫|狗|汽车|飞船|城堡|建筑|产品|物体|角色|主体|人物群像)",
        r"(?:他|她|它)(?:的|在|正|缓缓|突然|静静|转身|抬头|低头|走|跑|看|站|坐)",
    ]
    COMPOSITION_WORDS = [
        "大远景", "远景", "全景", "中全景", "中景", "中近景", "近景", "特写", "大特写",
        "构图", "景别", "镜头", "俯拍", "仰拍", "平拍", "鸟瞰", "顶视", "广角", "长焦",
        "wide shot", "medium shot", "close-up", "close up", "overhead", "low angle", "high angle",
    ]
    LIGHTING_WORDS = [
        "光", "影", "亮", "暗", "灯", "阳光", "月光", "烛光", "逆光", "侧光", "轮廓光",
        "柔光", "硬光", "顶光", "霓虹", "窗光", "自然光", "体积光", "曝光", "色温",
        "lighting", "backlight", "rim light", "soft light", "hard light",
    ]
    VISIBLE_CUE_WORDS = [
        "眉", "眼", "瞳孔", "眼神", "嘴角", "嘴唇", "下颌", "咬紧牙", "呼吸", "胸口起伏",
        "肩膀", "手指", "握拳", "掌心", "后退", "退缩", "僵住", "发抖", "颤抖", "流泪",
        "吞咽", "移开视线", "避开目光", "攥紧", "松开", "脊背", "步伐", "踉跄", "停顿",
        "身体前倾", "低头", "抬头", "转身", "沉默", "voice", "breath", "eyes", "jaw", "hands",
    ]
    CONCRETE_DETAIL_WORDS = [
        "颜色", "色温", "纹理", "材质", "毛孔", "布料", "金属", "木纹", "玻璃", "雨滴", "雾气",
        "颗粒", "边缘", "轮廓", "镜头", "焦段", "光线", "阴影", "位置", "背景", "前景", "动作",
        "表面", "反射", "折射", "色彩", "蓝色", "红色", "黑色", "白色", "银色", "金色",
        "具体", "毫米", "mm", "f/", "iso", "fps", "8k", "4k", "16:9", "9:16", "24fps",
    ]

    def __init__(self, prompt: str, prompt_type: str = "video"):
        if prompt_type not in VALID_TYPES:
            raise ValueError(f"不支持的提示词类型 {prompt_type!r}；仅支持 video 或 image")
        self.prompt = prompt if isinstance(prompt, str) else str(prompt)
        self.prompt_type = prompt_type
        self.issues: list[dict[str, str]] = []
        self.warnings: list[dict[str, str]] = []

    def _add(self, level: str, issue_type: str, content: str) -> None:
        target = self.issues if level == "error" else self.warnings
        # 防止单轮校验中同类问题重复堆叠。
        if not any(x["type"] == issue_type and x["content"] == content for x in target):
            target.append({"level": level, "type": issue_type, "content": content})

    def check_blank(self) -> None:
        if not self.prompt.strip():
            self._add("error", "empty_prompt", "提示词为空，无法进行有效生成")

    def check_vague_words(self) -> None:
        found = [word for word in self.VAGUE_WORDS if word in self.prompt]
        if not found:
            return
        has_concrete_details = any(word.lower() in self.prompt.lower() for word in self.CONCRETE_DETAIL_WORDS)
        if has_concrete_details:
            self._add(
                "warning", "vague_word_with_details",
                f"发现概括性审美词（{ '、'.join(found[:8]) }）；提示词已有部分可见细节，建议将审美词逐项落实为颜色、材质、光线、构图或动作，不应仅靠抽象形容词。",
            )
        else:
            self._add(
                "warning", "vague_word",
                f"发现概括性审美词（{ '、'.join(found[:8]) }），但缺少足够的可验证视觉细节；建议补充主体外观、材质纹理、光线方向、构图和动作。",
            )

    def check_emotion_externalization(self) -> None:
        found = [word for word in self.EMOTION_WORDS if word in self.prompt]
        if not found:
            return
        if any(word.lower() in self.prompt.lower() for word in self.VISIBLE_CUE_WORDS):
            return
        self._add(
            "warning", "emotion_may_need_externalization",
            f"检测到情绪词（{ '、'.join(found[:8]) }），但未识别到明确可见表演线索；建议具体写出眉眼、嘴角、呼吸、手部、姿态或动作变化。",
        )

    def check_length(self) -> None:
        length = len(self.prompt.strip())
        min_len = 50 if self.prompt_type == "image" else 100
        if length == 0:
            return
        if length < min_len:
            self._add("warning", "too_short", f"{ '图片' if self.prompt_type == 'image' else '视频' }提示词为 {length} 字符，低于建议参考值 {min_len}；短提示词不一定错误，请按任务复杂度判断。")

    def check_has_subject(self) -> None:
        if not self.prompt.strip():
            return
        lower = self.prompt.lower()
        if not any(re.search(pattern, lower, flags=re.IGNORECASE) for pattern in self.SUBJECT_PATTERNS):
            self._add("warning", "subject_not_obvious", "未识别到常见主体表达。若提示词描述的是抽象图形、环境、纹理或纯场景，此项可忽略；否则建议明确主体、数量及其位置。")

    def check_composition(self) -> None:
        if not self.prompt.strip():
            return
        lower = self.prompt.lower()
        if not any(word.lower() in lower for word in self.COMPOSITION_WORDS):
            self._add("warning", "no_composition", "未识别到常见景别、构图或机位词；复杂画面建议注明主体位置、景别、视角和画面比例。")

    def check_lighting(self) -> None:
        if not self.prompt.strip():
            return
        lower = self.prompt.lower()
        if not any(word.lower() in lower for word in self.LIGHTING_WORDS):
            self._add("warning", "no_lighting", "未识别到常见光线描述；需要控制写实度或情绪时，建议注明光源、方向、软硬度、色温和阴影。")

    def run_all_checks(self) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
        # 幂等：重复调用不累积旧结果。
        self.issues = []
        self.warnings = []
        self.check_blank()
        self.check_vague_words()
        self.check_emotion_externalization()
        self.check_length()
        self.check_has_subject()
        self.check_composition()
        self.check_lighting()
        return self.issues, self.warnings

    def result(self) -> dict[str, Any]:
        issues, warnings = self.run_all_checks()
        return {
            "validator": "QHSJ AIGC 全能影视 PromptValidator",
            "prompt_type": self.prompt_type,
            "character_count": len(self.prompt),
            "passed": not issues,
            "error_count": len(issues),
            "warning_count": len(warnings),
            "issues": issues,
            "warnings": warnings,
            "disclaimer": "规则校验仅提供静态提示，不保证特定模型生成结果；应结合目标平台实测和人工审片。",
        }

    def report(self) -> str:
        result = self.result()
        lines = ["=" * 54, "QHSJ AIGC 全能影视 提示词校验报告", "=" * 54]
        lines.append(f"提示词类型：{result['prompt_type']}")
        lines.append(f"总字符数：{result['character_count']}")
        lines.append(f"\n错误（{result['error_count']}项）：")
        if result["issues"]:
            lines.extend(f"  {i}. [{item['type']}] {item['content']}" for i, item in enumerate(result["issues"], 1))
        else:
            lines.append("  无")
        lines.append(f"\n警告（{result['warning_count']}项）：")
        if result["warnings"]:
            lines.extend(f"  {i}. [{item['type']}] {item['content']}" for i, item in enumerate(result["warnings"], 1))
        else:
            lines.append("  无")
        lines.append("\n" + result["disclaimer"])
        lines.append("校验状态：" + ("通过（警告项请按任务需要判断）" if result["passed"] else "未通过，请修复错误项"))
        lines.append("=" * 54)
        return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="QHSJ AIGC 全能影视 提示词质量检查")
    parser.add_argument("file", help="UTF-8 提示词文件路径")
    parser.add_argument("--type", choices=sorted(VALID_TYPES), default="video", help="提示词类型：video/image，默认 video")
    parser.add_argument("--json", action="store_true", help="输出机器可读 JSON")
    parser.add_argument("--strict", action="store_true", help="严格模式：存在错误返回非零；警告不导致失败")
    args = parser.parse_args(argv)
    path = Path(args.file)
    try:
        prompt = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"错误：文件不存在：{path}", file=sys.stderr)
        return 2
    except (OSError, UnicodeError) as exc:
        print(f"错误：无法读取提示词文件：{exc}", file=sys.stderr)
        return 2
    try:
        validator = PromptValidator(prompt, args.type)
    except ValueError as exc:
        print(f"参数错误：{exc}", file=sys.stderr)
        return 2
    result = validator.result()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        # report() is deterministic, but uses the same idempotent check pipeline.
        print(validator.report())
    return 1 if args.strict and result["error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
