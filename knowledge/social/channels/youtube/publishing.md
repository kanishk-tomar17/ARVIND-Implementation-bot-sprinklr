# YouTube — Publishing (Sprinklr Social — YouTube)
**Source:** sprinklr.com/help — YouTube channel (multiple articles; see links below)

## What it is
- How to publish and manage YouTube video content from Sprinklr's [[publishing]] composer (Create Post / Quick Publish).
- Covers full long-form video posts, YouTube Shorts, captions/subtitles, custom thumbnails, monetisation, and scheduling a video to be made private.
- All flows start from the Create Post window where you select a YouTube account, attach a video, and set YouTube-specific metadata (title, description, privacy, license, category, tags, playlist).
- Several actions are gated by account-type and role-level permissions (e.g. Update Thumbnail, Edit Privacy, Create Playlist).

## Key features & how to use

### Publish a post on YouTube
- Open the **Publishing Options** icon (top-right nav bar) → **Create Post**. (Quick Publish within Engage also works.)
- **Select Accounts**: search and pick your YouTube account; use **Advanced Search** to filter.
- Attach media: **Select Video** (from Media Uploader) or **Upload Video** (from device).
- Optional per-video edits on the video tile: **Add Caption** and **Change Thumbnail** (Change Thumbnail needs the *Update Thumbnail* permission).
- **Title** (≤100 chars shown as counter) and **Description** (≤5000 chars); emoji picker available in the content box.
- **Privacy** (required): dropdown controls visibility/viewership; tick **Set as default** to reuse.
- **License**: e.g. *Standard YouTube License* (dropdown).
- **Tags**: comma-separated tags for discoverability.
- **Category** (required): dropdown; tick **Set as default**.
- **Playlist**: select one or more (admins control which playlists are available).
- **Choose position of the video in playlist** → *Position of [playlist]* (e.g. **Top**). Position only takes effect if the playlist's **Default video order = "Manually sorted in YouTube"** (set in Playlist details → Visibility/Default video order).
- Checkboxes: **Notify your subscribers for this post**, **Embed your video for others to auto-play it in their sites**, **This video is made for kids**.
- Also available lower in the composer: **First Comment**, **Campaign** (+ **Sub-Campaign**, Set as default), **URL Shortener**, post **Tags**/Social bars, **Properties**, and **Approval** type + notes.
- Preview renders in the right pane (mobile/desktop toggle; expand via preview icon).
- Finish: **Post** (publish now), **Save as Draft**, or **Schedule Post** (pick month/date/time → Apply). Tick **Publish Another** to keep composing.

### Create and publish YouTube Shorts
- Prerequisite role: Social Media Manager or Publishing Supervisor.
- Use **Quick Publish within Engage** (New Tab icon → Sprinklr Social → Quick Publish) or Create Post.
- Select the YouTube account, then **Select Video** / **Upload Video**.
- Sprinklr auto-detects Shorts when media meets: **Duration ≤ 60 secs** and **Aspect ratio ≤ 1** (vertical/square). A "Video" / Short label shows on the tile.
- Set **Title**, **Description** (emoji picker available), **Privacy** (Set as default), **Category** (Set as default), **Campaign** (Set as default).
- Same publish controls: preview pane, **Post** / **Save as Draft** / **Schedule Post**, **Publish Another**.

