# Facebook — Publishing Posts (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- How to compose and publish every Facebook post type from Sprinklr's [[publishing]] tool (Publisher / Quick Publish → **Create Post**).
- One unified **Create Post** dialog: pick the account(s), pick **Type of Message**, add media/text, set properties (campaign, tags, approval), then Post / Save as Draft / Schedule.
- Type of Message dropdown options for Facebook Pages: **Post, Album, Carousel, Live Video, Cross Post Video, Reel, Story**.
- The right pane shows a live mobile/desktop preview; toggle device with the icons at bottom-right of the dialog.
- Bottom bar is consistent across types: **Schedule Post**, **Publish Another** (checkbox), **Save as Draft**, **Post**.

## Key features & how to use

### Create a Facebook Post (text / photo / video)
- Open the **Publisher** icon (top-right of the top nav) → **Create Post**. Select the Facebook Page under **Select Accounts** (use **Advanced Search** to filter). A blue **Page Post** badge confirms the post type.
- Set **Type of Message = Post**.
- Type the post in the **Message** box. Tag/mention Pages by typing `@` and picking from the dropdown.
- **Insert** icon (+) adds Custom Links, Content Placeholders, saved Text Templates, or YouTube Videos. **Emoji Picker** (smiley icon) adds emojis.
- Media: use the **Photo / Video** radio toggle, then **Select Photo/Video** (from Media Uploader / [[asset-manager]]) or **Upload Photo/Video** from device.
  - **Alt text**: type in "Write alt text here…" beside the photo. Photos/GIFs only (not video); read only by screen readers.
- **First Comment** field: auto-post a first comment (e.g. extra hashtags to boost reach); supports Insert + emoji; 10,000-char limit.
- **Add Another Media** to attach more; previews render in the right pane.
- Targeting: **Add Targeting** (preferred audience) / **Add Gating** (audience restrictions) — see [[targeting-gating]].
- Post-type flags (pick only ONE — the other two disable): **Dark Post**, **Draft Post**, **Native Scheduling** ("Schedule this post on Facebook Page").
- Properties: **Campaign** (+ Set as Default, + Sub-Campaign), **Tags**, **Social Bars**, **URL Shortener**, **Approval Type** + **Approval Note**.
- Finish: **Post** (publish now), **Save as Draft**, or **Schedule Post** (pick month/date/time → **Apply**). **Publish Another** keeps the composer open.

### Create a Facebook Video Post
- Same flow as Post; **Type of Message = Post**, then choose the **Video** radio. **Select Video** (uploader) or **Upload Video** (device).
- **Add Caption** (bottom-left of video preview) → **Add New Language** → pick language. SRT format only; keep ≤109 chars per subtitle group. Subtitles show only if the native account's locale matches the subtitle language code.
- **Change Thumbnail** (bottom-right of preview) → pick the **Prominent Frame** in the uploader → **Use this frame**. Requires the **Update Thumbnail** permission (Role Permissions → Outbound Execution).
- **Video Title** (255-char limit) and **Description** (no limit). If left blank, both default to the video file name.
- **Tags** field: custom Facebook tags to aid discovery.
- Monetization supported — see the "Monetise Videos from Sprinklr" doc.
- Same targeting / dark/draft/scheduling / campaign / approval / publish controls as a standard Post.

### Create a Facebook Album Post
- **Type of Message = Album** (badge: **Page Album**).
- **Album Name** (required) — pick an EXISTING album from the dropdown. **Album Description** field exists but is read-only.
  - API limit: you **cannot create a new album** or **edit the album description** from Sprinklr.
- Add images/GIFs via **Select Photo** / **Upload Photo**; add per-photo **description** ("Write photo description here…") and **alt text**.
- **Add Another Photo** for more images.
- Properties / approval / publish controls as standard.
- Reporting note: individual photos in the album are counted separately in [[reporting]].

### Create a Facebook Reel Post
- **Type of Message = Reel** (badge: **Page Reel**).
- You **cannot tag FB pages or profiles** on a Reel.
- **Select Video** / **Upload Video**. Hover the video → **Options** (3-dot) icon → **Change Thumbnail** or **Edit Thumbnail**. Thumbnail sources: DAM, UGC, or device.
  - Thumbnail max file size 10 MB; thumbnails only possible on videos already associated with a Page.
- **Description** box (10,000-char counter; Insert + emoji + AI assist). Optional **Generate Web Analytics Links**.
- Targeting, Dark/Draft (mutually exclusive with Native Scheduling), Campaign/Sub-Campaign, Tags, Social Bars, URL Shortener, Approval — same as standard.
- Publish / Save as Draft / Schedule as usual.

