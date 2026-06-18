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

## Live builder — VERIFIED (prod8, 2026-06-18)
**Access:** Launchpad → **Care Console Manager** → `/care/console-manager` (needs the Record Page / Care Console Manager permission).

**Landing = Record Pages list.** Columns: **Status** (toggle = active/inactive), **Name [ID]**, **Roles** (which roles it's assigned to), **Modified Time**. Top three are **system Defaults** (can't edit/delete — only **Preview** + **Clone** in their ⋮ menu): `Default LiveChat / Email / Social Layout` (`@sprinklr/defaultRecordPage/DEFAULT_UNIVERSAL_CASE_<CHANNEL>_LAYOUT`).

**Create vs Clone:**
- **Create Record Page** → asks only for **Record Page Name** → opens a *blank* builder.
- **Clone** (a Default's ⋮ → Clone) → asks **Name + API Reference ID** (both mandatory) → opens the builder pre-filled with that layout. **Prefer Clone** (best practice #1 — avoids blank-build/activation friction).

**Builder:** live preview + right-rail tabs **Settings** and **JSON Editor**. Toolbar icons: **Open Full Page Preview** (eye), **Edit Settings** (gear), **Edit Translations** (A𝐀); per-widget **Edit Widget Properties**. Footer: **Close · Activate · Save**.

**Right rail — two modes:**
- **Page-level (no widget selected):** Settings tab shows **Config → "Fields to update in real-time"** — a multi-select of case/asset fields the layout **refreshes live** (no manual reload) as they change. Options (20+): Case Number, Creation Time, Assignee, Created By, Sentiment, Due Date, Archived, Language, Case Tags, Case Sub Title, Case Sub Type, Campaign Name, Latest Customer Phone Number, Latest Called Number, Latest Call Type, Duration, Date & Time, Asset ID, Asset Type, etc. Pick the fields that must update in real time on the agent's screen (e.g. voice fields during a live call).
- **Widget-level (a widget selected via Edit Widget Properties):** Settings tab swaps to **that widget's config form** (Title/Height/Read Only/Variant/Entity Type + widget-specific fields, and a **Visibility Condition** footer). See `care-console/widgets.md` for the per-widget forms and the full ~68-widget catalog.

**Tabs (left nav) in the Default layout:** *Omni-Channel Interaction* (Conversation + reply box), *Case Details* (Properties/Case Details, Case Collaboration, Customer Happiness, Historical Cases), *Customer 360*. Each tab is its own nested **Layout** (e.g. `HEADER_TWO_COLS_FIFTY_FIFTY`).

**Add / remove a widget:** every widget shows **Add Widget Above / Add Widget Below** (the + controls placement) → opens the **widget library** (Search Widget + **STANDARD / CUSTOM** categories, ~68 standard widgets) → pick widget, choose **entity type (Case/Profile)** where prompted. **Delete Widget** removes one. Full catalog + per-widget config: `care-console/widgets.md`.

**Activate (= Make Live):** dialog requires **Role IDs*** (mandatory, multi-select) + an *Advanced Settings* expander → **a record page can't go live without ≥1 role assigned** (this is the activation friction; assign a role to activate). Status toggle on the list also activates/deactivates.

## JSON model — how the layout & widgets are structured (JSON Editor)
The JSON Editor exposes the whole page object; **widgets are managed here** (historically the only way to add them). Shape:
- **`RecordPage`**: `id`, `name`, `entityType` (e.g. `_s_UNIVERSAL_CASE`), `roleIds` (null until activated), `grants`, `children: ["0"]`, and **`allComponents`** = a map keyed by string id.
- **`allComponents["<id>"]`** = a component: `id`, **`templateId`** (`@sprinklr/widget/<Type>`), `name`, `order`, **`children: [ids]`**, **`props`**, optional `buttons`, field config, `translations`.
- **Root = a Layout widget** (`@sprinklr/widget/Layout`) with `props.pageTemplate` (e.g. **`STICKY_HEADER_TWO_COLS_PINNED_LEFT`**), `leftColSpan`/`rightColSpan`, `stickyHeaderId`, and `children` = the widget ids it contains.
- **Layouts nest:** a tab/sub-area is itself a `Layout` component with its own `pageTemplate` (e.g. **`HEADER_TWO_COLS_FIFTY_FIFTY`**) inside a `Tabs`/`HorizontalTabs` widget — so "add a new layout under the Layout widget" = add another Layout component and reference it in a parent's `children`.
- **Widget templateIds seen:** `Layout`, `CaseControls` (top case-control bar + its `buttons`), `Conversation`, `Tabs`, `HorizontalTabs`, `RecordCard` (fields like `{type:"TEXT", key:"fullName"}`), `SmartSummary`, `Properties`, `Timeline`, `Collaboration`, `Activity`.
- **To add a widget via JSON:** add a new entry to `allComponents` with a `templateId` + `props`, then reference its id in the target parent component's `children` array. The visual builder does the same thing under the hood.

## Notes / gaps
- From the course video transcript + verified live. JSON-editor button config requires the Sprinklr documentation for the exact snippet. Related: `care-console/overview.md`, `care-console/widgets.md`. Macro: `clone_care_console_record_page` (ledger).
