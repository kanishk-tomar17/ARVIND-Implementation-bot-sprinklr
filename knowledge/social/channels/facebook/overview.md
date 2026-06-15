# Facebook — Overview & Capabilities (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- Facebook is a core publishing + engagement + listening channel in [[sprinklr-social]], covering Facebook Pages and the separate **Facebook Workplace** channel.
- ~2.7B monthly active users; brands use it for reach, demographic/behavioural audience targeting, industry listening, and brand-to-brand collaboration (mentioning other Pages).
- In Sprinklr you can publish (text, images, video, links, live, dark/unpublished posts), engage (comments, replies, Messenger DMs), report on performance, and run/boost ads.
- Onboarding requires connecting a Facebook Page where your personal Facebook account has the **admin** role. Workplace is a distinct channel with its own capability set (groups, internal collaboration).

## Key features & how to use

### Why Facebook matters (use the channel)
- **Reach** — huge user base; listen and align social strategy to conversations.
- **Targeting** — target by demographics, behaviours, interests; **dark posts** let you test messaging without affecting brand image / public feed.
- **Insights** — mine conversations on posts, public groups and workplaces for industry trends and customer behaviour.
- **Collaboration** — mention other brand Pages in posts to lift visibility and reach.

### What you can do with Facebook in Sprinklr
- **Engage better** — use Smart triaging to auto-classify messages into categories: **Engageable, Enquiry, Lead, Compliment, Non-Engageable**; use [[macros]] for one-click multi-action; configure [[rule-engine]] rules to Auto-Respond to messages.
- **Publish creatively** — plan/schedule via the [[editorial-calendar]] (can be customised to view organic + paid in one view); publish live videos and carousel posts; apply audience targeting.
- **Analyse** — Facebook [[reporting]] dashboards measure likes/comments/shares/clicks, ad metrics (impressions, CTR, CPC, CPM); use to optimise posting frequency, timing, content type, ad spend.

### Facebook (Page) capabilities & limitations
- **Publishing supported:** single/multi-image, text, video, album, link posts; Facebook Stories and Live video (account must be 60+ days old, 100+ followers); alt text on photos; cover-photo updates; dark/unpublished posts; organic post targeting.
- **Engagement supported:** like posts; send/receive [[messenger]] DMs; comment, reply, delete, archive, suggest actions; view external mentions and user info; edit/delete published posts.
- **Reporting:** reaction counts, comments, shares, clicks, reach.
- **Ads:** boost organic posts; set CPM/CPA/CPC bids; create slideshow and canvas ads.
- **Limitations:**
  - Cannot post a Poll on a Page wall; cannot tag photos or create events (API limits).
  - Video comments post as a **link**, not embedded video.
  - Tagging individuals in posts cannot be done from engagement columns.
  - No real-time updates for dark posts or event engagements.
  - **24-hour messaging window** to respond to a person in Messenger.
  - Reporting data may lag **2–3 days** (API restriction); cannot export more than **10,000** audience profiles.

### Facebook Workplace capabilities & limitations (separate channel)
- **Engagement supported (groups):** view/reply/delete on Workplace Group posts, comments, and replies.
- **Monitoring — supported:** text/link post, photo/video, multi-photo, document, tagged user in post, note, poll (text only), achievement (text only), event, live video, check-in, activity (text only), feeling (text only), to-do (text only), mixed attachments, photo/text/link comments, comments with tagged profile, sticker & emoji.
- **Monitoring — NOT supported:** GIF post, Q&A post, rich-text post; video comments, GIF comments, document comments, rich-text comments.
- **Publishing:** publish a post (Yes); add image/video media (Yes); hashtags (Yes); emoji (Yes); edit published post (Yes); **@mention another Workplace group user — No**.
- **Character/limits:** post message **5000**; video title **255**; video description **1000**; image alt description **8000**.
- **Reporting:** post comments, post reactions, post seen, group-level metrics.

### Facebook best practices
- **Adding the account:** your personal FB account must have **admin** role on the Page. If an account is deactivated by token expiry, restore it by re-adding it.
- **Governance:** admin access authorises publishing, engagement fetch, and reporting; designate specific users/user groups for publishing vs engagement; add users to the **subscribers** list for activity notifications; organise Pages into [[account-groups]].
- **Publishing:** pin your Page in account selection; tag posts to campaigns/sub-campaigns for tracking; use scheduling; **verify domain ownership** to unlock thumbnail customisation and CTA buttons on shared links; apply demographic targeting for organic posts; add keywords + custom tags to videos for discoverability; monetise videos to claim ownership.
- **Engagement:** message access depends on account ownership/admin status; reply to comments as private messages from [[engagement-dashboards]]; respect the 24-hour Messenger window; filter columns to exclude own-brand mentions from external mentions.

