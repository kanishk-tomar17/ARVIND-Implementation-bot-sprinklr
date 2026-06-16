# TikTok — Reporting Glossary (Sprinklr Social — TikTok)
**Source:** sprinklr.com/help — TikTok channel (multiple articles; see links below)

## What it is
- The complete dictionary of TikTok metrics and dimensions you can add to Sprinklr [[reporting]] dashboards and widgets.
- Metrics split into three groups: **Post-level** (per video), **Account-level** (per TikTok handle/page), and **Dimensions** (the breakdown axes you slice metrics by).
- Use these exact names when building widgets in [[reporting]] or [[engagement-dashboards]] — they match the field picker in Sprinklr's report builder.
- Several metrics also expose a paired **"Trend"** variant that plots the same value by date of engagement (time series).
- A handful of post-level metrics (website clicks, lead submissions, app download clicks) require a **Registered Business Account** to populate.

## Key features & how to use

### TikTok Reporting Glossary
Use the metric/dimension names below verbatim when adding columns or measures to a TikTok widget.

**Post-level metrics (per video):**
- **TikTok Video Views** — total number of views. (`...Trend` = views by date of engagement.)
- **TikTok Video Likes** — total likes. (`...Trend` = likes by date of engagement.)
- **TikTok Video Comments** — total comments. (`...Trend` = comments by date.)
- **TikTok Video Shares** — total shares. (`...Trend` = shares by date.)
- **TikTok Video Reach** — unique viewers. (`...Trend` = reach by date.)
- **TikTok Video Watched To Completion Rate** — % of viewers who watched the entire video. (`...Trend` = completion rate by date.)
- **TikTok Video Total Time Watched in Seconds** — total video watch time. (`...Trend` = watch time by date.)
- **TikTok Video Average Time Watched in Seconds** — average watch time. (`...Trend` = average watch time by date.)
- **TikTok Video Impressions Percentage By Source** — % of impressions by source; requires pairing with the **TikTok Video Source** dimension.
- **TikTok Video Viewer Percentage By Country** — top 10 countries by viewer % distribution.
- **TikTok Video Saves** — total number of times the video was added to favorites.
- **TikTok Video Website Clicks** — total clicks on the website link from profile visitors (**Registered Business Accounts only**).
- **TikTok Video Lead Submissions** — total leads collected (e.g. quotes, signups) from profile visitors (**Registered Business Accounts**).
- **TikTok Video App Download Clicks** — total clicks on the app download link from profile visitors (**Registered Business Accounts**).
- **TikTok Video Audience Retention Over Time** — % of viewers still watching after specific durations.
- **TikTok Video View Percentage By Audience** — distribution of viewers by type (New, Returning, Followers, Non-Followers).
- **TikTok Video Engagement Likes Percentage Over Time** — % of viewers who liked the video at specific timeline points.

**Account-level metrics (per handle/page):**
- **TikTok Account Likes** — total likes across videos (daily).
- **TikTok Account Comments** — total comments across videos (daily).
- **TikTok Account Shares** — total shares across videos (daily).
- **TikTok Account Video Views** — total views across videos (daily).
- **TikTok Account New Followers** — new followers per day.
- **TikTok Account Lost Followers** — lost followers per day.
- **TikTok Account Profile Views** — profile views per day.
- **TikTok Account Followers** — total followers (**snapshot only** — point-in-time, not a daily trend).
- **TikTok Last 60 Days Follower % By Country** — country distribution (accounts with **100+ followers** only).
- **TikTok Last 60 Days Follower % By Gender** — gender distribution (accounts with **100+ followers** only).
- **TikTok Page Followers Online By Hour** — hourly active-follower distribution (accounts with **100+ followers** only).
- **TikTok Total Subscribe (Page Event)** — total subscriptions on a page.

**Dimensions (breakdown axes):**
- **TikTok Video Source** — source of views/impressions: For You, Follow, Hashtag, Sound, Personal Profile, Other Profile, Search. (Pair with *Impressions Percentage By Source*.)
- **TikTok Hour of Day** — enables time-based widget creation in the user's local time zone.
- **TikTok Audience Type** — New Viewers, Returning Viewers, Followers, Non-Followers.
- **TikTok Video Time (Seconds)** — shows the time of the video in seconds (used with retention / over-time metrics).

## Common issues & fixes
- **Website Clicks / Lead Submissions / App Download Clicks show no data** — these only populate for a **Registered Business Account**; a Personal/Creator account returns blank.
- **Follower demographic metrics (Country / Gender / Online By Hour) are empty** — TikTok only returns this data for accounts with **100+ followers**.
- **"Followers" total looks flat over time** — *TikTok Account Followers* is a **snapshot** metric; for daily change use *TikTok Account New Followers* / *Lost Followers*.
- **Impressions-by-source % renders nothing** — add the **TikTok Video Source** dimension to the widget; the metric needs it to break out.

## Notes & gaps
- "Trend" suffix = same metric plotted by date of engagement (time series); the base name = the aggregate total.
- Account-level engagement metrics (Likes/Comments/Shares/Video Views) are reported **daily**.
- Prerequisites: a connected TikTok account in [[asset-manager]]; business-account-only metrics need a Registered Business Account.
- This article is a glossary only — it does not cover building the widget UI; see general [[reporting]] / [[engagement-dashboards]] docs for dashboard construction.
- Source article contains no UI screenshots (text/table-only glossary), so no screenshot-derived detail was available to fold in.

## Sources
- TikTok Reporting Glossary — https://www.sprinklr.com/help/articles/report-on-tiktok-activities/tiktok-reporting-glossary/68317dec0a718d29a578f82e