### Add caption (subtitles) to a YouTube video
- In Create Post, after attaching the video click **Add Caption** (bottom-left of the video preview; also under the video tile's caption/thumbnail menu).
- In the **Add Video Captions** pop-up: click **Add New Language** → pick the language from the dropdown.
- Click **Add Caption file here** next to the language to upload the subtitle file.
- Click **Save** (bottom-right of the pop-up). "See Supported Formats" link lists accepted types.
- **Supported caption file types**: .SRT, .SCC, .SUV, .SBV, .SUB, .LRC, .MBSVP, .CAP, .RT, .VTT, .TTML, .DFXP.

### Change video thumbnails in a YouTube post
- Requires the **Update Thumbnail** permission (Publishing → Outbound Execution → *Update Thumbnail*).
- In Create Post, on the attached video open the tile menu and choose **Change Thumbnail** (next to **Add Captions**).
- In the Media Uploader, choose one of three sources:
  - **Prominent Frame** — an auto-selected frame from the video.
  - **Custom Thumbnail** — pick an existing asset from DAM ([[asset-manager]]).
  - **Upload Image** — add a new image from your device.
- Click **Use this frame** (bottom-right) to apply; the thumbnail updates immediately.
- Context note from Sprinklr: ~90% of best-performing videos use custom thumbnails.

### Monetise YouTube videos
- Prerequisites: the YouTube channel must have **rights management access** and be added via the authorised **content owner's Google account**; follow YouTube's monetisation policies.
- In Create Post, tick **Monetise this video** to expand **Monetisation Options**. Fields shown in the composer:
  - **Copyright Rule** (required) — select the upload/copyright rule (Monetise / Block / Track type policy).
  - **Content Category** (required) — e.g. asset type such as TV Episode, Film, or Web (enter related details).
  - **Monitoring Type** (required) — e.g. **Video only** (Content ID match scope).
  - **Include Territories** — search and select countries/regions to claim ownership in (or claim Globally).
  - **Exclude Territories** — select regions to exclude.
  - **Allowlist** — pages/channels to allowlist.
  - Optional: block the video outside owned territories.
  - **Advertising options**: Display Ads are on by default and cannot be deselected; add other ad types as needed.
  - **Video ad placement**: 8+ minute videos support pre-roll, mid-roll, post-roll; under 8 minutes supports pre-roll and post-roll only. For mid-rolls: **Create mid-rolls** → set timestamps → **Save**.
- Then publish normally.
- Limits: Ads Suitability cannot be set at publish time; **monetisation cannot be disabled once enabled and published**; **bulk monetisation is not supported**.

### Schedule a video to be made private (sunset public videos)
- Purpose: automatically turn a public video private at a chosen time via a **Scheduled Action** + [[macros]].
- **Part 1 — create the Macro**: New Tab → Settings → **Manage Workspace → Macros** → **Create Macro**.
  - *Apply Macro on* = **Outbound Message**.
  - *Automated Actions* = **Make Message Private**, *Value* = **Yes**.
  - Set sharing settings → **Save**. (Create a "Make Public" macro the same way for the reverse.)
- **Part 2 — schedule the action**: open the YouTube post in the **Editorial Calendar** → **Overview** (third pane) → **Schedule Action** (top of the third pane) → set execution time → select the macro → **Add**.
- The video flips to private automatically at the scheduled time. See [[rule-engine]] / [[publishing]] for related automation.

## Common issues & fixes
- **Playlist position has no effect** — the target playlist must use **Default video order = "Manually sorted in YouTube"** (set in YouTube/Playlist details). Otherwise YouTube ignores the chosen position.
- **Change Thumbnail option missing/greyed** — the role lacks the **Update Thumbnail** permission (Publishing → Outbound Execution).
- **Cannot monetise** — channel lacks rights management access or wasn't added via the content owner's Google account; once published, monetisation cannot be turned off, and bulk monetisation isn't available.
- **Caption upload rejected** — file must be one of the supported formats listed above.
- **Shorts not detected** — video must be ≤60s and aspect ratio ≤1 (vertical/square).

## Notes & gaps
- **Permissions**: Create Playlist, Attach Video, Delete Post, Delete Comment/Reply, **Edit Privacy** are YouTube account-type permissions; **Update Thumbnail** lives under Publishing → Outbound Execution (role-level). Set these in Setup → Users/Roles.
- Roles referenced for Shorts: Social Media Manager / Publishing Supervisor.
- Required fields in the composer: Privacy and Category (and Copyright Rule / Content Category / Monitoring Type when monetising).
- The monetisation field labels seen in the live composer (Copyright Rule, Content Category, Monitoring Type, Include/Exclude Territories, Allowlist) are slightly more specific than the older help text (Upload Policy / Content ID / Asset Type) — use the on-screen labels.
- Source articles are based on older (2023) UI screenshots; exact label wording may have shifted, but the flow and field set match the current composer.
- The "schedule made private" article text was recovered via the direct Sprinklr URL (jina returned 404); no usable screenshots were captured for that article.

## Sources
- Publish a post on YouTube — https://www.sprinklr.com/help/articles/publish-on-youtube/publish-a-post-on-youtube/641147de7517d84a3aaf6631
- Create and publish YouTube Shorts from Sprinklr — https://www.sprinklr.com/help/articles/publish-on-youtube/create-and-publish-youtube-shorts-from-sprinklr/641c590c55c4c33ae8b81558
- Add caption to a YouTube video — https://www.sprinklr.com/help/articles/publish-on-youtube/add-caption-to-a-youtube-video/6405e70232d12b63c5f56f57
- Change video thumbnails in a YouTube post — https://www.sprinklr.com/help/articles/publish-on-youtube/change-video-thumbnails-in-a-youtube-post/64008e9b32d12b63c5f560b3
- Monetise YouTube videos from Sprinklr — https://www.sprinklr.com/help/articles/publish-on-youtube/monetise-youtube-videos-from-sprinklr/645561920104980882a5495d
- Schedule videos to be made private — https://www.sprinklr.com/help/articles/publish-on-youtube/schedule-videos-to-be-made-private/6405e4df7a695d65a1606af1
