# Advanced — Dashboard Tools (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- A set of advanced controls for building, filtering, comparing, auditing, and exporting custom [[reporting]] dashboards in Sprinklr Social (Analyze > Reporting).
- Covers dynamic time intervals, section-level and side-by-side comparison filtering, in-platform metric glossary/tooltips, a consolidated widget warning system, dashboard version history, historical data backfill rules, configurable standard metrics, and the Google Data Studio connector.
- Several features are gated behind dynamic properties — enable via Success Manager or tickets@sprinklr.com.
- Most apply to custom (cloned) dashboards with edit permissions; standard dashboards have limits.

## Key features & how to use

### Dynamic Date Range
- Lets you set reporting periods relative to "now" (e.g. second last week, last 3 weeks to last 1 week) instead of fixed dates — useful for measuring content performance at intervals after publication.
- Steps: New Tab > Sprinklr Social > Reporting (within Analyze) > open dashboard via the Show Dashboard dropdown > click the date range calendar at top > under **Date Range** select **Dynamic Range** > enter the value for **Duration of** and pick the unit (minutes, hours, days, week, or months) > select the time denoting the end date > **Apply** (bottom right).
- Custom date ranges can be saved and reused; preferences persist across sessions.
- Caveat: for monthly follower aggregations, deactivated accounts show data from deactivation date; active accounts show last-day-of-month data (Facebook, TikTok, X, YouTube). Instagram includes only active accounts.

### Section-Level Filtering
- Applies custom filters at an individual dashboard section level, separate from dashboard-level filters; when both are set they combine.
- Steps: Sprinklr Social > Reporting > select dashboard > toggle on **Section filters** (right side) > configure filters and select duration.
- Filter fields: **Select Duration** (Date Range pop-up), **Dimension** (dropdown), **Select Type** (dropdown), **Select Values** (based on dimension), **Add New Filter** (button for more filters).
- Rules: Dimension required alongside date range; date-only filtering allowed if dimension omitted. Section filters override only matching dashboard-level filter types for that section. Widget-level filters take highest precedence across all three levels.
- Not applicable to standard dashboards (works on cloned/exported versions). Enable feature `SECTION_LEVEL_FILTERING_ENABLED` via Success Manager / tickets@sprinklr.com.

### Side-by-Side Compare Mode
- Compares products, topics, campaigns, brands etc. next to each other; auto-creates up to 3 copies of a section's widgets.
- Steps: open a custom dashboard with edit permissions > **Add Widget** to populate sections > select **Enable Side By Side Compare Mode** > widgets convert to 50% view > click **+** to add sub-sections (max 3, adjusting to 33% view) > set sub-section filters/time ranges independently > add sub-section titles > apply widget-level filters without affecting other copies.
- Filter behavior: dashboard + section filters apply to all sub-sections; sub-section filters apply only to that column; widget filters don't affect other copies.
- Available on Listening, Benchmarking, Research Explorer (Custom Research Query), Engagement Reporting, Care Reporting, Ads/Marketing Reporting, and Story (Media Monitoring & Analytics) dashboards.
- Supported widgets: counters, trend charts, bar/column charts, tables, word clouds, pivot tables, pie charts, funnels, tree maps. Unsupported visualizations won't display in compare mode.

### Tooltips & Floating Reporting Glossary
- **Floating Reporting Glossary**: while building widgets, view metric/dimension details in-platform — descriptions, comparison to native analytics metrics, and organic/paid/total classification. Currently limited to custom metrics and custom fields.
- **Tooltips**: hover over a metric/dimension name in a widget to see detailed info.
- Supported widget types (8): Bar Chart, Column Chart, Counter, Dual Axes Chart, Line Chart, Percentage Area Chart, Table, Combination Chart.
- Limit: only the Social Analytics data source and its top 300 metrics/dimensions; broader support rolling out.

