# Leverage AI in Publishing (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- A set of Sprinklr AI+ capabilities that sit inside the Publisher (Quick Publish, Editorial Calendar, Full Screen Publisher) to speed up content creation, compliance, and scheduling.
- Covers six features: AI content generation, AI alt text, AI video thumbnails, Smart Approvals, Smart Scheduling, and highlighting non-compliant keywords.
- Aimed at reducing manual effort (e.g. alt text in seconds vs. 3–5 minutes) and catching compliance/quality issues before posts go live.
- Most features are gated behind AI+ permissions and Dynamic Properties — they need account-team enablement before they appear. Related: [[ai-in-publishing]], [[approval-workflows]], [[editorial-calendar]].

## Key features & how to use

### Generate content for posts and messages (Sprinklr AI+)
- Generates post/reel/message content for social and non-social channels from a topic, phrase, or keyword; also proofreads grammar, spelling, and style.
- Supported channels: Facebook, Instagram, X, TikTok, LinkedIn, Email, SMS, Blog, Website, Press Release.
- Steps: New Tab → Sprinklr Social → Quick Publish tab → fill Create Post details → select account and message type → enter text in the **Message** field → click the **Sprinklr AI+** icon.
- Editing options: Reword, Fix Spelling & Grammar, Make it Longer/Shorter, Modify Tone, Simplify Language, Translate.
- Generation options: Generate Product Description, Generate Content Variations, Generate Hashtags, Generate Post Content (options vary by channel and message type).
- Tuning fields: **Define the tone** field; **Who is your audience?** dropdown.
- Action buttons: Generate, Insert, Replace, Copy, Restart, Retry. Publish via Save as Draft, Post, or Post and Boost.
- Prerequisite: Limited Availability — must be enabled by Success Manager / account team; Dynamic Property `GPT_ACTIONS_ENABLED_PRODUCTS: Social`.

### Create alt text in Publisher (Sprinklr AI+)
- AI auto-generates image descriptions for accessibility; one click can handle multiple images at once.
- Supported channels: LinkedIn, Facebook, Pinterest, Twitter, Telegram, Bluesky.
- Steps (Publisher): open Create a Post (Quick Publish or Editorial Calendar) → upload images → click **Generate Alt Text** (shown for supported channels) → AI fills descriptions for images missing alt text → optionally refine with translate / spell-grammar tools.
- Steps (customize in AI+ Studio): Platform modules → **AI+ Studio** → **Deploy your Use-Cases** → Sprinklr Social → **Generate Image Alt Text** → use the options icon on a deployment to edit, undeploy, test, or delete.
- Media limits: up to 30 MB; formats PNG, JPEG, WebP (GIF coming in a future release). Works best on media with English text.
- LLM: default Google Bard (Sprinklr-recommended). Not supported on Bedrock or Claude models.
- Permissions: Dynamic Property `<GPT_ACTIONS_ENABLED>`; existing Sprinklr AI+ permission in the **Outbound Message** category under Publishing. Included in AI+ at no extra cost (Limited Accessibility). Enable via Success Manager or tickets@sprinklr.com.
- Note: each alt-text-supporting channel must be generated separately.

### Generate thumbnails for videos (AI)
- AI picks relevant, visually appealing video frames and can generate optimized thumbnails for videos that lack one.
- Change/edit a thumbnail: hover the default thumbnail → click the Options icon → choose **Thumbnail Using AI** or **Thumbnail Using DAM** → pick from AI-generated options → (optional) use the Duration selector for a specific segment → confirm on the Review Screen.
- Create a custom AI thumbnail: Quick Publish → select Account and Message Type → under Media click **Select Media** → in Media Uploader click **Generate Image** (top right) → choose **Create an Image**, **Edit an Image**, or prompt via **Ask Sprinklr Copilot** → preview (eye icon), download, or add via checkbox → review and publish.
- AI frame-selection criteria: visual clarity/sharpness, scene relevance, emotional engagement, composition/framing, action/movement, lighting/color, text & graphics detectability, uniqueness/variety, brand cues (logos, settings).
- Permissions: Dynamic Property `GENERATIVE_AI_ACTIONS_ENABLED`; permission `SPRINKLR_AI_PLUS_FOR_MEDIA`. Enable via Success Manager or tickets@sprinklr.com.

### Smart Approvals
- AI content moderation that assists campaign managers during approval by flagging content that needs updates before publishing.
- Steps: Menu icon → **Engagement Dashboards** (Sprinklr Social) → open the dashboard → find the **Smart Approval** column → review the **Smart Content Score** → approve or request changes.
- Classification buckets: **Content Looks Good for Approval**, **Content Might Need Review**, **Content Must be Reviewed** (inappropriate/NSFW).
- AI checks: Inappropriate Content (profanity/nudity/NSFW, ~80% accuracy), Image Quality (blur, low contrast, poor focus), Brand Logo (missing logo / wrong aspect ratio), Appeal (alignment to intended message), Tone (aggressive / lacking empathy, ~80% accuracy), plus a legal/compliance parameters check.
- Components: Smart Content Score, Smart Approval column, approval queue, approval paths. Model retrains from user feedback on brand-specific identity.
- Permissions: **View Smart Approvals** permission (account-level); Data Profile `SMART_APPROVAL_OUTBOUND_ENABLED` (extra setup). Languages: English and Arabic. Requires Success Manager enablement.
- Related: [[approval-workflows]], [[rule-engine]].

