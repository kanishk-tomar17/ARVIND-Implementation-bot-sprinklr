# Facebook — Adding Accounts (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- How to connect Facebook assets to Sprinklr so they can be used for [[publishing]], [[engagement-dashboards]], and [[reporting]].
- Sprinklr supports several Facebook channel types from one "Add Account" picker: **Facebook Domain, Facebook Page, Facebook Profile, Facebook Ads, Facebook Business Manager, Facebook Group (now disabled), Facebook Workplace Bot**.
- A page can be added at different permission levels depending on the access the connecting profile holds natively on Facebook: **Admin**, **Editor**, or **Advertiser**. The dialog labels each page with the role it will be added as (e.g. "Adding as Admin").
- Some capabilities are gated: System User functionality, Meta Work Accounts, and the Facebook Groups API (deprecated/removed).
- Rule: **one social account can only be added to a single Workspace** — share it across spaces if other workspaces need it.

## Key features & how to use

### Add a Facebook Page (standard)
- Go to **Sprinklr Social tab → Listen → Owned Social Accounts** (top-level tab picker shows the four products; under Sprinklr Social the left column "Listen" contains "Owned Social Accounts").
- Click **Add Account** (top-right). In the **Add Account** picker, search "face" and select **Facebook Page** (tiles: Domain, Page, Profile, Ads, Business Manager, Group, Workplace Bot).
- Click **Go to Facebook** and authorize Sprinklr (enter the Facebook email/password of a profile with admin access to the page; complete Facebook auth prompts).
- In the **"Select the accounts you want to add"** dialog: tick the page(s) or **Select all**. The dialog shows last-sync time, a search box, and **Account Status / Added in Sprinklr / Account Groups** filters. Each page shows its role on the right (**"Adding as Admin"**). Footer shows "X/Y Selected". Click **Add**.
- If a recently granted page is missing, click **Resync** (top-right of the dialog) and reselect.
- In the **Update Account** window set: Account Details (name, owner, character count, URL shortener, signature), Permissions (channel actions per user/group), **Share this Account Across Spaces** (workspace visibility), Subscribers, Timezone (country + zone), Properties. Click **Save**.
- Prereqs: Sprinklr Social access, Facebook page **admin** access, permission to add accounts to your Workspace. Facebook pages are treated as company pages in Sprinklr.

### Add Facebook Pages — limited availability (large page sets)
- Same flow as standard, but built for accounts that own **many pages**: Sprinklr fetches and stores the pages in parts via backend synchronization, so the list can populate progressively.
- If newly acquired pages don't appear in the "Select the accounts you want to add" pop-up, use **Resync**, then reselect and **Add**.
- This is a limited-availability behavior; enablement may require Sprinklr support.

### Add a Facebook Business Manager account
- Add Account → **Facebook Business Manager**. Lets you manage ad accounts, pages, and people from one place.
- Authenticate, select the desired business manager account, then edit details in the **Update Account** window and **Save**.
- Prereq: you must be an **Admin of the Ad Account natively in Facebook**.
- Can be reached either via Owned Social Accounts or via **Governance Console → Accounts** under Platform Setup.

### Add Facebook Pages with System User functionality (gated)
- Purpose: connect pages via a Meta **System User** token so access doesn't depend on a personal profile's login.
- **Enablement requires a support ticket.** Needs Facebook Business Manager admin access.
- Setup: 1) Connect Business Manager to Sprinklr (Add Facebook Business Manager → authenticate/grant permissions; Sprinklr stores the BM ID + token). 2) Choose **Setup System User** on the connected Business Manager — Sprinklr generates the System User token automatically via Meta's "On-Behalf-Of" APIs with minimum permissions for publishing, engagement, reporting.
- Then add pages via the normal Add Facebook Page flow. In the **Accounts** list, open the per-row **⋮ (three-dot) action menu** and choose **Enable System User** (supports single or bulk). Other menu actions there: Details, Edit, Web Analytics, Update Cover Photo, Add Locations, Configure Your Messenger, Authenticate Tokens, Activity, Deactivate, Remove Account, Configure Conversation Routing, Grant Permission to Take Thread Control, Link Account, Authorise Url.
- Verify with the **"Page moved to System User"** filter.
- System User **can**: publish (incl. dark posts), fetch/moderate comments & messages, read insights. **Cannot**: delete pages, remove other users' access, or do sensitive admin-only tasks.

