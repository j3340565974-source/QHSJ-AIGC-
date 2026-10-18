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
