# TikTok — Overview, Setup & Capabilities (Sprinklr Social — TikTok)
**Source:** sprinklr.com/help — TikTok channel (multiple articles; see links below)

## What it is
- TikTok is a short-form video platform; Sprinklr connects a **TikTok Business Account** for managing owned organic content.
- In Sprinklr you can: add/configure the account, create and schedule video posts, engage on comments/replies/DMs/mentions, and report on account- and post-level metrics.
- **Only Business accounts are supported** — personal accounts cannot be added or published from.
- **Listening is NOT available** for TikTok due to TikTok's platform policies; only owned organic content reporting is supported. See [[listening]].
- All published content must be **original video** (no editing/deleting after publish, no Duet/Stitch).

## Key features & how to use

### TikTok overview (what Sprinklr supports)
- Core supported functions: account setup, content creation/publishing, audience engagement, column creation for organizing content. See [[publishing]], [[engagement-dashboards]].
- Detailed workflows live in the dedicated setup, capabilities, and best-practices articles below.

### Add a TikTok Business Account
Path and exact UI confirmed from screenshots:
1. Open a **New Tab** → under **Sprinklr Social**, go to **Listen → Owned Social Accounts** (opens the **Accounts (Settings)** window in the **Core & Social Cloud** workspace).
2. Click **+ Add Account** (top-right button; sits beside the existing accounts grid showing Status / Owner / User ID / Reach columns).
3. On the **"Add Account — Choose a channel you would like to add an account for"** screen, use the **Search** box or pick the **TikTok Business Account** tile (blue TikTok logo). You're redirected to the TikTok login pop-up.
4. **Log in** to TikTok: enter the account email and password → **Log In**.
5. On the TikTok **authorization** window: select the account(s) to grant permission, tick the **TikTok Platform Services Agreement** checkbox, then **Agree to Authorize**.
6. On the **Update <account>** details screen, configure:
   - **Account Details** — Account Name (required), UserId (auto-filled, read-only), Owner (required), Custom Character Count, Default URL Shortener.
   - **Groups to include Account in** — add to Account Groups (Select Groups).
   - **Permissions** — grant channel actions to users/user groups (publish, engage, report).
   - **Share this Account Across Spaces** — pick visible Workspaces.
   - **Subscribers** — users/user groups to notify on activity.
   - **Timezone** — country + time zone.
   - **Properties** — set account properties as needed.
7. Click **Save** (bottom-right).
- Requires **Admin access** to the TikTok Business account when adding. See [[asset-manager]].

### Capabilities & limitations
**Publishing (supported):** original video only; .mov/.mp4/.webm; min resolution 360×360; 23–60 fps; aspect 16:9 or 9:16; caption max **2200 characters (UTF-16)**; cover images/custom thumbnails; @mentions in captions; CML sounds. Rate limit: **2 videos/min, max 20 posts/day**.
**Publishing (NOT supported):** personal-account publishing; editing/deleting published posts; custom text/stickers; hashtags in captions; Duet/Stitch; AI-content disclosure; copyright checks.

**Engagement — content grabbed:** brand posts & comments, replies on brand posts, mentioned videos/comments, mentioned hashtags (must be registered with TikTok — beta), direct messages.
**Engagement — NOT grabbed:** brand reposts, liked videos, private video likes.
**Message actions** (all replies/comments **text only, max 150 characters**):
- Brand posts → Comment, Like, Hide, Reply
- Comments / Replies on brand posts → Like, Hide, Reply
- Mentioned videos → Comment; Mentioned comments → Reply
- Direct messages → Reply, Like (you can only **reply** to received DMs — cannot initiate DMs to fans)
**Engagement — NOT supported:** reporting comments, reposting videos, adding to favorites, embedding, cross-platform sharing, deleting fan content, tagging other Business users. See [[engagement-dashboards]], [[rule-engine]].

