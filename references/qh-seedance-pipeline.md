# QHSJ Seedance 全流程管线

# Seedance 2.0 — Pipeline Skill

**Version:** 6.7.0  
**Model:** Seedance 2.0  
**Scope:** Workflow operations, API integration, surfaces, post-production, batch workflow

---

## When to Use This Skill

- User asks about **Seedance 2.0 workflow** or **production pipeline**
- User wants **API integration** guidance (BytePlus, Volcengine, Runway, providers)
- User asks about **web surfaces** (Dreamina, Jimeng, Doubao)
- User needs **post-production** workflow (editing, stitching, color, audio)
- User asks about **batch generation** or **sequence automation**
- User wants **professional delivery** standards (film, commercial, agency)
- User asks about **first/last-frame workflows** or **I2V chaining**
- User mentions **ComfyUI, nodes, or community workflows**

---

## Intent

Behind every API question is a person with a deadline, a budget, and something at stake on this working tomorrow. Reliability is the kindness this user needs. Answer with dates, sources, and a working path — not optimism.

---

## Workflow Categories

### 1. Web Workflow (Consumer/Creator)

**Surfaces:**
- **Dreamina** (China, Chinese language, consumer-focused)
- **Jimeng** (China, Chinese language, integrated with Douyin ecosystem)
- **Doubao** (China, Chinese language, ByteDance AI assistant with video capabilities)

**Typical flow:**
1. Log in to web surface
2. Upload reference images (optional)
3. Write prompt (Chinese or English depending on surface)
4. Select generation settings (duration, aspect ratio)
5. Generate
6. Review output
7. Download or continue editing

**Limitations:**
- No API access from web surfaces
- Batch generation manual
- No programmatic workflow control
- Output resolution and format determined by platform

**Best for:** Individual creators, testing prompts, quick iterations, visual exploration

---

### 2. API Workflow (Professional/Scale)

**Official API providers:**

#### BytePlus ModelArk
- **Status:** Production, official ByteDance API
- **Access:** Requires business account, API key
- **Model name:** Check current documentation for exact model identifier
- **Documentation:** https://www.byteplus.com/

#### Volcengine (火山引擎)
- **Status:** Production, China-focused
- **Access:** Requires account, API key
- **Region:** Primarily serves China market
- **Documentation:** https://www.volcengine.com/

#### Runway (Seedance 2.0 integration)
- **Status:** Available through Runway API
- **Model name:** `seedance2`
- **File upload:** Uses `runway://` URI scheme
- **Audio reference:** Supported via combination rules
- **Documentation:** Check Runway API docs for current status

**Third-party providers/routers** (label as provider-specific, verify before guidance):
- EvoLink, OpenRouter, Kie.ai, PiAPI, LaoZhang, Runware, ModelsLab, AI/ML API, MuAPI, SeeGen, Segmind
- **Status:** Must be verified per-provider
- **Risk:** Provider uptime, pricing, and feature support varies
- **Documentation:** Check provider-owned documentation

**Typical API flow:**
1. Authenticate (API key, token)
2. Upload assets (images, audio references) → receive asset IDs
3. Create generation task (prompt + settings + asset IDs)
4. Poll task status or use webhook
5. Retrieve output URL when task completes
6. Download and store final video
7. Track usage/cost via task ledger

**Best for:** Batch generation, automation, custom workflows, integration with existing tools

---

### 3. Professional Production Workflow

**Phases:**

#### Pre-Production
1. **Treatment:** Story overview, visual direction, reference mood boards
2. **Shot list:** Scene-by-scene breakdown with camera, lighting, action notes
3. **Continuity ledger:** Character wardrobe, props, environment consistency tracking
4. **Reference rights map:** Which reference images cleared for use, which need rewrites

#### Production
1. **Prompt batch creation:** Write all prompts following continuity ledger
2. **Generation:** Execute via API or web surface
3. **Review loop:** QC each clip, accept/reject/revise
4. **Task tracking:** Log generation attempts, costs, accepted takes

