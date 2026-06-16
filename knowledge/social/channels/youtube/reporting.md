# YouTube — Reporting & Insights (Sprinklr Social — YouTube)
**Source:** sprinklr.com/help — YouTube channel (multiple articles; see links below)

## What it is
- Sprinklr pulls YouTube analytics into [[reporting]] dashboards so you track channel and video KPIs in one place — no need to bounce to YouTube Studio.
- Data comes from the YouTube Insights/Analytics API and is split into three lenses: **Account Insights** (channel-level), **Video/Post Insights** (per-video), and **Audience Understanding** (demographics: age, gender, location, interests).
- A ready-made **Standard Reporting Dashboard** ships out of the box; you can also build custom widgets from the same YouTube metrics in [[reporting]].
- Sync cadence, historical backfill depth, and which metrics exist are governed by what the YouTube API exposes — covered below.

## Key features & how to use

### Standard Reporting Dashboard
- Pre-built dashboard to visualize core YouTube KPIs (reach, engagement, subscribers, views) with real-time-ish data from YouTube Insights.
- Three core sections: **Account Insights** (brand reach/engagement/conversions/CTR), **Post Insights** (per-video performance on the same metrics), **Audience Understanding** (age, gender, location, interests for content targeting).
- Widgets seen in the dashboard (confirmed from screenshots):
  - **Outbound Summary** — Published Videos count, Engagements, Engagement Trend/Video, each with a "Previous Period" comparison and % change.
  - **Engagement Summary** — Likes, Comments, Shares (vs previous period, % change).
  - **Account Summary** — Total Subscribers, New Subscribers, Total Inbound Messages.
  - **Most Engaging Published Video** — thumbnail card of the top video with shares/likes/comments/views.
  - **Published Videos and Total Engagement** — dual-axis chart: bar = Volume of Published Videos, line = Total Engagement, plotted by date; side panel lists **Top 3 Videos**.
  - **Subscribers Insight** — bar chart of Followers (Subscribers Count) plus Change in Followers, by date.
  - **View By Players** — donut splitting **YouTube Video Views by player location** (e.g. WATCH vs SHORTS_FEED).
- Each widget has refresh and "..." (options) controls; some (e.g. View By Players) offer a chart-type toggle.

### YouTube Account Insights (channel-level metrics)
Metrics available at the channel level, segmentable by dimension:
- **Engagement:** Likes, Dislikes (deprecated by YouTube), Shares, Comments — each with country variants.
- **Subscribers:** Subscribers Gained, Subscribers Lost, and Net Subscribers (gained minus lost) — with country variants.
- **Viewership:** Channel Views and Estimated Minutes Watched, each with country and traffic-referrer variants; Average View Duration (avg length in seconds of playbacks) and Average View Percentage, with country variants.
- **Revenue (monetized channels only):** Earnings (net revenue from Google-sold + non-advertising sources), Gross Revenue and variants, Monetized Playbacks (carries an estimated +/-2.0% error margin), Ad Impressions.
- **Performance:** Annotation Close Rate (with country variants).
- **Dimensions to slice by:** Country, Demographics (age/gender), YouTube Traffic Referrer, and specific Video.
- **Deprecated metrics (do not rely on):** Unique Views (30-day and 7-day variants) and Favorites (added/removed) — based on retired cookie-counting methodology.

### YouTube Video Insights (per-video metrics)
Per-video performance to understand which content engages:
- **Views:** YouTube Video Views (counted instantly on watch); Views by Country, Device Type, Player Location, and Referrer; paid views from advertising (updated daily, up to a 72-hour delay); Average View Duration and Average View Percentage (% of video watched).
- **Engagement:** YouTube Video Shares (Share-button shares), Likes/Dislikes (Dislikes deprecated), Comments.
- **Monetization (monetized channels):** Monetized Playbacks, Ad Impressions, Estimated Gross Revenue from advertising, CPV (Cost per View), revenue per thousand ad impressions and per thousand playbacks, Earnings (net revenue after adjustments).
- **Dimensions / video attributes:** Video Title, Duration, Tags; Video Dimension (1D/2D/3D); Audio Language; Captions; Thumbnail (custom vs auto-generated); Projection type (horizontal vs vertical for Shorts); Player Location; Traffic Referrer; Licensed Content flag.
- **Deprecated:** Favorites (added/removed), Unique Views.

