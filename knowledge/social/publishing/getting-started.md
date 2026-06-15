# Getting Started with Publishing (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- The core toolset for composing, scheduling, targeting, and publishing outbound content across social and non-social channels in Sprinklr Social.
- Two composers: the **Quick Publisher** (fast, scaled-down or maximized) and the **Advanced Publisher** (multi-section, document-style editor for richer content).
- A **Publisher Console** workspace that surfaces day-to-day publishing tasks (failed/rejected/pending posts) plus quick links to DAM, Campaigns, Engagement, and Reporting.
- Supporting capabilities at compose time: media upload, thumbnails, alt text, @-mentions, audience targeting/restrictions, URL shorteners, and a per-message Third Pane for quick actions.
- Mostly governed by **Dynamic Properties (DPs)**, **permissions**, and **mandatory-field** config — many features need a Success Manager / support ticket to enable. See [[rule-engine]], [[approval-workflows]], [[editorial-calendar]].

## Key features & how to use

### Quick Publisher — create a post
- Open: **New Tab icon** → **Publishing Options icon** (top-right of Navigation Bar) → **Create Post**.
- By default the **scaled-down** Publisher opens; click the **Maximize icon** (top-right) for the expanded Create Post window.
- **Select Accounts** field: search and select account(s).
  - Active and Inactive accounts shown separately (Active first); requires DP `PUBLISHING_DEACTIVATED_ACCOUNTS_VISIBILITY_ENABLED` (Success Manager to enable).
  - **Advanced Search** narrows accounts by filters.
  - **Pin** favorite accounts via the checkbox alongside them; unselect to remove the pin.
- Enter post content in the **Message box**. Use the **Insert icon** (bottom-left) to add Custom Links, Content Placeholders, Text Templates, or YouTube Videos. Use the **Emoji Picker icon** to add emojis.
- Add media: **Photo** (image/GIF) or **Video** → **Select Photo icon** opens the **Media Uploader**; or **Upload Photo/Video** / drag-and-drop from device.
  - Multiple images can be **re-arranged** after upload to set publish order (needs special setup via Success Manager).
- **Preview** renders in the right pane (Preview icon in scaled-down view). Click the **Desktop icon** (bottom-right of Preview) for desktop preview.
- Publish actions (bottom-right): **Post** (publish immediately), **Save as Draft**, or **Schedule Post icon** → pick **Time Zone**, month/date/time → **Apply**.
- Check **Publish Another** (bottom) to keep composing after posting.
- **Schedule recurring drafts:** in the scheduler, set **Repeat Post** = Does Not Repeat (default) / Daily for a Week / Weekly for a Month / Fortnightly for a Month / Monthly for a Year / Custom Repetition. Check **Notify me everywhere 30 minutes before** for reminders; **Custom Repetition** allows custom cadence/notifications → **Apply**.
- **Smart Scheduling:** picks best publish time by time-of-day and account; returns multiple recommended slots on a date and respects gaps with already-scheduled posts.
- **Enhanced error/warning system:** errors (image size, missing custom property, mismatched campaign) are surfaced and hyperlinked inside the draft for quick fixing.
- **Recommended Hashtags:** suggested for Instagram based on entered hashtags; First Comment box available for extra content/hashtags.
- **Post and Boost:** click **Post and Boost** to publish and boost in one step → fill details on the **Boost Post** pop-up → **Boost All Posts** (needs enablement via Success Manager).

### Advanced Publisher — create a message
Four-section, document-style composer.
- **Overview section:** Account Type (dropdown), Template (filtered by Account Type), Message Name (identification only), Campaign (with "Set as Default" checkbox), Sub-Campaign (appears only when a Campaign is selected), Source Language, **Is Message Confidential** checkbox (blurs content from unauthorized users), URL Shortener.
- **Content section:** rich text (bold, italic, underline, bullets, numbering, heading styles 1–2, hyperlinks), word count, change tracking/revision history, page outline, export editor content as HTML or PDF.
  - Channel options: Instagram Business **Direct Publish** checkbox (live) vs publish via mobile; Facebook & Twitter **Publish this Post as Dark Post** checkbox; verified Facebook Pages **Make this post Branded Content** checkbox + account selector.
  - Media sources: device upload, Asset Manager, User Generated Content; live preview updates in real time.
