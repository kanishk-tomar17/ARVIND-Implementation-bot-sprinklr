# Sprinklr Specialised AI Insights Features (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-insights-specialized-ai-use-cases/sprinklr-specialised-ai-insights-features/69415ad02727657ea200140d

## What it is
- A set of advanced AI/ML + NLP capabilities baked into Sprinklr Insights that surface deep, actionable signals from large volumes of customer and social data.
- Auto-detects patterns, sentiment shifts, emerging themes, and brand-health metrics across text and visual content.
- Grouped into three use-case categories: Competitive Insights & Benchmarking, Social Listening, and Visual Insights.

## When to use
- Comparing your performance vs. competitors in real time (engagement, sentiment, share of voice) → Competitive Insights & Benchmarking.
- Tracking what people say about your brand, competitors, industry, or topics across social/digital → Social Listening.
- Analysing images, video, memes, and infographics (not just text) for brand mentions, safety, and context → Visual Insights.

## Configuration steps
This article is a feature catalogue, not a setup walkthrough — it lists capabilities and their enablement status rather than click-by-click config. Concrete points it does give:

1. Most features are **enabled by default** with **no role-based access control (RBAC) restrictions**.
2. Competitive Insights features surface automatically on **Benchmarking Dashboards**.
3. Capabilities by category:
   - **Competitive Insights & Benchmarking:** Sentiment Detection; Emotion analysis; Spam detection; Paid Post Detection; Global Insights Category Dimension.
   - **Social Listening:** Entity Operator; Smart Theme Explorer; Influencer Score; Intuition Moderation; Global Category Dimensions; Brand Reputation Dimensions; Sentiment Detection; Emotion detection; Spam filtering.
   - **Visual Insights:** Logo Detection; Image/Video Similarity Search; NSFW Detection; OCR (Optical Character Recognition); Object Detection; Activities Detection; Scene Detection; Age Detection; Gender Detection; Visual Sentiment Detection.
4. To use a given dimension/operator, add it as a column/filter/dimension on the relevant Insights or Benchmarking dashboard widget (per-feature setup is documented in that feature's own KB article, not here).

## Notes & gaps
- Article is thin on step-by-step config, prerequisites, and limits — it documents *what exists* and *default enablement*, not *how to turn each on*. Treat per-feature KB articles as the source for actual setup.
- "Enabled by default, no RBAC" applies to the Benchmarking set; confirm in-environment before assuming a feature is live for the client.
- Visual Insights features (age/gender/scene/activity detection) are inference-based — flag accuracy caveats to clients before relying on them for decisions.
- Related GROOT topics: [[sentiment-detection]], [[emotion-analysis]], [[smart-theme-explorer]], [[entity-operator]], [[influencer-score]], [[intuition-moderation]], [[visual-insights]], [[benchmarking-dashboards]], [[social-listening]], [[custom-fields]].
