# Instagram — Advanced Publishing (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- Advanced Instagram publishing capabilities in Sprinklr's [[publishing]] tools — beyond basic caption + media.
- Covers feed preview/grid planning, location tags, account/people tags, product (shopping) tags, hashtags, video thumbnails, IG Live comment capture, pre-publish copyright detection, large-image (>8MB) upload workaround, and mobile-app publishing.
- Most actions live in the **Create Post** (Quick Publisher) window; a few use the **Editorial Calendar**, **Engagement Dashboards**, or the **[[rule-engine]]**.
- Several features are gated behind dynamic properties (DPs) or permissions — confirm enablement with your Success Manager before promising them to a client.

## Key features & how to use

### Instagram Feed Preview (grid planner)
- Shows how scheduled + published posts will look in the IG grid, so you can plan visual order before posts go live.
- **From Editorial Calendar:** New Tab icon → **Editorial Calendar** (under Publish) → **Options** icon (top-right) → **Instagram Feed Preview**.
- In the preview window: pick the IG account from the **Select Account** dropdown (searchable), then filter by status chips: **Draft**, **In Approval**, **Scheduled**, **Sent** (each chip can be toggled off).
- The right side renders a phone mockup of the actual grid. **Drag-and-drop images to swap positions** — swapping also swaps the scheduled publish times.
- Click **Apply** (bottom-right) to commit.
- **At post level:** hover a scheduled/published post's **Options** icon → **Preview** → **Feed Preview** tab → swap → **Apply**.
- **From Engagement Dashboard:** New Tab → **Engagement Dashboards** (under Engage) → open a dashboard with an Outbound column + IG account → hover post Options → **Preview** → **Feed Preview** tab → swap → **Apply** (top of pop-up).
- Notes: re-arranging does not require re-approval of already-approved posts; you can re-adjust times from the Editorial Calendar; natively archived posts are shown.

### Add location to a post
- In **Create Post** (Publishing Options icon → **Create Post**), select the IG **Business** account in **Select Accounts**, pick message type, upload media.
- Find the **Tag Location** field (below the media box). Type **at least 3 characters** to search the dropdown, then select.
- A public **Facebook event/page can be used as a location**.
- Limit: only **existing** locations can be tagged — you cannot create new locations from Sprinklr.

### Tag other Instagram accounts (Tag People)
- **DP-controlled** — enable via Success Manager.
- In Create Post, under the uploaded media click **Tag People** (tag-person icon, next to Tag Products).
- Click the spot on the photo where the person/object is → enter the **complete** IG handle → press **Enter** to verify → click **Tag** (bottom-right of the Tag People window).
- Handle auto-complete is **disabled** — type or paste the full, exact handle.
- Only **public profiles and business accounts** can be tagged; invalid handles block publishing.
- Limit: **max 20 accounts per image post**.

### Add product tags (Instagram Shopping)
- **Prerequisites:** IG Shopping approval on the business account; re-authenticate the linked **Facebook Page** (with shop connection); re-authenticate the **IG business account** in Sprinklr; re-sync (or add) the **Product Catalog** in [[asset-manager]]. Reel product tagging needs extra enablement from your Success Manager.
- In Create Post: select account → **Type of Message** = **Post** or **Reel** (single image/video) or **Carousel** (up to 10 media). Carousel posts cannot use location tagging or user mentions.
- Under **Media**, use **Select Media** / **Upload Media**; add description if wanted.
- Click **Tag Products** (bag icon under the media) → click anywhere on the media → in the **Tag Products** window pick a product from **All Products** → **Select Product** → review under **Selected Product Details** (Product Name, Product Website Link, price/currency) → **Add Product** (use **Replace Product** to swap).
- Click **Tag** (bottom-right) to confirm.
- Limits: single photo post = **5** product tags; per carousel slide = **5**; whole carousel = **20** total.

### Add hashtags
- In Create Post, select IG Business account(s), choose message type (Photo / Video / Story / Carousel), pick **Publishing Type** (Direct Publish or Publish Via Mobile), add media.
- In the caption box (**Add caption to your media**, 2200-char limit) type `#` + text (e.g. `#flower`). Sprinklr shows a **SUGGESTIONS** list and a **RECENTLY USED** list of hashtags.
- Recently-Used Hashtags also works for [[facebook]], Twitter/X, and LinkedIn.
- Best practice from the article: 3–4 hashtags in the caption, the rest in the **First Comment** (the "insert additional hashtags as a first comment" box) — IG allows **max 30** hashtags total. Store reusable branded hashtag sets as **Text Templates** in [[asset-manager]] and insert with the Insert button before picking accounts.