- **Scheduling and Targeting section:** account selection (required); **Repeat Post** options (same set as Quick Publisher); Schedule Date & Time + **Apply**; **Smart Scheduling** toggle; **Targeting** (segment to reach) and **Gating** (segment to exclude) via the Target Audience dialog → **Set Target Audience**.
  - Note: you can schedule a message outside the date range of the associated campaign/sub-campaign.
- **Review section:** read-only final preview; toggle Desktop/Mobile view; **Save as Draft** or **Schedule**. To edit, scroll back to the earlier section.
- See [[editorial-calendar]], [[asset-manager]].

### Publisher Console
- Consolidated publishing workspace. Open: **New Tab icon** → **Sprinklr Social** → **Publisher Console** (within Engage).
- **Left Rail:** quick links to DAM, Campaigns, Engagement Dashboard, Reporting; plus **Calendar** (full view of Campaigns, Events, Messages, Tasks — the [[editorial-calendar]]).
- **Create a post here:** Publisher Console → **Calendar** → **Create Post** (top-right) → fill details → **Post**.
- **Message Updates** (button, top-right) — tracks day-to-day tasks with eight tabs: Overview (top 3 per category, "Show all"), Failed, Rejected, Drafts, Pending (awaiting approval), Required (immediate attention), Scheduled, Published. Includes Search, Sort, Refresh; opening a post launches the Message Third Pane.
- DP-controlled (Success Manager / support ticket to enable). Relevant DPs: `PUBLISHER_CONSOLE_ENABLED`, `VIRALITY_ENABLED [CURRENT_USER_MESSAGE_UPDATES]`, `VIRALITY_ENABLED [OUTBOUND_GROUP]`, `PUBLISHER_CONSOLE_ENABLED_MODULES [CAMPAIGNS, AUDIENCE_MANAGER]`, `CURRENT_USER_MESSAGE_UPDATES_VIRALITY_ENABLED`.

### Message Third Pane (outbound messages)
- Snapshot + quick actions on a single outbound message. Opens from Production Dashboards, Editorial Calendar message cards, Engagement Dashboard outbound columns, and Campaign Detail Views.
- Tabs:
  - **Overview** — scheduled date, channel, templates, translation status, favorited properties, campaign details, collaboration snapshot, attachments, tasks; quick actions: Apply Macro, Edit, Delete, Clone.
  - **Properties** — all default + custom properties; edit custom fields.
  - **Collaborate** — team chat with @-mentions, replies, emoji reactions; edit/delete sent messages.
  - **Attachments** — view collaboration attachments (search/sort), add assets.
  - **Media** — images/videos with thumbnails, closed captions, title, description, alt text (needs special setup via Success Manager).
  - **Tasks** — assignee/assigner/due date/status; filter, sort, create; quick actions: Macro, Edit, Delete, Open Detailed View, Clone.
  - **Activity** — chronological user/system action history with timestamps.

### Social Planning & Publishing Persona App
- Centralized persona app for end-to-end planning and publishing; home dashboard summarizes post performance/engagement.
- **Left Navigation:** Calendar, Asset Manager, Publisher, Engagement dashboards, Reporting dashboards.
- **Home Page:** weekly performance/engagement widgets; shortcuts to favorite dashboards and campaigns.
- **Onboarding flow:** guided videos + in-platform practice with tracked progress (first visit or from home page).
- **Focused Dashboards:** shows only the user's selected engagement/reporting dashboards.
- Typical flow: Calendar → Asset Manager → Create Post → [[approval-workflows]] (if tiered approvals configured) → Reports → Inbox engagement → Campaigns → Audience Manager (segments for targeting) → User Generated Content. See [[web-analytics]].

