# X — Reporting & Insights (Sprinklr Social — X (formerly Twitter))
**Source:** sprinklr.com/help — X (formerly Twitter) channel (multiple articles; see links below)

## What it is
- Sprinklr pulls X (formerly Twitter) analytics directly from the X Insights API and surfaces them in [[reporting]] dashboards and widgets so you can track followers, content performance and audience.
- Three layers of data: **Account Insights** (whole-account KPIs), **Post & Poll Insights** (per-post / per-poll performance) and **Audience Understanding** (demographics).
- Data is synced on a schedule (not instant) and is bound by X-API retention limits — important for setting client expectations on freshness and history.
- Major platform change: X deprecated the real-time **InsightsTrack** metrics on **1 Aug 2023**; older metrics were replaced by V2 organic/paid metrics. Accounts may need re-adding to get the new data.

## Key features & how to use

### Standard Reporting Dashboard
- A prebuilt analytics dashboard to "visualize and track your key X KPIs" and understand your X audience; data is pulled from X Insights in real time (subject to sync limits below).
- Use it to monitor follower trends and evaluate content performance, and to present results to clients simply and transparently.
- Three sections:
  - **Account Insights** — brand effectiveness: reach, engagement, conversions, click-through rates.
  - **Post Insights** — per-post performance using the same metric families to see how each post lands with the target audience.
  - **Audience Understanding** — demographics: age, gender, location, interests, for more targeted content.
- The article does not specify the exact menu path; build/clone it from the X channel reporting template in [[reporting]] or [[engagement-dashboards]].

### X Account Insights
- Account-level metrics drawn from the X API; use to learn overall follower trends and content performance. Available metric fields include:
  - **Inbound engagement:** X Direct Messages, X Mentions, X Replies, X Retweets, X Profile Clicks, X Profile Clicks per Hour.
  - **Account activity:** X Followers, X Followings, X New Followers, X Un-followers, X Un-followings, X Likes, X Listed.
  - **Outbound activity:** X Sent Direct Messages, X Sent Mentions, X Sent Replies, X Sent Retweets, X Sent Updates.
- Add these as metrics/columns when building an account-level widget in [[reporting]].

### X Post & Poll Insights
- 40+ post-level metric fields, grouped:
  - **Engagement:** X Post Likes, X Post Retweets, X Post Replies, X Total Engagements (a count of times a user interacted with the post).
  - **Reach / impressions:** X Impressions (lifetime), X Impressions per Hour, X Post Direct Reach, X Estimated Reach.
  - **Actions:** URL clicks, hashtag clicks, media clicks, email shares, app installs, profile follows.
  - **Video:** count of video views plus hourly breakdowns.
- **Poll metrics on the post:** X Poll Label (option text), X Poll Votes (votes per option), X Poll Start Time, X Poll End Time, X Poll Duration.
- **Data retention to plan around:**
  - Post-level data updates for **60 days** from publication.
  - Engagement-API metrics available for **60 days**.
  - Real-time "Insights track" data was available for **7 days** post-publish (now deprecated — see Reporting Updates).

### X Poll Insights
- Analyze poll performance and audience engagement with drill-down capability.
- Metric fields:
  - **X Poll Label** — the label for each poll option.
  - **X Poll Start Time** — when the poll started.
  - **X Poll End Time** — when the poll ended.
  - **X Poll Duration** — how long the poll was active.
  - **X Poll Votes** — total votes received per option/label.
- Drill down into a poll to see results by option and the **percentage of votes in each option**. Pair with the [[publishing]] poll feature to close the loop on poll campaigns.

