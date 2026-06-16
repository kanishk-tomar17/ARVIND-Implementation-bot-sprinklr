# TikTok — Publishing & Engagement (Sprinklr Social — TikTok)
**Source:** sprinklr.com/help — TikTok channel (multiple articles; see links below)

## What it is
- How to publish to TikTok Business accounts from Sprinklr — both **Direct Publish** (Sprinklr posts for you) and **Publish Via Mobile** (Sprinklr hands off to the user's native TikTok app).
- How to add licensed audio from **TikTok's Commercial Music Library (CML)** to videos/photos at compose time.
- How to build **TikTok engagement columns** (brand posts, comments, replies, mentions, DMs) and act on incoming messages.
- How to **reply to direct messages** from TikTok profiles, and **track brand mentions** (videos/comments) in engagement columns.
- TikTok only supports **Business accounts** for publishing and most engagement; manual mobile publishing exists because TikTok limits API direct-posting. See [[publishing]] and [[engagement-dashboards]].

## Key features & how to use

### Create TikTok engagement columns (overview & creation)
- Path: **New Tab icon → Sprinklr Social → Engagement Dashboards (within Engage) → Add Column** (top-right).
- In **Add New Column**, search and select the **TikTok** tile as the content source (TikTok tile sits in the source grid alongside Twitter, WhatsApp Business, Web, etc.).
- In **Add New TikTok Column**, pick a **column type** from the list on the left.
- Fill: **Name**, **Description**, **Accounts** (select account/account group), and **Basic Information**; a live preview renders on the right.
- **Workflow Properties** — set message workflow status, user assignment, priority, spam flag, sentiment (applied automatically or manually).
- **Custom Properties** — include/exclude messages by the properties applied to them.
- Click **Create Column** (bottom-right) to finish.

### Publish to TikTok Business via Sprinklr (Direct Publish)
- Path: **New Tab icon → Sprinklr Social → Quick Publish (within Engage)** → **Create Post** window.
- Select a **TikTok Business account** in **Select Accounts** (use **Advanced Search** to filter). Window header shows a **TikTok Business Post** chip.
- **Publishing Type** radio: choose **Direct Publish**. (Note on screen: "TikTok supports manual publishing only through Business accounts.")
- **Caption** — up to **2000 characters**; **@-mentions capped at 30 characters**; **line breaks are NOT supported**. Use the **Insert** menu for custom links, placeholders, templates, YouTube videos; emoji picker available; Sprinklr AI+ assist available.
- **Media** — **Select Video/Media** (from Media Uploader / [[asset-manager]]) or **Upload Video/Media** from device.
- **Thumbnail** — must be chosen **from a video frame** (no external upload). Edit (brightness/saturation/exposure) requires the **Update Thumbnail** permission.
- Toggle off **Comments**, **Duets**, or **Stitches** as needed; add **First Comment**; assign **Campaign / Sub-Campaign**, **Tags**, **URL Shortener**, **Properties**, **Approval Type**.
- Publishing limits: **2 videos per minute**, **max 15 video posts per day**.
- Actions: **Post** now, **Save as Draft**, or **Schedule Post** (Calendar icon; **Smart Scheduling** checkbox). **Publish Another** to chain posts.

### Publish to TikTok Business via mobile app (Publish Via Mobile)
- In **Quick Publish → Create Post**, select TikTok account, then set **Publishing Type = Publish Via Mobile**.
- Enter **Caption** (line breaks not supported), pick **Select Video** or **Upload Video** for **Media**.
- **User to notify** (required) — choose the person responsible for publishing on the native TikTok app ("This user would be notified when the post has to be published on TikTok").
- Complete **Properties** (incl. **Campaign**); review preview on the right. Then **Post**, **Schedule Post** (Smart Scheduling), or **Save as Draft**.
- On the **Sprinklr Mobile App** (the notified user): tap the **Notification** icon → in **Details**, tap **Publish On TikTok** (bottom-left) → tap **Open TikTok** (opens native TikTok).
- In TikTok: tap **Create Post** → **Upload** (bottom-right) → select the video → **Next** (bottom-right). The caption is **auto-copied to the clipboard** to paste. Tap **Post** (bottom-right).
- Back in Sprinklr Mobile: open the notification → **Mark as Publish** → in the pop-up select the video → **Mark as Published** (bottom-right) to close the loop.

### Add music from TikTok's Commercial Music Library (CML)
- Purpose: attach **licensed/trending** audio to videos and photos to avoid copyright issues.
- Path: **New Tab → Quick Publish (Sprinklr Social, Engage)** → select TikTok Business account → enter caption → add media via **Photo or Video** (Media Uploader).
- After media is added, use the **Song Selection** box. Filter by **Country**, **Time Period**, **Genre**, and **Audio** selection.
- Limitation: **song-name search is NOT supported** — only **trending songs by country** are listed.
- Configure track: **duration, start time, volume, country, genre**; **trim** to a segment; **Play/Pause** to preview fit; adjust **Sound Volume** (up/down) and video volume independently.
- Audio **does not loop** — if the video is longer than the track, audio stops after it finishes.
- Finish: select **Campaign**, then **Post** / **Save as Draft** / **Schedule Post** (Smart Scheduling). **Publish Another** to continue.

### Engage with TikTok accounts (acting on messages)
- Pick a post in your engagement column, then use the action bar: **macros, assign, comment, archive**, plus **more options** (split into **Channel Actions** and **Sprinklr Actions**).
- **Channel Actions** (act on TikTok): **Like, Hide, Delete** (availability varies by content type).
- **Sprinklr Actions** (internal): Open Details, Reminders, Sentiment, Email, Suggest, Create Canned Response, Update Tags, Translate, Mark as Spam, Mark Secure, Create Case, Associate/Disassociate Cases, Preview on a Rule. See [[rule-engine]].
- Supported content types in engagement columns: **brand posts, comments on brand posts, replies on brand posts, mentioned videos, mentioned hashtags, direct messages**.
- **Not supported:** brand reposts, liked videos, mentioned comments; and **Report / Repost / Embed / Share on Social Media Channels** are unavailable for most content types.
- Action matrix by type: **brand posts** → comment, like, reply, hide; **replies on brand posts** → like, reply, hide; **mentioned videos** → comment only; **direct messages** → reply only.

### Engage with TikTok direct messages (DMs)
- Business accounts **cannot initiate** DMs; they can only **reply** to DMs from individual TikTok users.
- **Enablement required:** dynamic property `<TIKTOK_DIRECT_MESSAGE_ENABLED>` must be turned on — contact your Success Manager or tickets@sprinklr.com. Account must be a **Business Account**; accounts must be **re-added with native permissions** enabled.
- Build a **TikTok Engagement Column** of type **Direct Messages** in Engagement Dashboards.
- Reply flow: **New Tab → Sprinklr Social → Engagement Dashboards (Engage)** → select dashboard (Dashboard Menu icon, top-left) → find the TikTok DM (header shows e.g. "Direct messages (60)") → click the **Reply** icon in the message action bar → type in **"Enter your reply here..."** → **Save as Draft** or **Send**.
- Limits: up to **10 replies within 48 hours** of the last received message; **no image/media** in replies; **message-request folder** messages are not available; **rich text** formatting is supported; if a username changes the **account must be re-added**.
- **Regional restriction:** not available for brand handles registered in the **EU or UK**; cannot retrieve messages from EU/UK TikTok accounts to handles anywhere.

### Track TikTok brand mentions in an engagement column
- Sprinklr integrates TikTok's **Brand Mentions API** to pull videos/comments that mention the brand.
- Path: **New Tab → Sprinklr Social → Engagement Dashboards (Engage) → Add Column** → select **TikTok** source → **Add New TikTok Column**.
- Column type: **Video Mentions** or **Comment Mentions**. Enter **Name, Description, Account / Account Group**. Under **Category**, select **Video Mentions** or **Video Hashtag Mentions**.
- Set **Workflow Properties** and **Custom Properties** as needed, then **Create Column**.
- Mention columns/stats show **Like Count, Comment Count, Share Count** per inbound mention; comment mentions also show parent video and parent-video likes.
- All mentioned videos are **non-brand posts**. Display: **top 1,000** mentioned videos sorted by likes (legacy); **after 20 Jul 2025** all videos are retrievable with a **~2–3 hour delay**.

## Common issues & fixes
- **DMs not appearing / can't reply:** the `<TIKTOK_DIRECT_MESSAGE_ENABLED>` dynamic property isn't on (raise with Success Manager / tickets@sprinklr.com), the account isn't a Business Account, or it wasn't re-added with native permissions. EU/UK handles are unsupported entirely.
- **DM reply blocked:** you've hit **10 replies / 48 hours**, or you're trying to send media (text/rich-text only).
- **Mention video won't play:** only a **thumbnail** is shown — click the mention's **Timestamp** to open the video; thumbnails expire after **48 hours** (API limit).
- **Mention author shows "Anonymous User":** API limitation for parent-video comment authors; profiles may also duplicate (username-only retrieval).
- **Publish fails / throttled:** respect the **2 videos/min** and **15 posts/day** caps.
- **Caption renders wrong:** **line breaks aren't supported**; @-mentions over **30 chars** won't work; captions over **2000 chars** are rejected.
- **Can't set external thumbnail:** thumbnails must come from a **video frame**; editing needs the **Update Thumbnail** permission.
- **Can't find a song:** **name search is unsupported** in CML — filter by country/genre/time period among trending tracks only.

## Notes & gaps
- Publishing and most engagement require a **TikTok Business account** (personal accounts not supported).
- **Publish Via Mobile** depends on a human with the **Sprinklr Mobile App** and the native **TikTok app** to complete the post; the loop only closes after **Mark as Published**.
- Mention age restrictions: content from users **<17 in the EU / <13 elsewhere** isn't returned; **live videos/comments** are not supported.
- Several articles' inline images were **blob:/localhost** placeholders and couldn't be downloaded — UI detail here is reconstructed from the screenshots that did load plus article text.
- Exact field-by-field layout of **Workflow/Custom Properties** and the full Direct-Publish toggle set isn't fully imaged in sources; confirm in-environment before configuring for a client.

## Sources
- TikTok Business Columns: Overview and Creation — https://www.sprinklr.com/help/articles/create-columns-publish-on-tiktok/tiktok-business-columns-overview-and-creation/68317da42a447159f7a7003c
- Publish to TikTok Business (Sprinklr Space) — https://www.sprinklr.com/help/articles/create-columns-publish-on-tiktok/publish-to-tiktok-business-sprinklr-space/68317da2c74d2f1a73933b55
- Publish to TikTok Business (Mobile Application) — https://www.sprinklr.com/help/articles/create-columns-publish-on-tiktok/publish-to-tiktok-business-mobile-application/68317da00a718d29a578f484
- Engaging with TikTok Accounts — https://www.sprinklr.com/help/articles/engagement-in-tiktok/engaging-with-tiktok-accounts/68317e212a447159f7a7078d
- Engage with Direct Messages from TikTok Company Accounts to Profiles — https://www.sprinklr.com/help/articles/engagement-in-tiktok/engage-with-direct-messages-from-tiktok-company-accounts-to-profiles/68317e03c74d2f1a73934077
- Track TikTok Brand Mentions in Engagement Column — https://www.sprinklr.com/help/articles/engagement-in-tiktok/track-tiktok-brand-mentions-in-engagement-column/68317dacc74d2f1a73933bdc
- Add Music from TikTok's Music Library to Videos and Photos — https://www.sprinklr.com/help/articles/advanced-tiktok-capabilities/add-music-from-tiktoks-music-library-to-videos-and-photos/69b7a77d2c7db0530b551586
