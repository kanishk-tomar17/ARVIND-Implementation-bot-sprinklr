# Care Console — Adding the Agent Copilot Widget to a Record Page

**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/configure-agent-copilot-widget-in-care-console/configure-agent-copilot-widget-in-sprinklr-care-console/686d46686862622c541f4d44
**Verified:** 2026-10-08

## What it is
- Agent Copilot is a distinct AI-assist product from the older Agent Assist widgets (Smart Assist, Smart Responses, etc. — see `agent-assist-ai.md`, `widgets.md`). It needs a deployment configured in **AI+ Studio** first, then gets surfaced as its own widget on a Care Console record page.

## When to use
- Consultant wants to add the Agent Copilot panel to a case/record page so agents see it while handling cases.

## Prerequisites
- **Agent Copilot must already be configured and activated in AI+ Studio** (deployment created, data/skills/settings configured) before it will appear as a usable widget. Enabled on request at the org level (see `ai-studio/copilot-service.md`).

## Configuration steps
1. Open a **new tab** in the Sprinklr platform.
2. Go to **Sprinklr Service > Resolve > Care Console Manager**.
3. Create a new record page, or edit an existing one.
4. Click the **Add [+]** button on the record page layout.
5. Pick **Agent Copilot widget** from the component list in the right pane.
6. Configure the widget settings panel:
   - **Title** — display title for the widget.
   - **Default State** — Expanded or Collapsed on load.
   - **Height** — expandable height in px (minimum 400px).
7. (Optional) **Visibility Conditions** — toggle to restrict by device (Desktop/Tablet/Mobile), and/or add Field/Operator/Value filters (combinable with logical grouping) — same visibility-condition footer pattern as every other widget (see `widgets.md`).
8. **Access control** — click **Change Activations** to assign which Role IDs can see the widget, with optional advanced filters on case attributes or user data.
9. **Save and Publish** the record page, then verify the widget shows and works for agents in Care Console.

## Common issues & fixes
- Widget not appearing in the component list → Agent Copilot likely isn't activated in AI+ Studio yet (do that first, it's a separate prerequisite step, not part of the record-page flow).
- Widget placed but agents can't see it → check **Change Activations** (Role ID assignment) and the record page's own role/profile assignment in Care Console Manager.

## Notes & gaps
- Help article is step-level but doesn't give pixel-level screenshots; the layout mechanics (Add [+], right-pane component list) match the general widget-adding pattern documented in `widgets.md`.
- Related ARVIND topics: [[agent-assist-ai]], [[widgets]], [[manager]], [[copilot-service]].