### X (formerly Twitter) Reporting Updates (the 1-Aug-2023 change)
- **What happened:** X deprecated **InsightsTrack** (real-time) metrics on **1 August 2023**.
- **Deprecated metrics (no real-time feed after that date):** X Unique Impressions, X Un-favorites, X Un-replies, X Unique Engagements, X Un-quote tweets, X Un-retweets, X Video Viewed 95%.
- **Replacement mapping (examples):** "X Favorites (Insights)" -> **X Post Likes**; "X Impressions (Insights)" -> **X Impressions**. Where no replacement exists the docs say "No equivalent metric available."
- **New V2 metrics:** organic vs paid breakdowns for impressions, video views, likes, replies, retweets, URL clicks and profile clicks.
- **Action required:** **re-add the X account after 1-Aug-2023** to access the new V2 metrics. Update any existing widgets that reference deprecated fields.

### Historical Backfill — capabilities & limits
- **What it is:** backfill updates data for posts published before the account was added in Sprinklr, or older than 60 days.
- **Range:** default backfill of **60 days** on account addition; impression & engagement data limited to a **90-day maximum** from the backfill processing start date.
- **Available at post level:** Likes, Replies, Retweets.
- **Time-limited (90 days only):** Impressions, Engagements.
- **Not supported:** account-level historical data; impressions older than 90 days; metrics from the Insight_Track API; trend metrics.

### Data Sync Frequency
- **Account-level metrics:** synced **once a day**; available as long as the X account stays active in Sprinklr.
- **Post-level metrics:**
  - Recent posts (0-10 days old): **every 4 hours**.
  - Older posts (11-60 days old): **once a day**.
- **Stories:** **every 4 hours**, within a **24-hour** window.
- Takeaway: newer content refreshes faster; expect up to a 1-day lag on account KPIs and older posts.

## Common issues & fixes
- **Old real-time metrics showing zero / blank after Aug 2023:** they were deprecated with InsightsTrack. Swap to the mapped replacement field (e.g. X Post Likes, X Impressions) and re-add the X account to pull V2 metrics.
- **Missing organic/paid breakdown metrics:** the account was added before 1-Aug-2023 — re-add it to enable V2 metrics.
- **Numbers look stale / dont match X:** expected. Account KPIs sync once a day; posts 11-60 days old sync once a day; only recent posts (0-10 days) and stories sync every 4 hours.
- **No data for old posts after adding an account:** backfill only goes 60 days by default; impressions/engagements cap at 90 days; account-level history and Insight_Track/trend metrics are never backfilled.

## Notes & gaps
- Prerequisites/permissions: the account must be added and active in Sprinklr; consultant needs reporting/dashboard access. The articles do not list specific role permissions.
- No exact navigation path is documented for opening the Standard Reporting Dashboard — clone/build from the X reporting template.
- All retention/sync limits are imposed by the X API, not configurable in Sprinklr.
- **Images:** the source articles contain only marketing/decorative assets (product spotlight, Aramex/HP/Uber hero banners) — no UI screenshots were available to view, so steps are text-only.

## Sources
- Standard Reporting Dashboard — https://www.sprinklr.com/help/articles/report-on-x-activities/standard-reporting-dashboard/6454a1e00d27fc559bbeb48f
- X (formerly Twitter) Account Insights — https://www.sprinklr.com/help/articles/report-on-x-activities/x-formerly-twitter-account-insights/640ab1c42680c35a78bb1fc1
- X Post & Poll Insights — https://www.sprinklr.com/help/articles/report-on-x-activities/x-post-poll-insights/640ab3182680c35a78bb1fc2
- X Poll Insights — https://www.sprinklr.com/help/articles/report-on-x-activities/x-poll-insights/664b52cd5b21d514edb7ae0f
- X (formerly Twitter) Reporting Updates — https://www.sprinklr.com/help/articles/report-on-x-activities/x-formerly-twitter-reporting-updates/64be3ee08515a91a7819f6eb
- Historical Backfill Capabilities and Limitations — https://www.sprinklr.com/help/articles/report-on-x-activities/historical-backfill-capabilities-and-limitations/640ab01e7517d84a3aaf41cf
- X (formerly Twitter) Data Sync Frequency — https://www.sprinklr.com/help/articles/report-on-x-activities/x-formerly-twitter-data-sync-frequency/640ab1307517d84a3aaf41d2
