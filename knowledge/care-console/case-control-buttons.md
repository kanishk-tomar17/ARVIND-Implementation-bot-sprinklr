# Care Console — Case Control Actions (GP buttons, CFs, macros on the top bar)

**Source:** Product Foundation Courses → `Care Console - Case Control buttons - GP, CFs and macros` (video `036_…`, transcript read) · **Cross-check:** `site:sprinklr.com/help case control`

Buttons/fields pinned to the **top bar** of the case so agents act fast without scrolling through the third pane / conversation pane.

## What they are
- **Case control actions** = buttons or fields rendered at the top of the case screen for quick view / quick actions.
- Purpose: pin the day-to-day essentials (key guided workflows, key custom fields, shortcut actions) so agents initiate and finish without hunting through widgets → boosts productivity, protects FRT/CRT.
- **Best practice:** only pin actions/flows needed for *most* cases (≈4 buttons upfront). Everything else stays in the Smart Assist widget / three-dot menu to avoid clutter/confusion. (When >4 are configured, Macro moves under the three-dot menu.)

## Guided Workflows as case control actions
- Render important GWs as top action buttons → agents start a flow in one click instead of opening the Smart Assist widget.
- Example flows pinned: **Update Properties** (autofills based on config → Next → fill remaining → Submit → GW finishes), **Create Ticket / sub-case** (for Case Management; fill info, attach file, Submit → ticket created), **Follow-up on a query** (brand-defined follow-up GW).
- All GWs remain available in the Smart Assist widget; only the essential ones are pinned.

## Selective custom fields as case control fields
- Pin important CFs on the top bar so agents don't dig into Case Details — e.g. **country, brand, number of calls**.
- Example: if "number of calls > 5" → top priority; showing it upfront tells the agent to pick and resolve within SLA.
- Example: a **Case vs Ticket** field pinned so agents instantly distinguish a parent case from a sub-ticket.

## Other shortcut actions (configurable buttons)
- **Forward as Email** — forward the case conversation to leads/supervisors who don't have Sprinklr access (details auto-fill; add content → send).
- **Reminders** — schedule reminders for self/colleagues/junior agents (notified on login) to view cases, check notes, follow up.
- **Schedule Call (callback)** — schedule a callback and assign to another agent in a couple of clicks.
- Buttons are fully configurable — **icon and label** can be changed.

## Notes / gaps
- From the course video transcript. Configuration of which GWs/CFs/buttons to pin is per brand/role (set in Care Console Manager / layout). Related: `care-console/manager.md`, `guided-workflow/overview.md`.
