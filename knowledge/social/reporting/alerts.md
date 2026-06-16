# Alerts in Reporting (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- A set of alerting capabilities inside Sprinklr [[reporting]] that notify users when metrics, volumes, or trends change.
- Centrally configured and managed in the **Alert Manager** (Governance Console > Alert Manager), which unifies all alerts in one place.
- Two main alert categories: **Smart Alerts** (AI-driven detection of changes in mentions, engagement, audience trends) and **Custom Volumetric Alerts** (spikes in listening volume against a threshold).
- Separately, **Widget Alerts** can be set directly on a reporting dashboard widget against a threshold value.
- Detected anomalies can be surfaced in [[engagement-dashboards]] via an Automatic Alerts column, and alert activity itself is reportable.

## Key features & how to use

### Create Reporting Alerts (Smart & Custom Volumetric — Alert Manager)
- Open the **New Tab** icon, then go to **Governance Console > Alert Manager** (under "Love").
- Click **New Alert** (top-right).
- Complete the **Alert Configuration** form, then click **Save**.
- Configuration fields:
  - **Alert Name** — required.
  - **Add Description** — optional.
  - **Add Tags** — optional, for organization.
  - **Module** — Listening, Benchmarking, Location Insights, or Product Insights.
  - **Category** — choose "Smart Alert" (or Custom Volumetric).
  - **Alert On** — define conditions; up to **4 filters maximum**, minimum **1 required** (via **Add New Filter**).
- Manage existing alerts via the Options menu: **Edit, Delete, Clone, Audit**. Audit tracks changes such as user removals and config modifications.

### Create Reporting Widget Alerts (threshold alerts on a dashboard widget)
- Go to **New Tab > Sprinklr Social > Reporting** (under "Analyze").
- Open the target dashboard, hover the **Options** icon on the widget's upper-right corner, and select **Alerts**.
- In the **Create an Alert** popup, configure and click **Apply** (lower right).
- Fields:
  - **Name** — required; alert cannot be applied without it.
  - **Add Condition** — three parts: **Metrics** (metric to watch), **Operator** (comparison), **Threshold Value** (trigger value).
  - **Check Conditions** (frequency) — Everytime, Every 15 mins, Every 1 Hour, Every 2 Hours, Every Day, Every Week, Every Month.
  - **Where do you want to be notified** — **Platform**, **Email**, and **Send Alert if Request changed since last Run**.
  - Recipients — select users or groups.

### Set up Alerts on Anomalies for Posts or Account (Custom Volumetric for Post/Account Insights)
- Uses **Custom Volumetric Alerts** for Post & Account Insights.
- **Account Insights** module: filter all accounts by a dimension, then set alerts on any account that breaches a threshold.
- **Post Insights** module: filter all posts by a dimension, then set alerts on any post that crosses a threshold.
- Core elements: filter by dimension, set threshold-based alerts, receive notifications on breach/crossing.
- Note: the source article does not provide step-by-step UI labels, defaults, or permission detail for this flow (see gaps).

### Anomalies in the Engagement Dashboard
- To view Alert Manager anomalies, add an **Automatic Alerts** column in the [[engagement-dashboards]].
- Three mandatory fields:
  - **Name** — label for the Automatic Alerts column.
  - **Module** — Listening, Benchmarking, Location Insights, or Product Insights.
  - **Alert Name** — select the alert you created in Alert Manager from the drop-down.
- After saving, anomalies display "as soon as they are detected."

### Reporting on Alerts
- "Consumption Analytics is the [[data-engine]] used to provide Reporting insights into alerts."
- Dimensions / metrics available:
  - **Alert Name**, **Alert Created Time**, **Alert Module**, **Alerts Count**
  - **Alert Email Ids**, **Alert User Ids**, **Alert User Group Ids** (recipients)