### Create a Facebook Live Video Post
- **Prereqs:** account ≥60 days old; Page/professional profile ≥100 followers; a **third-party streaming app** (OBS etc.) — Sprinklr mobile/desktop does NOT natively stream Live; you need Facebook access or task access.
- **Type of Message = Live Video** (badge: **Page Live Video**). Add Message + emojis.
- Enter **Video Title**, then copy the **Stream Key** and **Stream URL** shown below it (Stream URL is `rtmps://live-api-s.facebook.com:443/rtmp/`; each has a **Copy** button).
- Configure targeting / dark / draft / native scheduling / campaign / approval as usual.
- Publish / Save as Draft / Schedule. Scheduling a Live post triggers an announcement post to followers.
- In your streaming software: **Settings → Stream**, paste the **Stream Key** + **Stream URL**, then go live; the stream appears on the selected Page.
- It can take ~1 minute for the live video to pull into the Facebook API / Outbound column. It appears as an outbound post in [[engagement-dashboards]].

### Crosspost Live Videos on Facebook Pages
- Same prereqs as Live Video, PLUS: you must be an **admin** on the other Page(s) and have an established **cross-posting relationship** (set in Facebook); all primary + secondary Pages must be added to Sprinklr.
- **Type of Message = Live Video**, then tick **Enable Crossposting**.
- Under **Manage Cross Posting** (required field, type-to-search dropdown) select the secondary Facebook Pages.
- Enter **Video Title**; copy **Stream Key** + **Stream URL**. Rest of flow (audience, dark/draft/scheduling, campaign, tags, approval, publish) identical to Live Video.
- Stream from your software → the live video posts to the primary Page and crossposts to the selected Pages; appears in [[engagement-dashboards]] as an outbound post.

### Create a Facebook Cross Post Video (non-live)
- Prereqs: admin on the other Page(s); established crossposting relationship; all Pages added to Sprinklr.
- **Type of Message = Cross Post Video** on the PRIMARY Page.
- Select secondary Page(s) under **Manage Cross-Posting**.
- Add **Video** (uploader/device), optional caption + thumbnail.
- **Video Title** (255 chars) + **Description** (no limit); custom **Tags**.
- Title/description apply to all secondary Pages by default but can be edited per Page.
- **Schedule Post** lets you schedule the secondary posts SEPARATELY — secondary scheduling must be set AFTER the primary post's schedule.
- Targeting / campaign / tags / social bars / URL shortener / approval as standard. Post / Save as Draft / Schedule / Publish Another.

### Create a Facebook Branded Content Post
- For posts featuring a third-party brand/product/sponsor, per Facebook's Branded Content Policy. **Feature must be enabled — contact your Success Manager.**
- Both the publishing Page and the tagged sponsor must be **verified** Facebook Pages.
- **Quick Publish** icon → **Create Post** → pick a verified Page.
- **Type of Message = Post** or **Carousel**; add content.
- Tick **Make this post Branded Content**.
- Pick the sponsor under **Select Account for tagging** (verified accounts only). The tagged account is notified and can run ads using the post.
- Complete remaining fields as a normal Post; Post / Save as Draft / Schedule.

### Create a Facebook Story — via Mobile Publishing Flow
- For full-creative stories (stickers, text, drawing) that must be finished in the native Facebook app. Stories disappear after 24h.
- **Web composer:** New Tab → **Quick Publish** (Engage, under Sprinklr Social) → select Facebook account → **Type of Message = Story** → **Publishing Type = Publish Via Mobile**.
  - **Select Media / Upload Media** — max **15** assets (photos+videos combined).
  - Add description (+ emoji). **User to notify** = the person who will publish from mobile (must have native FB access on their device).
  - **Campaign is required** under Properties. Then **Post** (queues for mobile), Calendar icon → **Schedule**, or **Save as Draft**.
- **Mobile publish:** Sprinklr mobile → **Notification** icon → open the FB post notification → **Publish On Facebook** → **Open Facebook** → compose a Story (swipe up to pick the auto-downloaded media; caption is auto-copied to clipboard) → **Your Story** to publish. Back in Sprinklr → **Mark Post as Published** → confirm → **Mark As Published**.
- Mobile-app composer alternative: Menu → Publishing → select account → **Create Post** → **Story** template → **ADD FROM DEVICE / ADD FROM DAM** → Write Caption → Next → Optimize → Save as Draft / Publish.