### Add a Facebook brand page with Editor permission
- Use when the connecting profile has **Editor** (not full admin) access to a brand page.
- **Grant access on Facebook first** (New Pages experience): Profile → Settings & Privacy → Settings → **New Pages experience** → **Page access** → under "People with task access" click **Add New** → select the profile → grant **all five** task areas: Content, Messages, Community activity, Ads, Insights → **Give Access**. The invited user must **accept** the invitation.
- In Sprinklr: Owned Social Accounts → Add Account → Facebook Page → authenticate with that Editor profile → in the select dialog the page shows **"Adding as Editor"** → **Add** → set details/permissions/sharing → **Save**.
- Verify: Account Role shows **"Authorized as Editor"**. Editor access enables publishing and engagement (Content, Messages, Community Activity, Ads, Insights).

### Add a Facebook brand page with only Advertiser access
- Use when the profile has only **Ads + Insights** access.
- **On Facebook (New Pages experience):** Page access → People with task access → Add New → select profile → grant **Ads** and **Insights** only → Give Access → user accepts.
- In Sprinklr: Add Account → Facebook Page → authenticate (do **not** edit/limit permissions during auth) → in the select dialog the page shows **"Adding as Advertizer"**; a tooltip notes an *Advertiser account can create dark posts and ads but cannot create organic posts* → **Add** → configure details/permissions/workspace → **Save**.
- Verify: Account Role shows **"Authorized as Advertiser"**.

### Add a Facebook Workplace account (Workplace Bot)
- Add Account → search and select **Facebook Workplace Bot**.
- Enter: Account image (Media Uploader), Name (reference identifier), **Bot Token**, **App Key**, **App Secret Key** — all obtained from your Facebook Workplace bot setup. Click **Save**.
- Then configure: Account Details, Groups to include, Permissions (users/user groups), Share Across Spaces (or share globally), Subscribers, Timezone, Properties → **Save**.

### Meta Work Accounts
- Meta Work Accounts are a business-tools account type that lets orgs manage Meta assets with SSO/automated provisioning **without personal Facebook accounts**.
- **Enablement:** contact your Success Manager. The connecting user must be **logged into the Managed Meta Account in the same browser**, and the flag `FACEBOOK_PAGE_BUSINESS_MANAGEMENT_SCOPE_DISABLED` must be **disabled** to allow account addition.
- Add via the normal flow: Owned Social Accounts → Add Account → **Facebook Page** or **Facebook Ads** → select account(s) → **Add** → configure in Update Account → **Save**.
- **Log into a Managed Meta Account:** go to **business.facebook.com → Other login options → Log in with managed Meta account →** enter email → **Next** → password → **Continue**.
- **Filter Work Accounts:** Sprinklr Social → Social Accounts → pick channel type (Facebook Page / Facebook Ads) → **Add Filter** → search icon → **Apply Filters**.
- **Migration deadline:** when a user migrates from a personal account to a Work account, a **30-day countdown** starts — the page must be **re-added in Sprinklr within 30 days** or access breaks.

## Common issues & fixes
- **Page not showing in the select dialog** → click **Resync** (recently granted access takes time to propagate), then reselect and **Add**. Confirm the connecting profile actually has access on Facebook.
- **"Account Addition is Disabled" on Facebook Group** → expected. Facebook **Groups API was removed by Meta on 22 Apr 2024**. You can no longer add new groups; publishing/scheduling, fetching new posts/comments/replies, engaging, and post insights for groups all stopped. **Historical group data is view-only.** No migration path — stop relying on Sprinklr for group management. Existing group accounts show a deprecation alert.
- **Can't create organic posts on a page** → the page was likely added as **Advertiser** (dark posts/ads only). Re-add with Editor/Admin access for organic publishing.
- **Work Account access suddenly broken** → likely missed the **30-day re-add window** after migrating from a personal account; re-add the page.

