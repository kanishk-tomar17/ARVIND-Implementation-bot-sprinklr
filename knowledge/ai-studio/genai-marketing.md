# Sprinklr Marketing Generative AI Use Cases (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-marketing-generative-ai-use-cases/sprinklr-marketing-generative-ai-use-cases/697b71b5c0c0b637f94b19f5

## What it is
- Catalog of generative-AI features built into Sprinklr Marketing to "create better content, faster" — turn ideas into branded copy, adapt it across channels, and surface performance insights.
- Spans three areas: **Content Marketing** (briefs, blogs, emails, SMS, landing pages, press releases), **Ads Reporting** (widget summarization), and **Social Advertising** (ad copy/headlines/carousels).
- Each use case has its own enablement tier (auto / Dynamic Property / DP + extra config) and access-control behavior.

## When to use
- Drafting campaign briefs, personas, key messages, CTAs, hashtags, USPs, tone/voice and visual guidelines inside Campaign and Sub-Campaign Briefs.
- Generating channel content in Advanced Publisher (FSP): blog posts, WordPress, SMS, email/newsletter, landing pages, press releases.
- Localizing a single message for multiple regions/languages (Message Localization).
- Running brand/compliance checks on content before publish (Smart Compliance).
- Writing or rewriting ad copy, headlines, and carousel slides in Ads Manager/Composer/Creative Library.
- Turning an ads reporting widget into plain-language insight (Ads Widget Summarizer).

## Configuration steps
Three enablement tiers — pick based on the use case (see table below):

1. **Auto-enabled with module** — live as soon as the module is on, no extra setup.
   - Applies to: **Improve Writing**, **Message Localization**.
2. **Dynamic Property (DP) required** — turn on a backend DP via Sprinklr Support, then the feature appears.
   - **Smart Compliance:** set `BRAND_COMPLIANCE_ENABLED = true` AND `SMART_COMPLIANCE_ENABLED = true`.
   - **Generate Ad Content / Ad Headline / Ad Carousel Content:** set `_CHAT_GPT_ADS_ACTIONS_ENABLED = True`.
3. **DP + additional configuration** — DP plus extra platform setup; covers most Content Marketing use cases (all blog/SMS/landing-page/email/press-release generators, all Campaign Brief generators, Summarize, Ads Widget Summarizer).

General steps:
1. Confirm the parent module is enabled (Marketing / Advanced Publisher / Ads).
2. For DP-gated features, **contact Sprinklr Support** to set the required Dynamic Property — DPs are backend and cannot be self-served.
3. Manage visibility per feature in **AI+ Studio → Feature Access Management**:
   - Enable/disable toggle per feature.
   - Role-based access control (RBAC) — grant by user role.
4. For the 11 AI-configurable features only, tune behavior in AI configuration: prompt editing, model selection, guardrails, data masking, orchestration pipelines.

### Use-case quick reference
**Content Marketing — Campaign & Sub-Campaign Briefs:**
- Campaign Ideas, Brainstorm Persona, Generate Campaign Brief, Call to Action, Hashtag Recommendations, Key Messages for Campaign, Social Media Post Content, Tone and Voice Guidelines, Unique Selling Propositions, Visual Style Guideline — all DP + extra config; **AI config: Yes**.
- Improve Writing — auto-enabled; AI config: No.
- Summarize — DP + extra config; AI config: No.

**Content Marketing — Advanced Publisher (FSP):**
- Generate Blog Post [Classic], Blog Post [Modern], WordPress Content, SMS [Classic], SMS [Modern], Website Landing Page [Classic], Landing Page [Modern], Email Newsletter Content, Email Content, Press Release Content, Press Release [Modern Template] — DP + extra config; AI config: No.
- Message Localization — auto-enabled; **AI config: Yes**.
- Smart Compliance — DP only (`BRAND_COMPLIANCE_ENABLED=true` + `SMART_COMPLIANCE_ENABLED=true`); AI config: No.

**Ads Reporting:**
- Ads Widget Summarizer — DP + extra config; AI config: No. Turns widgets into plain-language insights.

**Social Advertising (Ads Manager / Composer / Creative Library):**
- Generate Ad Content, Generate Ad Headline, Generate Ad Carousel Content — DP only (`_CHAT_GPT_ADS_ACTIONS_ENABLED=True`); AI config: No.

## Notes & gaps
- **Dynamic Properties are backend** — must be set by Sprinklr Support; consultants cannot toggle them in-app. The DP names/values above are exact from the article.
- **AI configuration (prompts, models, guardrails) is available for only 11 features** — the 10 Campaign-Brief generators plus Message Localization. Everything else is fixed behavior, enable/disable only.
- Nearly all features support **Feature Access Management + RBAC** in AI+ Studio; the article notes a limited set fall outside Feature Access Management but does not enumerate them — verify per-feature in the client's AI+ Studio.
- Watch the **Classic vs Modern editor** split for blogs, SMS, landing pages, and press releases — they are listed as separate use cases and may be gated independently.
- Article is a capability catalog, not a step-by-step build guide — for actual screen-by-screen setup of a given generator, follow up in Advanced Publisher / Campaign Briefs / Ads UI.
- Related GROOT topics: [[ai-studio]], [[feature-access-management]], [[rbac]], [[dynamic-properties]], [[advanced-publisher]], [[campaign-briefs]], [[smart-compliance]], [[message-localization]], [[ads-manager]], [[ai-configuration]]
