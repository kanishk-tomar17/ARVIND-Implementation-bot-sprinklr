# Care Console Manager (building agent desktop layouts)

**Source:** Product Foundation Courses → `Care Console - Care Console Manager` (video `032_…`, transcript read) · **Cross-check:** `site:sprinklr.com/help care console manager`

Where you **build and customise the agent desktop layout** — which widgets show, which fields, and how the reply box behaves — per role/user group.

## What it is / why it matters
- Configure the agent desktop layout: pick widgets and the fields shown in them, grouped for a role to give a productive layout.
- Assign layouts **by role or user group**; iterate based on agent feedback.
- Goal: surface the right widgets to boost productivity, reduce **FRT/CRT**, and avoid **SLA breaches**.
- Found in **Launchpad → Care Console Manager** (needs the relevant permission).

## Core workflow
1. **Clone before editing.** Open a default layout to preview it; to change it, **always Clone** (give it a name) so you don't impact the layout agents are live on. Edit the clone, then **Make Live** when confident.
2. **Add a widget:** a **+** icon appears above/below each widget (controls placement) → opens the **widget library** → search the widget (e.g. Activity widget) → choose **entity type (Case or Profile)** → add. Repeat across tabs (Omni-channel Interaction, Case Details, Customer 360, etc.).
3. **Remove a widget:** open it → **Delete widget** (e.g. remove a repeated Case Activity widget from a tab).

## Case Details section (custom fields)
- A widget for **case-related custom fields**. **Select field to display** → tick fields → **Add selected**. Remove a field with the **✕**. **Drag-and-drop** to reorder (e.g. bring Case Tags to top).
- **Widget height** adjustable; **column count** selectable (e.g. 3 or 4 columns) — per client preference.

## Customer 360 tab
- Holds Customer Profile widget, Profile Properties, User Journey, etc. Same add/remove/reorder behaviour (e.g. Delete the User Journey widget).

## Reply Box customisations (important)
- **Read-only mode**: hide the reply box / prevent the agent replying (per role/requirement).
- **Message controls to remove**: hide specific icons (canned responses, emojis, etc.) by ticking them under message controls.
- **Reply box mode**: **Inline** (default, bottom of conversation pane) or **Widget** (renders the reply box as a separate widget) — Widget mode is common for **Email** (long emails, refer while replying); can be enabled for other channels too.
- **Smart Responses mode**: also Inline or Widget (select widget → assign smart-response widget).
- Other toggles: hide reply-box properties, canned-response count, hide modes button.

## Advanced (JSON editor)
- Deeper customisations not in the Settings UI are done via the **JSON editor** — e.g. adding a **Guided Workflow button** on the case control bar. Copy the JSON from the provided documentation, paste into the editor, and set your **Guided Workflow ID** / button IDs.
- Example shown: GW buttons on top of the case → clicking renders a step-by-step guided workflow (e.g. retail "select order" flow) so agents get info without extra clicks.

## Notes / gaps
- From the course video transcript. JSON-editor button config requires the Sprinklr documentation for the exact snippet. Related: `care-console/overview.md`, `care-console/widgets.md`.