**Reporting (account-level, sync every 6 hrs):** total likes/comments/shares (daily), video views (daily), new followers/day, profile views/day, total followers (snapshot only), follower distribution by country & gender (needs 100+ followers), hourly active followers.
**Reporting (post-level — 0–10 days: every 3 hrs; 11–60 days: once daily):** views, likes, comments, shares, reach, watch-to-completion rate, total/avg watch time, impressions % by source, viewer % by country (top 10) — all with trends. See [[reporting]].
- All metrics include **both paid & organic**; paid cannot be segregated without Unified Analytics. Backfill up to 60 days; follower data is snapshot-only (no backfill).

### Best practices
- Add account with **Admin access**; verify users/groups have publish + engage permissions; add subscribers for activity alerts; file accounts into relevant **Account Groups**.
- **Pin** the TikTok channel for quick access; assign content to campaigns/sub-campaigns for tracking; **schedule** posts in advance. See [[publishing]].
- Recommended video specs: .mp4/.mov/.webm, max **1 GB**, **3–600 seconds**, min 360 px height/width, **23–60 FPS**.
- Engagement: avoid disabling comments unless needed; use **View Conversation** for full threads; assign comments/replies and update status via **Cases**; build **Listening Columns** to categorize comments (complaints, compliments, leads, etc.).
- Token refreshes automatically after 365 days — **re-add** the account when needed rather than deactivating.

### Data sync frequency
- **Account-level metrics:** every 6 hours (ongoing).
- **Post-level metrics:** posts 0–10 days old every 3 hours; posts 11–60 days old once daily.
- **Comments:** near real-time (a couple of minutes' delay).
- **Backfill:** account metrics up to 60 days prior to API request; comments backfilled for the most recent ~1,000 posts/comments (30-day default). Follower data cannot be backfilled (real-time snapshot only).

## Common issues & fixes
- **Metrics missing in dashboard:** post metrics refresh at **T+24 hrs (UTC)** from publish on TikTok's side; can extend to ~48 hrs for API-returned values.
- **Comment visibility delay:** expect **15–20 minutes** before a TikTok comment appears in Sprinklr; mentioned content arrives ~2–3 hrs late.
- **Photo/sticker comments:** photo comments fetched as **text only**; sticker-only comments appear **blank** (API limitation).
- **Cannot filter spam/offensive comments**, no keyword filters; livestream comments not fetchable and live moderators cannot be assigned.
- **Native changes don't sync:** password/username changes made directly on TikTok won't sync — **re-add** the account.
- **Account deactivates** when the refresh token expires after **365 days** — re-add to restore.
- **Brand mentions** (fans mentioning the brand) **cannot be fetched** — API limitation.

## Notes & gaps
- **Prerequisites/permissions:** TikTok **Business Account** + **Admin access** at add time; per-user publish/engage/report permissions set in the account's Permissions section.
- **Tokens:** access token refreshes **daily**; refresh token valid **365 days**.
- Hashtag-mention tracking requires registering the hashtag with TikTok (beta access).
- Paid vs. organic cannot be separated without Unified Analytics.
- Gaps: the **Overview** and **Capabilities** articles surfaced only decorative/note icons (no UI screenshots to view); the difference between a "Business account video" and an "authorized post" is referenced in the FAQ but not actually answered in the source.

## Sources
- TikTok Overview — https://www.sprinklr.com/help/articles/overview-tiktok/tiktok-overview/68317d93a6fe4f29b3d5eac2
- Add a TikTok Business Account in Sprinklr — https://www.sprinklr.com/help/articles/account-addition-tiktok/add-a-tiktok-business-account-in-sprinklr/68317d9b2a447159f7a6ffeb
- TikTok Business Capabilities and Limitations — https://www.sprinklr.com/help/articles/capabilities-and-limitations-tiktok/tiktok-business-capabilities-and-limitations/68317e3ca6fe4f29b3d5fd4e
- TikTok Best Practices — https://www.sprinklr.com/help/articles/know-more-tiktok/tiktok-best-practices/64525fe40d27fc559bbe535d
- TikTok Data Sync Frequency — https://www.sprinklr.com/help/articles/know-more-tiktok/tiktok-data-sync-frequency/67b488cc8bfab47e7c5e826c
- Frequently Asked Questions — TikTok — https://www.sprinklr.com/help/articles/know-more-tiktok/frequently-asked-questions-tiktok/645260250d27fc559bbe5376
