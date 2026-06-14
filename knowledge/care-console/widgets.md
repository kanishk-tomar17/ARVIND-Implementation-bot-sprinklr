# Care Console — Standard & Custom Widgets

**Source:** Product Foundation Courses → `Care Console - Standard and Custom widgets` (video `040_…`, transcript read) · **Cross-check:** `site:sprinklr.com/help care console widgets`

The default/standard widgets in the agent desktop (and how custom ones differ).

- **Default widgets** = available out of the box once Care Console is enabled.
- **Standard / custom widgets** = integrated via **API** or customised for a brand's specific use case.

## The default widgets
- **Conversation widget** — the customer↔agent conversation; refer, take conversation-level actions (three-dot), reply from the reply box. The most important widget.
- **Profile Card** (right side) — publicly available customer info, **varies by channel**: Twitter/X → followers/following + tweet count; Email → email ID; WhatsApp → phone number.
- **Smart Assist** (AI) — recommends top 3 **guided workflows**, 3 **KB articles**, and **similar cases** by message intent. Open an article → **Copy to response** inserts text into the reply box (edit or send as-is). Big help for newly onboarded agents.
- **Customer Happiness** (AI smart case summary) — **Last CSAT score** (predicted on the fan's last message), **Average waiting time**, **Last waiting time**, **Last sentiment**.
- **Workflow Properties** (AI) — predicts **sentiment**, **priority** (by intent), **case type** (by intent), and **status** (new/open/assigned, per config).
- **Collaboration widget** — exchange notes at case & profile level (see `collaboration-notes.md`).
- **Case Details** — case-level **custom fields** shown upfront (per role config); **Show all** → full detailed list of all CFs on the case.
- **Task widget** — create tasks for other agents on the case: task name, description, **due date**, **assign to** (supervisor/junior); assignee is notified.

## Notes / gaps
- From the course video transcript. Which widgets/fields appear is controlled per role/layout in Care Console Manager. Related: `care-console/manager.md`, `care-console/agent-assist-ai.md`, `care-console/collaboration-notes.md`.
