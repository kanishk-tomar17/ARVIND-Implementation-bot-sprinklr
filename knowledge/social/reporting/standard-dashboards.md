# Standard Reporting Dashboards (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- Pre-built, out-of-the-box reporting dashboards inside Sprinklr Social > Reporting that visualize key social KPIs without building widgets from scratch.
- Channel dashboards (LinkedIn, Twitter/X, YouTube) pull analytics in real time from each platform's native insights to track account performance, post performance, and audience demographics.
- Cross-channel dashboards: Campaign Dashboard (marketing metrics by campaign) and Value Realization Dashboard (ties Sprinklr usage to business outcomes / ROI).
- A redesigned navigation experience (left menu bar) for finding, favoriting, and managing dashboards.
- A Message Text filter for searching widget/dashboard data by specific post text.
- Related GROOT topics: [[reporting]], [[engagement-dashboards]], [[data-engine]], [[rule-engine]], [[care-console]].

## Key features & how to use

### Revamped Reporting Dashboard Navigation
- New **left navigation bar** on the Reporting Dashboards screen with icons for: All Dashboards, Favorite Dashboards, Recently Viewed Dashboards, Standard Dashboards, Settings.
- **All Dashboards** section default filters: Type, Owner, Tags; All Options (when no filter applied); Folder Types; Shared with me; Created by me. A **+ icon (Additional Filters)** adds filters for Tags and Workspace. Default View options differ for first-time vs. repeat users.
- **Activity column** shows context such as: "You viewed this X hrs ago", "Other user edited this X hrs ago", "You edited this X hrs ago", "Other user shared with you X hrs ago".
- **Default Sorting** is supported.
- **Options icon** menu includes: Manage Columns, Refresh, Export, Group By.

### LinkedIn Standard Reporting Dashboard
- Visualizes and tracks key LinkedIn KPIs; pulls data from LinkedIn Insights in real time.
- **Account Insights** — brand effectiveness via reach, engagement, conversions, click-through rates.
- **Post Insights** — effectiveness of individual posts via reach, engagement, conversions, click-through rates.
- **Understand your Audience** — engagement demographics: age, gender, location, interests, to enable more targeted content.
- Stated benefits: identify target audience, educate clients on strategy, build transparent client relationships, present results clearly.

### Twitter (X) Standard Reporting Dashboard
- Visualizes and tracks key Twitter KPIs; combines Twitter analytics into one platform to demonstrate campaign ROI to clients/executives.
- **Account Insights** — "effectiveness of a brand's presence and content on social media platforms" measured via reach, engagement, conversions, click-through rates.
- **Post Insights** — effectiveness of individual posts and their impact on the target audience.
- **Understand your Audience** — demographics (age, gender, location, interests) to target marketing effectively.
- Stated benefits: hone in on target audience; educate clients on strategy; foster transparent, trusting relationships; showcase results clearly.

### YouTube Standard Reporting Dashboard
- Tracks key YouTube KPIs; pulls data from YouTube Insights in real time; combines all YouTube analytics into a single platform; tracks follower trends and content performance.
- **Account Insights** — brand presence/content effectiveness via reach, engagement, conversions, click-through rates.
- **Post Insights** — per-post performance using the same metric categories.
- **Audience Understanding** — characteristics of people engaging with content (age, gender, location, interests).
- Stated benefits: hone in on target audience; educate clients on strategy; foster transparent, trusting relationships; showcase results straightforwardly.

### Campaign Dashboard
- "Visually appealing and easy-to-read displays of key marketing metrics" with daily, weekly, and monthly tracking. Comprises two dashboards: **Campaign Overview** and **Campaign Insights**.
- **Grant permission (Workspace Role):**
  1. Click **New Tab** icon → **All Settings** under Platform Setup.
  2. Select **Manage Workspace** → **Workspace Roles**.
  3. Click **Create Role** and fill details.
  4. Enable the **Campaign Dashboards** box under **Dashboards within Reporting**.
  5. Save the role and assign to users/groups.
  - Role fields: Role Name (unique identifier), Description (optional), Select Permissions, Users to Assign, User Groups to Assign.
- **Open Campaign Overview:** New Tab → **Sprinklr Social → Reporting** → click **Dashboard Menu** icon (top left) → select **Overview** within **Campaign**.
  - Widgets: Most Liked Campaigns, Most Commented Campaigns, Most Shared Campaigns, Most Clicked Campaigns, Engagement & Reach by Campaign, Campaign Scorecard.
- **Open Campaign Insights:** New Tab → **Sprinklr Social → Reporting** → click **Dashboard Menu** icon → select **Insights** within **Campaign**.
  - Widgets: Engagement over time, Engagement by Channel, Message Scorecard, Engagement by Account.

### Sprinklr Social Value Realization Dashboard
- Measures business outcomes and prompts action. Presents **Primary Business Use Cases (PBUC)** linking Sprinklr capabilities to **Positive Business Outcomes (PBO)**.
- **Grant permission (Role level):**
  1. New Tab → **Governance Console** → **All Settings** within Platform Setup.
  2. In Platform Settings, choose **Workspace Roles** or **Global Roles**.
  3. Click **Create Role**.
  4. Under **Select Permissions**, search and select **'Pbuc Value Dashboard'**, then Save.
