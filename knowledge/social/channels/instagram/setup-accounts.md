# Instagram — Account Setup (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- How to connect and manage Instagram accounts in Sprinklr: which account types are supported, how to add them, how to link/relink them to Facebook Pages, how to grant per-action channel permissions, and how to re-add an account when its token expires.
- Sprinklr only supports Instagram **Business** and **Creator** accounts. Personal profiles are no longer supported (Instagram deprecated the Personal Profile API in March 2020).
- Every Instagram account must be a Business/Creator account **linked to a Facebook Page** on which you hold an **admin** role — this is the hard prerequisite for adding it to Sprinklr.
- A social account can live in only **one Workspace** at a time; to use it elsewhere, share it via account sharing.
- Account connections rely on social-network access tokens; when a token expires the account goes inactive and must be **re-added** (re-authenticated) to keep working.

## Key features & how to use

### Types of Instagram accounts
- **Business account** — Instagram's equivalent of a Facebook Page. Signals the account is used for marketing and unlocks features unavailable to personal profiles. **Preferred type** for full Sprinklr functionality.
- **Creator account** — aimed at influencers/creators; offers similar exclusive features and detailed analytics. Limit: if a Creator account has **≥ 500K followers**, the Instagram API will **not** fetch Instagram Direct Messages for it. Convert such Creator accounts to Business to retain DM fetching.
- **Personal profile** — **not supported.** Instagram deprecated the Platform API behind personal-profile support in March 2020; you cannot add a personal Instagram account in Sprinklr (cutoff 31 March 2020).
- Bottom line: use Business (preferred) or Creator (mind the 500K DM limit).

### Add Instagram Business/Creator accounts in Sprinklr
- **Prerequisites:** be logged into the exact Instagram account you want to add; account must be a **Business** (or Creator) account linked to a Facebook Page; you must have **admin** rights on that Facebook Page.
- **Limit:** an account can be added to only one Workspace — share it for multi-workspace use.
- **Steps:**
  1. Click the **New Tab** icon → under **Sprinklr Social**, go to **Listen → Owned Social Accounts**. (The launcher shows four product columns — Sprinklr Service, Insights, Marketing, Sprinklr Social. "Owned Social Accounts" sits under the **Listen → Integrated Listening** heading in the Sprinklr Social column.)
  2. In the Accounts Settings window, click **Add Account** (top right).
  3. In the **Add Account** window ("Choose a channel you would like to add an account for"), search/select **Instagram** from the channel tile grid. (Tip: type "in" in the search box to filter; the Instagram tile uses the camera-style Instagram glyph.)
  4. In the authorization popup, click **Go to Instagram** and log into the associated **Facebook profile** when prompted.
  5. Configure account details: edit the **account name** shown in Sprinklr; assign a **Sprinklr User** as account owner; set a **custom character count** for replies; choose a **default URL shortener**; add an **auto-populated signature** for replies.
  6. Under **Permissions**, assign channel access to Users and User Groups.
  7. Set remaining options: **Share this Account Across Spaces** (workspace visibility), **Subscribers** (notification recipients), **Timezone**, and **Properties**.
  8. Click **Save** (bottom right).
- **If you see "No Instagram Business Accounts Found":** Sprinklr is telling you the account doesn't meet requirements. The dialog spells out two conditions: (1) it must be **a business profile** — it even lets you type an Instagram username and click **Verify**; a personal account returns "<username> is not a Business account or does not exist on Instagram"; (2) it must be **linked to a Facebook Page on which you have admin access**. Fix the account natively, then **Go Back** and retry.

### Link Instagram Business account with Facebook page
- **Prerequisites:** your Facebook profile must have an **admin** role on the target Page; the Instagram account must be a **Business** account (the article notes "not a Creator account" for this native flow).
- **Method 1 — via Facebook:**
  1. In Facebook, open **Pages** from the left menu and **Manage** your Page (the **Manage** button sits in the Page header next to Create ads / Edit).
  2. Go to **Linked Accounts** in the left column (under the Professional dashboard → "Linked accounts" — "Engage with your community across WhatsApp, Instagram and Facebook").
  3. Select **Instagram** → **Connect Account**.
  4. Enter your Instagram credentials when prompted.
- **Method 2 — via Instagram:**
  1. Open your Instagram profile → **Edit Profile**.
  2. Under **Public Business/Profile Information**, choose **Page**.
  3. Select the Facebook Page — linkage happens automatically. (Tap **Create Facebook Page** if you need a new one.)

### Change Instagram accounts linked to Facebook pages
- **Prerequisite:** your personal Facebook account must have **admin** access on the target Page.
- **Method 1 — from Facebook:**
  1. Facebook → **Pages** → open the Page → **Manage**.
  2. **Linked Accounts** (left column) → **Instagram** → **Disconnect Account**.
  3. Confirm with **Yes, Disconnect** and enter your Instagram credentials.
  4. Follow the prompts to connect a different Page.
- **Method 2 — from Instagram:**
  1. Instagram profile → **Edit Profile**.
  2. Under **Public Business/Profile Information**, find the **Page** section.
  3. Select **Change or Create Page** and pick a different Facebook Page (or create one).

### Grant access to perform specific channel actions
- **Steps:**
  1. New Tab → **Sprinklr Social → Listen → Owned Social Accounts**.
  2. On the account, open the **Options** icon (⋮) → **Edit**. (You can also assign permissions while adding a new account.)
  3. Ensure you have **Administrator** access to the Instagram account — required to grant action permissions.
  4. Add the **Users / User Groups** that need access and assign the relevant action permission(s). Action types include: **Publishing**, **Viewing Planner**, **Fetching Engagement**, **Obtaining Reporting data**, and **Performing Channel Actions**.
  5. Click **Add New Permission** to grant additional action-type permissions.
  6. Click **Save** (bottom right).

