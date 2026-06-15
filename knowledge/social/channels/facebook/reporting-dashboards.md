# Facebook — Reporting Dashboards (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- Standard, pre-built [[reporting]] dashboards in Sprinklr Social that measure a brand's Facebook performance. No manual widget building — they ship ready to use.
- Three lenses: **Account Performance** (page health and follower growth), **Post Performance** (which content works), and **Understand Your Audience** (who follows and engages).
- Each dashboard is a set of widgets (trend charts, donut breakdowns, scorecard tables, "top post" cards) over a selectable date range.
- Use them to track reach, engagement, impressions, follower/like trends, and demographics across one or many connected Facebook Pages.
- Pulled from native Facebook insights via connected accounts in [[asset-manager]].

## Key features & how to use

### Account Performance
Measures the effectiveness of a brand's Facebook presence and how a Page fares against its peers.
- **Audience Growth** (area/line chart over Date): plots **Page New Likes (Unique)** vs **Page Unlikes (Unique)** day by day. Use it to see how follower count is shaped over the period and map spikes/drops to events or campaigns.
- **Page Like Source Breakdown** (donut, center = **Page Likes (Unique)** total): shows where new likes come from — e.g. *Page_Suggestions*, *Search*, *Other* — each with % and absolute count. Tells you which channels drive traction so you can allocate resources.
- **Page Unlike Source Breakdown** (donut, center = **Page UnLikes (Unique)** total): breaks down why people unliked — e.g. *Suspicious_Account_Removals*, *Unlikes_from_Page,_Posts,_or_News_Feed*, *Other*.
- **Page Scorecard** (table, one row per connected account, "Showing 1–20 of N Rows" with pagination): per-Page health overview for benchmarking. Columns include: Accounts, **Avg. Daily Reach**, **Avg. Organic Daily Reach**, **Avg. Paid Daily Reach**, **Total Impressions**, **Organic Impressions**, **Paid Impressions**, **Avg. Daily Engaged Users**, **Negative Feedback (Unique)**, **Negative Feedback**, **Video Views (3 secs or more)**, **Organic Video Views (3 secs or more)**, **Paid Video Views (3 secs or more)**. Column headers have dropdown carets for sort/options; the table can be sorted by any metric (e.g. sort by Avg. Daily Reach).

### Post Performance
Measures the effectiveness of individual posts and their impact on the target audience.
- **Posts Published** (bar chart over Date): count of **Posts** published per day — shows publishing cadence/volume.
- **Top Engaged Post** (card): surfaces the single best post by engagement, showing the post thumbnail, account handle, date, and metrics — **Post Engagement** and **Post Impressions**.
- **Top Viewed Post** (card): the best post by impressions/views, with thumbnail, handle, date, **Post Impressions** and **Post Engagement**.
- **Post Scorecard** (table, one row per post, paginated "Showing 1–20 of N Rows", with a search icon): ranks posts by organic performance. Columns: Post (thumbnail + handle + caption + date), **Organic Impressions**, **Organic Reach**, **Organic Engagement**, **Organic Likes**, **Organic Comments**, **Organic Post Saved**, **Organic Video Views**. Default sort is by Organic Impressions (caret on that column); click any header to re-sort.
- Workflow: scan reach/engagement to see what resonates, then deep-dive the top-performing and top-engaging posts to inform content strategy.

### Understand Your Audience
Analyzes audience characteristics so you can create more relevant content and improve performance.
- **Page Likes by Gender** (donut, center = **Page Likes** total, e.g. 17.7K): split into **Male / Female / Unknown** with % and counts. Shows which gender groups are most interested in the brand.
- **Reach by Gender** (donut, center = **Page Reach** total): same Male/Female/Unknown split applied to reach.
- **Page Likes by Demographics** (stacked bar by **Age Range** — 13-17, 18-24, 25-34, etc.): each bar stacked by Male/Female/Unknown. Identifies which age+gender segments like the Page.
- **Reach by Demographics** (stacked bar by **Age Range** across full bands 13-17 through 65+): Male/Female/Unknown reach per age band. Use to find high-potential demographics and tailor content plans.

## Common issues & fixes
- Sources do not document specific errors. General gotchas:
  - **Paid columns show 0** (e.g. Avg. Paid Daily Reach, Paid Impressions): expected when the Page runs no paid/boosted content or ad-account permissions aren't connected.
  - **Demographic widgets blank or "Unknown" heavy**: Facebook only returns demographic insights when the Page has enough audience volume; small Pages may show little data.

## Notes & gaps
- Prerequisites: a Facebook Page connected as an account in Sprinklr (see [[asset-manager]]); the connection must carry insights/analytics permissions for paid and demographic metrics to populate.
- These are **standard** dashboards — exact navigation to open them (Reporting module path) is not spelled out in the source articles. Customisation/cloning to build your own is via standard [[reporting]] tooling, not covered here.
- The "Understand Your Audience" source text references IG/Instagram accounts in places (article reuse) — on a Facebook dashboard the metrics are Page-level (Page Likes, Page Reach).
- Metrics are Facebook-native (Unique vs total variants, Organic vs Paid). "(Unique)" = de-duplicated people; non-unique = raw counts.
- Screenshots show real widget titles and column names but not date-range or filter controls; assume the standard global date filter applies.

## Sources
- Account Performance — https://www.sprinklr.com/help/articles/standard-reporting-dashboard-for-facebook/account-performance/63ebc503ef1b447d6c61e8f0
- Post Performance — https://www.sprinklr.com/help/articles/standard-reporting-dashboard-for-facebook/post-performance/63ebc6daf6e2cc7d18f99a10
- Understand Your Audience — https://www.sprinklr.com/help/articles/standard-reporting-dashboard-for-facebook/understand-your-audience/63ebc5f1ef1b447d6c61e8f4

Related: [[reporting]] · [[engagement-dashboards]] · [[publishing]] · [[asset-manager]]
