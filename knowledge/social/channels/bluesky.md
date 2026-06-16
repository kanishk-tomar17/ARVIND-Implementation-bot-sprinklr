# BlueSky (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — BlueSky channel (multiple articles; see links below)

## What it is
- BlueSky is a decentralised, Twitter-like social platform. Sprinklr integrates it as a [[social]] channel for [[publishing]], [[engagement-dashboards]], profile actions, and [[reporting]].
- Publishing supported: text/link posts, photo posts, video posts, reposts, replies, and quote posts.
- Engagement supported: reply, repost, like/unlike, delete, and direct messages (DMs). Profile actions: follow/unfollow and mute/unmute.
- Grabbing (inbound): brand & fan quote posts, brand & fan reposts, new posts, liked posts, replies on brand posts, brand mentions, and DMs.
- Limitations: Feed and User-List columns do not support filters/sorting and the [[rule-engine]] does not apply rules to them. DMs are gated behind a dynamic property and are text/emoji only.

## Key features & how to use

### Setup — Add a BlueSky account
- Path: **Launch Pad > All Settings > Manage Customers > Accounts** (use the search box to find Accounts).
- Click **+ Add Accounts** > select **BlueSky**.
- Fill the two required fields (both marked required): **Username** ("Enter Username") and **Password** ("Enter Password"). These are the native BlueSky account credentials.
- Click **Submit**.
- Backend: the Sprinklr engineering team completes account addition (add request → mapping to account-addition API → add via operation call). For most clients this is handled during onboarding/account-mapping.

### Capabilities (channel matrix)
- Publishing: Photo, Video, Repost, Text/Link, Replies, Quote Post — all supported in Sprinklr.
- Message-level actions: reply, repost, like, unlike, delete, send DM.
- Profile-level actions: follow, unfollow, mute, unmute (and per capabilities matrix, block/unblock).
- Grabbing: quote posts (brand + fan), reposts (brand + fan), new posts, liked posts, replies on brand posts, brand mentions.
- Note: the publishing article lists Quote Post and DM as "not yet supported" inline, but dedicated articles exist for both — treat quote posts and DMs as available (DMs require the dynamic property below).

### Publishing — Publish a post
- Path: **Launch Pad > Sprinklr Social > Quick Publish** (under Publish in Engage). This opens the **Create Post** window.
- **Select Accounts** (required): pick the BlueSky account from the dropdown, or use **Advanced Search**. A live mobile preview renders on the right.
- **Message** field: type content; **Insert** menu adds custom links, placeholders, YouTube videos; AI+ assists with content/hashtag generation; emoji picker on the right. Character counter shows **300** remaining.
- **Generate Web Analytics Links** dropdown for tracked links.
- Media — toggle **Photo** / **Video**:
  - Photo: **Select Photo** / **Upload Photo**; **Write alt text here…** (alt text mandatory); per-image size limit shown as 1000000 (1 MB); **+ Add Another Photo**. Up to 4 images; PNG/JPG/WEBP; images taller than 2:1 are cropped.
  - Video: 1 per post; max 50 MB; 60 s; aspect 4:1 to 9:22; MP4/MPEG/WEBM/MOV; fixed thumbnail; no subtitles.
- Text limit: 300 characters, up to 8 hashtags.
- **Campaign** (required) and **URL Shortener** selectors; add tags / custom fields.
- Approvals: Not required / Required by Account Owner / Follows an approval path; optional approval notes + media.
- Footer: **Schedule Post** (date/time/timezone, repetition, smart scheduling), **Publish Another**, **Save as Draft**, or **Post** to publish now.

### Publishing — Quote post
- Path: **Sprinklr Social > Engagement Dashboards** > open a dashboard containing BlueSky content.
- On the post you want to quote, click the **ellipsis (…)** in the bottom-right of the post card > **Quote Post**. This opens the Create Post window.
- The quoted post appears embedded inside the **Message** field; add your own message above it.
- Complete post details/scheduling (same fields as standard publishing) and click **Post** (bottom right).

### Engagement — Add columns (Engagement Dashboards)
- Path: **New Tab > Sprinklr Social > Engage > Engagement Dashboards**. Either **Create Dashboard** (top right, fill fields, **Add**) or search an existing BlueSky dashboard.
- Click **+ Add Column** (top right) > search/select **Bluesky** in the Add New Column screen.
- The **Add New Bluesky Column** screen offers these column types in the left menu: **Inbox, Replies, Mentions, Reposts, My Posts, Liked Posts, Direct Messages, Lists, Feeds**.
- Common fields: **Name** (required), **Account / Account Group** (required), **Sort**, **Default Date Range** (e.g. Lifetime), **Campaign**, **Refresh Time**, **Column Color**, **Notify new Messages**, plus **Workflow Properties** and **Custom Properties** to filter messages. Click **Create Column** (bottom right). A live **Column Preview** shows on the right.

### Engagement — Reposts column
- Add Column > **Bluesky** > **Reposts**.
- **Name** field, then **Account / Account Group**.
- **Post Type** field with three options:
  - **All** — both brand and fan reposts
  - **Brand Post** — brand reposts only
  - **Others Post** — fan reposts only
- **Create Column**.

### Engagement — Feeds column
- Add Column > **Bluesky** > **Feeds**.
- Fields: **Name** (required), **Account** (required), **Bluesky Feed** (required — select the brand feed; preview shows on the right), **Default Date Range** (e.g. Lifetime), **Description**, **Refresh Time**, **Column Color**, **Notify new Messages**.
- **Create Column** to save.
- Limitation: filter and sort options do not work on Feed columns; the [[rule-engine]] does not apply rules to them.