### Re-add an account
- **When/why:** social-network access tokens expire or become invalid; the account then shows **Inactive** ("Deactivated due to invalid access token, please re-add the account"). Re-adding regenerates a fresh token. Use a Quick Filter of **Inactive** to find affected accounts.
- **Steps (list view):**
  1. New Tab → under Platform Modules / Sprinklr Social, open **Social Accounts** (within Listen).
  2. Next to the inactive account, click the **red triangle** (⚠) icon. A small dialog appears with two buttons: **Notify Admin** and **Re-Add**.
  3. Click **Re-Add** to launch the account type's authentication flow (same steps as Add an Account).
- **Steps (account-detail view):** open the account; the third pane (Overview) shows the same banner with **Notify Admin** and **Re-Add**, plus toolbar actions **Remind owner to re-add**, **Edit**, **Web Analytics**, **Activity**, **Remove Account**. Account Details here also show Owner, Owner Workspace, User ID, Custom Character Limit, Timezone, Account Role, and the token **Expired** date.

### Instagram post preview changes (Oct 2025)
- **What changed:** Meta deprecated the **oEmbed API** endpoint effective **1 October 2025**. Affects how Sprinklr displays previews for **inbound** Instagram content (fetched via APIs — comments, tagged media, listening mentions) where media has **expired or is no longer available**.
- **What consultants/users see:** instead of the image/video inline, affected posts show a placeholder with a **"Click to View"** link to open the content at source.
- **Where it shows up:** Listening Dashboards, Reporting Dashboards (metrics still available), Engagement Columns (comments may lack thumbnails for tagged media), UGC Discovery, Care Console (tagged mentions / story mentions show "Click to View"), and PII-masking scenarios.
- **What is NOT affected:** data availability, reporting metrics, and your ability to engage. Active, non-expired Instagram media and content **published through Sprinklr** are unaffected.

## Common issues & fixes
- **"No Instagram Business Accounts Found" when adding** — the account isn't a Business profile and/or isn't linked to a Facebook Page you admin. Convert to Business in the Instagram app, link it to a Page where you're admin, then retry. Use the dialog's **Verify** field to confirm the username resolves to a Business account.
- **Direct Messages not fetching for a Creator account** — caused by the **≥ 500K follower** API limit on Creator accounts. Convert the account to **Business**.
- **Account shows Inactive / "Deactivated due to invalid access token"** — token expired; click the red triangle → **Re-Add** (or use Remind owner to re-add). See [[manage-accounts]].
- **Instagram previews show "Click to View" instead of media** — expected post-1 Oct 2025 oEmbed deprecation for expired inbound media; not a data loss. See post-preview section above.
- **Re-add after relinking** — if you changed the native Instagram↔Facebook link: confirm the link natively, then in Sprinklr open the IG account's Options → **Unlink Business Account**, re-add the Facebook Page account, re-add the Instagram account, and relink via the Options icon.

## Notes & gaps
- **Hard prerequisites for adding:** Business (preferred) or Creator account + linked Facebook Page + **admin** role on that Page + Administrator access on the Instagram account to grant permissions.
- One account = one Workspace; cross-workspace use requires account sharing.
- The native linking article specifies Business (not Creator) for the Instagram↔Facebook link flow; in practice Creator accounts are still addable to Sprinklr (subject to the DM follower limit).
- Menu labels vary slightly across articles ("Owned Social Accounts" vs "Social Accounts within Listen") — both refer to the same Accounts settings under Sprinklr Social → Listen.
- Facebook's native UI (Pages, Manage, Linked Accounts, Professional dashboard) changes frequently; exact button placement may differ from the screenshots dated Feb 2023.
- Not specified in sources: exact permission-scope behavior per role, token lifetime/expiry windows, and whether re-add preserves historical engagement data (implied yes — re-add only refreshes the token).

## Sources
- Add Instagram Business & Creator Accounts in Sprinklr — https://www.sprinklr.com/help/articles/setting-up-instagram-in-sprinklr/add-instagram-business-creator-accounts-in-sprinklr/63e37742a9d51179030165fa
- Link Instagram Business Account with Facebook Page — https://www.sprinklr.com/help/articles/setting-up-instagram-in-sprinklr/link-instagram-business-account-with-facebook-page/63e3760ea9d51179030165f5
- Types of Instagram Accounts — https://www.sprinklr.com/help/articles/setting-up-instagram-in-sprinklr/types-of-instagram-accounts/63e37045a9d51179030165cf
- Change Instagram Accounts Linked to Facebook Pages — https://www.sprinklr.com/help/articles/setting-up-instagram-in-sprinklr/change-instagram-accounts-linked-to-facebook-pages/63e379e3a9d5117903016607
- Grant Access to Perform Specific Channel Actions — https://www.sprinklr.com/help/articles/setting-up-instagram-in-sprinklr/grant-access-to-perform-specific-channel-actions/63e37b6a55780d70a15bd994
- Re-add an Account — https://www.sprinklr.com/help/articles/manage-accounts/readd-an-account/63ef5b18ef1b447d6c631c85
- Instagram Post Preview Changes — https://www.sprinklr.com/help/articles/instagram-post-preview-changes/instagram-post-preview-changes/68be66601c434d661336f089

## Related
[[facebook]] · [[publishing]] · [[engagement-dashboards]] · [[reporting]] · [[rule-engine]] · [[care-console]] · [[asset-manager]] · [[user-generated-content]]
