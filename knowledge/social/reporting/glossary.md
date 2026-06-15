# Reporting Glossary (Metrics & Dimensions) (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- An in-platform reference tool that gives quick access to metric and dimension definitions across all channels without leaving your workspace.
- Distinguishes **metrics** (numerical measures: reach, impressions, engagement rate) from **dimensions** (categorizations: channel, account, date, region) used to build [[reporting]] widgets.
- Covers Sprinklr-defined metrics and native channel metrics for Facebook, X (Twitter), Instagram, YouTube, TikTok, LinkedIn and Threads.
- Lets consultants understand exactly what each metric counts, how trend data is derived, and how organic vs paid is split before building [[engagement-dashboards]].

## Key features & how to use

### Reporting Glossary tool
- Access: **Launchpad → Analytics section**, which opens the full metrics and dimensions list.
- Search the glossary via the search bar; tag metrics as **Favorites** to create a dedicated Favorites Tab.
- New or deprecated metrics are tagged for easy identification.
- **Export Consumption** — shows where a specific metric is used across dashboards and reports.
- **Export** — downloads metric names and descriptions.
- Filter by category: All metrics, New metrics, Deprecated metrics, Favorited metrics.

### Common metrics and dimensions (Social Analytics)
- **Account metrics:** Followers (all follower types across networks), Social App Tab Visits, Social App Widget Actions.
- **Post metrics:** Click Count Trend (clicks excluding known bots), Total Clicks (Bot + Non Bot), Clicks w/ Ref URL, Post Comments, Post Likes and Reactions, Post Reach (estimate of people reached), Engagement Rate (total engagements ÷ reach), Engagement Trend (likes + comments + shares), Estimated Clicks, Post Shares, Reach Rate (Post Reach ÷ followers at post time, %), Total Engagements (likes incl. reactions + comments + shares), Volume of Fan Messages Replied, Volume of Published Messages, Volume of Published Messages from Platform, Volume of Messages Resolved.
- **Dynamic date-range metrics:** Number of Days / Weeks / Months / Years in the selected range.
- **Account dimensions:** Account, Account ID, Account Group, Client, Client Group, Social Network, Social Stream (monitoring column name), Is Brand Message (Brand vs Fan), Date, Day Of Week, Month Of Year, Time Of Day (24-hour), Custom Property Visibility Scope, Social Apps Widget / Action / Type / Source URL.
- **Post dimensions:** Media Type (Photo, Video, Link, Album, Pdf, Document, Presentation, Mixed, Audio), Media Asset, Outbound Post, Outbound Post ID, Parent Post / Parent Post ID, Permalink, Link, Published Date, Is Parent Asset / Is Child Asset, Parent SAM Asset, Is Auto Imported, Post Video Length (duration buckets), Smart Response Indexes.
- **User dimensions:** User, User Group, Agent, User Current Status, Current Availability Status (Available, Busy, Not Available, On Break, Meeting, Away, Snooze), Login Current Status, Browser, Operating System, Device Type / Device Name, Assigned To User / User Group, Session ID, Email. Useful for [[care-console]] and [[sla-monitoring]] reporting.

### Social Analytics — Reporting Summary
- Documents, per platform (Facebook, X/Twitter, Instagram, YouTube, TikTok): which content types are captured (brand posts, comments, private messages, other messages), sync latency, data backfill limits, and refresh frequency.
- Example backfill: 2 years for Facebook posts; no limit for Twitter likes.
- Example Facebook refresh: every 100 mins for first 10 days, then once a day for the next 60 days.
- Core metric definitions: Impressions (times a post was displayed), Reach (unique people shown the post), Likes (likes + reactions), Comments (excluding replies), Shares, Total Engagements (likes + comments + shares).

### Understanding organic and paid metrics
- **Organic impressions** = times users viewed the post in their feed / brand timeline; **paid impressions** = times users were shown the post as an ad. Total = both combined.
- **Organic reach** = unique users who viewed via feed/timeline; **paid reach** = unique users shown the post as an ad. Total = both combined.
- **Engagement (likes/shares/comments)** is split by distribution: organic = fan engaged after viewing via organic distribution; paid = engaged after viewing via paid distribution. Kept separate so you can see which distribution drove the action.

### Understanding trend metrics
- Trend metrics (e.g. **Total Engagements Trend**) report activity based on the date the engagement **occurred**, not the date the content was published.
- Contrast with **lifetime metrics**, which show cumulative performance from publication date onward.
- Limitation: trend metrics and lifetime metrics are **incompatible** — they cannot be combined in a custom metric. Use separate widgets to avoid incomplete datasets / missing values.