### Change thumbnail for IG videos (Carousel/Reel)
- **Permission-controlled** — needs the **Update Thumbnail** permission; ask your admin if the button is missing.
- After selecting a video, click **Change Thumbnail** (bottom-right of the video).
- In the **Media Uploader** window, **From Video** tab, pick a **Prominent Frame** (auto-suggested frames grid) or use **Capture Manually**. By default the 0th-second frame is selected.
- Thumbnail can only be a frame **from the video itself** (no external image on Instagram).
- Click **Use this frame** (bottom-right) to confirm.

### Capture comments on IG Live videos
- IG Live videos appear in Sprinklr only as **thumbnails**; comments surface only after the **first comment** is added to the live video.
- **Build a Media column:** New Tab → **Engagement Dashboards** (under Engage) → open dashboard → **Add Column** → source = **Instagram** → column type = **Media** → set Name, Description, Accounts (Basic Information) → set Workflow Properties (status, assignment, priority, spam, sentiment) and Custom Properties → **Create Column**.
- **Reply:** replies go out as **Instagram Direct Messages** during the live stream. Click the **Reply** icon on the comment (or use the **Thread** tab / third pane) → type reply → **Send** (or **Save as Draft**).
- **Automate via [[rule-engine]]:** New Tab → **Manage Rules** (under Triage) → **Create New Rule** → context **Inbound** → conditions: Channel = Instagram, Message Type = Instagram Comments, Message Subtype = **Live Comment**, Account = target → add Action(s) on Yes/No branch → **Save** / **Save as Draft**.

### Detect copyright violations before publishing (Instagram only)
- Supported for **Instagram only**. Works for Reels, Carousel videos, and Stories.
- In Create Post: select IG Business account → message type (Post/Story/Carousel/Reel) → upload video under **Media**.
- After upload, the **preview pane** shows the copyright result — e.g. a green banner "Copyright detection is successfully completed for Instagram Reel. No violations found." Large files take longer; you can save-as-draft or publish before it appears and check the result later in the outbound post's **third pane**.
- **Important:** Sprinklr does **NOT auto-block** publishing on a detected violation — it only warns on the publisher / notifies after creation.
- **To hard-stop violating posts**, build a [[rule-engine]] rule (Outbound / pre-publishing): condition **"Is Copyright Violated" Is Yes** → Action = **Stop**.
- Carousel notifications: violation → "...This may impact your post, but Sprinklr will not block the publishing..."; detection error → "...Copyright detection didn't work as intended... does not block publishing... please try again."
- If copyright is falsely claimed against your work, file a case with Instagram (link in the article).

### Upload images larger than 8MB
- **DP-controlled** — enable via Success Manager or tickets@sprinklr.com.
- Instagram natively caps images at **8MB** with aspect ratio **4:5 to 1.91:1** (JPEG/JPG). Facebook allows up to **1GB**, any aspect ratio, JPEG/PNG/GIF.
- How Sprinklr works around it: (1) uploads the original image to Facebook as a **dark post** (up to 1GB); (2) Meta auto-resizes to IG-compatible dimensions; (3) Sprinklr fetches the **resized image URL** from Facebook; (4) the dark post is **auto-deleted** from both Sprinklr and Facebook; (5) the resized image publishes to Instagram via Meta API.
- Caveats: images outside IG's aspect-ratio range are still rejected; Meta's pixel guidance is a recommendation not a hard limit; very large/high-res files may not process; larger files risk quality loss — keep below 8MB where possible.

