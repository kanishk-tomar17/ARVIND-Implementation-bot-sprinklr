# Sprinklr Specialised AI Features for Marketing (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-marketing-specialized-ai-use-cases/sprinklr-specialised-ai-features-for-marketing/69415930041df6338a0326d1

## What it is
- A bundle of generative + predictive AI capabilities for marketing teams, spanning ads publishing, content marketing, and ads management.
- Goal: build better campaigns — analyse audience sentiment, spot trends, optimise content/spend across social, digital and paid, auto-generate ad copy, forecast performance, and personalise at scale while keeping brand consistency.

## When to use
- Running paid campaigns and you want the platform to optimise budget, bids, and ad rotation automatically rather than tuning by hand.
- Managing a large asset library and need auto-tagging, deduplication, compliance checks, or semantic search to find assets fast.
- You want early warning on campaign performance swings (anomaly detection) instead of manually watching dashboards.

## Configuration steps
1. Confirm access first: all features need RBAC at **Paid > Strategy Group** level or higher.
2. **Ads Publishing features** — appear in Ads Manager / Ads Composer:
   - Smart Budget Allocation — on by default; allocates budget across the campaign.
   - Smart Bidding — on by default; optimises bidding across channels.
   - Smart Ad Rotation — on by default; manages which ads serve.
   - Performance Insights — **enabled on request**; analytics surface in the Creative Management App.
3. **Content Marketing features** — for the asset library:
   - Smart Image Tags — auto-tags images.
   - Duplicate and Similar Asset Detection — flags redundant assets.
   - Smart Compliance — checks regulatory adherence.
   - Contextual Search — semantic asset discovery.
4. **Ads Manager features**:
   - Anomaly Detection — on by default; flags unusual patterns in campaign performance data.

## Notes & gaps
- The published article is high-level: it lists the features and their default/on-request state but does NOT give per-feature step-by-step setup, options, or limitations. Treat the above as a feature map, not a config runbook.
- Default-on features: Smart Budget Allocation, Smart Bidding, Smart Ad Rotation, Anomaly Detection.
- On-request feature: Performance Insights (raise with Sprinklr to enable; surfaces in Creative Management App).
- All gated by RBAC at Paid > Strategy Group or higher — check the consultant's role before troubleshooting "feature missing" reports.
- For deeper setup of individual capabilities, re-fetch / cross-check against the specific Ads Manager and Creative Management App KB articles.
- Related ARVIND topics: [[ads-manager]], [[creative-management-app]], [[rbac]], [[custom-fields]], [[ai-studio-overview]]
