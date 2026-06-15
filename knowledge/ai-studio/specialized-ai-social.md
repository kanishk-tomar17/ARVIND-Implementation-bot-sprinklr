# Sprinklr Specialised AI Social Features (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-social-specialized-ai-use-cases/sprinklr-specialised-ai-social-features/694159da041df6338a03343e

## What it is
- A catalogue of AI features baked into Sprinklr Social (publishing, engagement, DAM, advocacy) for smarter, faster, more personalised engagement at scale.
- Mostly out-of-the-box AI helpers — sentiment, moderation, asset intelligence, compliance — not standalone AI+ Studio models. Only Thumbnail Generation is an AI+ Studio feature.

## When to use
- You need to know whether a given AI Social feature is on by default or must be requested.
- You're enabling asset intelligence (smart tags, contextual search, duplicate detection) and need to know the RBAC/role requirement.
- You're turning on compliance or moderation helpers in engagement/publishing and a consultant asks where it shows up.

## Configuration steps
Enablement depends on the feature. Two patterns:

1. **Enabled by Default** — already live, no setup needed. Covers:
   - Sentiment Detection / Sentiment Analysis (Advocacy + Engagement Dashboards)
   - Intuition Moderation (Engagement Dashboards)
   - Smart Approvals

2. **On Request** — raise with Sprinklr to enable, then surfaces in the noted screen:
   - **Contextual Search** — requires Data Platform (DP) role. Shows in Social → DAM, "All Assets".
   - **Duplicate / Similar Asset Detection** — requires DP role. Shows in the asset third pane.
   - **Smart Image Tags** — requires DP role. Shows in Social → DAM, "All Assets".
   - **Media OCR Compliance** — no RBAC noted. Shows in Engagement Dashboards.
   - **Smart Response Compliance** — enable via Publishing → Outbound Execution. Shows in the reply publisher.
   - **Thumbnail Generation** — enable via Publishing → Outbound message. Shows in Social → Quick Publisher. This is the only AI+ Studio feature in the set.

## Notes & gaps
- This article is a feature matrix, not a step-by-step config guide — for any single feature's detailed setup, follow its own KB article / [[ai-studio]] flow.
- **Data Platform (DP) role** is the gating permission for the three DAM asset features (contextual search, duplicate detection, smart image tags).
- Almost all features are **not** available in AI+ Studio; Thumbnail Generation is the exception.
- "On Request" = needs Sprinklr-side enablement; "By Default" = already on.
- Related GROOT topics: [[sentiment-analysis]], [[dam]], [[smart-image-tags]], [[intuition-moderation]], [[smart-approvals]], [[custom-fields]], [[rule-engine]].