### Upload media while publishing
- Available in Quick Publisher, Care Console, Agent Console.
- Open: New Tab → Sprinklr Social → **Quick Publish** → select account(s) → **Photo** or **Video** → Media Uploader → pick a tab → **Add** (bottom-right).
- Media Uploader tabs: **Favorites**, **Add from DAM**, **Upload Image/Video** (device or drag-drop), **Add from URL**, **Add from UGC**, **Dynamic Image** (templates or Quick Image Creator), **Media Valet**.
- **Import to Asset Manager** checkbox (bottom-left) saves uploaded media to Asset Manager (may need Success Manager config).
- Search/filter icons for DAM, UGC, Dynamic Image tabs; board selection for DAM/UGC.
- **Dynamic Image:** hover template → **Use Template** → fill details → **Apply**. **Quick Image Creator:** select canvas size → enter text → choose background → **Create Image**.
- Media Valet requires prior integration; shows asset metadata. See [[asset-manager]].

### Manage permissions for the Media Uploader
- Admins control which Media Uploader tabs distributed users see, via **user role permissions** + **Distributed Control Panel** (configured in the Enterprise platform).
- Permission → tab mapping:
  - **Desktop Upload** → Upload tab
  - **Sprinklr DAM** → Add from DAM tab + Favorites tab
  - **External DAM** → all external DAM tabs
  - **Add From URL** → Add from URL tab
  - **Dynamic Image** → Dynamic Image tab
- Add/remove permissions on new or existing roles; changes apply to assigned users.

### Preferred Audience and Audience Restrictions (Facebook)
- Facebook-specific audience controls. **Preferred Audience = Targeting**; **Audience Restrictions = Gating**.
- **Preferred Audience** — limits who sees the post **in their news feed** only. Non-matching users still see it on the brand page and in search.
  - Parameters vary by channel; unlimited countries; users must like/follow the page; relies on public profile info. Example params: Gender, Relationship Status, Age. Don't over-target (limited public data).
  - Use case: a large event — let all followers see it, but push it to the most relevant nearby audience.
- **Audience Restrictions** — limits who sees the post **everywhere** (news feed, brand page, search). Non-matching users cannot see it at all.
  - Parameters: **Location**, **Language**; capped at **25 countries** (Facebook limitation); users must like/follow the page; relies on public info. Example params: State, Language.
  - Note: the parameters chosen define who **can** see the post (like targeting), not who is excluded.
  - Use case: location-specific retail deals shown only to people in that area.
- Visibility matrix:
  - **No config:** visible on brand page, timeline, and search.
  - **Preferred Audience, fulfills:** all three; **doesn't fulfill:** brand page + search, NOT timeline.
  - **Audience Restrictions, fulfills:** all three; **doesn't fulfill:** none.

### URL shortener — expired / rate-limited
- Warns when a pre-selected shortener has hit its monthly API rate limit. Warning icon + message: the rate limit for the selected URL shortener has been exhausted; recommends switching shorteners to avoid publishing failure.
- Affects posts, comments, and replies. Third-party shorteners (e.g. Bitly) reset on the **first day of each month** and are limited by their pricing tier.
- Configure the shortener via the **Rule Engine** ([[rule-engine]]) or manually in Quick Publish.
- Recommended fix: use **Sprinklr's internal URL shortener** (no rate limits).

### Change / edit a video thumbnail
- Select a custom thumbnail for video posts via DAM or Publisher. Supports **MP4** and **WebM**; manual frame capture for **MP4 only**. Only available after upload completes and the default thumbnail shows.
- **Publisher method:** Quick Publisher → Create Post → select account + post type → add video → hover the default thumbnail → **Options icon** → **Change Thumbnail** / **Edit Thumbnail** → in Media Uploader pick the **Prominent Frame** (defaults to 0th second) → **Use this frame**.
- **Asset Manager method:** upload video to DAM → wait for thumbnail generation → **Change Thumbnail** (three-dot menu, top-right of video) → pick frame → **Use this frame**. See [[asset-manager]].
- Channel notes: Instagram & TikTok — thumbnail only from video stills; Facebook, LinkedIn, Twitter, YouTube — custom thumbnail selectable from the Media Uploader.

