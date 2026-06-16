# PowerReviews (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — PowerReviews channel (multiple articles; see links below)

## What it is
- PowerReviews is a ratings-and-reviews platform; integrating it as a Sprinklr Social channel lets brands pull native review conversations into Sprinklr and reply from there.
- Manage PowerReviews alongside all other channels from one dashboard — view reviews, reply, and report on review activity.
- Read/reply only: you can view reviews and post replies, but you **cannot edit or delete** reviews or replies from Sprinklr.
- Captures useful metadata on each review: consumer email address, Review ID, and Order ID.
- Supports SLA and Inbound reporting for the channel. See [[reporting]].

## Key features & how to use

### Setup — Add a PowerReviews account
Adds the PowerReviews integration as an owned account so it can feed [[engagement-dashboards]].
1. Click the **New Tab** (+) icon, go to **Listen → Owned Social Accounts** (Accounts / Settings).
2. Click **Add Account**, then search and select **PowerReviews** (blue "R" tile) from the channel grid.
3. In the **Add Power Reviews account** dialog, under **Basic Details**, fill in:
   - **Client Id** (required) — application identifier.
   - **Client Secret** (required) — credential used to access the data.
   - **Merchant Id** — found in the PowerReviews Portal under **Configuration → Configure Reviews**.
   - **Merchant Group Id** (required) — application identifier.
   - **Merchant Name** (required) — the merchant designation.
4. Click **Save** to store the initial details.
5. Configure advanced/account settings as needed: permissions, groups/workspace sharing, timezone association, character counts, URL shorteners, signatures, subscriber notifications, and other account properties.
6. Save again to finalize.

### Engagement — Create a PowerReviews column
Once the account is linked, surface reviews and replies in an [[engagement-dashboards]] column. See [[engagement]].
1. Click the **New Tab** icon → under **Sprinklr Social**, click **Engagement Dashboards** within **Engage**.
2. In **Engagement Home**, search & select the desired engagement dashboard.
3. In the dashboard, click **Add Column** (top right).
4. In the **Add New Column** window, search and select **PowerReviews** (blue "R" tile) as the column source.
5. In the **Add New PowerReviews Column** window, select the column **type**:
   - **Reviews** — the inbound review feed.
   - **PowerReviews Reply** — for replying to reviews.
6. Enter **Name**, **Description**, add **Accounts**, and any other **Basic Information**. A live preview renders on the right.
7. Set **Workflow Properties** as desired — these are properties applied (automatically or manually) that drive the message's workflow status, user assignment, priority, Spam designation, and sentiment. See [[rule-engine]].
8. Set **Custom Properties** to include/exclude messages based on the properties applied to them.
9. Click **Create Column** (bottom right). The column appears in the current dashboard.

### Capabilities & limitations (engagement actions)
- **View Review & Reply** — Yes.
- **Edit Reviews & Reply** — No.
- **Delete Review & Reply** — No.
- **Get Consumer Email Address** — Yes.
- **Get Review ID** — Yes.
- **Get Order ID** — Yes.

### Reporting
- Reporting on PowerReviews is supported: **SLA reporting** and **Inbound reporting** are available for the channel. See [[reporting]].

## Common issues & fixes
- **Can't edit or delete a review/reply from Sprinklr** — expected; the channel is read/reply only. Edits/deletes must be done in PowerReviews directly.
- **Account won't connect** — verify Client Id, Client Secret, Merchant Group Id and Merchant Name (all required). Confirm the Merchant Id matches the value in the PowerReviews Portal under Configuration → Configure Reviews.
- **PowerReviews column missing as a source** — the account must be added/linked first before the PowerReviews tile appears in Add New Column.

## Notes & gaps
- **Prerequisite:** a PowerReviews account must be added in Sprinklr before any PowerReviews column can be created.
- **Credentials** (Client Id, Client Secret, Merchant Id, Merchant Group Id, Merchant Name) come from the PowerReviews side; Merchant Id specifically lives in Portal → Configuration → Configure Reviews. The other identifiers' exact source locations aren't documented in the help articles.
- The capabilities article does not specify rate limits, sync frequency, or how often reviews are pulled in — unspecified.
- Required-field markers observed in the Add account dialog: Client Id, Client Secret, Merchant Group Id, Merchant Name (Merchant Id shown without a required asterisk in the screenshot, but the setup text lists it as a needed field).

## Sources
- Add a PowerReviews Account — https://www.sprinklr.com/help/articles/powerreviews/add-a-powerreviews-account/6458cc1f0104980882a57d64
- PowerReviews Capabilities and Limitations — https://www.sprinklr.com/help/articles/powerreviews/power-reviews-capabilities-and-limitations/6458cc1ae66f2e36b4515d6e
- Create a PowerReviews Column — https://www.sprinklr.com/help/articles/powerreviews/create-a-powerreviews-column/6458cc1d0104980882a57d63
