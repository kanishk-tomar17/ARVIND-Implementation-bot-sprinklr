# Facebook — Reporting Glossary & Metrics (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- The full reference for every Facebook metric and dimension Sprinklr can report on, plus how often that data refreshes, how far back it backfills, and which metrics Meta is deprecating.
- Facebook reporting is built on **six building blocks**: account-level metrics, post-level metrics, cross-post metrics, non-cross-post metrics, Reels metrics, and dimensions.
- **Metrics** are quantitative (counts, reach, views, earnings). **Dimensions** are qualitative categories used to slice metrics (age, gender, region, reaction type, distribution type).
- All metrics are browsable in the in-product **Reporting Glossary** tool, where you can search by Sprinklr metric name, see the matching Channel (Meta API) metric name, read the description, and Export a Metric Usage Report. Use this when building [[engagement-dashboards]] and [[reporting]] widgets.

## Key features & how to use

### Types of metrics in Facebook (the six categories)
- **Account-Level Metrics** — overall performance of a Facebook Page/account in Sprinklr.
- **Post-Level Metrics** — performance of each individual post.
- **Cross Post Metrics** — aggregate the performance of cross-posted videos across all the pages they were posted to, for a comprehensive view.
- **Non-Cross Post Metrics** — split a single post''s video views across demographics returned by the channel API (excludes cross-posted data).
- **Reels Metrics** — Reels-specific play counts (see below).
- **Facebook Dimensions** — qualitative categories for granular slicing.
- Pick metric type by question: page health -> account; single post -> post; a video shared to many pages -> cross-post; demographic split of one post -> non-cross-post.

### Facebook Dimensions (account/post slicing)
- **Impressions Frequency Distribution** — how many times people saw Page content (frequency buckets).
- **Video Retention (Seconds)** — % of viewers still watching at set intervals.
- **Like Source / UnLike Source** — where fans liked/unliked the Page (page suggestion, timeline, ad, others). Note: affected by the Reach/Likes deprecations below.
- **Consumption Type** — clicks on content that did not generate a story.
- **Story Type** — activity type: like, post, comment, share, RSVP, check-in.
- **Login Top** — tabs shown on the Page.
- **Monetization Tool** — Meta monetization source (Stars, Subscriptions, Ads on Reels, In-stream ads, etc.).
- **Earning Source** — breakdown of sources feeding Content Monetization earnings.
- Pair the right dimension with the right metric (e.g. video time-by-age needs the Age & Gender dimension) or the widget returns no split.

### Facebook Account Metrics (page level)
- **Reach & Impressions** — Total Reach (people who have seen any content associated with your Page) plus organic / paid / viral variants and frequency distribution. (Being deprecated — see change-log sections.)
- **Engagement** — Engaged Users (people who engaged with your Page; includes any click), positive feedback (likes, comments, shares), negative feedback (unlikes, post hides), and reactions (Love, Wow, Haha, Sorry, Anger).
- **Video** — auto-played, click-to-play, organic, paid, repeat, and unique views, measured at 3+ and 30+ second thresholds.
- **Page Actions** — Call Now clicks, Get Directions clicks, Website CTA button clicks, total contact-info actions.
- **Audience Demographics** — city, country, locale, age range, gender, device type.
- **Monetization** — approximate earnings by tool (Stars, Subscriptions, Ads on Reels, In-stream ads) and content monetization earnings by source.
- Available across daily, weekly (7-day), and 28-day windows.

### Facebook Post Insights (post level)
- **Reach / Impressions** — Post Reach (people who saw the post); Post Impressions (deprecated).
- **Engagement** — Post Engaged Users (people who clicked anywhere in the post); Stream Likes, Comments, Shares.
- **Reactions** — Stream Angry / Love / (and other) reactions per post.
- **Video** — Video Views (3 seconds or more); Video Average Time Viewed.
- **Monetization** — Post Content Monetization Earnings (per individual post).

