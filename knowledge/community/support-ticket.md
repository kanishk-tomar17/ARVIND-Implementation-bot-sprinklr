# Support Ticket / Support Cases on Community (Community 189)
**Source:** Product Foundation Courses → Community / 189 Support Ticket (video transcript + demo) · **Help:** search `site:sprinklr.com/help community support case guided workflow widgets`

## What it is
**Support cases** let community customers **raise issues** to the brand. They are **Guided Workflows** (a form) that capture the issue details, let user + brand **track the issue** from raised → completed, maintain contact, and boost CSAT.

## 1. Build the support-case form (Guided Workflow)
- Launchpad → **Agent Augmentation → Guided Workflows → Create** (name e.g. "Support case community") → canvas.
- Build the form: a **Screen** (title bar text, navigation, buttons) with **Text inputs** (subject — placeholder, default value, character limit), **dropdowns** with predefined options, etc.
- **Add the "Create Support Case" node** — this **maps the GW input items to Sprinklr variable names** so the captured details reflect as a case in Sprinklr. Select an **active Email ID account** to use for support-case creation → Save.
- **End** the workflow → **Save and Deploy**.

## 2. Enable support cases on the community
- **Community Builder → ⋯ → Edit → Content Settings → Advanced Settings → Community Support Case** (disabled by default) → enable.
- **Map statuses to action items** (multiple actions per status), add **colors** to statuses — fully configurable per requirement.

## 3. Page layout — 3 pages, 3 widgets
After enabling, the **Page Layout** shows 3 pages: **Home, Case, Case Creation**. Create a widget on each:
1. **Home → "All Requests"** = **Support Case List entity** widget (all cases created by the customer; set title + items-per-person).
2. **Case page → Support Case entity** widget — loads/shows the captured **case details** to the user.
3. **Case Creation page → Support Case Creation entity** widget — **map the Guided Workflow** you built (the support-case form) here.

## Notes / gaps
- Combines [[guided-workflow-on-community]] (the form) + Community Builder page-layout widgets ([[community-builder]]); the Create-Support-Case node maps GW data → Sprinklr case variables.
- Part of Community: [[community-builder]], [[global-workspace-roles]], [[message-level-rules]], [[live-chat-on-community]], [[guided-workflow-on-community]], [[spam-model]], [[case-management-for-community]], [[social-sso]], [[survey-on-community]], [[community-reporting]].
