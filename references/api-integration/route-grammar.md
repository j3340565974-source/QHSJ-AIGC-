# Natural-language capability routing grammar

The router uses four layers of evidence:

1. explicit deliverable words;
2. semantic capability phrases;
3. implicit dependency signals;
4. tool/target hints.

A capability may be activated by one strong explicit signal or by multiple weaker signals. Co-occurrence matters: “原创 + 巨物 + 正视图 + 生物 + 提示词” activates a compound route rather than four independent single-output routes.

## Dependency examples
`creature_design → giant_scale(optional) → front_view(optional) → composition → image_prompt → model_compile(optional) → visual_qa`.

`reference_image → reverse_engineering → identity_lock → multi_view → image_prompt`.

`novel → adaptation → short_drama → screenplay → storyboard → prompt_ir`.

`video_edit → editorial → pacing → audio → platform_adaptation(optional) → qa`.

## Router invariants
Hard constraints are copied into every downstream node that depends on them. Soft preferences may be compressed. Target model names do not determine the creative task; they only select the compiler.