### Facebook Non-Cross Post Insights (single-post demographic split)
- Lets brands drill into age, gender, location, interests for one post (no cross-posted data folded in).
- **Post Video View Time By Age Bucket and Gender** — total play time (ms) for top audiences; pair with the Age & Gender Type dimension.
- **Post Video View Time By Region Id** — total play time (ms) for top 45 locations (Region-Country); pair with Region Type dimension.
- **Post Video Views By Distribution Type** — plays by distribution type (page_owned, shared); pair with Distribution Type dimension.
- **Post Video View Time By Distribution Type** — total play time (ms) by distribution type; pair with Distribution Type dimension.
- **Post Video View Time By Country Id** — total play time (ms) for top 45 locations (Country); pair with Country Type dimension.

### Facebook Cross Post Insights (video across multiple pages)
- **Total Video Views By Distribution Type** — plays by distribution type including **page_owned, shared, and cross-posted**; pair with the Facebook Distribution Type dimension.
- **Total Video View Time By Distribution Type** — total play time (ms) across page_owned, shared, and cross-posted; pair with Distribution Type dimension.
- Difference vs non-cross-post: cross-post metrics include the cross-posted distribution type; non-cross-post metrics do not.

### Facebook Crosspost Dimensions
- **Facebook Action Type** — user actions on a post: mark as Spam, delete, archive, or channel-specific (e.g. mark as favourite).
- **Region** — region name derived from the IP address where the click originated.
- **Facebook Reaction Type** — like, love, haha, wow, anger, sorry.
- **Facebook Distribution Type** — own page vs shared post.
- **Age Group** — sorts account/post insights by age range.
- **Gender** — gender of the person tied to the activity.

### Facebook Reels Glossary
- **Post Initial Reel Plays** — times a reel starts to play after an impression is counted; counts sessions of 1 ms+ playback, **excludes replays**. (Replaced the older "Facebook Total Reel Play Count".)
- **Post Reel Replays** — times a reel starts to play again after the initial play (1 ms+ in the same reel session).
- **Post Total Reel Plays** — total reel plays after an impression, **including initial plays + replays** (sessions of 1 ms+).

### Historical Backfill — capabilities & limitations
- **What it is:** updating data for posts published before the account was added in Sprinklr, or more than 60 days prior.
- **Default:** a **60-day** backfill range is applied automatically when an account is added.
- **Account-level metrics:** Sprinklr records up to **2 years** back from the date the account was added; no backfill beyond 2 years before backfill processing starts.
- **Post-level data:** automatically updated when a new account is added or an account is re-activated. Up to **2 years** of post-trend backfill is available; the post trend metric itself is "not available" by default.
- Extended/full backfill must be enabled via your Success Manager.

### Data Sync Frequency (how often data refreshes)
| Metric type | Sync frequency | Time period |
|---|---|---|
| Account level | Once daily | Whole time the page is active in Sprinklr |
| Post level | Every 4 hours | Days 0-10 after publish |
| Post level | Once daily | Days 11-60 after publish |
| Stories | Every 4 hours | First 24 hours |
- After day 60 a post''s metrics effectively stop refreshing on the normal cadence — explains why old posts look "stale".

### Reporting Glossary tool (in-product)
- Open **Reporting Glossary**, use the search box (e.g. "Facebook Post Reach") to find a metric.
- Columns shown: **Sprinklr Metric Name**, **Channel Metric Names** (the Meta API name, e.g. "Lifetime Post Total Reach"; shows **"Not Available on Channel"** when Meta does not expose it), and **Description**.
- Use **Quick Filter** / **+ Add Filter** to narrow the list; star a metric to favourite it.
- The upload/export icon on a row runs **Export Metric Usage Report** — use it to see where a metric is used before you change/retire it.

## Common issues & fixes
- **Impressions metrics stopped updating (effective Nov 15, 2025).** Meta deprecated ~53 impression/Page-Likes metrics (14 post-level, 31 page-level, 8 Page Likes). Switch to the new **Views** metrics: post-level Views, Paid Views, Fan Views, Organic Views; account-level Page Views Count, Page Paid/Organic/Fan Views Count. Update widgets, dashboards, and custom metrics before the cutoff. Do **not** compare historical Impressions to new Views. For Page Likes, report on **Page Follows** instead.
  - Impressions = every time a post appears on screen (even briefly). Views = actual media consumption with a minimum visibility threshold (typically 1 second for video/reels). The numbers will not line up.