### Unified Widget Warning System
- Consolidates all widget-level warnings into a single warning icon per widget to avoid alert clutter.
- Alert types surfaced: **Account Health Alerts (AHA)** — flags accounts in "action required" state, with CTAs to re-add accounts or notify admins; **Incompatible Dashboard-Level Filters** — flags filters that conflict with a widget's report type; **Other** — data inconsistencies, missing metrics, configuration problems.
- Access via dynamic properties `ACCOUNT_HEALTH_STATUS_SCREEN_ENABLED` and `ACCOUNT_HEALTH_STATS_ENABLED_REPORTS`; enable via Success Manager / tickets@sprinklr.com.
- Related: [[care-console]], [[sla-monitoring]].

### Activity Tab — Audit History & Version Restore
- Tracks all user-made changes to a dashboard and lets you restore a previous version (protection against accidental edits/corruption).
- Steps: Sprinklr Social > Reporting > select dashboard > **Options icon** (top right) > **Activity** > view **Dashboard Audit Log** pane.
- Actions: **Copy icon** duplicates that version; **Restore icon** restores that version to the original dashboard.
- On restore, selected metrics/dimensions stay the same but values/data reflect the most recent updates.
- Tracked events: Compare Mode (on/off); Dashboard added/updated/locked/shared/restored; External Link changes; Dashboard Filters; Section Filters; Quick Filters; Tabs; Widgets; Exports.

### Historical Reporting Data Capabilities
- Sprinklr collects data after an account is added; on add it pulls at most the last two months of historical data. Custom scripts are needed to fetch beyond that.
- A requested historical backfill causes a spike in the respective trend metrics for post-level data.
- Channel backfill (Account / Post):
  - **Facebook**: account 2 years (page views, likes); post 2 years (no trend metrics).
  - **X (Twitter)**: account not possible; post limited metrics only; impressions/engagements capped at 90 days.
  - **Pinterest**: account not possible; trend metrics unavailable.
  - **YouTube**: account lifetime period; post lifetime metrics; supports trend metrics.
  - **LinkedIn**: no account backfill; post lifetime metrics; company accounts only.
  - **Instagram**: account 2 years (except followers); post for business accounts only; non-business unsupported.
  - **TikTok**: account 60 days max; post supported; followers cannot be backfilled.
  - **WeChat**: account and post since Dec 2014; supports lifetime and trend metrics.

### Standard Metrics Configuration
- Workspace-level feature to redefine Sprinklr standard metrics with custom formulas (no separate custom metric needed), since metric definitions vary by brand.
- Examples: **Total Engagements** can include channel-specific granular engagements beyond likes/shares/comments; **Average Engagement Rate** computed across individual posts rather than as an overall average; **Post Likes** for Instagram can represent post likes or reel likes.
- Location: **Reporting Settings** (Reporting > Service Reporting Configuration screen).
- Permissions: admins assign **View access** (see formulas) or **Edit access** (modify setup); an Activity/Audit Log tracks changes.
- Limited availability; gated by dynamic property `REPORTING_ADVANCE_SETTING_ENABLED`. Enable via Success Manager / tickets@sprinklr.com. Affects Sprinklr Service, Sprinklr Social (SES), Reporting (SES). Release 26.4.

### Google Data Studio Connector (Integration)
- Adds Sprinklr as a data source in Google Data Studio (Looker Studio) for visualization reports; provides out-of-the-box dashboards for Marketing, Advertising, Research, Care, and Engagement across 35+ channels with near real-time data.
- Export dashboard mapping: New Tab > Sprinklr Social > Reporting > choose dashboard > **Options icon** (top right) > **Export Dashboard Mapping** > Excel export lists widget-wise filters, dimensions, measurements, and mappings.
- Connect as data source: sign into Data Studio > **Create** > **Data Source** > under Partner Connectors select **Sprinklr** > authorize Data Studio to Google account > authorize **Sprinklr-Data Reporting Connector** to Sprinklr > enter Sprinklr username/password and submit > select Customers and Workspaces > select Workspace > NEXT > select Engine and Report > CONNECT.
- Build/share: **CREATE REPORT** from Data Source Fields > add charts/controls via Report Editor > share by email or Google Groups.