- **Navigate:** New Tab → **Sprinklr Social** → **Value Realization** within **Analyze** → opens the Sprinklr Social Value Realisation Report window.
- **Three PBUC categories:**
  - Turn Social into a Revenue Driver (PBUCs #37–39).
  - Get More Output from Social Media Managers (PBUCs #40–42).
  - Protect your Brand's Reputation (PBUCs #43–45).
- **Selected PBUC detail:**
  - **#37 Engagement Opportunities** — Brand Mentions, Competitor Unhappiness, Direct Outreach (owned channels), Review Engagement, Paid Ad Comments, Audience Segmentation. Metrics include CVR (Conversation/Conversion Rate), AOV (Average Order Value); adoption = messages engaged vs. identified engageable messages.
  - **#38 Social Channel Integration** — Offline Marketing Integration (earned/owned mentions from offline marketing); Customer Moment Sharing (cost savings from user-generated content).
  - **#39 Advocacy & Influencer Leverage** — Employee Advocacy and Influencer Engagement (reach expansion, cost savings, active users/advocates).
  - **#40 Manager Productivity** — Automated Triaging; Lead & Complaint Identification (CAC = Customer Acquisition Cost; CLV = Customer Lifetime Value).
  - **#41 Manager Productivity Enhancement** — AI-Assisted Responses; Bot Automation; Housekeeping Automation (macros/canned responses).
  - **#42 Content Planning & Publishing** — Content Reuse; CMS Integration (AEM, Mediavalet, Sprinklr); Multi-Channel Publishing; Organic Post Boosting; Analytics Centralization; BI Tool Integration (Omniture, Google Analytics).
  - **#43 Compliance Protection** — posts processed through approval workflows.
  - **#44 Governance & Access Control** — Role-Based Permissions (users active in last 30 days); Audit Access.
  - **#45 Crisis Management** — Account Security (passwords shared securely); Kill Switch (messages stopped).
- Related: [[rule-engine]], [[sla-monitoring]], [[care-console]].

### Message Text Filter
- Adds a text-search dimension to filter Reporting widgets/dashboards by specific post text. Covers **Outbound and Inbound posts**.
- **Not** a replication of Keyword List in Listening; **Keyword Query is excluded**. Currently in **Limited Availability**.
- **Behavior:**
  - A widget-level filter overrides the dashboard-level filter; the two also work in conjunction (dashboard filter ABC + widget filter XYZ returns results matching both).
  - Supports multiple characters; **operators don't work** (e.g. an "and" between terms is treated as a literal character, not a logical operator).
  - No minimum character limit; **not case sensitive**.
  - Only Inbound & Outbound posts; available **only for the Post Insights report type** in Social Analytics — other Social Analytics report types are not currently supported.
  - Cloning a dashboard retains Message Text filters at both dashboard and widget levels.
- **Apply at dashboard level:**
  1. New Tab → **Reporting** under **Sprinklr Social > Analyze**.
  2. From Reporting Home, search and select the dashboard.
  3. In the Filter bar's **Message Text** field, enter the keyword.
- **Apply at widget level:**
  1. New Tab → **Reporting** under **Sprinklr Social > Analyze**.
  2. Select the dashboard.
  3. On an editable widget, hover the **Options** icon → **Edit Widget**.
  4. Under **Define Advanced Options > Filters**, select **Message Text** as the dimension.
  5. Enter the text to filter.
  6. Click **Update Widget**.

## Common issues & fixes
- **Operators ignored in Message Text filter:** searching with "and"/"&" between terms treats them as literal characters, not logical operators. Use plain text; do not expect Boolean/operator behavior.
- **Message Text filter shows no results on a widget:** confirm the report type is **Post Insights** (the only supported type) and that posts are Inbound/Outbound. Other Social Analytics report types are unsupported.
- **Message Text not visible to all users:** capability is in **Limited Availability** — may not be enabled in every environment.
- **Campaign / Value Realization dashboard not accessible:** the user's role lacks the permission. Add **Campaign Dashboards** (Campaign) or **'Pbuc Value Dashboard'** (Value Realization) to the role and reassign.

## Notes & gaps
- **Prerequisites/permissions:** Campaign Dashboard requires the **Campaign Dashboards** permission under Dashboards within Reporting; Value Realization requires the **'Pbuc Value Dashboard'** permission (Workspace or Global Role).
- The channel dashboard articles (LinkedIn, Twitter/X, YouTube) describe sections and metric categories (reach, engagement, conversions, CTR; demographics) at a conceptual level but do **not** enumerate exact widget names, individual metric formulas, or step-by-step build instructions.
- The articles do not specify data refresh frequency/latency, historical data limits, or export limits for these dashboards.
- Message Text filter is **Limited Availability** and scoped to Post Insights only; rollout state and any character/volume ceilings beyond "no minimum" are not stated.
- Twitter is referred to as "Twitter" in the source; treat as X where relevant.

## Sources
- Revamped Reporting Dashboard Navigation — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/revamped-reporting-dashboard-navigation/66aa0fca5b2b41725c0416ee
- LinkedIn Standard Reporting Dashboard — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/linkedin-standard-reporting-dashboard/64ff0d09503ed17eb5c498d8
- Twitter Standard Reporting Dashboard — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/twitter-standard-reporting-dashboard/64ff0d0b923c104940d1481f
- YouTube Standard Reporting Dashboard — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/youtube-standard-reporting-dashboard/64ff0d0c503ed17eb5c498d9
- Campaign Dashboard — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/campaign-dashboard/64ff0d21503ed17eb5c498da
- Sprinklr Social Value Realization Dashboard — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/sprinklr-social-value-realization-dashboard/64ff0d07923c104940d1481e
- Message Text Filter — https://www.sprinklr.com/help/articles/standard-reporting-dashboards/message-text-filter/68219ac3cffeb5201c98125e
