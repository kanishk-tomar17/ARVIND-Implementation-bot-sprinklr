# Advanced Publishing — Media & Video (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- Advanced media-handling capabilities inside the Sprinklr Publisher / Quick Publish flow for posts that include emojis, GIFs/stickers, images, and video.
- Covers expressive content (emojis, skin tone, GIFs/stickers), video handling (ProRes transcoding, in-line playback, caption preview), media optimization, and channel-specific compliance (TikTok branded-content disclosure, video monetization on Facebook/YouTube/Twitter).
- Most features live in the Create Post / Media Uploader interface; a few need Dynamic Properties (DP) flags or Workspace Role permissions enabled first.
- Use this as the reference when configuring how a client's posts render media across channels before publish. See also [[ai-in-publishing]], [[asset-manager]], [[editorial-calendar]].

## Key features & how to use

### Use emojis while creating posts
- Make text posts more expressive; emoji-rich posts tend to engage better.
- Steps:
  1. New Tab icon > **Quick Publish** (under Sprinklr Social within Engage).
  2. In the **Create Post** window, select account(s) (Advanced Search available for filtering).
  3. Compose content, click the **Emoji Picker icon** (bottom-right of the compose area).
  4. Finish and click **Post** (bottom-right).
- No character limits or permissions are stated for this feature.

### Choose your skin tone for emojis
- Sets a **default skin tone** applied to emojis in posts and emoji reactions.
- Steps (continues from the emoji picker):
  1. Open the **Emoji Picker icon** (bottom-right).
  2. Click the **Hand icon (✋)** in the bottom-right of the emoji menu and choose the default skin tone.
  3. Compose and **Post**.
- Selection persists as your default preference within Sprinklr Publisher.

### Publish GIFs and stickers (GIPHY / Tenor)
- Attach GIFs and Stickers from GIPHY/Tenor while creating or drafting posts.
- Steps to add:
  1. Add post content in the **Content** section, then click **Select Photo**.
  2. In the **Media Uploader** pop-up, select **Add GIF** (Tenor tab).
  3. Search or browse the GIPHY/Tenor tab (preview playability varies by channel).
  4. Click **Add** (bottom-right) to attach.
- Permissions (grant via Workspace Role):
  1. New Tab > **All Settings** (under Platform Setup).
  2. **Manage Workspace** > **Workspace Roles** > **Create Role** (top-right).
  3. Under Publishing, enable **Giphy Search** (for GIPHY) and **Tenor Search** (for Tenor).
  4. **Save**.
  - Role fields: **Role Name** (unique), **Description** (optional), **Select Permissions**, **Users/User Groups**.
- Notes:
  - GIFs count as image files; engagement shows under **Image Reporting Insights**. See [[web-analytics]].
  - Brand-specific GIF curation is available via your Success Manager.
  - GIF source depends on **Dynamic Publishing (DP)**: if DP is enabled, both GIPHY and Tenor are available; if not, only GIPHY.

### ProRes transcoding for videos
- Detects incompatible ProRes uploads and transcodes them to a channel-compatible format; final file lands within channel limits. Transcoding runs in the background.
- In Quick Publisher:
  1. Sprinklr Social > **Quick Publish** (within Engage).
  2. Pick account via **Select Accounts** field.
  3. Enter content in the **Message box**.
  4. Click **Video** to upload (Media Uploader or from computer).
  5. Click **Post**; when prompted about ProRes incompatibility, select the transcode option.
  6. Publishing is blocked until transcoding completes — but you can **minimize the window** and keep drafting other posts.
- In DAM (Digital Asset Management):
  1. Sprinklr Social > Asset > Engage.
  2. **Create Asset icon** (top-right) > select **Video**.
  3. Upload or drag-and-drop the file > **Save** in the Media Uploader.
  4. System auto-checks compatibility and transcodes; you're notified on completion.
  5. Fill in description and save in the **Create New Video Asset** window.
- Videos already transcoded in DAM can be published directly without re-transcoding. See [[asset-manager]].

### Play video assets while publishing
- Preview/play video directly in the Publisher or Media Uploader without going to DAM — works when adding videos from the Publisher and when responding to users.
- Controls:
  - **Play icon** (center of video) to start.
  - **Full-screen icon** (bottom-right of the video).
  - **Options icon** (bottom-right) menu:
    - **Download** — download the video file.
    - **Picture-in-Picture** — keep watching while browsing.
    - **Playback speed** — control playback speed during play.
- Media Uploader is available from the Publisher, response publishing, and DAM.

### Show caption preview for scheduled and draft posts
- Preview captions on video posts at the draft and scheduled stages, for **all video posts regardless of channel**.
- Available in: **Asset Manager**, **Editorial Calendar**, **Engagement Dashboards/Column**, and **Production Dashboard**. See [[editorial-calendar]].
- Steps:
  1. New Tab icon > go to where the draft/scheduled video lives.
  2. Double-click the video to play.
  3. Click the **Options icon** (bottom-right) and select **Captions**.

### Video monetization from Sprinklr (Facebook / YouTube / Twitter)
- Claim ownership of owned video content and control monetization/access at publish time.
- Account prerequisites:
  - **Facebook:** Page must have Rights Manager access (verify in Facebook Rights Manager). Enable DP flag **FACEBOOK_VIDEO_COPYRIGHT_ENABLED**. Then All Settings > Accounts > Edit the page > enable **Page is Authorized with Rights Manager Access to Monetise Facebook Videos**.
  - **YouTube:** Channel needs rights management access (verify via YouTube Monetization Policies). Enable DP flag **YOUTUBE_RIGHTS_MANAGEMENT_ENABLED**. Channel must be added using an authorized content owner's Google account.
  - **Twitter:** Requires a linked Twitter Ads account connected to the organic account.
