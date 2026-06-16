# LinkedIn — Publishing (Sprinklr Social — LinkedIn)
**Source:** sprinklr.com/help — LinkedIn channel (multiple articles; see links below)

## What it is
- One place to publish to LinkedIn **Profiles, Company Pages, and Showcase Pages** from Sprinklr — schedule, post, target audiences, and engage followers without switching to LinkedIn natively.
- All publishing happens in the **Create Post** window: open the **New Tab icon → Quick Publish** (under **Sprinklr Social → Engage**).
- Supports multiple message types per account: **Post, Poll, Event** (the **Type of Message** dropdown shows which are available for the selected account).
- Covers rich media (photos, multi-photo, video with captions, documents), reshares, @mentions, polls, and LinkedIn Events.
- See also [[publishing]], [[engagement-dashboards]], [[asset-manager]], [[rule-engine]], [[reporting]].

## Key features & how to use

### Publishing a standard post (text, photo, video, document)
- Open **Quick Publish**; the **Create Post** window opens.
- **Select Accounts** (required, marked with red dot) — search LinkedIn Profile or Company accounts; use **Advanced Search** (top right) to filter. A small channel chip (e.g. "Profile Post" / "Company Post") appears under the selected account.
- **Type of Message** dropdown — choose **Post** (also lists Poll, and Event where supported).
- **Share with** (Profiles only, required) — dropdown with **Public** or **Connections**.
- **Message** box — character counter shows remaining (Profile posts ~**3000**; Company posts shown as **1300** in UI). Tools:
  - `@` then a name to mention accounts (dropdown of matches appears).
  - `#` then text for hashtags (recently used surface).
  - **Insert** (⊕) icon — custom links, content placeholders, text templates, YouTube videos.
  - **Emoji Picker** (smiley) icon.
  - **Generate Web Analytics Links** dropdown for tracked URLs.
- **Link previews:** when you paste a link, a preview with **title + description** renders. Both are **mandatory** — the post won't publish if either is empty.
- **Media** (radio buttons: **Photo / Video / Document**):
  - **Photo** — **Select Photo** (Media Uploader) or **Upload Photo** (device). Up to **20 images** for a multi-photo post. **Alt text** field (max 4,086 chars; keep <120 recommended) sits beside the photo.
  - **Video** — **Video** / **Upload Video**. Hover the video thumbnail for icons: delete, download, and **CC (Add Captions)**. Use the Options (⋮) menu for **Change Thumbnail** (needs *Update Thumbnail* permission) and **Add Captions**. Optional title & description. Checkbox: **"Add the Call to Action & URL only if you plan to use this post as an Ad later"** → then pick a **Call to Action** and enter **Website URL**.
  - **Document** — from Media Uploader or device. Limits: PDF / PPT(X) / DOC(X) all **100 MB max, 300 pages max**. After upload you can edit post text but **not the document**.
- **First Comment** — optional text (links/names/promo allowed). **Cannot be used at the same time as Targeting.**
- **Add Targeting** — Company accounts only; mutually exclusive with First Comment (see Share Targeting below).
- **Campaign / Sub-Campaign**, **URL Shortener**, **Tags**, **Social Bars**, **Properties**, **Approval** (type + notes) — all optional config.
- **Preview** renders in the right pane (mobile/desktop toggle).
- Finish with **Post** (immediate), **Save as Draft**, or **Schedule Post** (pick date/time). Tick **Publish Another** to keep composing.

### Share Targeting (Company accounts only)
- Click **Add Targeting** to segment which followers see the post.
- **Each targeting segment needs a minimum of 300 connections** in that segment or the post fails.
- **Select from Saved Target Audiences** → check audience → **Add Selected**, OR **Create new Audience** with fields: **Function, Location** (Geography deprecated — Location gives county/city), **Industry, Language, Seniority, Company Size**, plus **Save this Target Audience for Future** checkbox → **Set Target Audience**.

### Reshare LinkedIn posts
- **Requires setup** — ask your Success Manager to enable it on the environment.
- Works for both Company page and Profile posts; you **cannot edit the original text or add/remove media** — you only add your commentary.
- Path: **New Tab → Engagement Dashboards** (Sprinklr Social → Engage) → **Add Column** (top right) → choose **LinkedIn** → column type **Company Status Update** → fill basic info → **Create Column**.
- In the column, open a post's **Options** icon → **Reshare** → type commentary in **Message** → **Post** (bottom right).

### Closed captioning for LinkedIn videos
- Add an **SRT** subtitle file to a video at publish time.
- In Create Post, add the video, then hover the thumbnail and click the **CC** icon (tooltip "Add Captions") — or use the video Options (⋮) → **Add Captions**.
- In the **Add Video Captions** popup: **Add New Language** → choose language from dropdown → **Add Captions files here** to upload the SRT → **Save**.
- **Only English** is available for caption uploads.
- A **CC toggle** later enables/disables captions when playing the video in Native and Inbound column views.

