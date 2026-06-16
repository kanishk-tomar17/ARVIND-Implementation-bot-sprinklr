# X — Advanced Publishing (Sprinklr Social — X (formerly Twitter))
**Source:** sprinklr.com/help — X (formerly Twitter) channel (multiple articles; see links below)

## What it is
- Advanced X publishing capabilities in Sprinklr beyond a standard tweet: video monetisation, long-form Pro Media video, threaded tweets, dark posts, reply controls, @-mentions, and X cards built from DAM assets.
- Most of these are configured inside the **Create Post** publisher window (or Quick Publish) on a selected X account.
- Several features need account prerequisites (linked X Ads account, whitelisted handle) and some choices are irreversible once published.
- Relevant across [[publishing]], [[engagement-dashboards]], [[rule-engine]], [[reporting]], and [[asset-manager]].

## Key features & how to use

### Monetise X videos
- **Prereq:** the organic X account must have an **X Ads account linked** to it and added in Sprinklr.
- In the **Create Post** publisher, tick the **Monetize this Video** checkbox (top-left of the post window) to reveal the **Monetization Options** panel.
- Fields (seen in publisher screenshots):
  - **Exclude Tags (optional)** — content categories to keep ads away from (e.g. Alcohol, Consumer Packaged Goods, Financial Services).
  - **Exclude advertiser @handles (optional)** — blacklist specific advertiser handles (e.g. @EvoltoborMKTNG).
  - **Monetize this video in these countries** (required, multi-select) — e.g. Australia, France, India, Canada.
  - **Tag Video Category** (required, multi-select) — best-fit categories (e.g. Digital Creators, Esports & Video Games, Entertainment & Pop Culture).
  - **Geo-restrictions** — radio choice of **None / Include / Exclude** at the bottom of the panel.
- Publish via **Post**, **Schedule Post**, or **Save as Draft**.
- **Limits:** monetisation can be enabled on a video post, but **once enabled and published it cannot be disabled**. Cannot select ownership links for matched content; bulk monetisation is not supported.

### Manage threaded tweets
- A thread publishes the **first tweet as a Post and every following tweet as a Reply** to the first.
- **Engagement Dashboards path:** build an Outbound column (Draft / Scheduled / Published) under Sprinklr Social > Engage; hover the post's **Options (…)** icon > **Preview**, then click **Show This Thread** to open the Third Pane and see every tweet. In the column cell, **only the latest message is visible** (each thread tweet shows "Show This Thread").
- **Editorial Calendar path:** open the Editorial Calendar; hover a thread post's **Options (…)** icon and choose **Preview** (the … menu also has Macro, Edit, Reschedule, Recall, Clone, Delete, View Workflows, Export Message, Schedule Action, Suggest, Boost Post, Open Details, Preview on a Rule). You can also **double-click** the thread to open the Third Pane.
- **Clone** copies the whole thread into the outbound column alongside the original.

### X dark posts
- **Dark posts** are tweets that do **not** appear on the brand's timeline — used for paid promotion/ads only. A dark post is **never published organically, only surfaced as an ad**.
- Use cases: A/B / split testing across audiences, keeping the timeline free of promotional clutter, targeting different audiences without posting publicly, and tracking engagement in [[reporting]].
- **Identify dark posts:** they show a specific dark-post icon; filter on **Is Dark Post = True** (unpublished/dark) vs **Is Dark Post = False** (published).
- **Rule Engine:** the **X Dark Update** action in [[rule-engine]] lets you post dark tweets automatically.

### X Pro Media (long-form video)
- Integrates X's Pro Media API for enhanced video publishing on **whitelisted @handles**.
- **Pro Media-only:** upload video up to **10:00** (vs standard 140 seconds), and access X In-Stream Monetization (sponsorships, pre-roll).
- **Available to all accounts (Pro and non-Pro):** video title & description, CTA with URL, custom thumbnail, embedded-tweet playback permission, geographic playback restrictions.
- **Specs — Pro Media vs Standard video:**
  - File size: **1 GB** vs 512 MB
  - Duration: **10:00** vs 2 min 20 sec
  - Bitrate: 60 Mbps (both)
  - Resolution: 2160x1080 vs 1900x1080
  - Frame rate: 60 FPS (both)
  - Access: Pro Media requires a **whitelisted @handle**; standard has no restriction.