### YouTube Data Sync Frequency
How often Sprinklr refreshes YouTube data from the API:
- **Account-level metrics:** once a day; available as long as the YouTube account/channel stays active and connected.
- **Post (video) metrics:**
  - 0-10 days since publish -> refreshed **every 4 hours**.
  - 11-60 days since publish -> refreshed **once a day**.
- **Stories:** every 4 hours, over a 24-hour window.
- Principle: newer content syncs more frequently; older content syncs less often.

### YouTube Historical Backfill — Capabilities & Limitations
- **What it is:** updating data for posts published before the account was added to Sprinklr (or up to 60 days prior). A **default 60-day backfill** is applied automatically when an account is added.
- **Coverage:**
  - Account-level metrics — available for a **lifetime** period.
  - Post-level metrics — supported for a **lifetime** period, with trends included.
- All post-level data is automatically refreshed when a new account is added or an account is re-activated.
- **Limitation / how to enable:** extended historical backfill is not on by default for everyone — **contact your Sprinklr Success Manager** to enable backfill capabilities in your environment.

## Common issues & fixes
- **Likes/Dislikes or Favorites show zero or missing:** these are deprecated by YouTube (Dislikes hidden publicly; Favorites and Unique Views retired). Use Views, Engagement, and Subscriber metrics instead.
- **Recent video metrics look stale:** sync is interval-based — 0-10 day-old videos update every 4 hours, 11-60 day-old once daily, account metrics once a day. Wait for the next sync rather than assuming a fault.
- **Paid/advertising view numbers lag:** paid views update daily with up to a 72-hour delay; revenue/monetization figures (e.g. Monetized Playbacks) carry an estimated +/-2.0% error.
- **No data older than 60 days:** only the default 60-day backfill is applied automatically. Raise a request with your Success Manager to extend historical backfill.
- **Revenue/monetization widgets empty:** these metrics only populate for monetized channels with revenue access granted via the YouTube connection.

## Notes & gaps
- **Prerequisites:** a connected YouTube account/channel in [[asset-manager]] / account management; revenue metrics require a monetized channel and appropriate API scopes.
- **Permissions:** building/editing dashboards needs reporting access in [[reporting]]; extended backfill needs Success Manager action.
- **Gaps in the source articles:** the Standard Reporting Dashboard article gives no step-by-step build/config instructions, field names, or required user permissions — it is descriptive only (widget detail above is reconstructed from screenshots). No image URLs were available for the Account Insights, Video Insights, Backfill, or Sync articles (only SVG icons / no images present), so those sections are text-only. Exact metric API IDs and full per-metric definitions beyond those quoted are not enumerated in the articles.

## Sources
- Standard Reporting Dashboard — https://www.sprinklr.com/help/articles/report-on-youtube-activities/standard-reporting-dashboard/6459f5ad0104980882a5808d
- YouTube Account Insights — https://www.sprinklr.com/help/articles/report-on-youtube-activities/youtube-account-insights/640ab98e2680c35a78bb1ff2
- YouTube Video Insights — https://www.sprinklr.com/help/articles/report-on-youtube-activities/youtube-video-insights/640ab8ca7517d84a3aaf4204
- YouTube Historical Backfill Capabilities and Limitations — https://www.sprinklr.com/help/articles/report-on-youtube-activities/youtube-historical-backfill-capabilities-and-limitations/640ab7107517d84a3aaf4202
- YouTube Data Sync Frequency — https://www.sprinklr.com/help/articles/report-on-youtube-activities/youtube-data-sync-frequency/640ab7922680c35a78bb1ff0

Related: [[reporting]] - [[engagement-dashboards]] - [[publishing]] - [[asset-manager]]
