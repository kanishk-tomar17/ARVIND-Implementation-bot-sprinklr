# Publishing — Reference (Permissions, FAQ, Errors) (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- Reference material for consultants configuring and troubleshooting outbound publishing in Sprinklr Social.
- Covers four things: per-channel media specs (image/video/file limits), the workspace-role permissions that gate the Publisher, common publishing FAQs, and the most common channel publishing errors with fixes.
- Use it to pre-validate media before a client publishes, to grant the right permissions, and to diagnose why a post failed to go out.
- All values below are taken verbatim from the help articles — do not assume specs for a channel not listed here.

## Key features & how to use

### Publishing permissions (Outbound Message)
- Set at: **Platform Settings > Manage Workspace > Workspace Roles**, under the **Outbound Message** section.
- Every user needs at least the relevant permission to use the Publisher. Permission names and what each allows:
  - **View** — access the publisher (baseline).
  - **Publish** — publish outbound messages.
  - **Create Draft** — create drafts from the Publisher.
  - **Create Localized Copy** — create localized copies from the publisher.
  - **Edit Sent Post** — edit previously sent posts or advocacy content.
  - **Edit and Approve** — edit and approve content.
  - **Approve/Reject** — approve or reject outbound messages.
  - **Delete** — delete outbound publisher messages.
  - **Show Response Suggestions** — view response suggestions.
  - **Enable Response Compliance** — turn on response compliance.
  - **Giphy Search** — search Giphy.
  - **View Confidential** — view confidential messages regardless of sharing.
  - **Add Cc** — add CC while replying to emails (requires success-manager approval).
  - **Add Bcc** — add BCC to email replies (requires success-manager approval).
- See [[approval-workflows]] for how Approve/Reject and Edit and Approve feed tiered approval paths.

### Channel media guidelines
When uploading media and publishing through Sprinklr, each channel has its own specs. Values below are the supported/recommended specs per channel.

- **Facebook**
  - Image format: JPEG, JPG, PNG, GIF. Video recommended: MP4, MOV (many others supported incl. AVI, MKV, MOV, WMV, etc.).
  - File size — Image post: 1 GB; DM attachment: 8 MB. Video post: 10 GB; video DM attachment: 25 MB.
  - Aspect ratio — Image: 1.91:1 to 1:1; Video: 16:9 to 9:16; Reels: 9:16.
  - Dimensions — Image 2048x2048; shared-link image 1200x628; carousel 1080x1080; video 4096x2048. Reels min 540x960 (540p), max 1080x1920.
  - Duration — Video up to 4 hours; Reels 3–90 seconds.
- **Twitter (X)**
  - Image format: JPG, PNG, GIF. Video: MP4, MOV.
  - File size — Image: 100 MB; Animated GIF: 15 MB; Video: 512 MB.
  - Aspect ratio — Image 2:1; Video landscape/portrait 16:9, square 1:1.
  - Dimensions — Animated GIF 1280x1080; landscape 1280x720; portrait 720x1280; square 720x720.
  - Duration — Video max 2 min 20 sec (not whitelisted); max 10 min with Media Studio.
  - Audio must be AAC Low Complexity profile; High-Efficiency AAC not supported.
  - Alt-text character limit: 1000 (image and video).
- **Instagram**
  - Image format: JPEG/JPG, PNG. Video & Reels: MP4, MOV.
  - File size — Image post 8 MB; image DM attachment 8 MB. Video post 100 MB; video DM attachment 25 MB. Reels max 300 MB.
  - Aspect ratio — Image 4:5 to 1.91:1; Video 4:5 to 1.91:1 (Story video 9:16); Reels 0.01:1 to 10:1 (recommended 9:16 to avoid cropping).
  - Dimensions — Image landscape 1440x754, vertical 1440x1800, square 1440x1440; Video landscape 1920x1005, vertical 1920x2400, square 1920x1920, story 1920x1080.
  - Duration — Video Direct Publishing 3–60 sec; Mobile Flow Publishing 3 sec–1 hour; Story 15 sec. Reels Direct Publishing 3 sec–15 min; Mobile Flow Publishing 3–90 sec.
  - Frame rate 23–60 FPS; bitrate VBR 25 Mbps max; audio 128kbps, AAC 48khz max, mono/stereo; video codec HEVC or H264.