## Notes & gaps
- **Permission level is inherited from Facebook**, not chosen in Sprinklr — the role label ("Adding as Admin / Editor / Advertizer") reflects native page access. Grant the right task access on Facebook *before* adding.
- One account = one Workspace; use **Share this Account Across Spaces** for multi-workspace visibility.
- System User and Meta Work Accounts are **gated** (support ticket / Success Manager). Work Accounts also need `FACEBOOK_PAGE_BUSINESS_MANAGEMENT_SCOPE_DISABLED` off.
- **Facebook Profile ID migration (effective 1 May 2019):** the first interaction of a fan with any brand page creates a **new profile** even if they've interacted with another brand page. Impact — duplicate profiles per fan across pages, conversations cannot be stitched (API limit), universal profile search and inbound analytics show duplicates. In [[Service|sprinklr-service]]: case association rules work only for existing **ASID** profiles; new **PSID** profiles can't associate cases across brand pages (cases restricted to originating account). Facebook **Public** Survey auth won't work for new (PSID) profiles; private surveys unaffected. Sprinklr migrated only profiles with ≥1 interaction since 1 Jan 2018; messages/cases were **not** migrated; newly activated pages treated as fresh.
- Workplace Bot credentials (Bot Token, App Key, App Secret Key) must be generated in Facebook Workplace beforehand — Sprinklr does not create them.
- Exact field availability in the Update/Add Account window can vary by environment and channel.

## Sources
- Add Facebook Page in Sprinklr — https://www.sprinklr.com/help/articles/add-facebook-account-in-sprinklr/add-facebook-page-in-sprinklr/63e9edb7ef1b447d6c61b233
- Add Facebook Business Manager Account to Sprinklr — https://www.sprinklr.com/help/articles/add-facebook-account-in-sprinklr/add-facebook-business-manager-account-to-sprinklr/63e9ece6f6e2cc7d18f96262
- Add Facebook Workplace Account in Sprinklr — https://www.sprinklr.com/help/articles/add-facebook-account-in-sprinklr/add-facebook-workplace-account-in-sprinklr/63e9f61cef1b447d6c61b239
- Add Facebook Brand Page with Editor Permission on Profile — https://www.sprinklr.com/help/articles/add-facebook-account-in-sprinklr/add-facebook-brand-page-with-editor-permission-on-profile/6530e58697b5a116694d7e29
- Add Facebook Pages in Sprinklr (Limited Availability) — https://www.sprinklr.com/help/articles/add-facebook-account-in-sprinklr/add-facebook-pages-in-sprinklrlimited-availability/65f2bb43b12e9e1ec77ba307
- Add Facebook Pages with System User Functionality — https://www.sprinklr.com/help/articles/add-facebook-account-in-sprinklr/add-facebook-pages-with-system-user-functionality/6968aa823b90964a40596e4c
- Add Facebook Brand Page with only Advertiser Access in Sprinklr — https://www.sprinklr.com/help/articles/getting-started-facebook/add-facebook-brand-page-with-only-advertiser-access-in-sprinklr/65ddb4215a724c45fadf35db
- Meta Work Accounts — https://www.sprinklr.com/help/articles/getting-started-facebook/meta-work-accounts/6645ce5fb184450fe1ac3a72
- Meta Deprecates Facebook Groups API — https://www.sprinklr.com/help/articles/getting-started-facebook/meta-deprecates-facebook-groups-api/66229eb25f9dd9599d632712
- Impact of Facebook Profile ID Migration on Sprinklr (effective May 1, 2019) — https://www.sprinklr.com/help/articles/getting-started-facebook/impact-of-facebook-profile-id-migration-on-sprinklr-effective-may-1-2019/6655824cb35fa9007da5dec3
