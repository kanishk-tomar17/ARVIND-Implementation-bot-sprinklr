# Creator IQ (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Creator IQ channel (multiple articles; see links below)

## What it is
- Creator IQ is an enterprise influencer-marketing platform (discover, manage, measure influencer campaigns). This integration pulls Creator IQ campaign + post data into Sprinklr so you can **measure influencer performance alongside owned, paid and earned social** in one place.
- Connection is via a **single API key** (one per Sprinklr instance). Sprinklr subscribes to selected Creator IQ campaigns and ingests each influencer post as a Universal Message (treated as a **brand post**).
- **Read-only / analytics-only integration.** No channel actions — you cannot reply, comment, like or boost Creator IQ posts from Sprinklr. It exists for reporting and dashboards.
- Supported source networks: **Instagram, Facebook, X (Twitter), TikTok, Snapchat, YouTube, Pinterest**. Twitch is **not** supported.
- Currently "Phase 1": focus is consolidated reporting. See [[reporting]] and [[engagement-dashboards]].

## Key features & how to use

### Overview / enablement (what you get)
- Combines Creator IQ metrics with existing Sprinklr dashboards; apply Sprinklr's advanced reporting + visualization to influencer data without exporting/switching tools.
- **Enablement is gated** — an integration fee applies for existing Creator IQ customers. After the SKU is purchased, the Sprinklr account team activates the `[CREATOR_IQ_ACCOUNT_TYPE_ENABLED]` flag for the environment.
- A standard out-of-the-box dashboard, **Creator IQ Reporting**, is provided (customizable via Hyperdrive).

### Setup — add a Creator IQ account ([[owned-social-accounts]])
Prerequisites: active Creator IQ customer with API access; an API key from Creator IQ support (support@creatoriq.com / sales@creatoriq.com); the integration flag enabled by your Sprinklr Success Manager/Support.
1. Sprinklr Social → **Integrated Listening → Owned Social Accounts**.
2. Click **Add Account**. In the "Choose a channel…" search box type `crea` — **Creator IQ** appears as a channel tile (tabs across the top: All / Social / Ads / Messaging / Review / Others; Creator IQ shows under **All**). Select it.
3. **Add Creator IQ Account** panel:
   - **Api Key** (required) — paste the key into the "Enter Api Key" field (eye icon toggles visibility).
4. **Campaigns** section:
   - Click **Fetch Campaigns** to load campaigns from the connected account (empty state shows "No Campaigns" until fetched).
   - Select the campaign(s) to ingest. Optionally tick **Auto Subscribe** to automatically pull in future campaigns.
   - A "Added in Sprinklr" filter helps see what's already subscribed.
5. Click **Save**. This creates a master Creator IQ account plus per-network **dummy channel accounts**, e.g. *Creator IQ Facebook Account, Creator IQ Instagram Account, Creator IQ YouTube Account, Creator IQ X Account, Creator IQ TikTok Account, Creator IQ Snapchat Account, Creator IQ Pinterest Account.*
- Re-authentication (re-entering the key) does **not** lose historical data.

### Engagement dashboards ([[engagement-dashboards]])
- Each ingested post becomes a Universal Message tagged with: its **original network**, its **Creator IQ campaign**, and a **Creator IQ-specific message type** — e.g. *Creator IQ Instagram Post, Creator IQ Facebook Post, Creator IQ YouTube Post, Creator IQ X Post, Creator IQ TikTok Post.* These types let you isolate Creator IQ activity in dashboards, reports and rules.
- To plot Creator IQ posts in a column: create a column for the native network, e.g. **Add New Facebook Column** → in the source/type list, **Creator IQ Posts** appears at the **bottom** (below Inbox, Posts, Comments, Replies, Messenger, Events, Shares, Story, Group/Instagram/Dynamic post types). Select it, pick the **Creator IQ Facebook Account**, complete the remaining details, and the posts render in the dashboard.
- Posts also remain visible under their native social channel columns.

### Reporting integration ([[reporting]])
Prerequisites: Sprinklr Reporting module with admin/config permission; Creator IQ API key + campaign-data permission; authenticated ad accounts in Sprinklr if you want paid metrics.
- Data flow: API key connect → ingest campaign/post/engagement data → mapped to Sprinklr dimensions & metrics → filter by Creator IQ specifics (campaign, message type) → build custom reports mixing Creator IQ with other social sources.
- **Data coverage / timing:** **60-day backfill** by default; up to **48 hours** for initial data to appear; **daily refresh** thereafter. Includes posts that customers imported into Creator IQ.
- **Metric categories available:** Engagement (likes, comments, shares, engagement rate), Reach & Impressions, Audience actions (follows, profile visits), Video consumption (watch time, view duration), Monetization (revenue, playbacks). Exact availability is constrained by each platform's API.

## Common issues & fixes
- **No campaigns listed:** click **Fetch Campaigns**; if still empty, confirm the API key is valid and that the Creator IQ account has campaign-data permission.
- **Creator IQ tile missing in Add Account:** the `CREATOR_IQ_ACCOUNT_TYPE_ENABLED` flag isn't set — the SKU must be purchased and enabled by the Sprinklr account team/Support.
- **Inflated KPIs / double counting:** Sprinklr auto-detects matching native posts by network ID and marks the Creator IQ copy as a **duplicate**. Standard reporting aggregations ignore duplicates by default, so reach/engagement aren't inflated. If you build custom metrics, make sure they also exclude duplicates.
- **Comments not visible:** comment visibility is restricted to **paid partnerships or brand-tagged** content (platform API limitation).
- **Rules not firing on Creator IQ:** Creator IQ campaigns are **not supported in the Sprinklr [[rule-engine]]** — don't build assignment/automation rules off them.
- **New campaign not ingesting:** ingestion is campaign-scoped; either enable **Auto Subscribe** or update the account and re-fetch to add the new campaign.

## Notes & gaps
- Prerequisites: paid SKU + enablement flag, valid Creator IQ API key, appropriate Reporting/admin permissions, and (for paid metrics) authenticated ad accounts.
- **Web-focused** — Sprinklr mobile apps don't support this integration.
- One API key **per Sprinklr instance**.
- Read-only: no engagement actions on Creator IQ posts.
- Gaps not specified in source: exact metric API names/dimension IDs, retention beyond the 60-day backfill, and how Auto Subscribe handles campaign deletions. WebFetch returned only partial image lists and jina was rate-limited (HTTP 429), so image confirmation is from the 3 screenshots that downloaded (Add Account search, Add Creator IQ Account form, Add Facebook Column source list).

## Sources
- Creator IQ — Overview: https://www.sprinklr.com/help/articles/creator-iq/creatoriq-overview/695e5042f0afa271d1aecad7
- Creator IQ — Account Addition: https://www.sprinklr.com/help/articles/creator-iq/creator-iq-account-addition/695e503a6e42ec423235ad3f
- Creator IQ in Engagement Dashboards: https://www.sprinklr.com/help/articles/creator-iq/creatoriq-in-engagement-dashboards/695e54f4ed1e4535a50283ae
- Creator IQ Integration with Sprinklr Reporting: https://www.sprinklr.com/help/articles/creator-iq/creatoriq-integration-with-sprinklr-reporting/695e502bed1e4535a5023d12