- **LinkedIn**
  - Image format: PNG, JPEG, GIF. Video: ASF, AVI, FLV, MPEG-1/4, MKV, QuickTime, WebM, H264/AVC, MP4, VP8/9, WMV2/3, AAC, MP3, Vorbis.
  - File size — Image dimension < 36152320 pixels (GIF up to 250 frames); Video 5 GB.
  - Aspect ratio — Image 1.91:1; Video 1:2.4 to 2.4:1.
  - Dimensions — Video 256x144 to 4096x2304.
  - Duration — Video 10 minutes.
  - Alt-text character limit: 300.
- **YouTube**
  - Video max file size 8 GB. Standard aspect ratio 16:9 (player adapts to other ratios). Recommended format MP4.
  - Common frame rates 24, 25, 30, 48, 50, 60 FPS; interlaced content should be deinterlaced before upload.
  - Dimensions: 240p (426x240), 360p (640x360), 480p (854x480), 720p (1280x720), 1080p (1920x1080), 1440p (2560x1440), 2160p.
- **Google (Business / Ads media)**
  - Image: JPG, JPEG, PNG; Video: MOV, MP4.
  - File size — Image max 10 MB (publisher specs may require smaller); Video up to 1 GB.
  - Aspect ratio — landscape 16:9 or 4:3; portrait 9:16 or 3:4.
  - Dimensions — Image 300x250; video landscape 1280x720 / 1920x1080 / 1440x1080; portrait 720x1280 / 1080x1920 / 1080x1440; square 720x720 / 1080x1080 / 1920x1920.
- **Pinterest** — Image JPG/JPEG/PNG/GIF, video MP4/MOV. Size: image 10 MB, video 2 GB. Aspect ratio image 2:3, video square 1:1 / vertical 9:16. Image 735x1102px; video min 240p; video duration up to 30 min.
- **LINE** — Image JPEG (1 MB, 1024x1024px), video MP4 (10 MB, 240x240px, 1 minute).
- **Sina Weibo** — Image JPG/GIF/PNG, 5 MB, 640x640px.
- **Flickr** — Image JPEG/PNG/GIF (200 MB); video MP4/AVI/WMV/MOV/MPEG/3GP/M2TS/OGG/OGV (1 GB).
- **SlideShare** — Presentations (PDF, ODP, PPT/PPTX/PPS/PPSX), Documents (PDF, DOC/DOCX, ODT, TXT), Infographics (PDF). File size 300 MB.
- **Tumblr** — Photo post 500x750px (1280x1920px high-res); various photoset widths; video MP4, 100 MB, max 5 minutes uploaded video per day.
- **VKontakte** — Image JPG/PNG/GIF/BMP (50 MB); video AVI/MP4/3GP/MPEG/MOV/MP3/FLV/WMV (200 MB); width+height not more than 14000px.
- **WordPress** — File-based; file size limit noted (article truncates the exact value).
- See [[asset-manager]] for storing/reusing approved media against these specs.

### Publishing FAQs
- **Media guidelines** — channel-wise; see Channel Media Guidelines (above).
- **Smart Scheduling with Create Message** — Yes, Smart Scheduling works in Create Message, not just Quick Publish (QP).
- **Multiple campaigns per post** — No; only one campaign can be associated with a post.
- **Recurring scheduled post status** — Posts stay in **draft** status when scheduled to recur.
- **Organic dark posts via QP** — Yes, organic dark posts can be published through QP.
- **Tiered approval, 2 approvers in 1 step (any one approves)** — Use **approval queues**: any one user provisioned to the queue can approve/reject. See [[approval-workflows]].
- **Editorial calendar colors** — Yes: three-dots menu (top right of editorial calendar) > Settings > Color configuration. See [[editorial-calendar]].
- **Limit posts per user per channel/account** — No, not possible in Sprinklr currently.
- **Apply approval paths when publishing** — Create a tiered approval path in Platform Settings, then use the "Follow the approval path" section in the publishing window. See [[approval-workflows]].
- **URL shortener** — Shortens long links from anywhere in the platform to just **19 characters**; used to minimize and track web addresses.
- **Video optimization** — Converts file format, compresses to reduce file size, and edits video to match channel specs. Available for **Facebook, Instagram, Twitter, and LinkedIn only**.
- **Emoji / skin-tone emoji** — Supported in the publishing window as needed.
- **Permission required to publish** — Yes; every user needs publishing permission (see Permissions section above).
- **Custom video thumbnails** — When publishing, select any image within the post to use as the video thumbnail ("Select thumbnail for video while publishing").
- See [[ai-in-publishing]] for AI-assisted publishing helpers.

