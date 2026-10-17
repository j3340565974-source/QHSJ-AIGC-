# Compatibility matrix and packaging rules

## Open Agent Skills
The current open specification requires YAML frontmatter in `SKILL.md`; `name` is lowercase letters/numbers/hyphens, max 64 chars, and must match the parent directory. `description` is required and max 1024 chars. Long references belong in separate files because the agent loads them progressively. See https://agentskills.io/specification.

## ByteDance / Volcengine Skill hosts
Verified current Volcengine documentation requires a single root folder whose name matches the Skill name, `SKILL.md` at that root, and a lowercase/digit/hyphen `name` of at most 64 characters. Some Volcengine upload surfaces also impose package-size limits; use the smallest package that preserves required references. Do not use a display name containing spaces as the technical `name`.

## Coze / 扣子
Current Coze documentation accepts `.skill` or `.zip` uploads and recommends a standard Skill package containing `SKILL.md`, scripts and references. Coze may repackage non-standard uploads, but the packaged form below already follows the open standard.

## Qwen / Alibaba Agent platforms
Current Qwen documentation supports custom Skill ZIP packages with `SKILL.md` at the package root and a 10 MiB package limit on the referenced platform. The same progressive-disclosure package is designed to fit this constraint.

## Bothub
Bothub's public site currently describes itself as a discovery/verification/registry and launch layer for AI agents, tools and autonomous systems. It exposes agent directory and submission/launch concepts, but the public material found during this build does not document a native `SKILL.md` upload/runtime contract. Therefore this package must not claim that Bothub can directly install and execute an Agent Skill. Treat Bothub integration as an agent/tool listing or external-runtime integration until an official Bothub Skill API/spec is provided.