### Smart Scheduling
- AI picks the best time to publish per account to maximize engagement, using 30 days of historical data and maintaining a minimum 1-hour gap from existing scheduled posts.
- Supported channels: Facebook, Instagram, Twitter, LinkedIn.
- Steps: create a post in Quick Publisher → click **Schedule Post** (bottom left) → check the **Smart Scheduling** checkbox → select a date range (defaults to next 7 days; max 7-day window) → click a suggested timeframe (green = most optimal, gray = secondary) → click **Schedule**.
- How it scores: engagement score per hour from five metrics — Share, Comment, Like, Impression, Fan Count (hourly fan count is Facebook/Instagram only) — ranked across the next 7 days.
- Permissions: available to all users by default but permission-controlled (admins can restrict).
- Reporting: use the **Is Smart Scheduled** dimension with the **Outbound Message** data source. Related: [[editorial-calendar]], [[web-analytics]].

### Highlight non-compliant keywords
- Flags problematic words in the post preview during creation (before publishing), letting teams set custom vocabulary standards. Scans transcripts from images and videos too.
- Create a keyword list: New Tab → **Keyword Lists** (Platform Modules, under Unify) → **Add Keyword List** (top right) → set **Name**, **Tags**, **Query Words** (terms to flag) → **Save**.
- Create the highlighting rule: New Tab → **Manage Rules** (Sprinklr Social → Triage) → **Create New Rule** → name + optional description → set **Rule Scope** = Workspace → set **Rule context** = **Autofill** (blocks publishing until flagged words are removed) → **Add Condition** in the Rule Engine Builder → name it and set condition type = **Message Keywords** → pick your list under **Select Keyword List** → on the **Yes** node click **Add Action** → action type = **Change properties of Message** → set these toggles to **Yes**: **Highlight Search Items**, **Highlight Link Search Terms**, **Highlight Image Search Terms**, **Highlight Video Search Terms** → **Save** → enable the rule from the Options menu.
- Alternative Rule contexts: Pre-publishing and Outbound let posts still be scheduled while issues are highlighted for approvers.
- Related: [[rule-engine]], [[approval-workflows]].

## Common issues & fixes
- **Feature not visible** — most AI+ features require enablement (Success Manager / account team / tickets@sprinklr.com) plus the right Dynamic Property and permission; if missing, the option won't appear.
- **Alt text limits** — media must be ≤ 30 MB and PNG/JPEG/WebP; GIFs not yet supported; works best on English text; not available on Bedrock or Claude models.
- **Smart Scheduling "insufficient data for Smart Scheduling"** — too little history for the account; predictions improve as more posts publish over time.
- **Thumbnails slow to appear** — AI thumbnails can take minutes to generate after a video upload; **Thumbnail Using DAM** needs the default thumbnail visible before changes.
- **Smart Approvals accuracy** — content and tone checks run at ~80% accuracy; treat flags as guidance, keep human review in the loop.
- **Keyword highlighting not blocking** — only the **Autofill** rule context prevents publishing until flagged words are removed; Pre-publishing/Outbound contexts only highlight.

## Notes & gaps
- Smart Approvals and AI alt text are limited to specific languages (Approvals: English + Arabic; alt text: best in English) — non-English client environments may see degraded results.
- Articles state permissions/Dynamic Properties by name but do not give the exact admin navigation path to toggle them — that is handled by the Success Manager / account team.
- No pricing detail beyond "alt text included in AI+ at no additional cost"; cost of other AI+ features is not specified.
- Exact retraining cadence and how feedback is submitted for Smart Approvals is not detailed.
- GIF support for alt text and any expansion of supported channels/LLMs (e.g. Claude, Bedrock) are noted as future/not-yet-available.

## Sources
- Generate content for posts and messages using Sprinklr AI — https://www.sprinklr.com/help/articles/sprinklr-ai/generate-content-for-posts-and-messages-using-sprinklr-ai/6746caa392765f31c830216d
- Create alt text in Publisher using Sprinklr AI — https://www.sprinklr.com/help/articles/sprinklr-ai/create-alt-text-in-publisher-using-sprinklr-ai/685ceb95c141ae04d1a9f774
- Generate thumbnails for videos using AI — https://www.sprinklr.com/help/articles/sprinklr-ai/generate-thumbnails-for-videos-using-ai/67ceb67b4f61f02eeb0d80eb
- Smart Approvals — https://www.sprinklr.com/help/articles/leverage-ai-in-publishing/smart-approvals/643655cfb7f3625d288e70ac
- Smart Scheduling — https://www.sprinklr.com/help/articles/leverage-ai-in-publishing/smart-scheduling/63fef0d532d12b63c5f55c51
- Highlight non-compliant keywords — https://www.sprinklr.com/help/articles/leverage-ai-in-publishing/highlight-noncompliant-keywords/6436632fc7dea832a77e10ab