### Choose who can reply to your tweet
- In **Quick Publish** (New Tab > Engage > Quick Publish), pick your X account in **Select Accounts**, then set the **"Who can reply to this Tweet"** dropdown.
- Options:
  - **Everyone** — anyone replies (followers only for protected accounts).
  - **People you follow** — only accounts you follow plus users you mention.
  - **Only people you mention** — only mentioned users.
- Then finish the post and click **Post**.
- **Limits:** the restriction is only visible once the tweet is live; it limits **replies only** (likes, retweets, poll votes stay open). You **cannot change the restriction after publishing** except by deleting the tweet. Replies/retweets inherit the root tweet's restriction; **quote tweets do not**. Deactivating the account temporarily lifts restrictions; reactivation reapplies them.

### Use X mentions in tweets
- In **Quick Publish**, select **one** X account in **Select Accounts** (Advanced Search available; pin frequently used accounts).
- Type your text in the **Message** box; a filling-circle indicator in the bottom-right tracks the character limit.
- To mention, type **@** followed by the name — a dropdown of matching accounts appears (verified X accounts are listed first, shown with the blue check). Click the account to insert it, then **Post**.

### Create X cards via DAM
- Build X card types from assets in [[asset-manager]] (DAM). Card types and key specs:
  - **X Image App Download Card** — image 800x800 (1:1) or 800x418 (1.91:1), max **3 MB**; requires Android + iOS app selections with deep-link URLs; CTAs: Shop, Play, Order, Install, Book, Connect, Install Open, Open.
  - **X Image Conversation Card** — same image specs; **Tweet to Unlock** reveals extra content after engagement; includes a cover-media field (when unlock is on).
  - **X Video App Download Card** — video max **1 GB**, duration 2 min 20 sec; codec H264 Baseline/Main/High; bitrate 6000K–10000K (1080p) / 5000K–8000K (720p); 29.97 or 30 FPS.
  - **X Video Conversation Card** — resolutions 720x1280 (portrait), 1280x720 (landscape), 720x720 (square); min bitrate 5000 kbps; H264 High Profile.
  - **X Video Website Card** — 16:9 or 1:1; same bitrate/codec as video app-download card.
  - **Carousel variants (Website / App / Video)** — multiple images/videos, max **6 cards**; website carousels min 800 px wide; video carousel files under 30 MB.
  - **Multi-Destination Cards** — up to 6 carousel cards, each with its own headline and URL.

## Common issues & fixes
- **Can't disable monetisation:** once enabled and published it is permanent — disable before publishing or do not enable.
- **Account group won't publish to X:** selecting an account group with multiple X accounts will fail to publish; X allows **only one account per post**. Multi-X-account selection is unavailable in the publisher.
- **Reply restriction can't be changed:** after publishing, the only way to change reply permissions is to delete and re-publish the tweet.
- **Only one thread tweet shows in a column:** expected — open Preview / Show This Thread to view all tweets.

## Notes & gaps
- **Prerequisites:** linked X Ads account (monetisation), whitelisted @handle (Pro Media), DAM assets meeting spec (cards).
- Dark-post article returned text only (blob image URLs) — no UI screenshots; X Cards article had no images.
- Exact navigation to build/select X cards inside the publisher is not detailed in the source beyond DAM specs; confirm in-environment.
- Pro Media/monetisation availability is gated by X program eligibility, not just Sprinklr config.

## Sources
- Monetise X Videos from Sprinklr — https://www.sprinklr.com/help/articles/advanced-capabilities/monetise-x-videos-from-sprinklr/64555f480104980882a54957
- Manage Threaded Tweets — https://www.sprinklr.com/help/articles/advanced-capabilities/manage-threaded-tweets/63f8d958e02459133724b1b0
- X Dark Posts — https://www.sprinklr.com/help/articles/advanced-capabilities/x-dark-posts/64555ef4e66f2e36b4512967
- X Pro Media — https://www.sprinklr.com/help/articles/advanced-capabilities/x-pro-media/63f8d5b8e02459133724b1a8
- Choose Who Can Reply to Your Tweet — https://www.sprinklr.com/help/articles/advanced-capabilities/choose-who-can-reply-to-your-tweet/63f4bb80e02459133724a6ba
- Use X Mentions in Tweets — https://www.sprinklr.com/help/articles/advanced-capabilities/use-x-mentions-in-tweets/63f8d72e9b334f7283b4dd70
- Create X Cards via DAM — https://www.sprinklr.com/help/articles/advanced-capabilities/create-x-cards-via-dam/64555e39e66f2e36b4512964
