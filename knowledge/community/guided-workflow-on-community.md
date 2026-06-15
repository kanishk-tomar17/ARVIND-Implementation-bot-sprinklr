# Guided Workflow on Community (Community 184)
**Source:** Product Foundation Courses → Community / 184 Guided Workflow on Community (video transcript + demo) · **Help:** search `site:sprinklr.com/help guided workflow on community application id`

## Why
A **Guided Workflow** is an automation tool (a configurable **form**) that collects user input and shows output per a predefined business flow. On community, GWs let users **self-serve** step-by-step (solve common issues, submit a request) — **reducing agent load**.

## Configure the GW in Sprinklr
- **Launchpad → Agent Augmentation → Guided Workflows** → folders hold GWs.
- Create a folder / GW (name + description) → **canvas** opens to define the flow (screens added via **+**, which are input screens the user sees).
- **Save and Deploy** → GW becomes active.
- **Crucial:** the GW **must be mapped to a folder** (e.g. "Tech Community Refund and Return" folder) to be usable in community. (See the Guided Workflow module: [[overview]], [[public-facing]].)

## Deploy the GW on community (demo)
1. **Community Builder → Edit** the community → **Content Settings → Guided Workflow** (left pane).
2. **Enable Guided Workflow** (toggle on) — enables creating/mapping GWs in community.
3. **Add the Application ID:**
   - Go back to Guided Workflow → **Home**; in the URL switch to **Application Manager** (the GW application manager listing all GWs).
   - Copy the **GW application ID** → paste into **Content Settings → Guided Workflow → Application ID** → the application is now active in the community.
4. **Map the GW to a category** (required — a GW only shows in community if mapped to a category):
   - **Community admin → Edit → Category Hierarchy Management** → pick/create a category → **Edit** → under **Mapped Guided Workflow Folders**, select the folder holding the GW (e.g. refund-and-return) → **Save**.

## Notes / gaps
- Reuses the **Guided Workflow** module ([[overview]], [[public-facing]]) + Community Builder category mapping ([[community-builder]]). Public-facing GW deployment overlaps with [[public-facing]].
- Part of Community: [[community-builder]], [[global-workspace-roles]], [[message-level-rules]], [[live-chat-on-community]], [[spam-model]], [[case-management-for-community]], [[social-sso]], [[survey-on-community]], [[support-ticket]], [[community-reporting]].
