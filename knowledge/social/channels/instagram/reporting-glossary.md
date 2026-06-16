# Instagram - Reporting Glossary & Metrics (Sprinklr Social - Instagram)
**Source:** sprinklr.com/help - Instagram channel (multiple articles; see links below)

## What it is
- The complete glossary of Instagram metrics and dimensions available in Sprinklr [[reporting]] and [[engagement-dashboards]], grouped by surface: Post, Account, Story, Reels, and Collab posts.
- Also covers the operational rules behind the numbers: how often Instagram data syncs into Sprinklr, how far back history can be backfilled, and which Instagram API metrics have been deprecated.
- All metrics are organic and require an Instagram Business account linked to a Facebook Page (see [[facebook]]). Personal/Creator-only setups are not supported for most metrics.
- Several legacy metrics (Impressions, Video Views) have been deprecated by Instagram and replaced by Views-based metrics - check the deprecation dates before building or trusting a widget.

## Key features & how to use

### Instagram Post Insights
Metrics for feed posts (and Reels-as-posts). Add these in a [[reporting]] widget under Instagram, Post metrics.
- Engagement core: Instagram Post Likes, Instagram Post Comments (includes Reel comments), Instagram Business Post Engagement (likes + comments + shares + saves + reposts), Instagram Business Post Saved, Instagram Business Post Shares (includes Reels and Story shares).
- Reach and views: Instagram Business Post Reach (unique accounts, includes Reels), Instagram Business Post Views (total times media seen - the surviving views metric, all media types), Instagram Business Post View Trend.
- Trend variants: Likes Trend, Comments Trend - same metric plotted against the Date dimension (date of interaction).
- Reels-specific: Reels Skip Rate (percent of views skipped within first 3 seconds), Reposts (how often media is reposted), Crossposted_Views (total views for Reels crossposted to Facebook across both platforms), Facebook_Views (views coming specifically from Facebook).
- CTA / link clicks (newer metrics): Bio Link clicks, Call CTA clicks, Direction CTA clicks, Email CTA clicks, Text CTA clicks, Other CTA clicks.
- Profile actions: Instagram Post Followers Gained (accounts that followed after seeing the post or Story), Instagram Post Profile Visits, Instagram Business Post Total Profile Activity.
- Deprecated, do not rely on: Instagram Video Views and Video Views Trend (deprecated 8 Jan 2025); Instagram Business Post Impressions (deprecated 21 Apr 2025). Use Views/Reach instead.

### Instagram Account Insights
Account/profile-level metrics. Use for follower growth and audience demographics.
- Audience size: Instagram Followers, Instagram Followings, Instagram Media Uploads, Instagram Business New Follower Count.
- Follower breakdowns: By City, By Country (top 45), By Demographics (gender + age), By Locale (country code), Online by Hour.
- Reach and views (active): Instagram Business Total Reach, Weekly Total Reach (7-day), 28 Days Total Reach, Instagram Account Daily Views, Daily Views by Product Type, Daily Views by Follow and Product Type.
- Profile actions (active): Instagram Business Total Website Clicks.
- New account metrics (current API): Impressions, Reach, Total Interactions, Accounts Engaged, Likes, Comments, Saved, Shares, Replies (Story replies), Follows and Unfollows, Profile Links Taps, Website Clicks, Profile Views, plus Engaged / Reached / Follower Audience Demographics.
- Deprecated account metrics: Total Impressions, Weekly Total Impression (7-day), 28 Days Total Impressions, Total Profile Views, Total Get Direction Clicks, Total Email Contacts, Total Phone Call Clicks, Total Text Message Clicks. (Replaced by the new metrics above.)

### Instagram Story Insights
Story metrics are only captured for the first 24 hours after publishing (Instagram delivers them via webhook at the 24-hour mark).
- Reach and views: Instagram Business Post Reach (unique accounts, first 24h), Instagram Business Post Views and Views Trend.
- Navigation taps: Story Navigation Taps Forward (taps to next photo/video), Taps Back (previous), Navigation Taps Exit (exited the story), Instagram Story Navigation Swipe Forward (shifted to next users story).
- Aggregate: Instagram Business Story Total Navigation (sum of tap exits + forwards + backs + swipes).
- Engagement: Instagram Business Post Story Replies, Instagram Business Post Engagement (likes + comments + saves + shares on the story), Instagram Post Business Shares.
- Completion Rate: impressions on the last segment divided by impressions on the first segment, times 100.
- Dimension: Story Name Grouping - groups stories by publication day (00:00 to 23:59 GMT).
- Deprecated: Instagram Business Post Impressions (21 Apr 2025).

### Instagram Reels Insights
Add under Instagram, Reels metrics, or filter posts with the IS IG REEL dimension.
- Engagement: Reel Comments, Reel Likes, Reel Shares, Instagram Business Post Reach.
- Watch time: Reels Average Watch Time (avg time spent playing the reel), Reels Total Watch Time (total play time).
- Views: Instagram Business Post Views and View Trend (total times media seen).
- Deprecated Reel metrics: Reel Engagements (likes+saves+comments+shares minus reversals), Initial Reel Plays, Reel Replays, Total Reel Plays. Use Views + Watch Time instead.