### How Sprinklr calculates trend data
- Social channel APIs return only the current cumulative value, not daily history. So: **Daily Trend Metric = Current Total Value − Previous Day's Total Value.**
- Example: Day 1 total 100 → trend 100; Day 2 total 300 → trend 200; Day 3 total 500 → trend 200.
- Trend metrics are calculated for a post for as long as its lifetime data is updated — **60 days** for most social channels.

### Trend solutions
- Provide the **daily-level performance** of posts (e.g. daily impressions, video views) instead of only lifetime values.
- Handles **negative values:** when a lifetime metric decreases (e.g. impressions 4000 → 3900), a **curve-fitting algorithm** generates realistic daily values instead of showing a negative trend.
- Handles **missing data:** when API calls fail on some dates, gaps are filled using the same curve-fitting approach against the next complete lifetime value received.
- Caveat: after an API failure, accumulated gains can compound into a single spike on the day data is finally retrieved, inflating that date.

### Viewing sentiment on outbound posts and inbound messages
- Sentiment classifies tone as **Positive, Negative, or Neutral**, set by AI models; manual adjustment is possible for ambiguous language (e.g. sarcasm).
- **Outbound posts:** Reporting → Reporting Insights → hamburger menu → select Dashboard → Add Widget → widget type **Social Analytics**, category **Outbound Post** → add metrics **Count of Positive / Negative / Neutral Comments** → save.
- **Inbound messages:** Reporting → Reporting Insights → hamburger menu → Dashboard → Add Widget → widget type **Inbound Analytics** → add metrics **Sentiment, Volume of Fan Messages Replied, %Volume of Fan Messages Replied Within SLA, Volume of Public Fan Messages Replied** → save. Ties into [[sla-monitoring]].

### Message types in filters (outbound and inbound reporting)
- Filters let you scope reporting to specific channel message types, each with an inbound and outbound meaning.
- **Facebook:** Facebook Comment, Facebook Event Type, Facebook Instagram Ad Comment/Post/Reply, Facebook Messenger, Facebook Post, Facebook Replies, Facebook Share.
- **Instagram:** Instagram Comment, Comment Mention, Direct Message, Mention, Reply, Story, Tagged Media.
- **X (Twitter):** X DM, X Mention, X Reply, X Retweet.
- **YouTube:** YouTube Comment Reply, Playlist, Video.
- **LinkedIn:** LinkedIn Post, Company/Profile Comment, Company/Profile Reply, Profile Private Message, Group Post/Comment.
- **TikTok:** TikTok Video, Comment, Reply, Ad Comment/Reply.
- **General:** Update = inbound copy of posts published by the brand (and outbound brand posts).

### Flag sponsored posts in Reporting Insights (Is Sponsored)
- The **Is Sponsored** dimension flags paid/sponsored posts; displays **True** (sponsored) or **False** (not sponsored).
- Steps: New Tab icon → Reporting (under Sprinklr Social → Analyze) → Dashboard Menu → choose dashboard → Add Widget → set Widget Name / Description / Data Source → pick chart type → bulk add → in "Add a Metric or Dimension" pop-up choose **Is Sponsored** → Add to Dashboard.
- Detection rules: most channels flag sponsored when an ad account is connected; **Facebook** flags when Paid Impressions > 0; **YouTube** flags when ads-based metrics > 0.

### Account deactivation dimensions
- Available via the **Consumption Analytics** data source; used to track account inactivity and reasons for deactivation.
- **Account Deactivation Time** — timestamp of when the account was last deactivated.
- **Deactivation Reason** — reason for deactivation; shows "Account Active" for active accounts.
- **Last Added Time** — timestamp of when the account was last re-added.
- **Last Published Time** — published time of the last post published from the account.

### Reporting Insights — Is Deleted dimension
- The **Is Deleted** dimension identifies whether posts were deleted; values **True** / **False**.
- Use as a widget-level filter to surface data on deleted posts that would otherwise be hidden (deleted posts are removed from Sprinklr Reporting, which can cause discrepancies vs native channel numbers).
- Platform support: **Facebook, Twitter, YouTube** — fully supported. **Instagram, LinkedIn** — limited; their APIs don't expose deleted-post info, so deleted posts appear as normal and can't be distinguished.
- Refresh: deleted-post data is grabbed every **12 hours**, so a freshly deleted post may take up to 12 hours to reflect.