- Consumption Analytics metrics for **Smart Alerts** email engagement:
  - **Alert Email – Top Posts Clicks**
  - **Alert Email – View in Sprinklr Clicks**
  - **Alert Emails Opened**
- Alerts operate at the **partner level** while users are **client-specific**, so reporting shows all relevant recipients.

### Roles and Permissions
- Alert Manager is **permission controlled**, with two permission-based roles:
  - **View** — can view all alerts set up in Alert Manager.
  - **Admin** — can create new alerts or modify existing ones.
- Role creation guidance is in the separate "Add a Role" resource. See [[rule-engine]] / governance for role setup context.

## Common issues & fixes
- **Receiving too many alerts** — use **Refine Alerts** filtering conditions, limit which alert categories trigger email notifications, or build hierarchies via queues and user groups.
- **Refine Alerts conditions** (seven): Mentions, Alert Severity (1–10 scale), Alert Longevity, Alert Severity Increase, Total Retweets, Retweets Gained, Alert Type (High/Low for Location/Product Insights).
- **Custom Volumetric Alert is Listening-module only** — not available for other modules.
- **No engagement column for Custom Volumetric Alerts** — these can only be checked via **email notifications**.
- **Alert status types (four):** In Progress, Active, Failed, Inactive. A new alert is "In Progress" during setup and becomes "Active" when complete; on Active you start getting emails as soon as an anomaly is detected.
- **"Every time" frequency** (Custom Volumetric) — triggers an email every time volume spikes above the preset threshold (e.g., threshold of 50 mentions emails immediately when volume crosses 50).
- **Past anomalies shown** — all anomalies detected in the **last 24 hours** from the time the current anomaly is detected (in engagement columns and emails).
- **Smart Alert sources** for Social Reporting: Post Insights and Account Insights.
- **Alert Manager vs old Smart Alerts** — Alert Manager configures/manages all alerts in one place, combining the Smart Alerts framework with more simplicity, scalability, and flexibility (e.g., alerts on topic + theme combinations in listening).

## Notes & gaps
- Prerequisite: Alert Manager access is permission-controlled (View vs Admin) — confirm the consultant's role before creating/editing.
- The "Set up Alerts on Anomalies for Posts or Account" article does **not** specify exact UI step labels, field names, threshold defaults/limits, or notification delivery methods for that specific flow — only the conceptual filter-by-dimension + threshold model.
- Articles do not state numeric limits on total alerts per partner, or exact email send latency beyond "as soon as detected."
- Anomaly history is capped at the last 24 hours from the current detection time.
- Related ARVIND topics: [[reporting]], [[engagement-dashboards]], [[data-engine]], [[rule-engine]], [[sla-monitoring]], [[care-console]].

## Sources
- Create Reporting Alerts — https://www.sprinklr.com/help/articles/alerts-in-reporting/create-reporting-alerts/6454deca0d27fc559bbeb52c
- Create Reporting Widget Alerts — https://www.sprinklr.com/help/articles/alerts-in-reporting/create-reporting-widget-alerts/64fef437503ed17eb5c4976a
- Set up Alerts on Anomalies for Posts or Account — https://www.sprinklr.com/help/articles/alerts-in-reporting/set-up-alerts-on-anomalies-for-posts-or-account/6454df1af65d86626c82b9a9
- Anomalies in the Engagement Dashboard — https://www.sprinklr.com/help/articles/alerts-in-reporting/anomalies-in-the-engagement-dashboard/6454e0ae0d27fc559bbeb52e
- Reporting on Alerts — https://www.sprinklr.com/help/articles/alerts-in-reporting/reporting-on-alerts/6454dfde0d27fc559bbeb52d
- Roles and Permissions — https://www.sprinklr.com/help/articles/alerts-in-reporting/roles-and-permissions/6454e03af65d86626c82b9af
- Alert Manager FAQs — https://www.sprinklr.com/help/articles/alerts-in-reporting/alert-manager-faqs/6454e1830d27fc559bbeb533