### Publish via Sprinklr Mobile App
- **Method 1 — Personalized Shortcuts:** add **Publish** as a shortcut, then create from the bottom nav bar.
- **Method 2 — Navigation Menu:** tap the **Menu** icon (bottom-right) → **Publishing** (under Sprinklr Social).
- In **Select Account**, search/select account(s). Simple messages (media + text) can be published to Twitter/X, Facebook, Instagram and LinkedIn **simultaneously**; advanced types (Carousel, Album, etc.) must be posted **individually**.
- Enter caption → tap the **Image** icon → **Upload Media** → **From Device** or **From DAM** (Digital Asset Manager) → tap **Customize** or **Next** (once you switch to the customize editor you **cannot return** to the basic editor) → fill the **Optimize** screen → **Save as Draft** or **Publish**.

## Common issues & fixes
- **Tag People button missing** → DP not enabled; contact Success Manager.
- **Handle won't tag / post won't publish** → handle is incomplete, private/personal, or invalid. Use full handle of a public/business account; max 20 per image.
- **Tag Products greyed out** → Shopping prerequisites incomplete (shop approval, FB Page + IG re-auth, catalog re-sync). Reels need extra enablement.
- **Change Thumbnail button missing** → user lacks the Update Thumbnail permission; ask admin.
- **Copyright-violating post still published** → expected; Sprinklr only warns. Add a rule with "Is Copyright Violated = Yes" → Stop to block.
- **Copyright check slow/absent** → large files take longer; you can publish meanwhile and verify later in the third pane.
- **Large image rejected by IG** → it's outside the 4:5–1.91:1 aspect ratio (size workaround doesn't fix ratio), or quality degraded — re-crop / reduce below 8MB.
- **IG Live comments not showing** → none exist until the first comment is posted on the live video; videos show as thumbnails only.

## Notes & gaps
- Instagram **direct publishing of photos/videos requires a Business account** (stated across the Create Post screens).
- Gated features: Tag People (DP), >8MB image upload (DP), Reel product tags (enablement), Change Thumbnail (permission). Confirm before scoping.
- The 8MB workaround relies on the linked Facebook Page — the IG account must be properly linked to a FB Page.
- Article text didn't specify exact video duration/format limits for thumbnails or copyright detection, nor catalog-sync detail (see Instagram Shopping / "How to sync Product Catalogs in Sprinklr" docs).
- Carousel: no location tagging or user mentions; up to 10 media.

## Sources
- Instagram Feed Preview in Sprinklr — https://www.sprinklr.com/help/articles/other-publishing-capabilities/instagram-feed-preview-in-sprinklr/63ee762bf6e2cc7d18facc27
- Add Location to Instagram Post — https://www.sprinklr.com/help/articles/other-publishing-capabilities/add-location-to-instagram-post/63e47c79a9d511790301759a
- Tag Other Instagram Accounts — https://www.sprinklr.com/help/articles/other-publishing-capabilities/tag-other-instagram-accounts/63eef25df6e2cc7d18facdfd
- Add Product Tags to Instagram Posts/Reels — https://www.sprinklr.com/help/articles/other-publishing-capabilities/add-product-tags-to-instagram-postsreels/63eef0b8f6e2cc7d18facdfa
- Instagram Hashtags Addition to Posts — https://www.sprinklr.com/help/articles/other-publishing-capabilities/instagram-hashtags-addition-to-posts/63e47b4455780d70a15be90d
- Change Thumbnail for Instagram Videos — https://www.sprinklr.com/help/articles/other-publishing-capabilities/change-thumbnail-for-instagram-videos/63ee7a3bef1b447d6c63193b
- Capture Comments on Your IG Live Videos — https://www.sprinklr.com/help/articles/other-publishing-capabilities/capture-comments-on-your-ig-live-videos/63ee7456ef1b447d6c631921
- Detect Copyright Violations While Publishing Videos — https://www.sprinklr.com/help/articles/other-publishing-capabilities/detect-copyright-violations-while-publishing-videos/6658205f5b3d5f5a8babe414
- Upload Images Larger than 8MB to Instagram — https://www.sprinklr.com/help/articles/other-publishing-capabilities/upload-images-larger-than-8mb-to-instagram/67a09d743caa102e75fe9a56
- Publish via Sprinklr Mobile App — https://www.sprinklr.com/help/articles/other-publishing-capabilities/publish-via-sprinklr-mobile-app/63ee796df6e2cc7d18facc33

Related: [[publishing]] · [[rule-engine]] · [[engagement-dashboards]] · [[asset-manager]] · [[reporting]] · [[facebook]]
