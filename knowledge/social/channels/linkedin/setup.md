# LinkedIn — Setup & Accounts (Sprinklr Social — LinkedIn)
**Source:** sprinklr.com/help — LinkedIn channel (multiple articles; see links below)

## What it is
- How to connect LinkedIn accounts to Sprinklr Social: **two distinct channel types** — **LinkedIn** (personal Profile) and **LinkedIn Company** (Company/Showcase Pages).
- Authentication is OAuth: you authorize Sprinklr from inside the live LinkedIn session, so you must be logged into the correct LinkedIn account first.
- Covers single-admin setup, multi-admin token resilience, what LinkedIn supports/blocks via its API, media specs, and channel changes over time.
- Connected accounts feed [[publishing]], [[engagement-dashboards]], and [[reporting]].

## Key features & how to use

### Add a LinkedIn Company Account
- Path: **Sprinklr Social** tab → under **Listen**, click **Owned Social Accounts** → opens **Accounts** (Account Management) screen.
- Click **+ Add Account** (top right of the Accounts grid) → in the **Add Account** channel picker, choose the **LinkedIn Company** tile (distinct from the plain "LinkedIn" profile tile and from "LinkedIn Ads").
- A dialog **Authorize Sprinklr on LinkedIn** appears → click **Go To LinkedIn** to authorize on the platform.
- LinkedIn returns a **"Select the accounts you want to add"** dialog listing pages you administer. It has a search bar, filters (**Account Status**, **Added in Sprinklr**, **Is Manually Deactivated**), a **Select all** checkbox, and per-page checkboxes. Tick the page(s), then click **Add** (bottom right; counter shows "0/1 Selected").
- Configure in the **Update Account** window, then **Save**:
  - **Account Details** — display name, owner, character count, URL shortener, reply signature.
  - **Permissions** — grant channel actions to Users / User Groups.
  - **Share this Account Across Spaces** — choose Workspace visibility or global sharing.
  - **Subscribers** — Users/User Groups to notify.
  - **Timezone** — country + timezone.
  - **Properties** — custom account properties.
- Requirements: you must hold the **Super Admin** role on the LinkedIn Company Page. If a page just granted you access and isn't listed, use the **Resync** button to refetch pages.

### Add a LinkedIn Profile Account
- Same path: **Sprinklr Social** → **Owned Social Accounts** → **+ Add Account** → choose the **LinkedIn** tile (profile, not "Company").
- Click **Go To LinkedIn** on the "Authorize Sprinklr on LinkedIn" dialog — note it reads "Sprinklr needs permission to access LinkedIn in order to manage your **Profile**" and warns to ensure the **correct LinkedIn Profile is logged in**.
- On the **Need Confirmation** screen, click **Add**.
- Configure the same **Update Account** sections (Account Details, Permissions, Share Across Spaces, Subscribers, Timezone, Properties) → **Save**.
- A social account can only be added to a **single Workspace** at first; sharing across Workspaces is a separate admin action.

### Multiple account administrators (multiple authorization tokens)
- Lets several users hold valid auth tokens for the **same** LinkedIn account. If one admin's token goes invalid, the account stays live on the remaining tokens — avoids disconnects when one person leaves or their session expires.
- **Limited-access feature**, gated by the dynamic property `MULTIPLE_AUTH_TOKENS_ENABLED_ACCOUNT_TYPES`. Get it enabled via your Success Manager or tickets@sprinklr.com.
- **Step 1 — grant admin on LinkedIn (native):** LinkedIn Page → **Me** icon → select your Page under **Manage** → **Admin Tools** dropdown → **Manage admins** → **Add admin** → search/select the person (must be a 1st-degree connection or have recently interacted with the page) → pick the admin role → **Save**. (You must be a Super Admin to assign roles.)
- **Step 2 — in Sprinklr:** each admin adds the same account via **Owned Social Accounts → + Add Account → LinkedIn**, authenticating natively.
- To inspect tokens: on the Accounts grid, click the **options (⋮) icon** next to the account → **Authenticate Tokens** / **Authorise Tokens**. The dialog lists every admin with an avatar, an **In Use / Not In Use** toggle, an **Expires On** date, and a delete icon per token — letting you see the active token and remove stale ones.

