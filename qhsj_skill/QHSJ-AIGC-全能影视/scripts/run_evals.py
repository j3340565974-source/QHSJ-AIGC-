#!/usr/bin/env python3
"""运行自然语言路由回归测试集。"""
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROUTER_PATH=ROOT/"scripts"/"route_request.py"
CASES_PATH=ROOT/"evals"/"routing-cases.json"

def load_router():
    spec=importlib.util.spec_from_file_location("qhsj_route_request",ROUTER_PATH)
    if spec is None or spec.loader is None: raise RuntimeError("无法加载路由模块")
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def main():
    p=argparse.ArgumentParser(description="QHSJ AIGC 全能影视 路由回归测试")
    p.add_argument("--json",action="store_true")
    p.add_argument("--case",help="只运行指定 case ID")
    args=p.parse_args()
    try:
        cases=json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
        if args.case: cases=[x for x in cases if x.get("id")==args.case]
        if not cases: raise ValueError("没有匹配到测试用例")
        router=load_router()
    except Exception as exc:
        print(f"初始化失败：{exc}",file=sys.stderr); return 2
    results=[]
    for case in cases:
        try:
            result=router.route(case["request"])
            caps={x["id"] for x in result["selected_capabilities"]}
            wfs={x["id"] for x in result["workflows"]}
            missing_caps=sorted(set(case.get("must_include_capabilities",[]))-caps)
            excluded_caps=sorted(set(case.get("must_exclude_capabilities",[]))&caps)
            missing_wfs=sorted(set(case.get("must_include_workflows",[]))-wfs)
            excluded_wfs=sorted(set(case.get("must_exclude_workflows",[]))&wfs)
            passed=not (missing_caps or excluded_caps or missing_wfs or excluded_wfs)
            results.append({"id":case["id"],"passed":passed,"request":case["request"],"missing_capabilities":missing_caps,"unexpected_capabilities":excluded_caps,"missing_workflows":missing_wfs,"unexpected_workflows":excluded_wfs,"selected_capabilities":sorted(caps),"selected_workflows":sorted(wfs)})
        except Exception as exc:
            results.append({"id":case.get("id","<unknown>"),"passed":False,"error":str(exc)})
    report={"suite":"QHSJ AIGC 全能影视 route regression","total":len(results),"passed":sum(1 for x in results if x["passed"]),"failed":sum(1 for x in results if not x["passed"]),"results":results}
    if args.json: print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(f"路由测试：{report['passed']}/{report['total']} 通过，{report['failed']} 失败")
        for r in results:
            if not r["passed"]: print(f"\n[FAIL] {r['id']}：{r.get('request','')}\n  缺失能力：{r.get('missing_capabilities',[])}\n  意外能力：{r.get('unexpected_capabilities',[])}\n  缺失工作流：{r.get('missing_workflows',[])}\n  意外工作流：{r.get('unexpected_workflows',[])}\n  异常：{r.get('error','')}")
    return 0 if report["failed"]==0 else 1
if __name__=="__main__": raise SystemExit(main())
