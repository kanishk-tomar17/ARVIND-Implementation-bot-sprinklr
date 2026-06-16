# X — Overview, Account Types & Premium (Sprinklr Social — X (formerly Twitter))
**Source:** sprinklr.com/help — X (formerly Twitter) channel (multiple articles; see links below)

## What it is
- X (formerly Twitter) is a real-time public conversation channel — thousands of posts per second — used in Sprinklr for listening, engagement/customer care, and publishing.
- A single post can scale fast (reposts/retweets, polls, video), so it doubles as a brand-awareness and crisis-detection channel.
- Public @mentions make it a frontline support channel; the open nature also enables competitor and hashtag/topic tracking for competitive analysis.
- In Sprinklr, X is wired into [[engagement-dashboards]], [[publishing]], [[listening]] and [[reporting]]; ad/dark-post capabilities tie into [[advertising]] and [[asset-manager]].

## Key features & how to use

### Why X is important (use cases)
- Real-time trend monitoring — surface customer insights from high-volume conversation.
- Brand awareness — amplify via reposts, polls, and video.
- Customer support — monitor @mentions; reply quickly with personalized help.
- Competitive intelligence — track competitors via hashtags/topics and use the channel's competitive analysis.

### What you can do with X in Sprinklr
- **Audience insights** — listen to topics/trends; use demographics (interests, vocations); set automated alerts for crisis detection/management.
- **Respond to conversations** — pool direct + indirect mentions (keywords, hashtags) into [[engagement-dashboards]]; review past conversation history for context; speed up replies with macros and canned responses.
- **Publish content** — images, videos, polls, sponsored posts, and dark posts via Sprinklr's social [[publishing]] tool; supports monetization/content-ownership claims.

### X capabilities & limitations (limits and what's supported)
- **Text / character limit:** 280 characters default. URLs always count as 23 characters regardless of actual length. Photo/GIF/video attachments do NOT count toward the limit. Up to 10k characters when DP (extended posts) enabled; up to 25k with X Premium.
- **Photos:** max 5 MB; up to 4 photos per post.
- **Video:** max duration 140 seconds.
- **GIF:** max 15 MB.
- **Supported publishing:** X Threads (schedule + publish), X Polls, dark posts.
- **Engagement actions:** reply, repost/retweet, editable retweet (repost with comment), DM, like, favorite/unfavorite, delete; send/delete DMs and read DMs sent to the account; follow/unfollow; view audience profiles and recent posts.
- **NOT supported / API limitations:** Hide replies, Pin a post to profile, Publish to multiple X accounts, Quote tweet, Editing published posts, Unmentioning, Live video publishing.
- **X Premium (ads) capabilities:** Create + promote X Ads; bid on CPM, CPA, or CPC; bulk-import images/videos for ad creatives. Create/Preview X Cards (image ≤1 MB, min 800px wide × min 320px tall, aspect ratio 5:2 or 1.91:1).
- **API rate limits:** DMs — 200 per 15-min window (~19,200/account/day). Posts — 2,400/day. Following — 1,000/day (after 5,000 follows, capped by account-specific ratios). Account email changes — 4/hour. Search — 180 queries per 15 minutes; 180-character keyword-search limit per account.

### X media guidelines (creative specs)
- **Image formats:** JPG, PNG, GIF. Images up to 100 MB; animated GIFs up to 15 MB. Aspect ratio 2:1.
- **Image dimensions:** Animated GIF 1280×1080; Landscape 1280×720; Portrait 720×1280; Square 720×720.
- **Video formats:** MP4 and MOV (H.264 codec only). Max file size 512 MB.
- **Video aspect ratios:** Landscape/Portrait 16:9; Square 1:1.
- **Video duration:** beyond ~2m20s requires whitelisting; up to 10 minutes with Media Studio.
- **Audio:** must be AAC, Low Complexity profile. High-Efficiency AAC (HE-AAC) is NOT supported.