## Common issues & fixes
Channel publishing errors and resolutions:

- **Facebook**
  - `(#551) This person isn't available right now` — recipient closed chat, blocked the page, or deleted the conversation. User must re-initiate; expected per Facebook privacy.
  - `(#200) User does not have sufficient administrative permission` — page needs Two-Factor Authentication authorization. Complete Facebook authorization, then re-add the account to Sprinklr.
- **Instagram**
  - `Instagram PSID profile not found` — DM no longer exists natively (user deleted conversation). Expected; no preventive action.
  - `We are currently experiencing a disruption with this channel API` — channel API downtime. Retry after minutes-to-hours.
  - `USER is restricted, The Instagram account is restricted` — account restricted by Instagram. Admin logs into native Instagram, then re-adds the account to Sprinklr.
  - `Mentions are not allowed per target user's settings` — target's privacy blocks mentions. Remove @mentions and republish.
  - Account unlinking issue — Facebook/Instagram need re-linking. Admin unlinks, re-adds both accounts, then re-links them in Sprinklr.
  - `Aspect ratio must be between 0.8 to 1.91` — wrong media specs. Use landscape 1080x566px, portrait 1080x1350px, or square 1080x1080px.
- **Twitter (X)**
  - `Account is temporarily locked` — Twitter detected suspicious/compromised behavior. Admin must unlock natively; Sprinklr cannot.
  - `You cannot send messages to this user` — recipient blocks DMs from non-followers. Recipient must follow the brand or allow DMs from everyone.
- **LinkedIn**
  - `Target audience does not meet 300 follower minimum` — targeted location has < 300 followers. Select locations meeting the 300-follower minimum.
  - `Video failed to process on LinkedIn` — intermittent API issue/downtime. Retry once API normalizes.
  - `Authorization error: Invalid/Expired Token` — LinkedIn tokens expire every 60 days. Account admin re-adds the account.
  - `Unable to upload asset in LinkedIn` — native processing failure. Retry publishing; no preventive step.
- **Bazaarvoice** — `Hub name empty for the account` — missing native hub-name config. Reconfigure the hub name natively.
- **Pinterest** — `Sorry! We blocked this link because it may lead to spam` — shortened URLs (bitly, po.st, awe.sm) flagged as spam. Use complete, unshortened links.
- General media-rejection issues: validate against the channel specs above before publishing (see [[asset-manager]]).

## Notes & gaps
- **Permissions** are workspace-role-scoped (Platform Settings > Manage Workspace > Workspace Roles > Outbound Message). Add Cc / Add Bcc require success-manager approval.
- The media-guidelines article is recommendations + supported limits, not a guarantee — native channel APIs can still reject media (see error list). Specs change as channels update; always re-check the source article for the latest.
- A few raw values in the source are ambiguous (e.g. LinkedIn "Dimension less than 36152320 pixels", YouTube 2160p dimension, WordPress file size truncated) — confirm against the live article if exact precision matters.
- The articles do NOT specify: text/caption character limits per channel (only alt-text limits for Twitter/LinkedIn are given), hashtag limits, number-of-media-per-post limits, or scheduling/rate limits.
- The FAQ confirms no native control to cap posts per user per channel, and only one campaign per post.
- Approval-path mechanics (tiered paths, approval queues) are referenced but configured elsewhere — see [[approval-workflows]] and [[rule-engine]].

## Sources
- Channel Media Guidelines — https://www.sprinklr.com/help/articles/know-more/channel-media-guidelines/63fdb018e02459133724bb28
- Permissions related to publishing — https://www.sprinklr.com/help/articles/know-more/permissions-related-to-publishing/64538286f65d86626c829b87
- Publishing — Frequently Asked Questions — https://www.sprinklr.com/help/articles/know-more/publishing-frequently-asked-questions/64538b74f65d86626c829d6b
- Common Publishing Errors — https://www.sprinklr.com/help/articles/know-more/common-publishing-errors/640abaad2680c35a78bb1ff3