- Facebook monetization at publish:
  1. Enable **Option to Monetize this Video**.
  2. Select a **Copyright Rule**.
  3. Choose **Content Category**: TV Episode, Film, or Web.
  4. Choose **Monitoring Type**: Video only, Video & audio, or Audio only.
  5. Define **Include Territories** / **Exclude Territories**.
  6. Add allowlisted Facebook Pages.
- YouTube monetization at publish:
  1. Enable **Option to Monetize this Video**.
  2. Select **Upload Policy** (Monetise / Block / Track).
  3. Activate **Content ID matching** and select a Match policy.
  4. Choose ownership scope: Global or specific territories.
  5. Choose **Asset Type**: TV Episode, Film, or Web.
  6. Ad placement: videos ≥ 8 min allow pre-roll, post-roll, and mid-roll; videos < 8 min allow pre-roll and post-roll only (default). **Display Ads** are on by default and cannot be deselected.

### New "Disclose video content" options in TikTok
- Lets creators disclose when TikTok Stories/Posts are branded content, matching the native TikTok experience; surfaced in Sprinklr Publisher.
- **Branded Content** = content that promotes or reviews a third-party brand or its products/services in exchange for payment or other incentive.
- Compliance: as of **August 22, 2025**, the disclosure parameters are required in all relevant TikTok API requests — requests missing them will fail.
- The disclosure fields themselves are **optional** for the user to select; labeling content as promotional is voluntary.
- Reference: TikTok Branded Content Policy — https://www.tiktok.com/legal/page/global/bc-policy/en

## Common issues & fixes
- **ProRes video won't publish / publish blocked:** upload triggers a transcode prompt; publishing is blocked until transcoding finishes. Minimize the window and keep working — or pre-transcode the asset in DAM so it's ready to publish.
- **GIF search only shows GIPHY (no Tenor):** Tenor requires Dynamic Publishing (DP) enabled; without DP only GIPHY is available. Also confirm the role has **Giphy Search** / **Tenor Search** permissions.
- **TikTok post fails after 22 Aug 2025:** missing branded-content disclosure parameters in the API request cause failures — ensure the disclosure fields are populated where required.
- **Facebook/YouTube monetization limitations:** Facebook — cannot select Ownership Link for matched content, In-stream Ads can't be enabled, Facebook Profiles and Instagram accounts are excluded from the allowlist, and monetization cannot be disabled after publishing. YouTube — Ads Suitability defaults to "None of the above" and cannot be changed; monetization cannot be disabled after publishing.

## Notes & gaps
- **Permissions/prerequisites:** GIFs/stickers need Workspace Role permissions (Giphy/Tenor Search); Tenor needs DP. Video monetization needs DP flags plus platform-side rights management (Facebook Rights Manager, YouTube content owner, Twitter Ads link).
- **Monetization is irreversible after publish** on both Facebook and YouTube. Bulk monetization is not supported. Monetization properties can be edited post-publication for Facebook and YouTube; cross-video Facebook posts are monetizable if the primary page has rights access.
- **Caption preview** is limited to draft and scheduled stages.
- **Not specified in the help articles:** emoji/skin-tone character limits and permissions; image/video size and format limits for the auto-optimization features; exact monetization eligibility thresholds beyond what's listed.
- **Could not be retrieved:** "Automatically Optimize Images for Publishing" and "Automatically Optimize Videos for Publishing" — both pages returned only navigation chrome (body loads dynamically) via WebFetch. Verify these two directly in the help center before advising clients. Related: [[ai-in-publishing]], [[rule-engine]], [[approval-workflows]].

## Sources
- Use Emojis While Creating Posts — https://www.sprinklr.com/help/articles/advanced-capabilities/use-emojis-while-creating-posts/6436846ec7dea832a77e10fa
- Choose Your Skin Tone for Emojis — https://www.sprinklr.com/help/articles/advanced-capabilities/choose-your-skin-tone-for-emojis/643687f1c7dea832a77e1101
- Publish GIFs and Stickers — https://www.sprinklr.com/help/articles/advanced-capabilities/publish-gifs-and-stickers/63fedc4532d12b63c5f55c2f
- ProRes Transcoding for Videos — https://www.sprinklr.com/help/articles/advanced-capabilities/prores-transcoding-for-videos/63fee3407a695d65a1605880
- Video Monetization from Sprinklr — https://www.sprinklr.com/help/articles/advanced-capabilities/video-monetization-from-sprinklr/64368069c7dea832a77e10ef
- Play Video Assets While Publishing — https://www.sprinklr.com/help/articles/advanced-capabilities/play-video-assets-while-publishing/63feddc67a695d65a1605879
- Automatically Optimize Images for Publishing (NOT retrieved — body did not load) — https://www.sprinklr.com/help/articles/advanced-capabilities/automatically-optimize-images-for-publishing/65af9b25d39ae90f842134bd
- Automatically Optimize Videos for Publishing (NOT retrieved — body did not load) — https://www.sprinklr.com/help/articles/advanced-capabilities/automatically-optimize-videos-for-publishing/6411518b7517d84a3aaf6642
- Show Caption Preview for Scheduled and Draft Posts While Playing the Video — https://www.sprinklr.com/help/articles/advanced-capabilities/show-caption-preview-for-scheduled-and-draft-posts-while-playing-the-video/66ac911fdac62338bfb09e57
- New Disclose Video Content Options in TikTok — https://www.sprinklr.com/help/articles/advanced-capabilities/new-disclose-video-content-options-in-tiktok/68a6ee4f47efcd5370b85aaf