### Social reporting changelog (notable changes)
- **Facebook — 1 Oct 2024:** "Followers" metric corrected to pull from Facebook Page Follows (was Facebook Page Regional Likes); past data may show old value, backfills available via support; use "Facebook Page Likes" for global page likes.
- **Facebook — 16 Sep 2024:** 70 metrics deprecated (negative feedback, reach by locale/country/city/demographics, organic impressions, viral reach); historical data remains, deprecated metrics show zero in widgets.
- **Instagram — 8 Jan 2025:** "Instagram Video Views" deprecated (videos reclassified as Reels as of Nov 2023); six User Insights metrics deprecated (email contacts, direction clicks, profile views, text message clicks, website clicks, phone call clicks).
- **Threads — 11 Mar 2025:** added "Threads Post Total Shares" and "Threads Post Total Shares Trend".

## Common issues & fixes
- **Reporting numbers differ from native channel:** deleted posts are removed from Sprinklr Reporting; apply the **Is Deleted** filter, and allow up to 12 hours for deletions to reflect.
- **Trend metric shows a spike / inflated day:** likely an API failure that compounded gains into the recovery date; trend solutions' curve-fitting smooths most cases but recovery-day spikes can remain.
- **Negative or missing daily values:** handled by the curve-fitting algorithm in trend solutions; expected behaviour, not a config error.
- **Widget shows incomplete data / missing values:** you likely mixed trend and lifetime metrics in one widget/custom metric — split them into separate widgets.
- **Deprecated Facebook/Instagram metrics show zero:** expected after the Sep 2024 / Jan 2025 deprecations; historical data is retained. For the Facebook Followers correction, request a backfill from support.

## Notes & gaps
- Prerequisite for sentiment, sponsored-post and most steps: access to **Reporting / Reporting Insights** in Sprinklr Social (Analyze section); account deactivation dimensions require the **Consumption Analytics** data source.
- Metric/dimension availability varies by platform and by organic vs paid classification — confirm in the glossary before building a widget.
- The articles do **not** specify exact role permissions required to view or build these widgets, nor exact API rate limits.
- The Reporting Summary article lists per-platform sync latency, backfill and refresh values but only sample figures were captured here — consult the live article for the full per-metric table.
- The common metrics/dimensions list is representative, not exhaustive; use the in-platform glossary search for the complete, current list.
- Related GROOT topics: [[reporting]], [[engagement-dashboards]], [[data-engine]], [[sla-monitoring]], [[care-console]], [[rule-engine]].

## Sources
- About the Reporting Glossary — https://www.sprinklr.com/help/articles/reporting-glossary/about-the-reporting-glossary/63f87bade02459133724b104
- Social Analytics Common Metrics and Dimensions — https://www.sprinklr.com/help/articles/reporting-glossary/social-analytics-common-metrics-and-dimensions/6463490b30f12540268faa01
- Social Analytics Reporting Summary — https://www.sprinklr.com/help/articles/reporting-glossary/social-analytics-reporting-summary/6497d1cd564e3e25f803e848
- Understanding Organic and Paid Metrics — https://www.sprinklr.com/help/articles/reporting-glossary/understanding-organic-and-paid-metrics/6497ceccefca565f6513b27b
- Understanding Trend Metrics — https://www.sprinklr.com/help/articles/reporting-glossary/understanding-trend-metrics/63f88c34e02459133724b127
- How Does Sprinklr Calculate the Trend Data — https://www.sprinklr.com/help/articles/reporting-glossary/how-does-sprinklr-calculate-the-trend-data/63f8cc18e02459133724b195
- Trend Solutions — https://www.sprinklr.com/help/articles/reporting-glossary/trend-solutions/6405e1fa7a695d65a1606ace
- Viewing Sentiment on Outbound Posts and Inbound Messages — https://www.sprinklr.com/help/articles/reporting-glossary/viewing-sentiment-on-outbound-posts-and-inbound-messages/64634b238ea3c9635cf3673c
- Message Types in Filters for Outbound and Inbound Reporting — https://www.sprinklr.com/help/articles/reporting-glossary/message-types-in-filters-for-outbound-and-inbound-reporting/64e375a3c86d912cb59df424
- Flag Sponsored Posts in Reporting Insights — https://www.sprinklr.com/help/articles/reporting-glossary/flag-sponsored-posts-in-reporting-insights/646345098ea3c9635cf36731
- Account Deactivation Dimensions — https://www.sprinklr.com/help/articles/reporting-glossary/account-deactivation-dimensions/66459b82246f737ee712f912
- Reporting Insights Is Deleted Dimension — https://www.sprinklr.com/help/articles/reporting-glossary/reporting-insights-is-deleted-dimension/646342c830f12540268fa9e6
- Social Reporting Changelog — https://www.sprinklr.com/help/articles/reporting-glossary/social-reporting-changelog/66e800e3bb738a467048957b
