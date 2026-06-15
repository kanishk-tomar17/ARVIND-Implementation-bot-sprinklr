# Journey Reporting (Journey Facilitator 145)
**Source:** Product Foundation Courses → Journey Facilitator / 145 Journey Reporting (video transcript + demo; Edit Widget / Outbound Message data source screenshot) · **Help:** search `site:sprinklr.com/help journey reporting outbound inbound audience activity widget`

## What it is
Journey reporting evaluates **message deliverability** and **audience engagement** for a customer journey via Sprinklr's reporting dashboards. It splits into **three categories** depending on data source + channel:
1. **Outbound reporting** — deliverability of messages (SMS, WhatsApp).
2. **Inbound reporting** — user engagement with the messages the journey sent.
3. **Audience Activity reporting** — used with **email** marketing (both deliverability and engagement).

## Common path to build a widget
New tab icon → **Care Reporting** (under **Analyze** in the **Sprinklr Service** tab) → Reporting home → pick/create a **dashboard** → **Add Widget** (top-right) or edit existing → name it → pick **visualization** (e.g. Table) → pick **Data Source** → select **metrics & dimensions** → set **filters** (Advanced options), **sorting**, **date filter** → **Add / Update Widget** (bottom-right).

## 1. Outbound reporting
- **Data Source:** **Outbound Message.** Channels: SMS, WhatsApp.
- **Key metrics/dimensions:**
  - **Volume of Messages** — number triggered or failed.
  - **Status** — whether a message failed or not.
  - **Publish Error** — reason a message failed.
  - **Published Date** — when Sprinklr sent it to the channel.
  - **Audience User ID** — phone number the SMS/WhatsApp was attempted to.
- **Filters:** by marketing journey, account, channel, or any field.

## 2. Inbound reporting
- **Data Source:** **Inbound Analytics.** Reports on engagement.
- **Key metrics/dimensions:**
  - **Message Count** — messages in a specific status.
  - **Message Delivery Status** — read / received / still in sent state (WhatsApp).
  - **Message Delivery Time** — when the message was read/received.
  - **Audience User ID** — phone number of the user who received/read it.
  - **Delivery Failure Reason** + **Delivery Failure Code** — why a message failed.

## 3. Audience Activity reporting
- **Data Source:** **Audience Activity.** Used with **email** (deliverability + engagement).
- **Key metrics/dimensions:**
  - **Activity Count** — total times an activity occurred (e.g. email opened/skipped).
  - **Activity Type** — email read, open, clicked, bounced, failed, skip.
  - **Audience Activity Actor** — email of the user who performed the activity.
  - **Time of the Day** — when the activity occurred.

## Notes / gaps
- Closes the Journey Facilitator loop: reports on messages sent via [[journey-nodes]] across [[channels-supported]], scoped by [[campaigns]]. Reporting mechanics overlap the broader Reporting module.
- Part of Journey Facilitator: [[audience-profile-import]], [[segment-manager]], [[campaigns]], [[journey-builder-basics]], [[journey-nodes]], [[channels-supported]].
