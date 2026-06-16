# Apple App Store (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Apple App Store channel (multiple articles; see links below)

## What it is
- Integrates **Apple App Store Connect** as a Sprinklr Social channel so you can pull all your apps' reviews into one place and reply to them from Sprinklr.
- Fetches reviews with **star ratings, review text, and user details**; supports creating [[cases]] from reviews, tracking edited reviews, and replying.
- Authentication is via App Store Connect **API keys** (JWT-based), not username/password.
- Feeds [[engagement-dashboards]] and [[reporting]] (inbound & outbound analytics, SLA tracking).
- Key limits: ~24h Apple moderation delay, **only one reply per review**, and **rating-only reviews (no text) are not retrieved**.

## Key features & how to use

### Setup — Add an Apple App Store account
Prerequisites: **Admin** or **Customer Support** role (since release 20.10) and access to your Apple **App Store Connect** account to generate API credentials.

Steps:
- New Tab icon → under **Sprinklr Social → Listen**, open **Owned Social Accounts**.
- In **Accounts (Settings)**, click **Add Account** (top right).
- In the **Add Account** picker ("Choose a channel you would like to add an account for"), search/select **Apple AppStore Connect** (blue App Store "A" tile — distinct from "Apple Messages for Business").
- In the **Apple AppStore Connect** dialog, enter:
  - **Key ID** (required) — from App Store Connect → **Users and Access → API Keys** tab.
  - **Private key** (required) — the key downloaded **once** from App Store Connect; it cannot be re-downloaded, so store it securely. (Free-text/paste box.)
  - **Issuer ID** — off by default; enable the toggle **only for Admin (Team) credentials**. It is not available for Customer Support (Individual) keys.
  - Both Key ID and Private key show info (i) tooltips; click **Next** to proceed.
- Sprinklr verifies the credentials in real time, then click **Add**.
- Configure account details: account name & owner, custom character count for replies, default URL shortener and auto-populated signature, **Account Groups**, channel **permissions** for Users/User Groups, workspace sharing/visibility, subscriber notifications, timezone, and account properties.
- Click **Save**.

Auth model (from the integration diagram): client API creds → Sprinklr generates a **JWT** → validates and signs it to fetch the app list and stream reviews. Activities like creating/revoking certificates or deleting App IDs are **not** done by Sprinklr (and aren't possible at all with Customer Support keys — a reason Admin keys are preferred for high-security clients).

### Engagement — Create an Apple App Store column
Prerequisite: an Apple App Store account must already be linked (see Setup).

Steps:
- New Tab icon → **Sprinklr Social** tab → under **Engage**, open **Engagement Dashboards**.
- From Engagement Home, search and open the target dashboard.
- Click **Add Column** (top right).
- Choose source: search/select **Apple AppStore**.
- Pick a **column type**:
  - **Inbox**
  - **Reviews**
  - **Replies**
  - **App Store Connect Reviews**
  - **App Store Connect Replies**
- Configure basic info: name, description, relevant account, and category.
- Set **workflow properties** (manual or automated): status, assignment, priority, spam, sentiment.
- Optionally apply **custom property** filters to include/exclude messages.
- Click **Create Column**.

### Reporting
- Supports **outbound & inbound analytics** and **SLA tracking** via [[reporting]] dashboards.
- Custom properties available for reporting include **Apple app version code** and **review country**.

## Common issues & fixes
- **Reviews/replies take a long time to appear** — Apple moderates all posted reviews and replies, which takes about **24 hours**. Successfully moderated/published reviews are then fetched by Sprinklr roughly **every 6 hours**; published replies can take about a day to reflect.
- **"Can't post a second reply"** — You can post **only one reply per review** from Sprinklr. If the review already has a reply from the App Store account, Sprinklr will not publish another.
- **Star-only reviews missing** — Reviews with **only a rating and no text** are not exposed by Apple's API, so they are not pulled into Sprinklr. Expected behavior, not a bug.
- **Issuer ID error / field unavailable** — Issuer ID applies only to **Admin (Team)** keys; leave the toggle off for **Customer Support (Individual)** keys.

## Notes & gaps
- Roles: Admin or Customer Support role required to add the account (since 20.10).
- The Private key is downloadable only once from App Store Connect — losing it means generating a new key.
- Review-fetch cadence (~6h) and moderation delay (~24h) are platform-side; build SLA expectations around this.
- Article 2 (limitations) and article 3 (column) had no usable screenshots; setup UI detail above is confirmed from article 1 screenshots (channel picker, credentials dialog, integration/JWT diagram).
- Not documented: exact character limit for replies (configurable per account), whether bulk reply is supported, and which specific reporting metrics/templates ship out of the box.

## Sources
- Add an Apple App Store in Sprinklr — https://www.sprinklr.com/help/articles/apple-app-store/add-an-apple-app-store-in-sprinklr/64576def0104980882a57959
- Apple App Store Limitations and Capabilities — https://www.sprinklr.com/help/articles/apple-app-store/apple-app-store-limitations-and-capabilities/64576e31e66f2e36b4515988
- Create an Apple App Store Column — https://www.sprinklr.com/help/articles/apple-app-store/create-an-apple-app-store-column/64576e930104980882a5795a

Related: [[publishing]] · [[engagement-dashboards]] · [[reporting]] · [[rule-engine]] · [[cases]]
