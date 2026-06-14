# Guided Workflow — Screen Creation (Screen node)

**Source:** Product Foundation Courses → `Guided Workflow - Screen Creation / 113_…` (video transcript) · **Cross-check:** `site:sprinklr.com/help guided workflow screen node`

A GW is **nodes stitched together**; the **Screen node** shows info to the agent and collects input.

## What a Screen node is
- Two component types: **Display components** (show info — images, text, videos, banners) and **Input components** (collect input — radio buttons, picklists, text areas, etc.).
- Example: customer wants to update address → display components show customer info for authentication; input components capture the new address.

## Configure a Screen node
- In the builder, **+ → Screen**. Left = **screen properties**; right = **live preview** + add-component option.
- **API name** — every component and the screen has a unique API name (used to access its value). No spaces; no two components share a name (e.g. `address_change`). Default provided; renameable.
- **Title bar** (mandatory) — name shown to the agent.
- **Navigation bar** — move between GW pages; **Back** + **Next** enabled by default. You can rename buttons (e.g. "Back" → "Go to previous screen"), change **API name**, change **button action** (move to next / close / go back), and reposition (bottom-right/left/center, top-right).

## Display components
- **Description text** — rich-text editor (formatting) that can print **dynamic info** via the **resource picker** (e.g. insert the customer's email to verify).
- **Image / Video asset** — display an image or video.
- **Banner** — out-of-the-box templates to draw attention; 5 supported: **Warning, Success, Error, Disclosure, Reminder**.

## Input components
- Radio buttons, picklists, text areas, etc. (configuration is intuitive; covered more in `guided-workflow/input-components.md`).

## Notes / gaps
- From the course video transcript. Each component's detailed config is intuitive/per-need. Related: `guided-workflow/overview.md`, `guided-workflow/input-components.md`, `guided-workflow/variables-resource-manager.md` (resource picker / dynamic values).