### X channel updates (deprecations to be aware of)
- **Sep 2023:** X Cards media/URL preview no longer supported without card IDs (API limitation). @mention discovery affected — the user/search endpoint for finding X handles was deprecated, no replacement timeline.
- **Jan 2019:** Deleted posts now show a visual indicator in the [[engagement-dashboards]] when tied to cases (profile + text removed per X API guidelines). Custom Audience manual upload deprecated (Ads API v3 → v4) — can no longer manually enter audience details for X Custom Audience creation.
- **Feb 2018:** Group Publishing to X is no longer supported (X anti-spam automation guidelines).

### Types of accounts on X
- **Verified — Gold checkmark:** authenticity for public figures, organizations, government bodies; free; priority in search results.
- **Premium — Blue checkmark:** subscription-based, price varies by country; open to anyone who pays; unlocks post editing, longer posts, reader mode for threads, and customization (e.g. color themes). Uses circular profile pictures.
- **Government — Grey checkmark:** free verification for official government accounts/officials; identifies official accounts for transparency; priority in search results.
- Distinctions: verified (non-premium) accounts use square profile pictures vs Premium's circular; only Premium enables post editing and extended character limits.

### X Premium and its three tiers
- Three tiers, each adding to the one below: **Basic → Premium → Premium+**.
- **Across all tiers:** Edit Post, Longer Posts (25k characters), Longer Video Uploads, Create a Community.
- **Basic:** Blue checkmark, Ads Revenue Sharing, Creator Subscriptions, Premium Gifting, Fewer Ads (~50% reduction), Reply to Verified-Only posts, ID Verification, Media Studio access, X Pro access.
- **Premium:** all Basic features, but "No Ads (occasional sponsored content)" replaces the ~50% ads reduction.
- **Premium+:** all Premium features plus Articles access.
- Caveat from the article: "this is indicative and is subject to change as per X policy" — confirm against X's official docs.

## Common issues & fixes
- **Can't preview X Cards / @mention lookup not working:** expected since the Sep 2023 API changes — preview needs card IDs; the handle-discovery endpoint is deprecated.
- **Can't publish to multiple X accounts / pin / hide replies / quote-post / edit a published post:** not bugs — these are X API limitations (see capabilities list).
- **Can't manually upload a Custom Audience:** deprecated with the Ads API v3→v4 migration.
- **Group Publishing to X missing:** removed in 2018 per X automation rules.
- **Video upload rejected:** check codec (H.264 only), audio (AAC LC, not HE-AAC), size (≤512 MB), and duration (whitelisting needed beyond ~2m20s; 10 min cap via Media Studio).

## Notes & gaps
- **Permissions/prerequisites unspecified:** the articles don't list the Sprinklr user permissions/roles needed to publish, engage, or run ads on X — confirm in the workspace's permission settings.
- **No pricing:** X Premium tier prices are not given (vary by country); tier features are "indicative" and change with X policy.
- **No UI screenshots:** these are conceptual/reference articles; the only images present are marketing/award banners (no menu paths or dialog screenshots to fold in). Exact Sprinklr UI click-paths for enabling X, configuring DP/extended posts, or setting up X Ads are not shown here — see the [[publishing]] and [[advertising]] KB for those.
- "Space" referenced in the capabilities article appears to denote a Sprinklr product surface/edition where certain actions (GIFs, favorite/unfavorite, follow/unfollow, X Cards creation) are available — scope not further defined in source.

## Sources
- Why is X important — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/why-is-x-important/63f49a5b9b334f7283b4d32e
- What can I do with X — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/what-can-i-do-with-x/63f49bc7e02459133724a674
- X Capabilities and Limitations — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/x-capabilities-and-limitations/640088a37a695d65a1605c92
- X Media Guidelines — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/x-media-guidelines/6400898132d12b63c5f56096
- X Channel Updates — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/x-channel-updates/64008a157a695d65a1605c96
- Types of Accounts on X — https://www.sprinklr.com/help/articles/types-of-accounts-on-x/types-of-accounts-on-x/67b6cddbb11591396c3097b2
- X Premium and Its Three Tiers — https://www.sprinklr.com/help/articles/x-premium-and-its-three-tiers/x-premium-and-its-three-tiers/67b6cd8a05f0a008a99f491d
