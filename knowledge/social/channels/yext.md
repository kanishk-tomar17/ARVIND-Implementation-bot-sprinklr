# Yext (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Yext channel (multiple articles; see links below)

## What it is
- Yext is a listings/reviews management platform; the Sprinklr Social integration pulls **Yext reviews** into Sprinklr so agents can read and respond to them from one place.
- Reviews land in Sprinklr's [[engagement-dashboards]] and can be replied to, drafted, scheduled, routed, and reported on like any other Social message.
- Primary use: **review response and management** — read in Yext reviews, reply publicly, and track agent performance.
- Key limitation: **you cannot edit a published post/response** through the Yext integration once it has gone out.

## Key features & how to use

### Setup — add a Yext column to an Engagement dashboard
- Click the **New Tab** icon (top of Sprinklr) and select **Engagement** under Sprinklr Social.
- In the dashboard, click **Add Column** (top-right).
- In the **Add New Column** picker ("Select a source for adding a new column to dashboard"), choose **Yext** (the blue "X" tile). The picker is searchable and lists channels like Community, Get Satisfaction, DailyMotion, Nextdoor, WhatsApp, Google RBM, Apple Business Chat, etc.
- Choose the column type: **Reviews** or **Comments**.
- Enter a **column name**, select the **account**, and complete the required details.
- Click **Create Column**. The column shows the live review feed (e.g. "reviews (114)") with reviewer name, star rating, and review text/date.

### Engagement — respond to a Yext review
- Open the Engagement dashboard via the **New Tab** icon.
- On the target review, click the **Comment / reply icon** (the curved-arrow icon on the review card).
- A **Comment** pop-up opens. Fields seen in the dialog:
  - **From** — the account responding (e.g. "Sprinklr HQ"). Required.
  - **Message Type** — fixed dropdown showing **Comment**. Required.
  - **Reply box** — "Enter your reply here…" with a **900-character** limit; toolbar supports attaching links, inserting **canned/saved responses (templates)**, custom links, and **content placeholders**.
  - **Campaign** — associate the post with a campaign (has a **Set as Default** checkbox). Required in the dialog shown.
  - **URL Shortener** — shorten any links pasted into the reply.
  - **Social Bars** — optional social-bar selection.
  - (Scroll for) **Custom Properties** — tag the post with metadata; **Approval Type** — required approvals; **Note** — internal note.
- Choose an action:
  - **Post** — publish the reply immediately.
  - **Save as Draft** — keep for later.
  - **Schedule** (calendar icon, bottom-left) — set a future date/time to publish.
- Review cards also expose inline controls: status (Closed/Not Set), **Queues** (No Queues), **Set Message Properties**, **Set Profile Properties**, assignee, and sentiment — same as other Social channels. See [[publishing]] for the shared composer behavior.

### Reporting
- Report on **Agent SLA**, **Timestamps**, and **Sentiment** for Yext reviews via standard Social reporting. See [[reporting]].

### Automation / routing
- **Route reviews based on Star Rating** using the [[rule-engine]] (e.g. send 1–2 star reviews to a priority queue).

## Common issues & fixes
- **Can't edit a published response** — editing published posts is **not supported** for Yext. To correct a reply, post a new response; the original cannot be edited in-platform.

## Notes & gaps
- Prerequisites: a connected Yext account in Sprinklr and access to a Social **Engagement** dashboard. Responding requires composer/publishing permissions on the chosen account.
- The capabilities article is a high-level support matrix (Engagement: pull in reviews — yes; edit published posts — no / Reporting: Agent SLA, Timestamps, Sentiment / Automation: route by star rating). It does not document the underlying account-connection/authentication steps.
- Approval workflow, custom properties, and Social Bars are available in the reply dialog but their specific config is not detailed in these articles.

## Sources
- Yext Capabilities and Limitations — https://www.sprinklr.com/help/articles/yext/yext-capabilities-and-limitations/645860ace66f2e36b4515cbc
- Respond to Yext Reviews — https://www.sprinklr.com/help/articles/yext/respond-to-yext-reviews/645860afe66f2e36b4515cbd
