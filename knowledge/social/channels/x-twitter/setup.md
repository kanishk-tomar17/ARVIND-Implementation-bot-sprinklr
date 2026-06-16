# X — Account Setup & Configuration (Sprinklr Social — X (formerly Twitter))
**Source:** sprinklr.com/help — X (formerly Twitter) channel (multiple articles; see links below)

## What it is
- How to connect and manage X (formerly Twitter) accounts inside Sprinklr Social.
- Covers four common admin tasks: adding an X account, changing the default reply handle, updating an account cover photo, and what changed under X's v2 API migration.
- All tasks live under **Sprinklr Social** (account management is in **Owned Social Accounts** / **Listen**); reply-handle changes also touch [[engagement-dashboards]] and the [[rule-engine]].
- An X account can belong to only **one Workspace** at a time; admins must share it to make it visible in other workspaces.

## Key features & how to use

### Add an X account
- **Prerequisite:** Log into the exact X account you want to connect *before* you start (the OAuth popup uses whatever X session is active in the browser).
- Open **Sprinklr Social** → under **Listen**, select **Owned Social Accounts** (Accounts window).
- Click **Add Account** (top-right of the Accounts window).
- In the **Add Account** picker ("Choose a channel you would like to add an account for"), search and select **X** — the blue X tile, not **X Ads** (a separate grey tile).
- In the **Authorize Sprinklr on X** popup: optionally toggle **Disable Private Messages** ON if you do not want to receive DMs for this account, then click **Next**. (The popup reminds you to ensure the correct X account is logged in.)
- In X's **Authorize SprinklrProd0 to access your account?** window, click **Authorize app**. The grant covers: reading tweets/timeline/Lists, profile and account settings, follow/unfollow, post/delete/engage with tweets, manage Lists/collections, mute/block/report, send/read/manage DMs, and read/manage advertising data (campaigns, audiences, ad accounts, creatives).
- Complete the **Update Account** window:
  - **Account Details** — display name in Sprinklr, owner user, custom character count, default URL shortener, auto-populated reply signature.
  - **Permissions** — grant channel-action access to specific Users / User Groups.
  - **Share this Account Across Spaces** — pick Workspaces or share globally.
  - **Subscribers** — Users / User Groups to notify about the account.
  - **Timezone** — associate a country and time zone.
  - **Properties** — any custom account properties.
- Click **Save** (bottom-right).

### Change default reply handle for X
Three ways to control which X account a reply is sent from. First two are per-reply (manual); the third automates it via [[rule-engine]].
- **Agent Console (per reply):** New Tab → **Agent Console** (under Sprinklr Service) → Dashboard Menu (top-left) → choose the X dashboard → select a case/message → **Write a Reply** → in the Reply window click the account **dropdown** and select the Account to reply from.
- **Engagement Dashboard (per reply):** New Tab → **Engagement Dashboards** (under Sprinklr Social) → Dashboard Menu → choose the X dashboard → **Reply** on the target message → click the **dropdown** in the Reply window and select the Account to reply from. See [[engagement-dashboards]].
- **Rule Engine (automated / Autofill):** Platform Modules → **Manage Rules** → **Create New Rule** → set **Rule Scope = Workspace** and **Context = Autofill** → add **Conditions** for Channel = X and the account → add an **Action: "Change properties of Message" → From Account → Set → <handle>** (this is the field highlighted in the rule builder) → **Save**.

### Update X account cover photo
- New Tab → **Sprinklr Social** → **Owned Social Accounts** (under Listen).
- In the Accounts window, click the **All Channels** filter (top-left), search/select **X** to filter to X accounts only (the dropdown shows active vs inactive counts per channel).
- **Check the box** next to the X account(s) to update — the bottom action bar appears showing the selected count.
- Click **Update Cover Photo** in that bottom bar (alongside Deactivate / Apply Macro).
- In the **Update Cover Photo** popup, click **Upload**.
- In the **Media Uploader**, pick an existing asset from [[asset-manager]] or upload a new image, then click **Add** (bottom-right).
- Click **Save** (bottom-right) to apply.
- **Image specs:** supported types jpeg, jpg, gif, png, BMP. Best results at **1500 x 500** px.

### X v2 API migration changes (19.5 release)
X moved all major endpoints to the v2 API; Sprinklr migrated starting in the 19.5 release. Three feature gaps result:
- **Reporting** — the **source** field is gone from v2. The inbound message **Message Source Name** and **Message Source Link** (e.g. "Twitter for iPhone", "Twitter Web App", "http://twitter.com/download/iphone") are no longer available when plotting inbound messages. See [[reporting]].
- **Rule Engine** — **Quick Reply** and **Quick Reply Response** fields are unavailable, so the **Template Button Post back** condition can no longer be used when building a rule. See [[rule-engine]].
- **Distributed Product Suite** — the **Cover Image URL** is not returned by v2 APIs, so cover images cannot be retrieved for X Social Accounts within Sprinklr (relevant to the cover-photo workflow above).

## Common issues & fixes
- **Wrong account authorized when adding:** the OAuth flow uses the X session already logged into the browser. Log into the intended X handle first, or log out of the wrong one before clicking Add Account.
- **Account not visible in another workspace:** an X account lives in one Workspace; have an admin share it across spaces (in **Update Account → Share this Account Across Spaces**).
- **Picked the wrong tile:** select **X** (blue tile), not **X Ads** (separate grey tile) — they are different channels.
- **Missing message source in Reporting / can't use Template Button Post back / cover image not rendering:** expected behaviour post v2 migration, not a config error (see v2 section). X controls parity-gap resolution timing, so continuity may vary.

## Notes & gaps
- **Permissions/role:** adding accounts, sharing across spaces, and building rules are admin-level tasks; specific permission names aren't spelled out in the articles.
- The X OAuth grant is broad (includes DMs and ad data) even if you only manage organic — toggle **Disable Private Messages** if DMs aren't wanted.
- Articles don't specify cover-photo file-size limits (only file types and the 1500x500 recommendation).
- No timeline given for if/when X may close the v2 parity gaps; treat the lost fields as ongoing limitations.
- Reply-handle articles reference both Agent Console (Sprinklr Service) and Engagement Dashboards (Sprinklr Social) — pick whichever console the team works in.

## Sources
- Add an X Account — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/add-an-x-account/63f49fe2e02459133724a67e
- Change Default Reply Handle for X — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/change-default-reply-handle-for-x/640aaf2e2680c35a78bb1fbd
- Update X Account Cover Photo — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/update-x-account-cover-photo/66840cb9bc79b41a23e25ffa
- X v2 API Migration Changes — https://www.sprinklr.com/help/articles/getting-started-x-formerly-twitter/x-v2-api-migration-changes/665424deefb7ac0fc978824e