#### Post-Production
1. **Edit:** Sequence accepted clips in timeline
2. **Conform:** Match resolution, frame rate, color space
3. **Stitching:** Join clips seamlessly (crossfade, match-cut, or hard cut)
4. **Stabilization:** Fix camera shake if needed (avoid over-stabilizing intentional handheld)
5. **Audio cleanup:** Remove artifacts, balance levels, add music/SFX
6. **Captions/Subtitles:** Add localized text if needed
7. **Color:** Grade for consistency across clips, match lighting continuity
8. **Localization:** Create alternate audio tracks, subtitle files
9. **Versioning:** Export textless version (for future localization), aspect ratio variants
10. **Delivery/QC:** Final check against delivery specs (resolution, codec, frame rate, audio format)

**Best for:** Commercial work, agency projects, client deliverables, film production

---

### 4. Post-Production Details

**Common operations:**

#### Video Stitching
- **Tool:** FFmpeg, DaVinci Resolve, Premiere Pro, Final Cut Pro
- **Method:** Concatenate clips, add transitions (cut, crossfade, match-cut)
- **Caution:** Match frame rate, resolution, color space before stitching
- **Tip:** Export intermediate clips at high quality (ProRes, DNxHD) before final stitch

#### Stabilization
- **Tool:** DaVinci Resolve (built-in stabilizer), After Effects (Warp Stabilizer)
- **When:** Camera shake unintentional, clip needs smoothing
- **When NOT:** Intentional handheld aesthetic, documentary feel
- **Caution:** Over-stabilization creates "floating" feel

#### Audio Cleanup
- **Tool:** Audacity, Adobe Audition, Fairlight (in Resolve)
- **Operations:** Remove background hum, normalize levels, EQ, compression
- **Caution:** Don't over-process — some ambient sound feels natural

#### Color Grading
- **Tool:** DaVinci Resolve (industry standard), Premiere Pro (Lumetri)
- **Goal:** Match lighting continuity across clips from same scene
- **Method:** Balance exposure, white balance, saturation, contrast
- **Tip:** Use reference frames from accepted clips to match look

#### Captions and Subtitles
- **Format:** SRT, VTT, burnt-in text
- **Tool:** Subtitle Edit, Aegisub, Adobe Premiere
- **Localization:** Translate captions for target markets

---

### 5. First/Last-Frame Workflow (I2V Chaining)

**Use case:** Multi-clip sequence with continuity

**Method:**
1. Generate **Clip 1** (T2V from prompt)
2. Extract **final frame** of Clip 1
3. Use final frame as **seed image** for **Clip 2** (I2V)
4. Write **Clip 2 prompt** describing:
   - Starting state (matching final frame of Clip 1)
   - Action that happens in Clip 2
   - Ending state
5. Generate Clip 2 (I2V)
6. Repeat for Clip 3, 4, etc.

**Extension depth tracking:**
- **Depth 0:** Clip from canonical reference (T2V)
- **Depth 1:** Clip from previous clip's frame (I2V)
- **Depth 2:** Clip from depth-1 clip's frame (I2V from I2V)
- **Max safe depth:** 2 (hard ceiling: 3)
- **Re-anchor rule:** At max depth, return to canonical reference (T2V) to prevent drift

**Best for:** Story sequences, continuity-heavy work, character consistency

---

### 6. China-Facing Workflow

**Official sources to prefer:**
- ByteDance official announcements
- Volcengine/BytePlus documentation
- Doubao product pages
- Jimeng/Dreamina help centers
- Jianying (剪映) official guides

**Caution:**
- Workflow hosts, Chinese-language blogs, and business-partner news are **not public API providers** without provider-owned documentation
- Verify API endpoints and authentication methods from official sources
- Don't assume feature parity between China-facing and international surfaces

**Best for:** Users in China, Chinese-language projects, Douyin/TikTok integration

---

### 7. Community Workflow (ComfyUI, Unofficial Nodes)

**Status:** Community/unverified unless officially documented

**Use case:** Custom workflows, experimental features, research

**Caution:**
- ComfyUI nodes for Seedance 2.0 are **community-created**, not official
- May break with model updates
- May not match official API behavior
- **Label clearly:** "This is a community workflow, not officially supported"

**When to recommend:**
- User explicitly asks for ComfyUI
- User is comfortable with experimental tools
- Official API doesn't support user's specific workflow need

**Best for:** Advanced users, researchers, custom pipeline builders

---

### 8. Batch Workflow and Automation

**Goal:** Generate multiple clips from shot list with minimal manual intervention

**Approach:**

