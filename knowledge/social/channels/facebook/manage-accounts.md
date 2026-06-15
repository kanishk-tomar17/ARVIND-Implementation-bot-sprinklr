# Facebook — Managing Accounts (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- Covers the day-to-day administration of connected Facebook Page accounts in Sprinklr: adding/re-adding pages, managing the people and authorization tokens behind a page, configuring Messenger, updating cover photos, adding location pages, and diagnosing why an account goes inactive.
- Most actions live in **Governance Console > Platform Setup > Accounts** (the Accounts/Settings screen), reached from the **+ New Tab** icon or Universal Search ("All Settings").
- Per-account actions are exposed via the **three-dot (vertical ellipses) menu** on each Facebook Page row. Bulk actions appear in a bottom action bar once you tick one or more accounts.
- Filter the Accounts list to **Facebook Page** (channel dropdown, top-left) and use Quick Filter (e.g. Active/Inactive) to find the page you need.
- See also [[publishing]], [[engagement-dashboards]], [[rule-engine]], [[asset-manager]], [[governance-console]].

## Key features & how to use

### Multiple page administrators / multiple authorization tokens
- **Why:** lets more than one user's token back a single Facebook Page in Sprinklr, so the page keeps working if one admin's account is deactivated, password-changed, or loses its page role.
- **Gated by** the dynamic property `MULTIPLE_AUTH_TOKENS_ENABLED_ACCOUNT_TYPES` — ask a Sprinklr admin/Success Manager to enable it if missing.
- **Step 1 — make the user a native Facebook page admin first** (token is only valid if the user actually has the role on Facebook):
  - *Classic Pages:* Facebook **Feed > Pages > Settings > Page roles** > enter name/email > pick **Admin** from the dropdown > **Add** > confirm with password. Invitee must accept the invitation before they can manage the page.
  - *New Pages:* Facebook **Manage > Page access > Add New** > enter name/email > choose partial or full control > confirm with Facebook password. Invitee accepts via email.
- **Step 2 — add the token in Sprinklr:** each admin logs into Sprinklr and connects the same page (see "Re-add / add a Facebook Page" below). Their token is added to the page's token pool.
- **Step 3 — manage tokens:** on the account row, three-dot menu > **Authenticate Tokens** opens the **Authorise Tokens** dialog. Each connected user is listed with an **In Use / Not In Use** toggle; switch which token is active, and delete (trash icon) tokens you no longer want. Sprinklr publishes/fetches using the "In Use" token.
- *Prereqs:* the page must already exist in Sprinklr; new admins must hold a native Admin (or sufficient) role on the Facebook page.

### Re-add a Facebook Page (re-authenticate)
- **Use when** tokens expire from a password change, account deactivation, or revoked access — re-adding refreshes the connection without rebuilding config.
- Steps (Accounts screen):
  1. **+ New Tab** > Governance Console > **Platform Setup > Accounts**.
  2. Click **Add Account** (top-right).
  3. In the Add Account window pick **Facebook Page**.
  4. Authenticate with Facebook; the Facebook Pages list appears — tick the page(s) and click **Add**.
  5. In the Sprinklr **Edit** window, fill all required account details and click **Save**.

### Configure Facebook Messenger (Welcome Screen + Persistent Menu)
- Account row three-dot menu > **Configure Your Messenger** opens the **Messenger Configuration** screen (live mobile preview on the right).
- **Configure Welcome Screen:**
  - **Enabled on Facebook** checkbox — turns the welcome screen on.
  - **Set Greeting Text** — shown only the first time a user opens Messenger with the page (character counter shown; e.g. limit ~160).
  - **Upload Asset** — the asset sent when the user taps the **Get Started** button; pulls from [[asset-manager]] (DAM).
- **Configure Persistent Menu** (the always-available menu in the chat):
  - **Enabled on Facebook** checkbox.
  - **Allow the user to chat with you** checkbox (keeps the text composer available).
  - **Add Another Menu Item** to add rows; each menu item has a **Label** (char-limited) and an **Action**:
    - **Add URL** — opens a destination URL (enter it in the **URL** field).
    - **Select Reply from Asset Manager** — sends a saved chat template/asset.
  - **Save** to apply.
- **Limitation (Meta):** the Persistent Menu is **not supported when Messenger is opened via the Facebook mobile browser**.

### Update cover photo (single or bulk)
- Account row three-dot menu > **Update Cover Photo**, OR tick multiple Facebook accounts and use **Update Cover Photo** in the bottom bulk-action bar (alongside Deactivate, Edit Channel Properties, Apply Macro).
- Choose an image from **Asset Manager** or **upload a new image**, then **Save**. Updates one or many pages at once.

### Add Facebook Location Pages (and Global Pages)
- **Use when** a business has multiple locations under a parent page; lets you manage each Location Page and run location-specific ads.
- *Prereqs:* a Facebook Page already connected to the workspace + admin permissions to manage workspace accounts.
- Steps:
  1. **+ New Page > Launch Pad > Sprinklr Social** (or open All Settings via Universal Search).
  2. **Manage Workspace > Accounts**.
  3. Set the channel filter to **All Channels** (or Facebook Page).
  4. Hover the parent Facebook Page > three-dot **(vertical ellipses)** > **Add locations**.
  5. In the popup, select the desired **Location Page(s)** > **Add**.
- **Note:** Facebook **Global Pages** behave like Location Pages — all Sprinklr Location-page capabilities apply to Global Pages too.