### Capabilities & limitations (LinkedIn API)
- **Publishing (both Profile + Company):** text posts, videos (with SRT captions), multi-image up to **20 images**, documents (PDF/PPT/DOCX, up to **100 MB / 300 pages**), LinkedIn Polls. Photos: Company yes, Profile no.
- **Sprinklr extra:** schedule a post for a precise future date/hour/timezone — beyond what the public API offers.
- **Engagement (both):** reply to comments and likes; delete/disable comments; edit published posts (**text only** — media/links can't change); auto-import natively published content; reply to DMs from LinkedIn Profiles. Comment-as-company is Company-only.
- **Character limit:** **3000 characters** for posts (Quick Publisher) and for comments/replies (Engagement Dashboards), both account types.
- **Targeting (Company/Showcase only):** by followers, language, location, company, job title, school, degree, skills, group, age, gender; placement (desktop/tablet/mobile); audience-size display. Profiles: no targeting.
- **Analytics:** Company/Showcase get video metrics (views, unique viewers, watch time, likes/comments — shares & impressions unavailable), reactions, likes/shares/comments, limited live-video and poll (text-only) reporting. Profiles: cannot report on videos published from Sprinklr; text-only reporting for articles/documents/job posts/polls. See [[reporting]].
- **Not supported (API limits):** job postings, LinkedIn Live Video, carousel posts, articles, custom video thumbnails, Events for profiles, InMail view/send, share/repost, engaging with video posts on company pages, product management, group management, comment-likes reporting, permalinks, employee vs non-employee filtering, UGC video post editing.

### Media guidelines
- **Images:** PNG, JPEG, GIF. Total dimension < 36,152,320 pixels. GIFs up to 250 frames. Aspect ratio 1.91:1.
- **Video:** formats ASF, AVI, FLV, MPEG-1, MPEG-4, MKV, QuickTime, H264/AVC, MP4, VP8, VP9, WMV2, WMV3, AAC, MP3, Vorbis. Max **5 GB**, max **10 minutes**. Dimensions 256×144 to 4096×2304. Aspect ratio 1:2.4 to 2.4:1. Audio must be **AAC, Low Complexity profile**.
- **Documents:** PDF/PPT/DOCX, up to 100 MB / 300 pages (per capabilities article).

### Channel updates (timeline)
- **Jun 2024:** LinkedIn Profiles can DM LinkedIn Company Accounts; company accounts can react/reply but **cannot initiate** conversations. Requires **re-adding** Company Page accounts in Sprinklr. Backfills up to 500 messages across 500 threads.
- **Mar 2023:** LinkedIn Polls — create/publish via Quick Publisher and Full Screen Publisher for both Profiles and Company Pages.
- **Apr 2019:** LinkedIn Notifications API for monitoring company-page activity; visibility of natively edited/deleted comments; dashboard columns for shares and brand mentions.
- **Jan 2019:** video analytics (view time, views, unique viewers); LinkedIn Carousel Ads support in Ads Composer/Manager + reporting.
- **Aug 2017:** re-authentication required for all accounts added before 14 Aug 2017.
- **Jun 2017:** LinkedIn Groups API discontinued — Groups content access via Sprinklr ended 30 Jun 2017.

## Common issues & fixes
- **Page not showing in the selection list:** click **Resync** to refetch pages you were just granted access to.
- **Can't add a Company Page:** you need the **Super Admin** role on that LinkedIn Page.
- **Account disconnects when one admin leaves/expires:** enable **multiple authorization tokens** so other admins' tokens keep it live; check active vs stale tokens under **Authenticate/Authorise Tokens**.
- **Wrong account gets connected:** ensure you're logged into the exact LinkedIn Profile/Page you intend before clicking **Go To LinkedIn** (OAuth uses the current live session).
- **DMs from a Company account won't start:** expected — company accounts can only react/reply, not initiate; and Company DM support needs the page **re-added** after Jun 2024.
- **Edit doesn't change media/link:** expected — published-post edits are text-only.

## Notes & gaps
- Prerequisites: Super Admin on the LinkedIn Page (Company); logged into the correct LinkedIn session (both types).
- Multiple auth tokens is **limited access** (`MULTIPLE_AUTH_TOKENS_ENABLED_ACCOUNT_TYPES`) — must be turned on per partner.
- A social account starts in one Workspace; cross-Workspace sharing is a separate step (see [[asset-manager]] / Workspace admin docs).
- Gaps: the Capabilities article gives no screenshots; exact image dimension/size limits for static photos (beyond the 36M-pixel total) aren't broken out; the Update Account fields are listed but per-field validation rules aren't documented; "Authenticate Tokens" vs "Authorise Tokens" labeling varies between the article text and the in-product dialog.

## Sources
- Add a LinkedIn Company Account in Sprinklr — https://www.sprinklr.com/help/articles/getting-started/add-linkedin-company-account-in-sprinklr/6406cc4232d12b63c5f5728b
- Add a LinkedIn Profile Account — https://www.sprinklr.com/help/articles/getting-started/add-a-linkedin-profile-account/63fef89032d12b63c5f55c55
- Add Multiple Account Administrators with Multiple Authorization Tokens (LinkedIn) — https://www.sprinklr.com/help/articles/getting-started/add-multiple-account-administrators-with-multiple-authorization-tokens-linkedin/685cd8afc141ae04d1a86b0d
- LinkedIn Capabilities and Limitations — https://www.sprinklr.com/help/articles/getting-started/linkedin-capabilities-and-limitations/63fef3567a695d65a1605897
- LinkedIn Media Guidelines — https://www.sprinklr.com/help/articles/getting-started/linkedin-media-guidelines/6406c9b97a695d65a1606e74
- LinkedIn Channel Updates — https://www.sprinklr.com/help/articles/getting-started/linkedin-channel-updates/63f76a399b334f7283b4da32