1. **Shot list preparation:**
   - Create CSV or JSON with: `clip_id`, `prompt`, `duration`, `aspect_ratio`, `reference_image_path`

2. **Script setup:**
   - Python script with API client (BytePlus, Volcengine, Runway)
   - Loop through shot list
   - For each clip:
     - Upload reference image (if any) → get asset ID
     - Create generation task with prompt + settings + asset ID
     - Store task ID in ledger

3. **Polling/webhook:**
   - Poll task status every 30-60 seconds, or
   - Set up webhook to receive completion notifications

4. **Download and organize:**
   - When task completes, download video
   - Save to organized directory: `outputs/{scene_id}/{clip_id}.mp4`
   - Log generation metadata (cost, duration, iterations)

5. **QC and iteration:**
   - Review all clips
   - Regenerate failed/rejected clips
   - Track accepted takes

**Best for:** Multi-clip projects, sequences, automation pipelines

---

## Status and Documentation Rules

**Always verify current status:**
- API availability changes
- Model names/IDs change
- Features are added/deprecated
- Pricing structures change

**Before giving API guidance:**
1. State your knowledge cutoff date (May 2025)
2. Direct user to official documentation for current status
3. Provide general workflow structure (upload → task → poll → retrieve)
4. Warn about specific fields/endpoints that may have changed

**Example response:**

"As of my knowledge cutoff (May 2025), Seedance 2.0 was available via BytePlus ModelArk and Runway APIs. The general workflow is: authenticate → upload assets → create task → poll status → retrieve output. However, API endpoints, model names, and pricing may have changed. Check the official BytePlus documentation at https://www.byteplus.com/ for current API details."

---

## Professional Delivery Standards

When user asks for **professional delivery** or **client-ready output:**

**Minimum standards:**
- **Resolution:** 1920×1080 or higher (1080p minimum, 4K preferred for commercial)
- **Frame rate:** 24fps (film), 25fps (PAL), 30fps (NTSC), 60fps (social/action)
- **Codec:** H.264 or H.265 for delivery, ProRes/DNxHD for archival
- **Audio:** 48kHz, 16-bit minimum (24-bit preferred), stereo or 5.1
- **Color space:** Rec.709 for web/broadcast, DCI-P3 for cinema
- **Captions:** SRT or burnt-in, localized if needed
- **Textless version:** Provided for future localization
- **Aspect ratio variants:** 16:9, 9:16, 1:1 as needed

**QC checklist:**
- No visible artifacts (flickering, banding, compression)
- Audio sync accurate
- Color consistent across clips
- Captions timed correctly
- Logo/branding present and correct
- Legal/compliance checks passed (music rights, talent releases)

**Best for:** Agency work, client deliverables, broadcast, cinema

---

## Output Contract

When responding to pipeline questions, return:

1. **Workflow path** (web, API, professional production, post, batch)
2. **Source status** (production, community, unverified)
3. **Required inputs** (API key, prompts, reference images)
4. **Production phase** (pre, production, post, delivery)
5. **Validation steps** (QC, review, delivery check)
6. **Delivery assumptions** (resolution, codec, frame rate)
7. **Risks** (API changes, provider uptime, drift in I2V chains)
8. **Next artifact to create** (shot list, prompt batch, review packet, QC preflight)

---

## Anti-Patterns

❌ **Claiming API availability without verification**  
→ State knowledge cutoff, direct to official docs

❌ **Recommending provider-specific workflows as official**  
→ Label clearly: "This is via third-party provider X, not official ByteDance API"

❌ **Ignoring professional delivery standards**  
→ For client work, specify resolution, codec, audio, QC checklist

❌ **Over-promising batch automation without error handling**  
→ Include polling, retry logic, failure tracking

❌ **Treating community workflows as production-ready**  
→ Label as experimental, warn about lack of official support

---

## Summary

**Pipeline workflow:**
1. Identify user's workflow type (web, API, professional, post, batch, community)
2. Verify status of APIs/surfaces (state knowledge cutoff, link to docs)
3. Provide general workflow structure
4. Include validation and QC steps for professional work
5. Warn about risks (API changes, drift, provider uptime)
6. Deliver next actionable artifact (shot list, script, QC checklist)

**Key principle:** Reliability is kindness — answer with dates, sources, and a working path.

---

**Related skills:** seedance-sequence, seedance-continuation, seedance-prompt