### Handover Protocol for Facebook Messages (bot <-> agent)
- **What it does:** lets a bot and Sprinklr (agent platform) hand control of a Messenger conversation back and forth. Only set this up if your bot actually hands off to human agents — fully automated bots don't need it. Capability is enabled by your Success Manager.
- **Roles:** **Primary Receiver** (usually the bot — starts conversations, can reclaim control from any app in v2) and **Secondary Receiver** (Sprinklr — takes over when a human is needed).
- **Set Sprinklr as Secondary Receiver (native Facebook):** Facebook Page **Settings & privacy > Page setup > Advanced messaging** > **Messenger receiver (Handover protocol)** > **Configure** > in App Settings click **Select** > choose **Sprinklr**.
- **Via [[rule-engine]] (Governance Console > Platform Setup > Manage Rules):**
  - *Condition:* **Has conversation control** (checks if Sprinklr currently controls the thread; Facebook Messenger source only).
  - *Action:* **Conversation Thread Control** — options: Request Thread Control, Take Thread Control, Pass Thread Control (As Primary to Secondary), Pass Thread Control (As Secondary to Primary/Secondary), Pass Thread Metadata, Release Thread Control, Extend Thread Control.
- **Manual control in [[engagement-dashboards]]:** add a Facebook Messenger column > message Options icon > **Pass on Control** (add comment > Pass) or **Request Control** (optional comment > Request).
- **Via Case Actions:** create a Yes/No custom field (e.g. "Initiate Handover"), set it to Yes in a Case Close macro, then use an On-Demand Case Update rule + a Queue rule to copy the flag to the last fan message and trigger the handover.
- **v2 behavior:** thread control is exclusive (only the controlling app can send; others stay on standby for analytics). **Idle mode** when no primary is set / ownership expires (24h) / controlling app releases — any app can then claim ownership. Apps can pass metadata and **Extend** the 24-hour window.

## Common issues & fixes
Facebook account shows **Inactive/deactivated** in Sprinklr — common reasons and fixes:
- **Password / security alert:** caused by password updates or a suspicious login. Fix: keep consistent credentials, don't share logins, enable login alerts, then re-add the account.
- **Access revoked:** Sprinklr removed from Facebook **Business Integrations**. Fix: reconnect the account to restore the connection.
- **Security checkpoint triggered:** suspected compromise / incomplete 2FA / policy issue. Fix: clear browser cookies & history, complete Facebook's security checks, enable 2FA, wait ~24h, then reconnect.
- **Token expired:** the connecting user no longer has the **Admin** role on the page/group. Fix: an admin must reconnect (or use the multiple-token feature above).
- **Unconfirmed account:** unresolved issue on Facebook's side. Fix: sign into Facebook and resolve what it flags.
- **Insufficient page role:** user isn't Admin/Editor. Fix: restore the proper page role, then reconnect.
- **Sprinklr lacks page permissions:** missing/removed scopes in **Business Integrations**. Fix: grant all requested permissions to Sprinklr.
- **Page restriction settings:** country/age restriction or page is unpublished. Fix: review and adjust page visibility.
- General recovery for most of the above is to **re-add the Facebook Page** (see that section).

## Notes & gaps
- **Permissions/prereqs:** workspace admin rights to manage accounts; the connecting Facebook user must hold a sufficient native page role (Admin for most actions). Multiple-token feature needs the `MULTIPLE_AUTH_TOKENS_ENABLED_ACCOUNT_TYPES` dynamic property enabled. Handover Protocol capability is enabled by Sprinklr (Success Manager).
- **Greeting text / menu-label character limits** are enforced in the UI but exact maxima aren't documented in the articles (counter shown is ~160 for greeting text).
- The deactivation-reasons article lists causes/fixes but does not give exact error strings as shown in the Accounts grid.
- Asset uploads for Messenger and cover photos draw from [[asset-manager]] (DAM).
- Navigation labels differ slightly between the classic Governance Console path and the newer Launch Pad / Manage Workspace path; both land on the same **Accounts** screen.

## Sources
- Add Multiple Page Administrators with Multiple Authorization Tokens (Facebook) — https://www.sprinklr.com/help/articles/manage-facebook-accounts/add-multiple-page-administrators-with-multiple-authorization-tokens-facebook/63ecd36def1b447d6c630704
- Re-add Facebook Page in Sprinklr — https://www.sprinklr.com/help/articles/manage-facebook-accounts/readd-facebook-page-in-sprinklr/63ebc10aef1b447d6c61e8c6
- Facebook Messenger Configuration — https://www.sprinklr.com/help/articles/manage-facebook-accounts/facebook-messenger-configuration/63e9e88cf6e2cc7d18f9625e
- Update Facebook Account Cover Photo — https://www.sprinklr.com/help/articles/manage-facebook-accounts/update-facebook-account-cover-photo/63ebbc48ef1b447d6c61e88e
- Facebook Account Deactivation Reasons — https://www.sprinklr.com/help/articles/manage-facebook-accounts/facebook-account-deactivation-reasons/63e9eb5cef1b447d6c61b22d
- Handover Protocol for Facebook Messages — https://www.sprinklr.com/help/articles/getting-started-facebook/handover-protocol-for-facebook-messages/6335d7fc389c4165d05714ed
- Add Facebook Location Pages — https://www.sprinklr.com/help/articles/add-facebook-location-pages/add-facebook-location-pages/671b9ea72e64c74e57239480