### Change the thumbnail image of a link
- Customize the link-preview thumbnail for **LinkedIn** or **Facebook** posts before publishing, in Quick Publisher.
- Add the link → preview auto-generates (if it doesn't appear, re-add the link; to change a link, remove the preview then add the corrected link).
- Hover the link thumbnail → **Change Image** → Media Uploader sources: Favorites, **Add from DAM**, Upload Image, Add from URL, Add from UGC, Dynamic Image, Media Valet → **Save** (bottom-right).
- Optional CTA button for Facebook links.
- Notes: Facebook supports static images only (DAM GIFs show first frame when published natively) and only thumbnails for domains verified natively on Facebook; LinkedIn supports pre-populated thumbnails, DAM images, device uploads, or image URLs.

### Add alt text to images while publishing
- Alt text = HTML description of an image; aids accessibility (screen readers), shows when images fail to load, and helps image SEO.
- Supported channels: X (**1000 char** limit), Facebook, Pinterest, Bluesky, Telegram, LinkedIn Company & Profile (**4086 char** limit; **<120 chars recommended**), LINE, Instagram, Threads. Media types: Photos, GIFs, Cards, Albums, Pins, DMs, Comments, Replies.
- **Quick Publisher:** upload image/GIF → type in the **"Write alt text here..."** field beside the photo (screen-reader only).
- **Response Publisher:** upload image → click the **alt text icon** (top-right of image) → enter text → **Save** → complete other fields → **Send**.
- **AI-generated alt text:** auto-generates platform-compliant descriptions in Quick Publisher, Full Screen Publisher, and Post Assets; customizable in AI Studio. See [[ai-in-publishing]].
- **Analytics:** "Is Alt Text Present" reporting dimension (Yes / No / Alt Text Not Supported). See [[web-analytics]].
- **Mandatory alt text:** brands can require it via Backend Configuration + Roles & Permissions, with user notifications for blank fields.
- Writing tips: avoid "image of"/"photo of", include color when meaningful, transcribe meaningful embedded text, read aloud to test, keep humor.

### Mention pages, handles, and profiles (@-mentions)
- Mention other pages/profiles/handles; mentions render as hyperlinks. Supported in Publisher for **Facebook, Twitter, LinkedIn**.
- **Quick Publisher:** select account → in Content type **@** + account name → pick from dropdown (verified accounts listed first) → repeat for multiple mentions.
- **Response Publisher:** find the comment/reply in the Engagement Dashboard → **Reply icon** → choose Account + Message Type → type response, then **@** + account name → select → repeat.
- Limitation: **Facebook Profiles cannot be @-mentioned** (API limitation) — only Facebook **Pages** can be mentioned in posts and replies.

### Mandatory fields in Quick Publisher
- Required fields are marked with a **red dot** and must be completed to publish.
- Field config:
  - **Select Accounts** — mandatory, not removable
  - **Content** — mandatory, not removable
  - **Campaign** — mandatory, not removable
  - **Advanced Search** — optional, removable
  - **Sub-Campaign** — optional, removable (permission controlled)
  - **URL Shortener** — optional, removable (permission controlled)
  - **Tags** — optional, removable (permission controlled)
  - **Social Bars** — optional, not removable
  - **Custom Properties** — optional, not removable
  - **Approval Type** — optional, removable (requires support ticket to remove)
  - **Approval Note** — optional, removable (requires support ticket to remove)
  - **Photo / Video** — conditional, depends on the channel
- See [[approval-workflows]].

## Common issues & fixes
- **Publishing fails on a URL shortener:** the selected shortener hit its monthly API rate limit. Switch shorteners or use Sprinklr's internal (no-limit) shortener; third-party limits reset on the 1st of the month. Set the shortener via Rule Engine or manually.
- **Inline draft errors** (image size, missing custom property, mismatched campaign): Quick Publisher surfaces and hyperlinks them in the draft — click to jump to and fix the issue.
- **Link preview not generating:** re-add the link to the message box; to change an existing link, remove the current preview first, then add the corrected URL.
- **Can't @-mention a Facebook user:** only Facebook Pages are mentionable; Profiles are blocked by the Facebook API.
- **Thumbnail can't be changed:** only possible after video upload completes and the default thumbnail is visible; manual frame capture is MP4-only; Instagram/TikTok limit thumbnails to video stills.
- **Alt text character limits:** X = 1000; LinkedIn = 4086 (keep <120). Some channels/post types do not support alt text ("Alt Text Not Supported").
- **Audience Restrictions hard cap:** max 25 countries (Facebook limitation).
- **Required field blocking publish:** a red-dot field is incomplete — fill all red-dot fields (Select Accounts, Content, Campaign at minimum).

## Notes & gaps
- Many capabilities are **DP-controlled or permission-gated** and need a Success Manager / support ticket to enable: Publisher Console and its DPs, Post and Boost, media re-arrange, deactivated-account visibility, Third Pane Media tab, Import to Asset Manager, and removal of Approval Type / Approval Note fields.
- Preferred Audience / Audience Restrictions documented here are **Facebook-specific**; Preferred Audience parameters "differ by channel" but the articles don't enumerate non-Facebook parameter sets.
- Media-uploader permissions are managed in the **Enterprise platform** via roles + Distributed Control Panel; the article gives no toggle-level UI path, limits, or troubleshooting.
- Channel-specific publishing steps (Facebook, Instagram, Twitter, LinkedIn, YouTube) are covered in separate articles not included here.
- Exact image/video size and file-format limits per channel are not specified in these articles (beyond MP4/WebM thumbnail support and alt-text character limits).
- AI alt text customization lives in **AI Studio**; configuration steps are out of scope here. See [[ai-in-publishing]].

## Sources
- Create a message using the Advanced Publisher — https://www.sprinklr.com/help/articles/getting-started-with-publishing/create-a-message-using-advanced-publisher/642edb4cc7dea832a77dcf55
- Create a post using the Quick Publisher — https://www.sprinklr.com/help/articles/getting-started-with-publishing/create-a-post-using-the-quick-publisher/642ea494c7dea832a77dcede
- Publisher Console — https://www.sprinklr.com/help/articles/getting-started-with-publishing/publisher-console/642ea48bc7dea832a77dcedc
- New Third Pane for Outbound Messages — https://www.sprinklr.com/help/articles/getting-started-with-publishing/new-third-pane-for-outbound-messages/650bd6f2cc94fb3f6632c58c
- Social Planning & Publishing Persona App — https://www.sprinklr.com/help/articles/getting-started-with-publishing/social-planning-publishing-persona-app/642ecd20c7dea832a77dcf32
- Upload Media While Publishing — https://www.sprinklr.com/help/articles/getting-started-with-publishing/upload-media-while-publishing/642ed179b7f3625d288e2f7d
- Preferred Audience and Audience Restrictions — https://www.sprinklr.com/help/articles/getting-started-with-publishing/preferred-audience-and-audience-restrictions/64555d1ee66f2e36b4512961
- Expired URL Shortener — https://www.sprinklr.com/help/articles/getting-started-with-publishing/expired-url-shortner/673c82402d57a62ef9f2df8a
- Change or Edit Thumbnails in a Video Post — https://www.sprinklr.com/help/articles/getting-started-with-publishing/change-or-edit-thumbnails-in-a-video-post/63feec197a695d65a160588c
- Change the Thumbnail Image of a Link — https://www.sprinklr.com/help/articles/getting-started-with-publishing/change-the-thumbnail-image-of-a-link/63feedf332d12b63c5f55c4c
- Adding Alt Text to Images While Publishing — https://www.sprinklr.com/help/articles/getting-started-with-publishing/adding-alt-text-to-images-while-publishing/64114fed7517d84a3aaf6641
- Mention Pages, Handles, and Profiles in Posts — https://www.sprinklr.com/help/articles/getting-started-with-publishing/mention-pages-handles-and-profiles-in-posts/63feef217a695d65a160588e
- Mandatory Fields in Quick Publisher — https://www.sprinklr.com/help/articles/getting-started-with-publishing/mandatory-fields-in-quick-publisher/63fee62f32d12b63c5f55c45
- Manage Permissions for Media Uploader — https://www.sprinklr.com/help/articles/getting-started-with-publishing/manage-permissions-for-media-uploader/6409d09e2680c35a78bb1b66