### LinkedIn Events
- Create and publish LinkedIn Events directly from Sprinklr (no native LinkedIn switch).
- **Account prerequisite:** **re-add the account** to grant two new permissions — **`r_event` and `rw_events`**.
- **LinkedIn Live eligibility:** 150+ followers/connections, account ≥30 days old, not available to mainland-China-based members/pages.
- In Create Post: **Type of Message → Event**. Fields seen in UI:
  - **Event Caption** (message, ~2970 char counter) with Insert/emoji tools.
  - **Upload or Browse Event Image**.
  - **Event type** (required): **Online** or **In-person**.
  - **Event format** (required) — e.g. **LinkedIn Live**.
  - **Event name** (required, e.g. max ~75 chars), **Timezone**, **Start date** / time.
  - For Online: event URL / platform (Zoom, Google Meet, Skype); for In-person: physical venue + address.
- Right pane shows the event card preview (date, "Online", **View Event** button). Finish with **Post**, **Save as Draft**, or **Schedule Post**.

### Mentioning LinkedIn profiles (posts, comments, replies)
- In the **Message** box (or a comment/reply), type `@` then the profile/company name → pick from the dropdown of matches.
- Same `@` flow works in **comments and replies** on LinkedIn content.
- Limits: only profiles with **prior interactions in Sprinklr** can be mentioned; profiles with **visibility filters** can't; **add mentions after** selecting the publishing account; company vs profile suggestions depend on the account type selected.

### LinkedIn Polls
- In Create Post: **Type of Message → Poll** (dropdown shows Post / Poll).
- **Post message:** max **3000** chars. **Poll question:** max **140** chars. **Options:** 2–4, each max **30** chars; duplicate options are rejected ("cannot add same options as a valid input").
- Pick **Poll Duration** from the dropdown.
- Publish via **Post / Save as Draft / Schedule Post** (set date/time → **Apply**); **Publish Another** to continue.
- **Engagement columns:** Inbound — Add Column → LinkedIn → *Company Status Update* or *Profile Network Update* → Media Type **Poll**. Outbound — Add Column → **Outbound** → Type **Sent** → Outbound Category **Poll**.
- **Rule Engine** ([[rule-engine]]): Manage Rules → Create New Rule → Scope *Customer/Workspace*, Context *Inbound*; outbound rules use Attachment type **Poll**, inbound rules use Message subtype **Poll**.
- **Editorial Calendar:** filter Channel = LinkedIn to view polls.
- **Digital Asset Manager** ([[asset-manager]]): Create Asset → Post → Channel **LinkedIn** → Type of Message **Poll**.

## Common issues & fixes
- **Post won't publish with a link** — link preview **title and description are mandatory**; fill both.
- **Reshare option missing / greyed** — feature needs enabling; contact your Success Manager.
- **Targeting post fails** — each segment must have **≥300 connections**; Targeting and First Comment can't both be used.
- **Captions not in desired language** — only **English** SRT is supported; file must be **.srt**.
- **Events not appearing as a message type** — re-add the account to grant **`r_event` / `rw_events`**; for LinkedIn Live, confirm 150+ followers, 30+ day-old account, and not China-based.
- **Document upload edits** — once a document is uploaded, the file itself can't be edited (only the post text).
- **Mention not suggesting a profile** — only profiles with prior Sprinklr interaction and without visibility filters can be @mentioned.

## Notes & gaps
- **Permissions:** *Update Thumbnail* permission needed to change a video thumbnail; LinkedIn Events need `r_event` + `rw_events` (re-add account). Reshare needs admin/Success-Manager enablement.
- **Limits captured:** photos ≤20; alt text ≤4,086 (recommend <120); documents 100 MB / 300 pages; poll question ≤140, options 2–4 ≤30 each; targeting segment ≥300 connections.
- **Unspecified:** exact native video size/length caps, photo file-size limits, full Showcase-page handling, and whether captions can be added post-publish are not stated in these articles.
- Character counters differ by surface in the screenshots (3000 vs 1300 vs 2970) — treat as account/message-type dependent and verify live.

## Sources
- Publishing on LinkedIn — https://www.sprinklr.com/help/articles/publish-on-linkedin/publishing-on-linkedin/64549d2ff65d86626c82b905
- Reshare LinkedIn Posts from Sprinklr — https://www.sprinklr.com/help/articles/publish-on-linkedin/reshare-linkedin-posts-from-sprinklr/64817e63723d925979db890e
- Adding Closed Captioning for LinkedIn Videos While Publishing — https://www.sprinklr.com/help/articles/publish-on-linkedin/adding-closed-captioning-for-linkedin-videos-while-publishing/64549d2df65d86626c82b904
- LinkedIn Events Publishing Support in Sprinklr — https://www.sprinklr.com/help/articles/publish-on-linkedin/linkedin-events-publishing-support-in-sprinklr/695e2007ed1e4535a5fdd06b
- Mentioning LinkedIn Profiles on Posts, Comments, and Replies — https://www.sprinklr.com/help/articles/publish-on-linkedin/mentioning-linkedin-profiles-on-posts-comments-and-replies/64549d2e0d27fc559bbeb485
- Create and Publish LinkedIn Polls from Sprinklr — https://www.sprinklr.com/help/articles/publish-on-linkedin/create-and-publish-linkedin-polls-from-sprinklr/64572d690104980882a57909