### Facebook media guidelines
- **Images:** JPEG/JPG/PNG/GIF; file size 1 GB (post) / 8 MB (DM); aspect ratio 1.91:1 to 1:1; dimensions — image 2048x2048, shared links 1200x628, carousel 1080x1080.
- **Video:** recommended MP4/MOV (many others supported); file size 10 GB (post) / 25 MB (DM); aspect ratio 16:9 to 9:16; dimensions up to 4096x2048 (min 540x960, max 1080x1920); duration up to 4 hours.
- **Reels:** MP4/MOV; aspect ratio 9:16; duration 3–90 seconds.
- **Live video:** max 720p (720x1280) @ 30 fps; keyframe at least every 2 seconds; max bitrate 4 Mbps; H264 video + AAC audio; title under 255 chars; 4-hour max stream (regenerate stream key after 240 min); square pixel aspect, progressive scan, audio 44.1 KHz / 128 Kbps stereo, CBR.

### Facebook channel updates (changelog)
- **Jun 2024:** Facebook Live now requires account 60+ days old and 100+ followers.
- **Oct 2023:** Meta deprecated APIs for publishing organic carousel posts — option removed from Sprinklr.
- **Dec 2020:** Messenger API features unavailable for European pages/admins/EU users.
- **Nov 2020:** Guest Mode added (website visitors chat without FB login).
- **Oct 2020:** Facebook Offer Post publishing discontinued (API limits).
- **Oct 2019:** Three Messenger v4.0 features deprecated (location requests, List Templates).
- **Jul 2019:** Album/photo/video engagement features removed (API deprecations).
- **Jan 2019:** New non-viral impression/reach metrics added for pages/posts.
- **2018:** Various deprecations (Facebook Events, Profile publishing restrictions, Group reauthorization).

## Common issues & fixes
- **Posts publishing as dark posts unexpectedly** — happens when the Page was **not added by the admin**. Fix: re-add the Page with an admin account. Convert dark → normal post from the **Inbound** column.
- **Scheduled posts fail during a Facebook/API outage** — they must be **rescheduled** manually; they do not auto-retry.
- **Can't like/react to private Messenger DMs** — API limitation; not supported.
- **Can't publish Stories from Sprinklr** — API limitation; not supported.
- **Reporting numbers look stale** — expect a 2–3 day API delay before data settles.
- **Account deactivated** — usually token expiry; restore by re-adding the account.

## Notes & gaps
- **Prerequisites/permissions:** admin role on the Page is required to authorise publishing, engagement, and reporting. Live video needs an account 60+ days old with 100+ followers.
- **CTA buttons** on organic posts are only available for **carousel posts** and **link previews** (link CTAs require domain verification).
- **Carousel:** up to **10 cards** per post (note: Meta deprecated organic carousel publishing APIs in Oct 2023 — verify current availability in-platform).
- **Geo-targeting** works only when publishing from Facebook **Page** accounts.
- **No instructional UI screenshots** exist in these "Getting Started — Facebook" articles — they are text/table reference pages. Images present are decorative marketing hero banners and a small "dark post" glyph (verified, non-informative), so exact button positions/menu paths are not documented here; confirm UI labels live in the consultant's environment.
- FAQ article lists ~15 Q&As; the live source surfaced Q1–Q8 in full plus a note that Q9–Q15 cover Live streaming requirements, capabilities, and reporting strategy — review the source URL for those specifics.

## Sources
- Why is Facebook important? — https://www.sprinklr.com/help/articles/getting-started-facebook/why-is-facebook-important/63e9cf75ef1b447d6c61b20d
- What can I do with Facebook? — https://www.sprinklr.com/help/articles/getting-started-facebook/what-can-i-do-with-facebook/63ecd1bdef1b447d6c6306f5
- Facebook Capabilities and Limitations — https://www.sprinklr.com/help/articles/getting-started-facebook/facebook-capabilities-and-limitations/63ea4217f6e2cc7d18f96316
- Facebook Workplace Capabilities and Limitations — https://www.sprinklr.com/help/articles/getting-started-facebook/facebook-workplace-capabilities-and-limitations/63e9e10bf6e2cc7d18f9624d
- Facebook Best Practices — https://www.sprinklr.com/help/articles/getting-started-facebook/facebook-best-practices/63ec8f00ef1b447d6c62a21f
- Frequently Asked Questions — https://www.sprinklr.com/help/articles/getting-started-facebook/frequently-asked-questions/63e9dedfef1b447d6c61b21a
- Facebook Media Guidelines — https://www.sprinklr.com/help/articles/getting-started-facebook/facebook-media-guidelines/63e9e031f6e2cc7d18f9624c
- Facebook Channel Updates — https://www.sprinklr.com/help/articles/getting-started-facebook/facebook-channel-updates/63ec8cd6f6e2cc7d18fa540e
