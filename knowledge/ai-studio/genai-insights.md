# Sprinklr Insights Generative AI Use Cases (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-insights-generative-ai-use-cases/sprinklr-insights-generative-ai-use-cases/697b71e1c0c0b637f94b1e26

## What it is
- Generative AI features built into Sprinklr Insights that let users explore data, surface patterns, summarize key points, and organize themes — no advanced technical skill needed.
- Spans two Insights modules: **Social Listening** (track online conversations, opinions, trends) and **Customer Feedback Management / CFM** (AI-driven survey analysis).

## When to use
- You need to summarize a large message stream or a single message fast instead of reading everything manually.
- You want auto-generated themes, keyword lists, hashtag/phrase suggestions, or AI-assisted query building (brand, custom, story) when setting up Listening.
- You're running surveys and want AI to surface insights, validate hypotheses, check survey quality, or analyze open-text answers.

## Configuration steps
Features fall into three enablement tiers — check which tier a feature is in before expecting it to appear:

1. **Auto-enabled** — works immediately once the module is on; no extra setup. Covers most Listening features (Summarize Message Stream, Summarize Message, Widget Summarizer, Alert Summarizer, Generate Themes, Create Keyword Lists, Generate Hashtag/Phrase Suggestions, Create Brand Query, Create Custom Query) and all CFM features.
2. **DP configuration required** — needs a Dynamic Property set after the module is enabled.
   - Create Story Query requires DP `_LST_STORY_ENABLED_`.
3. **DP + additional configuration required** — needs the DP plus extra setup.

To manage access:
4. Go to **Feature Access Management in AI+ Studio** to toggle features and (where supported) apply RBAC.
   - **Enable/disable + RBAC supported** — full on/off plus role-based restriction. Applies to the Listening features above.
   - **Enable/disable only** — toggle on/off, no RBAC. Applies to all CFM features (Survey Insights, Survey Hypothesis Validation, Survey Quality, Survey Text Analytics).
   - **Not in Feature Access Management** — cannot be managed here (Widget Summarizer, Alert Summarizer).
5. For features marked "AI Configuration: Yes" (Summarize Message, Generate Themes, Create Keyword Lists, Create Brand Query, Create Custom Query), an additional AI config step applies.
6. For any DP configuration or additional setup, **contact Sprinklr Support** (tickets@sprinklr.com).

Where each feature lives:
- Listening summarizers/themes/queries: Listening & Benchmarking Dashboards, Theme Record Manager, Keyword/Topic List creation, Topic/Story Query creation, Alert Record Manager.
- CFM features: Survey Analytics Feed, Survey Builder, Text Questions.

## Notes & gaps
- Article is a feature/availability matrix, not a step-by-step setup guide — it lists *where* features appear and *how* they're gated, not detailed click paths. Detailed per-feature config steps are not in this article.
- DP setup (e.g. `_LST_STORY_ENABLED_`) is not self-serve; route through Sprinklr Support.
- The article does not specify granular user permissions beyond RBAC, dataset size limits, or performance caveats.
- Related GROOT topics: [[custom-fields]], [[rule-engine]], [[intents]]
