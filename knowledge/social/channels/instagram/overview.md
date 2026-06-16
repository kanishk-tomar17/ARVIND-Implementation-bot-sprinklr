# Instagram — Overview & Capabilities (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- Instagram is a visual photo/video sharing channel that Sprinklr integrates for publishing, engagement, advertising, e-commerce and reporting — all from one platform.
- Brands use it to increase reach (1B+ users, high visual engagement), drive commerce (shoppable stores, product tagging), and showcase brand personality (Stories, live events, influencer partnerships).
- Sprinklr connects to Instagram via Meta's Graph API, so capabilities are bounded by what that API allows — many gaps below are "API limitations," not Sprinklr bugs.
- Only **Instagram Business or Creator accounts** can be added (linked to a Facebook Page). Personal/profile accounts are not supported.

## Key features & how to use

### Why Instagram is important
- **Increase reach** — 1B+ users; visual-first design drives higher engagement than most channels; 1M+ brands active.
- **Drive commerce** — shoppable stores and product tagging enable direct sales; strong for influencer partnerships.
- **Showcase brand personality** — Stories and live events build trust and deepen customer relationships.

### What you can do with Instagram in Sprinklr
- **Customer engagement** — surface leads, complaints and inquiries; reply faster with canned responses/macros; use conversation history and Sprinklr AI to read intent. See [[engagement-dashboards]].
- **Publishing** — post all formats including Reels and Stories; run end-to-end campaigns. See [[publishing]].
- **Advertising** — create targeted ads with bid strategies inside budget limits. See [[advertising]].
- **Analytics & reporting** — pre-built and custom reports; organic, paid and listening data in unified dashboards; drill-down on metrics. See [[reporting]].
- **E-commerce** — sell via shoppable stores; add product tags to posts.
- **Influencer partnerships** — discover/partner with influencers; add personalized branding.

### Capabilities & limitations
Publishing (what Sprinklr supports):
- Publish **Post** with up to **10 images/videos** (Instagram native allows 20).
- **Reels** with thumbnail selected from a video frame; **Stories** with up to 10 images.
- Collaborative posts (Collab), Alt text on photos, and the option to **disable comments** on Posts and Reels.

Publishing restrictions (API):
- GIFs publish as **static photos**.
- **SRT captions cannot** be added to Reels.
- **IGTV (deprecated), Live Videos, and Broadcast channels** are not supported for publishing.

Engagement (supported):
- Comment on posts; reply to comments; view and send/reply to **DMs** (within a **7-day** message window); reply to **Instagram Live comments**.
- Community management: **hide/unhide** post comments, **delete** comments.

Engagement restrictions (API): cannot **like** posts/comments, **follow** users, **delete media posts**, **initiate** DMs, or fetch **Live Video reactions**.

Reporting limits: **Story data available 24 hours only**; post engagement counts pull, but complete native comment data does not. See [[reporting]] and [[benchmarking]].

Other limits: personal accounts can't be added; media posts can't be deleted via Sprinklr; native posts take **up to 10 minutes** to auto-import; reposting is unavailable.

### Media guidelines
Images:
- Formats: **JPEG/JPG or PNG**. Max size **8 MB** (posts and DMs).
- Aspect ratio **4:5 to 1.91:1** (or 3:4). Optimal: vertical 1440×1800, landscape 1440×754, square 1440×1440. Min width 320px, max width 1440px.

Videos:
- Formats: **MP4 or MOV**. Max **100 MB** posts / **25 MB** DMs.
- Aspect ratio 4:5 to 1.91:1 (Stories 9:16). Recommended dims: vertical 1920×2400, landscape 1920×1005, square 1920×1920.
- Duration: **3–60s** direct publish; up to **1 hour** via mobile flow.

Reels:
- Formats MP4/MOV up to **300 MB**. Duration **3s–15 min**. Ratio **9:16**.
- Technical: **23–60 FPS**, **25 Mbps** max bitrate, **128 kbps** audio bitrate, **AAC** codec (48kHz, mono/stereo).
- Best practice: use vertical **4:5** grid view rather than square 1:1 to avoid distortion.

### Best practices
Account setup (from the **Create Post** composer — Direct Publish requires a Business account):
- Account must be **business-oriented**, **linked to a Facebook Page with admin access**, and the user must hold the right permissions. Business accounts are preferred for full functionality.
- **Creator accounts with 500K+ followers** should convert to Business — the API will not fetch DMs for Creator accounts at ≥500K followers.

Governance & account management (from the channel config screens):
- Admin access is required to authorize publishing, engagement fetching and reporting.
- In the channel **Permissions** block, set per-action access via **Select Action** → users/user groups. Actions available: **All, Publish, Engage, View Reporting, Channel Action, View Planner**.
- Add relevant people to the **Subscribers** block (Users / User Groups) to receive activity notifications. See [[user-management]] and [[rule-engine]].

Publishing practices:
- Schedule content; use **3–4 hashtags** in the caption (up to **30** total including comments); use location tags.
- API caps posting at **50 posts per 24 hours** from first publish.
- Videos up to 60 min can be **3.6 GB** max via mobile publishing.

Engagement practices:
- DMs require the recipient to have messaged within **7 days**.
- System captures organic post comments; dark posts retrieve the **last 1000 posts and their comments**.

Composer UI detail (Create Post):
- **Select Accounts** (e.g. ACME Instagram) → choose message **Type of Message**: Carousel, Post, Reel, Story.
- **Publishing Type**: **Direct Publish** or **Publish Via Mobile** (note: direct publishing of photos/videos is Business-accounts only).
- **Photo**: **Select Photo** (from Media Uploader / DAM) or **Upload Photo**; add **Caption**.
- Media Uploader tabs include: Add Image from DAM, Upload Image, Add from URL, Add from UGC, Image Template, OneDrive/SharePoint, Google Drive, Add GIF from Giphy, Generate Image.
- Footer actions: **Schedule Post**, **Publish Another**, **Save as Draft**, **Post**. See [[publishing]] and [[asset-manager]].

