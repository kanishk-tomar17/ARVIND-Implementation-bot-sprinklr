# Instagram — Reporting Dashboards (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- Sprinklr ships **standard (out-of-the-box) reporting dashboards** for Instagram Business accounts, grouped into three analysis areas: **Account Performance**, **Post Performance**, and **Understand Your Audience**.
- These dashboards are pre-built collections of widgets (charts, scorecards, tables) — no manual widget building required to get started; you can clone and customise them.
- They answer three questions: how the account is growing/performing, which posts work, and who the audience is (demographics, location, language).
- Metrics are pulled from the connected Instagram Business profile; data is subject to Sprinklr's [[reporting]] sync frequency, not real-time.
- **Important 2025 change:** Instagram **Impressions** and **Reel Plays** metrics were deprecated and replaced by a single **Views** metric — see the changelog section below.

## Key features & how to use

### Account Performance dashboard
Tracks the effectiveness of the brand's overall presence — reach, engagement, conversions, follower growth.
- **Audience Growth** widget — a line/trend chart of **New Followers** over a date range (X-axis = Date, Y-axis = New Follower count). Use it to spot follower-growth spikes and tie them to events/campaigns (event mapping).
- **Account Scorecard** widget — a table comparing multiple connected Instagram accounts side by side, one row per account handle. Columns seen in the UI:
  - Total Impressions, Avg. Weekly Total Impressions, Avg. 28 Days Total Impressions
  - Avg. Daily Reach, Avg. Weekly Total Reach, Avg. 28 Days Total Reach
  - Total Profile Views
  - Conversion clicks: Total Website Clicks, Total Email Contacts, Total Get Direction Clicks, Total Phone Call Clicks, Total Text Message Clicks
- Scorecard supports per-column sort (chevron on each header) and paginates (e.g. "Showing 1–20 of 27 Rows") — good for benchmarking your accounts against each other.
- Each widget has a top-right toolbar: insights/AI icon, refresh, chart-type toggle, and a "..." menu (export/edit/clone).
- Note: Impressions columns here are legacy — they will read as **Views** going forward (see changelog).

### Post Performance dashboard
Measures the impact of individual posts; surfaces top content and lets you benchmark.
- **Posts Published** widget — bar chart of number of **Posts** published per day over the date range (Y-axis = Posts, X-axis = Date). Shows publishing cadence.
- **Top Engaged Post** and **Top Viewed Post** widgets — spotlight cards showing the post thumbnail, account handle, publish date, and the post's metrics (e.g. *Instagram Business Post Engagement*, *Instagram Business Post Impressions* — now Views).
- **Post Scorecard** widget — a per-post table (one row per post with thumbnail, handle, caption snippet, date). Columns seen:
  - Organic Impressions (→ now Views), Organic Reach, Organic Engagement, Organic Likes, Organic Comments, Organic Post Saved, Organic Video Views
- Use the scorecard's sort + search (magnifier icon in toolbar) to find top-performing posts; paginates (e.g. "Showing 1–20 of 272 Rows").
- Benchmark dimensions called out: engagement rate, follower growth, reach, impressions (Views).

### Understand Your Audience dashboard
Profiles the people who follow/engage with the account — demographics, location, language — to target content.
- **Followers by Demographics** widget — stacked bar chart of follower count by **Age Range** (13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+), split by gender: **Male / Female / Unknown** (colour-coded legend).
- **Top Countries by Followers** — table: Country | Followers (sorted desc; paginates, e.g. "Showing 1–5 of 36 Rows").
- **Top Cities by Followers** — table: City | Followers (city shown as `City__Region`, e.g. `Delhi__Delhi`; paginates, e.g. of 105 Rows).
- **Top Languages by Followers** — table: Locale | Followers (e.g. English (United States), Spanish (Spain)).
- Use these to localise content and target campaigns where fans actually are.

### Changelog — Impressions/Reel Plays deprecation → Views metric
Major reporting change consultants must account for in any IG dashboard:
- **Deprecation date:** 21 April 2025. **Last data collection:** 20 April 2025.
- **Backfill of Views:** completed August 2024 for most clients; 11 May 2025 for the rest.
- **Deprecated post-level metrics:** Instagram Business Post Impressions (+ Trend), Post Initial Reel Plays (+ Trend), Post Total Reel Plays (+ Trend), Post Reel Replays (+ Trend).
- **Deprecated account-level metrics:** Instagram Business Total Impressions, Weekly Total Impressions, 28 Days Total Impressions.
- **Replacement post-level metrics:** Instagram Business Post Views, Instagram Business Post Views Trend.
- **Replacement account-level metrics:** Instagram Account Daily Views, Daily Views by Follow and Product Type, Daily Views by Product Type.
- Views serves the same purpose but uses a **different calculation** — do not treat old Impressions and new Views as identical for trend continuity.

## Common issues & fixes
- **Old Impressions/Reel Plays widgets show no new data after 21 Apr 2025.** Existing dashboards keep working but stop receiving new data for those metrics — rebuild affected widgets/custom metrics on the new **Views** metrics.
- **Widgets "lose relevance," especially for content published after 1 July 2024.** Impressions/Reel-Plays-based widgets, dashboards, and custom metrics gradually become inaccurate — migrate them to Views.
- **Numbers look like zero / very low (e.g. Total Website Clicks = 0).** Conversion-action columns only populate if the IG Business profile has those actions configured and traffic; expect zeros on low-activity accounts, not necessarily a sync fault.

## Notes & gaps
- Requires a connected **Instagram Business** account (consumer/creator data differs; these dashboards reference Business metrics).
- Dashboards are **standard/templated** — clone before customising; respect [[reporting]] sync frequency (data is not real-time).
- The three help articles are introductory overviews — they do **not** document exact navigation path to open the dashboards, permission/role requirements to view or edit, or per-metric definitions; confirm in-platform under Reporting and via the metrics glossary.
- Scorecards aggregate across all connected IG accounts in scope; ensure the consultant's account access matches the accounts they expect to see.
- Related: [[engagement-dashboards]], [[publishing]], [[asset-manager]], [[facebook]], [[rule-engine]].

## Sources
- Instagram Standard Reporting Dashboard — Account Performance — https://www.sprinklr.com/help/articles/standard-reporting-dashboard/account-performance/63e384ae55780d70a15bd9bb
- Instagram Standard Reporting Dashboard — Post Performance — https://www.sprinklr.com/help/articles/standard-reporting-dashboard/post-performance/63ec7875ef1b447d6c627531
- Instagram Standard Reporting Dashboard — Understand Your Audience — https://www.sprinklr.com/help/articles/standard-reporting-dashboard/understand-your-audience/63e384ada9d511790301662f
- Instagram Reporting Changelog — Impressions & Reel Plays Deprecation and Introduction of Views Metric — https://www.sprinklr.com/help/articles/instagram-reporting-changelog/impressions-and-reel-plays-deprecation-and-introduction-of-views-metric/68072c6acbfca249dfba78e1
