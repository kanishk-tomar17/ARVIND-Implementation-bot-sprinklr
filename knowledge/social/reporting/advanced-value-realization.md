# Advanced — Value Realization & Insights (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- A set of advanced [[reporting]] capabilities in Sprinklr Social > Analyze > Reporting that turn raw social data into business value.
- Covers value-realization framing for owned-channel (outbound) and inbound data, click/URL performance tracking, AI-driven anomaly explanation (Smart Insights), in-widget math (Summaries), and dashboard/widget building (including for Empower).
- Most features are built as widgets added to a Reporting dashboard via **Add Widget**.
- Several require enablement by a Success Manager or are limited to specific data sources.

## Key features & how to use

### Owned Channel (Outbound) Reporting — value realization
- Use cases the feature is meant to deliver:
  - **Custom Tags** — create tags for brand, product, campaign, etc. for granular reporting on specific initiatives.
  - **Custom Metrics** — define your own metric formulas (e.g. include video views in an engagement calculation) instead of standard definitions.
  - **Account Summaries** — follower counts, follower growth/loss, and inbound message volume per account.
  - **Post Performance** — use message scorecards to see which individual posts performed best by engagement and impressions.
  - **Outbound Summaries** — widgets showing published posts, total engagement, and average engagement per post.
- This article is a value/use-case overview; it does not give field-level UI steps.

### Inbound Reporting — value realization
- Use cases:
  - **Sentiment view** — visualize inbound sentiment with the **Sentiment** and **Inbound Count** metrics; break sentiment by message type (e.g. public comments positive vs. private messages negative).
  - **From User and Message Count** — identify frequent communicators and classify them as influencers, advocates, or detractors for proactive engagement.
  - **Contact Reason tagging** — apply inbound tags to categorize issues (manufacturing, logistics/supply chain, feature issue) and spot common problems early.
  - **Volume metrics** — total inbound volume over a period plus distinct user counts, to support staffing decisions.
  - **Network breakdown** — visualize by social network to see which platforms drive the most conversation.
- Overview/use-case article; no field-level UI steps provided.

### Click Insights — Reporting
- Tracks clicks on URLs published through Sprinklr — links shortened by Sprinklr (**spr.ly**) or by an authenticated third-party shortener — when posts are published via Native/Sprinklr channels.
- Metrics:
  - **Total Clicks (Bot + Non Bot)** — every click on a URL, including known search engines/bots. Compatible dimensions: Account, Post. Incompatible: Auto-Import campaign.
  - **Estimated Clicks** — human clicks only (bots filtered out).
  - **RefURL_Clicks** — clicks originating from referred sites.
  - **Referrer** — the referral URL source for clicks.
  - **Click Count** — pairs with the **Click Type** dimension to split bot vs. non-bot; also segments by Referrer, Country, Region, City. Incompatible: Published Date.
  - **Click Count Trend** — daily click performance. Compatible: Click Type, Referrer, Country, Region, City, User. Incompatible: Published Date.
  - **Vanity URL Click Count** — aggregate lifetime totals for vanity URLs. Compatible: Click Type, Referrer, Country, Region, City.
- Sample custom widgets provided: Click Count by Referrer, Estimated vs. Total Clicks, Click Count by Vanity URL, Click Count vs. % Change.
- Note: works with Sprinklr's URL shortener; third-party shorteners may count differently.

### Estimated Clicks metric
- Previously called **Filtered Clicks**; a metric in Reporting Insights that counts link clicks while filtering out non-human activity.
- Excludes: repeat clicks from a single IP address, clicks by known automated bots, and clicks by web crawlers.
- Produces lower totals than standard web analytics but better reflects genuine human engagement.
- Steps to view:
  1. New Tab > Sprinklr Social > Reporting (under Analyze).
  2. Click the **Dashboard Menu** icon for the left menu.
  3. Select your dashboard.
  4. Click **Add Widget** (top right).
  5. Enter **Widget Name** and **Description**.
  6. Choose **Data Source** from the dropdown.
  7. Select a visualization/chart type.
  8. Add Metrics/Dimensions (bulk add option).
  9. Select **Estimated Clicks** from the metrics dropdown.
  10. Complete remaining details and click **Add to Dashboard**.
- Prerequisite: for shortened URLs published through Sprinklr, the account must be authenticated in the platform to capture click counts.

### Smart Insights (AI-powered) in Reporting dashboards
- AI tool that surfaces the top drivers behind a dashboard metric and pinpoints factors contributing to any deviation or anomaly.
- Supported data sources: **Inbound Analytics**, **Post & Account Insights** only.
- Supported chart types (9): Column, Bar, Line, Spline, Area, Area Spline, Combination, Table, Dual Axis.
- Steps:
  1. Sprinklr Social > Reporting > Analyze.
  2. Search and select the dashboard.
  3. Click **Add Widget**.
  4. Enter **Widget Name** and **Description**.
  5. Select **Inbound Analytics** as Data Source.
  6. Choose a chart type.
  7. Add Metrics/Dimensions (bulk add available).
  8. Click **Add to Dashboard**.
  9. Click the **Smart Insights** icon in the widget's top-right corner.
  10. Bulb markers appear at peaks / top insight-worthy points.
  11. Click a bulb to open the insight card (summarized top contributing drivers).
  12. Click **Details** for the expanded information panel.
