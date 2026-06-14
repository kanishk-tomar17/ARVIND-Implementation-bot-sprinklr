# Record Page Basics — adding widgets & GW-trigger buttons (GW 119)
**Source:** Product Foundation Courses → Guided Workflow - Record page basics (119, video transcript) · **Help:** search `site:sprinklr.com/help record page editor smart assist widget guided workflow button`

## What it is
How to surface a guided workflow in the Care Console. A GW can be initiated from:
- **Smart Assist widget**
- **Agent Nudge widget**
- A **button** on the Care Console

All of these are added to the Care Console via the **Record Page Editor**.

## Step 1 — find the Record Page ID (the layout you're editing)
1. Go to **Sprinklr Service → Omni Channel Dashboards → Care Console**.
2. In the Care Console, **right-click → Inspect**.
3. In DevTools **Elements**, search for **`record page`** → find the **Record Page ID** (e.g. *Universal case record page*) → **copy** it.
4. Open a **new tab**; in the address bar go to **Tools → Record-Page-Editor**.
5. In the Record Page Editor, **search the record page name/ID** you copied → it appears → click the **three dots → Edit**.

## Step 2 — add a widget
1. Click the **plus (+) icon** → search **"Smart Assist widget"** → add it.
   - You can **rename** the widget and **adjust its height**.
2. For agent nudges: **plus icon → search "Smart Alerts widget"** → add → **rename to "Agent Nudges"** → adjust height.
3. **Preview** with the preview icon to see how it looks.
4. **Save** (or keep editing).

## Step 3 — add a button that triggers a guided workflow
1. Click the **topmost section** of the record page editor (existing buttons may already be there).
2. Open the **JSON editor** → scroll → search **`buttons`**.
3. **Copy an existing button's code and paste** it as a new entry.
   - If no button code exists, **reach out to the support/product team** responsible for adding buttons.
4. Change **three things** in the pasted code:
   1. **ID** — must be **unique** (e.g. previous button was `3`, change to `4`).
   2. **Label** — name it as required.
   3. Under **Universal case action**, **replace the ID** with the **Guided Workflow ID** you want to embed.
5. **Apply changes → Save** the record page.

## Fetching the Guided Workflow ID
- Open the guided workflow you want to embed; the **GW ID is at the end of the URL** in the address bar — copy it and paste it into the button's Universal case action ID.

## Notes / gaps
- Editing the record page button is a **JSON edit** — unique IDs matter; a duplicate ID is the classic mistake.
- This is the deployment/surfacing step for everything built in [[overview]], [[screen-creation]], [[input-components]], etc. — the GW only reaches agents once a widget/button points to its ID.
- Smart Assist widget vs Smart Alerts widget (renamed "Agent Nudges") are two distinct widgets added the same way.