### Instagram Collab Posts Reporting
Track Instagram Collaboration posts separately from regular brand posts in both Inbound Analytics and Social Analytics.
- Filter to find them: open the widget Apply Filters dialog, add a Where row, field "Is Collab Post" (also labelled "Is IG Collab Post"), operator "Containing", value "true" (the screenshot shows: Is Collab Post | Containing | true). A Date Range row sits above it. Click Apply. Set value to false to compare against standard posts.
- Dimensions available as table columns: "Is Collab Post" (true/false) and "Name of the collaborator" (shows accepted collaborator handles, e.g. vibecafe1802). Build a Table widget with columns: Outbound Post, Name of the collaborator, Is Collab Post, and any metric (e.g. Post Likes And Reactions).
- Is Collab Post = True only when at least one collaborator has accepted the collaboration request.
- Limit: a maximum of 3 collaborators per post.
- Status window: acceptance/declination status keeps updating for up to 7 days after publishing.
- Use it to: see which collaborators drive more traction, and whether collab posts outperform regular posts.

### Instagram Data Sync Frequency
How often Sprinklr refreshes Instagram data from the API:
- Account level: once per day; active accounts stay available indefinitely.
- Post level: every 4 hours for days 0 to 10 after publish; then once daily for days 11 to 60.
- Stories: every 4 hours, but only for the 24-hour window (Instagram sends final story metrics via webhook at the 24h mark).
- Data stays available as long as the Instagram Business account and its linked Facebook Page remain active in Sprinklr.

### Instagram Historical Backfill - Capabilities and Limitations
- Default: a 60-day backfill runs automatically when an account is added. All post-level data is auto-updated on add.
- Post-level metrics backfillable: Impressions, Reach, Engagement, Saved, Likes, Comments - available since the day the IG account was natively linked to the Facebook account. Trend metrics cannot be backfilled.
- Account-level metrics: can be backfilled up to 2 years, but not automatically - requires a request via your Sprinklr Success Manager. Supported: Total Reach, Impressions, Profile Views, Website Clicks, Phone Call Clicks.
- Followers cannot be backfilled (Instagram API limitation).
- Business accounts only - non-Business accounts are no longer supported.

### Instagram User Insights - API Changes (deprecation)
- Instagram has dropped the last_14_days, last_30_days, last_90_days, and prev_month timeframes for audience demographics and engagement metrics.
- Replacements: this_month and this_week timeframes.
- Affected metric families: Engaged Users by Demographics, Reached Users by Demographics, Engaged Users by Country, Reached Users by Country, Reached Users by City, Engaged Users by City - every 14/30/90-day variant is discontinued.
- Action required: for any existing widget that used the deprecated metrics, you must remove those metrics manually - they will not auto-migrate.

## Common issues & fixes
- Old widget shows zeros or blank after a date: likely a deprecated metric. Impressions (post and story) ended 21 Apr 2025; Video Views ended 8 Jan 2025. Swap to Views / Reach.
- Demographic/engagement widget broke: the 14/30/90-day and prev_month timeframes were removed - manually delete the affected metrics and rebuild with this_week / this_month.
- No story metrics: stories only report for the first 24 hours; after that the window closes and no further data syncs.
- History missing beyond 60 days: only 60 days backfill automatically. For account metrics up to 2 years, raise a request with your Success Manager. Followers can never be backfilled.
- Collab metrics not showing or Is Collab Post = false: the collaborator has not accepted yet - status can take up to 7 days post-publish to update.
- Recent post numbers look stale: post-level data only refreshes every 4 hours (days 0 to 10), then daily - it is not real-time.

## Notes & gaps
- Prerequisites: Instagram Business account linked to a Facebook Page; all metrics are organic (no paid/ads metrics in these glossaries). See [[facebook]] and [[publishing]].
- Backfill beyond defaults and account-level history require Success Manager involvement - not self-serve.
- The articles do not give an enforcement deadline for the user-insights API timeframe deprecation (article only noted a recent update); confirm current status before relying on those timeframes.
- Exact widget-build paths beyond the Collab filter dialog were not shown in screenshots - most metrics are added via standard [[reporting]] / [[engagement-dashboards]] metric pickers.
- Asset/post-level reporting links back to published content in [[asset-manager]] and [[publishing]].

## Sources
- Instagram Post Insights - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-post-insights/63e4836055780d70a15be947
- Instagram Account Insights - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-account-insights/63e3868fa9d5117903016637
- Instagram Story Insights - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-story-insights/63e484e8a9d51179030175d5
- Instagram Reels Insights - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-reels-insights/63e48630a9d51179030175d9
- Instagram Collab Posts Reporting - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-collab-posts-reporting/66f27ba6e15cf8648e87dfb7
- Instagram Historical Backfill Capabilities and Limitations - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-historical-backfill-capabilities-and-limitations/63e384a2a9d511790301662e
- Instagram Data Sync Frequency - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-data-sync-frequency/63e384a055780d70a15bd9ba
- Instagram User Insights API Changes - https://www.sprinklr.com/help/articles/reporting-glossary/instagram-user-insights-api-changes/668546d1679a1c4c5c780ae5