- Availability: must be enabled through your Success Manager.

### Evaluate Reporting Data with Summaries
- Summaries are math functions applied to numeric report columns; they compute per-widget subtotals and grand totals across all widget data — no formula writing needed.
- Answers questions like "Which account has the most engagement?" and "What is the average engagement across all accounts?"
- Steps:
  1. New Tab > Reporting (under Sprinklr Social > Analyze).
  2. Choose a dashboard from Reporting Home.
  3. Click **Add Widget** (top right).
  4. Enter widget name and select **Data Source**.
  5. Select visualization and metrics.
  6. Apply the **summaries** option alongside the respective metrics/dimensions.
  7. Click **Add to Dashboard**; rearrange widgets as needed.
- Available functions: Sum, Average (aggregate averages over time periods), Min, Max, Change, Percentage, % Change, Percentile, Standard Deviation, Variance.
- Limit: Standard Deviation and Variance summaries do **not** work with calculated and custom metrics.

### Create a Reporting Dashboard and Widgets for Empower
- Empower reporting dashboards monitor content performance and must be shared with the appropriate **Primary User Groups**.
- Access is restricted to the central brand team's core Sprinklr admins; Empower users do not have access to the Sprinklr environment.
- Create a dashboard:
  1. New Tab > Reporting (under Social Core Cloud).
  2. Hover the **Options** icon and select **Create**.
  3. Enter a **Dashboard Name** and select **Starter Dashboard Type**.
  4. Add tags as needed.
  5. Click **Save**.
- Create a widget:
  1. Open Reporting via New Tab.
  2. From the dashboard, click **Add Widget** (top right or center).
  3. Select widget **Type** and enter a **Name**.
  4. Select **Visualization Type**.
  5. Configure remaining preferences based on Type/Visualization.
  6. Click **Save**; the widget appears at the bottom of the dashboard.
  7. Drag widgets to rearrange.
- Widget types (11): Social Analytics, Outbound Analytics, Inbound Analytics, Benchmarking, Paid, Listening, WEB, Audience Activity, Outbound Message, Advocacy, SAM, Social DMP.
- Visualization types (20+): Column, Bar, Pie, Stacked Column/Bar, Line, Spline, Area, Bubble, Dual Axis, Combination, Table, Counter, Funnel, Summary Table, Post Card, Text, Title, Grouped Summary, Geo Map.

## Common issues & fixes
- **Click counts missing for shortened URLs:** the publishing account must be authenticated within Sprinklr; without authentication, click counts are not captured.
- **Estimated/Total clicks lower than third-party analytics:** expected — Estimated Clicks excludes repeat-IP clicks, bots, and crawlers; third-party shorteners also count differently.
- **Standard Deviation / Variance summary returns nothing:** these two functions do not work with calculated or custom metrics — switch to a standard metric.
- **Smart Insights icon not available:** confirm the data source is Inbound Analytics or Post & Account Insights, the chart is one of the 9 supported types, and the feature has been enabled by your Success Manager.

## Notes & gaps
- The Owned Channel and Inbound "value realization" articles are use-case/value overviews — they do **not** specify field-level UI steps, exact toggle names, permissions, or limits.
- Smart Insights requires Success-Manager enablement; specific permission/role names are not stated.
- Empower dashboards: exact Primary User Group sharing steps and Empower-side limits are not documented in the article.
- No explicit role/permission entitlement names are given for Click Insights, Estimated Clicks, or Summaries.
- Click Insights is limited to Native/Sprinklr-published posts using Sprinklr (spr.ly) or authenticated third-party shorteners.

## Sources
- Owned Channel Reporting Value Realization — https://www.sprinklr.com/help/articles/advanced-features/owned-channel-reporting-value-realization/6463315730f12540268fa9c8
- Inbound Reporting Value Realisation — https://www.sprinklr.com/help/articles/advanced-features/inbound-reporting-value-realisation/646330fb8ea3c9635cf3670e
- Click Insights: Reporting — https://www.sprinklr.com/help/articles/advanced-features/click-insights-reporting/646330f830f12540268fa9c7
- Estimated Clicks Metric in Reporting — https://www.sprinklr.com/help/articles/advanced-features/estimated-clicks-metric-in-reporting/64632f4b8ea3c9635cf36708
- Smart Insights in Reporting Dashboards — https://www.sprinklr.com/help/articles/advanced-features/smart-insights-in-reporting-dashboards/646330fa8ea3c9635cf3670d
- Evaluate Reporting Data with Summaries — https://www.sprinklr.com/help/articles/advanced-features/evaluate-reporting-data-with-summaries/6457c4cd0104980882a57bc6
- Create a Reporting Dashboard and Widgets for Empower — https://www.sprinklr.com/help/articles/advanced-features/create-a-reporting-dashboard-and-widgets-for-empower/6457c45ce66f2e36b4515bdc

---
Related: [[reporting]] · [[engagement-dashboards]] · [[data-engine]] · [[care-console]]