- **Reach metrics being retired (effective June 15, 2026; replacements from release 26.4.1 / ~May 2026).** Meta is removing ~85 reach + impressions metrics: 19 post-level, 30 video post-level, 36 page-level (daily/7-day/28-day). Replaced by **Unique Views**: "Facebook Page Unique Views Count" (with weekly/28-day variants) and "Facebook Post Unique Views" (+ trend variant).
  - Parallel window: old and new coexist from 26.4.1 until June 15, 2026 — migrate dashboards during this window.
  - Differences: Unique Views replaces Reach terminology; **no viral / non-viral breakdowns**; **fan-specific metrics discontinued**.
  - Only **Facebook Post Unique Views** is eligible for a **1-year retroactive backfill**. Request historical carryover from Sprinklr Support if you need continuous trend lines.
  - Update custom-metric formulas and any API payloads / downstream BI tools that reference deprecated metric identifiers.
- **Old post shows no fresh data** — expected: post-level sync stops after day 60 (see Data Sync table).
- **Demographic/video split widget returns nothing** — the metric must be paired with its required dimension (Age & Gender, Region, Country, or Distribution Type).
- **Single-metric reporting help / deprecation questions** — contact tickets@sprinklr.com.

## Notes & gaps
- **Permissions/prereqs:** the Facebook account must be connected via [[asset-manager]] with valid Meta API access; extended historical backfill is gated behind your Success Manager.
- These articles are **glossaries** — they list metric/dimension names and definitions, not step-by-step dashboard build instructions. For building widgets see [[engagement-dashboards]] / [[reporting]].
- Exact counts: the impressions-deprecation article lists 14 post + 31 page + 8 Page-Likes metrics; the reach-deprecation article lists 85 metrics (19 post + 30 video post + 36 page). Full per-metric name lists live in those two change-log articles — consult them directly when auditing a specific dashboard.
- The Reels glossary covers only three play-count metrics; engagement/reach for reels falls under the broader Views/Unique Views deprecation changes.
- Most images on these pages are marketing/nav assets, not UI; only the Reporting Glossary tool screenshot (reach-deprecation article) shows real product UI.

## Sources
- Types of Metrics in Facebook — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/types-of-metrics-in-facebook/63ebc90def1b447d6c61e953
- Facebook Dimensions — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-dimensions/63ebcd08ef1b447d6c61e96e
- Facebook Account Metrics — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-account-metrics/63ebd03def1b447d6c61e997
- Facebook Post Insights — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-post-insights/63ebca2cf6e2cc7d18f99a6e
- Facebook Non-Cross Post Insights — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-noncross-post-insights/63ebcc36ef1b447d6c61e96a
- Facebook Cross Post Insights — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-cross-post-insights/63ebcb55f6e2cc7d18f99a83
- Facebook Crosspost Dimensions — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-crosspost-dimensions/63ebce07f6e2cc7d18f99a9e
- Facebook Reels Glossary — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-reels-glossary/6682bc63614893335bafea48
- Facebook Historical Backfill Capabilities and Limitations — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/facebook-historical-backfill-capabilities-and-limitations/63ec906def1b447d6c62a24f
- Data Sync Frequency — https://www.sprinklr.com/help/articles/facebook-reporting-glossary/data-sync-frequency/63ec8fe3ef1b447d6c62a23a
- Impressions Deprecation and Introduction of Views (Change Log) — https://www.sprinklr.com/help/articles/facebook-change-log/impressions-deprecation-and-introduction-of-views/68e8cff868135a3d59e05a3c
- Facebook Reach Metrics Deprecation (Change Log) — https://www.sprinklr.com/help/articles/facebook-change-log/facebook-reach-metrics-deprecation/69f9ad05c8cbd953ddfa379c