### Engagement — Lists (grabbing user lists)
- Prerequisite: the user list must already exist on the native BlueSky channel before importing into Sprinklr.
- Add Column > **Bluesky** > **Lists** > fill required fields, set Workflow/Custom Properties to include/exclude messages > **Create Column**.
- Limitation: filters/sorting don't work on User-List columns; [[rule-engine]] rules don't apply.

### Engagement — Direct Messages (receive & reply)
- Prerequisite: dynamic property **`bluesky.direct.message.enabled`** must be turned on — request via your Success Manager or tickets@sprinklr.com.
- Add Column > **Bluesky** > **Direct Messages** tab > fill fields > **Create Column**. The DM column shows threaded conversations (sender, "Direct Me…" tag, timestamp).
- To reply: select a DM > **Reply** > the Reply Box opens > choose **Direct Message** from the dropdown (only available for eligible fan profiles).
- Limits: text + emojis only, up to **1000 characters**. Cannot reply if the recipient doesn't follow you, has DMs disabled, or has blocked you.
- Rate limit: global **3,000 API calls per IP address per 5 minutes**.

### Engagement — Profile actions
- From a BlueSky engagement column, select a profile and choose a profile action.
- Actions: **Follow / Unfollow** and **Mute / Unmute** (capabilities matrix also lists Block / Unblock).

### Engagement — Access feeds / reposts summary
- Both Feeds and Reposts are added via the same **+ Add Column > Bluesky** flow, selecting the matching column type from the left menu.

### Reporting — Glossary
- Reporting metrics for BlueSky, used in [[reporting]] / [[engagement-dashboards]] widgets.
- **Post Insights** (lifetime + matching trend versions, plotted against date):
  - BlueSky Post Total Likes / Likes Trend — likes on your post.
  - BlueSky Post Total Quotes / Quotes Trend — times your post was quoted.
  - BlueSky Post Total Replies / Replies Trend — replies on your post.
  - BlueSky Post Total Reposts / Reposts Trend — times your post was reposted.
- **Account Insights:**
  - BlueSky Profile Posts Count — total posts published from your profile.
  - BlueSky Profile Followers — total followers.
  - BlueSky Profile Followings — profiles you follow.

## Common issues & fixes
- **"Failed to fetch channel templates" in Create Post** — transient; click **Refresh** (seen in the publishing UI).
- **Can't reply to a DM** — recipient must follow you and have DMs enabled, and must not have blocked you; DM column requires `bluesky.direct.message.enabled`.
- **Filters/sorting greyed out on a column** — expected on Feed and User-List columns; rules don't apply there either.
- **DM send failures at scale** — respect the 3,000 calls / IP / 5-min rate limit.

## Notes & gaps
- Account addition requires native BlueSky username + password; backend mapping is done by Sprinklr engineering during onboarding.
- DMs gated by a dynamic property; raise via Success Manager or tickets@sprinklr.com.
- Profile-actions article only details follow/unfollow + mute/unmute steps; block/unblock appears in the capabilities matrix but exact UI steps aren't documented.
- The capabilities article's inline note marks Quote Post and DM as "not yet supported," which conflicts with the dedicated quote-post and DM articles — the dedicated articles are newer and authoritative; treat both as supported.
- Lists column requires a pre-existing native user list.
- Reporting glossary does not list engagement-rate or impressions metrics for BlueSky (none documented).

## Sources
- BlueSky Account Addition in Sprinklr — https://www.sprinklr.com/help/articles/bluesky/account-addition/6731ed61c5615c3695ee7aae
- Capabilities of BlueSky — https://www.sprinklr.com/help/articles/bluesky/capabilities-of-bluesky/671f5d001788a8794fea2941
- Publish a Post using BlueSky — https://www.sprinklr.com/help/articles/bluesky/publish-a-post-using-bluesky/671b8e772e64c74e572386fa
- Create and Publish a BlueSky Quote Post from Sprinklr — https://www.sprinklr.com/help/articles/bluesky/create-and-publish-bluesky-quote-post-from-sprinklr/67ff6cf48f20fd1afebc1274
- Create an Engagement Column in BlueSky — https://www.sprinklr.com/help/articles/bluesky/create-an-engagement-column-in-bluesky/67dac2f74f61f02eeba449be
- Access BlueSky Feeds in Sprinklr — https://www.sprinklr.com/help/articles/bluesky/access-bluesky-feeds-in-sprinklr/67ff6d1cde7b4670fb4961d8
- Grabbing User Lists in BlueSky — https://www.sprinklr.com/help/articles/bluesky/grabbing-user-lists-in-bluesky/67e52f08de7b4670fbad62c6
- How to Access BlueSky Reposts in Sprinklr — https://www.sprinklr.com/help/articles/bluesky/how-to-access-bluesky-reposts-in-sprinklr/67ff6d38ff9d5d60fd7d441c
- Receive and Reply to Direct Messages on BlueSky — https://www.sprinklr.com/help/articles/bluesky/receive-and-reply-to-direct-messages-on-bluesky/67e533d6906b9016978aa7a1
- Profile Actions on BlueSky Account — https://www.sprinklr.com/help/articles/bluesky/profile-actions-on-bluesky-account/67e53d93906b9016978b1801
- BlueSky Reporting Glossary — https://www.sprinklr.com/help/articles/bluesky/bluesky-reporting-glossary/67360de9c5615c3695f14b1a