## Common issues & fixes
- **Section filters greyed out / not available**: not supported on standard dashboards — clone or export the dashboard, and ensure `SECTION_LEVEL_FILTERING_ENABLED` is enabled.
- **Filter conflict warning on a widget**: dashboard-level filter is incompatible with the widget's report type (shown via the Unified Widget Warning icon) — correct the mismatched filter.
- **Account-health warning on a widget**: account is in "action required" state — use the CTA to re-add the account or notify an admin to restore reporting accuracy.
- **Tooltips/glossary not showing**: only the Social Analytics data source and its top 300 metrics/dimensions are supported, and the glossary is limited to custom metrics/fields.
- **Backfill spike in trend data**: expected after a historical backfill request for post-level data — not an error.
- **Data Studio numbers don't match Sprinklr**: set Sprinklr to the **GMT** time zone (Data Studio is always GMT).
- **Accidental dashboard change**: use the Activity tab to Copy or Restore a prior version.

## Notes & gaps
- Gated features requiring enablement: `SECTION_LEVEL_FILTERING_ENABLED`, `ACCOUNT_HEALTH_STATUS_SCREEN_ENABLED` + `ACCOUNT_HEALTH_STATS_ENABLED_REPORTS`, `REPORTING_ADVANCE_SETTING_ENABLED` (Standard Metrics, limited availability).
- Compare mode and section filtering generally require dashboard **edit permissions** and apply to custom/cloned dashboards.
- Historical backfill beyond two months needs custom scripts (article does not specify how to request/run them).
- The articles do not specify exact required role/permission names for Dynamic Date Range, Activity tab, Tooltips, or Data Studio (beyond Standard Metrics View/Edit access).
- Pinterest post-level backfill and several "not clearly specified" entries are not detailed in the source.
- Related ARVIND topics: [[reporting]], [[engagement-dashboards]], [[data-engine]], [[care-console]], [[sla-monitoring]], [[rule-engine]].

## Sources
- Use Date Range in Reporting Dashboard to Customize Time Intervals — https://www.sprinklr.com/help/articles/advanced-features/use-date-range-in-reporting-dashboard-to-customize-time-intervals/64ff0ce6503ed17eb5c498d7
- Apply Section Level Filtering in Reporting Dashboard — https://www.sprinklr.com/help/articles/advanced-features/apply-section-level-filtering-in-reporting-dashboard/649c2156efca565f6513bbeb
- Use Side By Side Compare Mode in Reporting Dashboards — https://www.sprinklr.com/help/articles/advanced-features/use-side-by-side-compare-mode-in-reporting-dashboards/649c24a1efca565f6513bbf6
- Tooltips & Floating Reporting Glossary — https://www.sprinklr.com/help/articles/advanced-features/tooltips-floating-reporting-glossary/664c84315b21d514edb8b923
- Unified Widget Warning System — https://www.sprinklr.com/help/articles/advanced-features/unified-widget-warning-system/67f4c92f8f20fd1afe19491b
- View Audit History with Activity Tab in Reporting Dashboards — https://www.sprinklr.com/help/articles/advanced-features/view-audit-history-with-activity-tab-in-reporting-dashboards/6540a493b1f59867f3be0476
- Historical Reporting Data Capabilities — https://www.sprinklr.com/help/articles/advanced-features/historical-reporting-data-capabilities/6583d5cac99bc66ce07bff74
- Standard Metrics Configuration — https://www.sprinklr.com/help/articles/advanced-features/standard-metrics-configuration/681e0b0ec9eef13c2d89f31e
- Connect with Google Data Studio — https://www.sprinklr.com/help/articles/integrations/connect-with-google-data-studio/64633e2230f12540268fa9db
