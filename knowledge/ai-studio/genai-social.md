# Sprinklr Social Generative AI Use Cases (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-social-generative-ai-use-cases/sprinklr-social-generative-ai-use-cases/697b71f6c0c0b637f94b1f35

## What it is
- A capability matrix of generative-AI features baked into Sprinklr Social, mapped module by module.
- Covers image generation/editing, content drafting, and AI summarization to help teams produce engaging content and digest large volumes faster.
- The article is a reference table, not a step-by-step guide — most setup is done by Sprinklr Support via Dynamic Properties (DPs), then governed by RBAC.

## When to use
- Editing/generating image assets in Asset Management (variations, generative fill, background remove/replace).
- Summarizing high-volume social comments in Engagement.
- Drafting platform-specific content in Publisher (captions, threads, carousels, reels, thumbnails, alt text) across Facebook, Instagram, LinkedIn, TikTok, X, etc.
- Auto-summarizing analytics widgets in Social Reporting.

## Configuration steps
Capabilities and how each is turned on, by module:

1. **Asset Management** (image gen/edit)
   - Features: Generate Image Variation, Generative Fill, Background Remove, Background Replace.
   - Enablement: **DP configuration required** — `GENERATIVE_AI_ACTIONS_ENABLED_PRODUCTS=True` and `IMAGE_EDITOR_V2`.
   - Appears in: Media Uploader, Image Editor (V2), Visual Brief.
   - Governance: Enable/disable + RBAC supported via Feature Access Management in AI+ Studio.

2. **Engagement** (comment summarization)
   - Feature: Comment Summarizer (digests large volumes of social comments).
   - Enablement: **Auto-enabled with the module** — no extra config.
   - Appears in: Engagement Dashboards.
   - Governance: Enable/disable + RBAC supported.

3. **Publisher** (content generation)
   - Features: generate captions, thumbnails, carousel posts, reels, threads, image alt text, and more (≈9 features) across the supported channels.
   - Enablement: **DP + additional configuration required.**
   - AI Configuration support: **Yes** — supports advanced AI config (prompt editing, model selection, guardrails).
   - Governance: Enable/disable + RBAC supported via Feature Access Management.

4. **Social Reporting** (widget summarization)
   - Feature: Social Widget Summarizer (auto-insights on dashboard widgets).
   - Enablement: **DP + additional configuration required.**
   - Governance: Enable/disable + RBAC supported.

5. **Turn features on/off and scope by role** in AI+ Studio → Feature Access Management (applies to all modules that say "RBAC supported").

## Notes & gaps
- This Help article is a capability/enablement matrix, not a procedure — it deliberately has no numbered UI walkthroughs. For the actual DP setup, the article says to **contact Sprinklr Support**.
- DPs are partition-level toggles set by Sprinklr; consultants cannot set them in-product.
- Asset Management image features require the V2 image editor (`IMAGE_EDITOR_V2`) — older partitions on the legacy editor won't show them.
- Publisher is the only module flagged with AI Configuration support (editable prompts, model choice, guardrails); the others are on/off + RBAC only.
- Per-feature access is governed via Feature Access Management — see [[feature-access-management]] and [[rbac]].
- Related ARVIND topics: [[ai-studio]], [[ai-plus-studio]], [[image-editor]], [[publisher]], [[engagement-dashboards]], [[social-reporting]], [[dynamic-properties]].