### Channel updates (chronological highlights)
- **April 2025** — Meta Graph API **v22**: to receive usernames of Instagram **ad post** commenters, the account must be linked to a Facebook Page with **admin access to all three** (Instagram account, Facebook Page, Ad Account). Without this, comments are attributed to an **Anonymous Profile** and won't trigger case workflows. See [[case-management]].
- **June 2023** — video publishing to Instagram deprecated (replaced by Reels/Video media type).
- **July 2022** — Instagram **Reels** became publishable with reporting analytics.
- **January 2022** — **Live comments** viewable in the Engagement Dashboard.
- **October 2021** — **IGTV** support ended; user profile data expanded.
- **January 2019** — video publishing and hashtag search introduced.
- 2018–2020 — API deprecations affecting hashtag engagement, profile info access and personal-account support.

### FAQ (selected)
- **Like posts/comments?** No — API limitation.
- **Tag users in Reels/video?** No — only in **photo posts**.
- **Delete IG posts from Sprinklr?** No — API limitation.
- **Custom thumbnail on Reels?** No — can only pick a **frame** from the video/reel.
- **Share a Reel to feed?** Use **Share To Feed** in Quick publisher after uploading the attachment.
- **Links on a Story?** Swipe Up links are an API limitation; paste links in the description via mobile flow.
- **Polls/quizzes on Stories?** API limitation for organic — only available for **Story Ads**.
- **Location on carousel posts?** Not supported (works only via **Publish via mobile**).
- **Video/Reel durations:** videos 3s–60s direct / 3s–60 min mobile; Reels up to 15 min direct / up to 90s mobile.
- **IG Live not shared to feed?** Media not stored in Sprinklr, but appears on the Engagement Dashboard as a video thumbnail; **Live comments are fetched, Live reactions are not.**
- **Collab feature?** Supported for Posts, Carousels & Reels — tag the user first; max **3 collaborators**; they must accept the request.
- **Instagram Guides?** Cannot post/create — API limitation.
- **Historic data for Business Accounts?** No — Business Insights only for posts published after the account was linked in Sprinklr; no data for inactive/unlinked periods.
- **IGTV?** Deprecated — no longer supported as a media type.
- **Story Highlights?** Not supported in Sprinklr — deleting a story via editorial calendar does not remove it from native Highlights.
- **Account deactivation?** A Business account deactivates when the **refresh token expires**.
- **Business vs profile?** Check natively in Settings — a personal profile shows "Switch to Business Profile."

## Common issues & fixes
- **Ad commenters show as "Anonymous Profile" / no case created** — link the IG account to a Facebook Page and grant admin access to all three (IG account, FB Page, Ad Account) per Graph API v22 (April 2025). See [[case-management]].
- **DMs not fetching for a Creator account** — convert to Business if followers ≥ 500K (API will not fetch DMs otherwise).
- **Account suddenly deactivated in Sprinklr** — refresh token expired; re-authorize the account.
- **Newly posted native content not appearing** — auto-import takes up to 10 minutes.
- **Reels caption file rejected** — SRT captions are not supported on Reels (API limit).
- **GIF posted as a still image** — expected; GIFs publish as static photos.

## Notes & gaps
- Prerequisites: Instagram **Business/Creator** account linked to a Facebook Page; **admin access** for publishing, engagement and reporting; for ad-comment usernames, admin on IG + FB Page + Ad Account.
- Permissions are set per action (Publish, Engage, View Reporting, Channel Action, View Planner, or All) against users/user groups.
- Hard caps: 50 posts / 24 hrs; 7-day DM reply window; Story data 24h; dark-post history last 1000 posts.
- Not supported: liking, following, initiating DMs, deleting media posts, reposting, IGTV, Guides, Story Highlights, Swipe-Up links, organic Story polls/quizzes, Live reactions, custom Reel thumbnails, tagging users in Reels/video.
- Unspecified in sources: exact ads bid-strategy options, shoppable-store setup steps, and influencer-discovery workflow detail — confirm against current product UI.
- Minor source inconsistency: video duration upper bound stated as "1 hour" (media guidelines) and "60 mins" (FAQ) — treat as ~60 min via mobile flow.

## Sources
- Why is Instagram important? — https://www.sprinklr.com/help/articles/getting-started-instagram/why-is-instagram-important/63e36de355780d70a15bd943
- What can I do with Instagram? — https://www.sprinklr.com/help/articles/getting-started-instagram/what-can-i-do-with-instagram/63e3699355780d70a15bd91f
- Instagram capabilities and limitations — https://www.sprinklr.com/help/articles/getting-started-instagram/instagram-capabilities-and-limitations/63ec6a94f6e2cc7d18fa2297
- Instagram media guidelines — https://www.sprinklr.com/help/articles/getting-started-instagram/instagram-media-guidelines/63ec6c26ef1b447d6c6270a0
- Instagram best practices — https://www.sprinklr.com/help/articles/getting-started-instagram/instagram-best-practices/63e4bd4ea9d51179030176f2
- Instagram channel updates — https://www.sprinklr.com/help/articles/getting-started-instagram/instagram-channel-updates/63e37d22a9d511790301661d
- Instagram frequently asked questions — https://www.sprinklr.com/help/articles/getting-started-instagram/instagram-frequently-asked-questions/63e392cd55780d70a15bda0e