### Publish a Facebook Story — via Direct Publishing
- Publishes the Story straight from Sprinklr, no mobile step. Stories vanish after 24h.
- New Tab → **Quick Publish** → **Create Post** → select account(s) → **Type of Message = Story** → **Publishing Type = Direct Publish**.
- **Media** (required) via **Select Media / Upload Media** — max **10** assets.
- **Campaign** + Sub-Campaign, **Tags**, **Social Bars**, **URL Shortener**, **Approval Type/Note**.
- Preview (Mobile/Desktop) → **Post**, **Save as Draft**, or **Schedule Post** (date/time → Apply). **Publish Another** to continue.
- **Media specs:**
  - Photos: .jpeg/.bmp/.png/.gif/.tiff; max 4 MB (.png recommended <1 MB).
  - Video: .mp4 (recommended), 9:16, 1080×1920 (min 540×960), 24–60 fps, 3–90 s (Page reels cap 60 s), codecs H.264/H.265/VP9/AV1, audio 128kbps+ stereo AAC 48kHz.

## Common issues & fixes
- **Can't create/edit an album in Sprinklr** — API limitation. Pre-create the album natively on Facebook; in Sprinklr you can only select an existing **Album Name** and cannot edit the album description.
- **Reel won't let you tag a Page/profile** — expected; tagging is unsupported on Reels.
- **Change/Edit Thumbnail greyed out or failing** — needs the **Update Thumbnail** permission (Role Permissions → Outbound Execution); for Reels, thumbnails only work on videos associated with a Page and ≤10 MB.
- **Video captions not showing** — must be SRT, ≤109 chars per group, and the native account's locale must match the subtitle's language code.
- **Live Video won't publish** — confirm account ≥60 days, ≥100 followers, third-party streaming software configured with the exact Stream Key + Stream URL, and FB/task access.
- **Crosspost target Page missing** — you must be admin on it and have an active crossposting relationship; the Page must be added to Sprinklr.
- **Live video slow to appear in Sprinklr** — normal; allow ~1 min to pull into the Facebook API / Outbound column.
- **Branded Content option not visible** — feature is gated; contact your Success Manager, and ensure both Pages are verified.
- **Direct Story limitations** — can't reuse media from prior posts; can't add stickers/overlay text/polls/questions/music (use the Mobile flow for those); video stories capped at 60 s; media may publish out of order (submit one at a time for controlled sequence; resharing unsupported).

## Notes & gaps
- **Dark Post / Draft Post / Native Scheduling are mutually exclusive** across Post, Video, Reel and Live types — selecting one disables the other two.
- Live Video and Cross Post Video publishing can be hidden for distributed users — contact Support.
- Live Video has no dedicated reporting metrics; filter standard Facebook [[engagement-dashboards]] by the assigned Campaign or Outbound Custom Field. You can route Live comments by building an inbound [[rule-engine]] rule on the outbound campaign. Threaded replies are unsupported on Live videos (appear as separate comments).
- Story media limits differ by flow: **Mobile = 15 assets**, **Direct = 10 assets**.
- Campaign is **mandatory** for the Story mobile flow; the notified user needs native Facebook access on their mobile device.
- Title char limits: video Title 255; descriptions/messages show a 10,000-char counter; video description itself has no hard limit per the article.
- Articles don't specify exact photo count limits per standard Post/Album or per-account publishing throttles.

## Sources
- Create a Facebook Post — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-post/63e9d69aef1b447d6c61b215
- Create a Facebook Video Post — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-video-post/63ea3b22f6e2cc7d18f96300
- Create a Facebook Album Post — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-album-post/63ea1ff0ef1b447d6c61b280
- Create a Facebook Reel Post — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-reel-post/63e9ddc0f6e2cc7d18f9624b
- Create a Facebook Live Video Post — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-live-video-post/63ea453eef1b447d6c61b2e2
- Crosspost Live Videos on Facebook Pages — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/crosspost-live-videos-on-facebook-pages/6641c8e31bca4f6f747fddf8
- Create a Facebook Cross Post Video — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-cross-post-video/63ec4fc9f6e2cc7d18f9f314
- Create a Facebook Branded Content Post — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-branded-content-post/63ec4c3aef1b447d6c623d79
- Create a Facebook Story Post via Mobile Publishing Flow — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/create-a-facebook-story-post-via-mobile-publishing-flow/646dfa2530f12540269000c6
- Publish a Facebook Story via Direct Publishing — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/publish-a-facebook-story-via-direct-publishing/6630c7bab95cec75ec7f57b7
