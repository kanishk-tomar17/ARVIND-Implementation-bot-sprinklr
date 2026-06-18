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

## Full widget catalog — every widget inspected live (prod8, 2026-06-18)
**+ Add Widget Above/Below** opens the **Widget Library** (a **Search Widget** box + **STANDARD** and **CUSTOM** categories; CUSTOM = brand/API-built components). Picking a widget inserts it at that position (the + controls placement, Above/Below) and **inherits the page entity** (no separate Case/Profile prompt for most). Remove via the widget's **Delete Widget** (confirm dialog: "You cannot undo this action"). I added and opened **all 97 STANDARD widgets** and recorded their config + what they render. **Every** widget ends with the same **Visibility Condition** footer (toggle → Included Devices Mobile/Desktop/Tablet + Field Based Conditions), so it's omitted from each row below.

**Common config primitives seen:** `Title` (+ Include Icon), `Height (px/rem)`, `Read Only`, `Variant`, `Entity Type` (Case/Profile), `Refreshable`/`Collapsible`, `Refresh Interval`/polling, `Empty Placeholder Title/Subtitle`.

### Conversation & messaging
| Widget | Distinct config | Renders / notes |
|---|---|---|
| **Conversation** | the big one — Read Only (hides reply box), Message controls to remove, **Reply box mode** Inline/Widget, Reply box height, Smart/Canned Responses Mode, Default thread display state, Initial view state (Open/Closed), ~20 toggles (Make chat feed readonly, Hide Add Notes, Load conversation from start, Keep CC/BCC open, Disable Survey Responses…), Header Actions to hide | the customer↔agent thread + reply box |
| **Lite Conversation** | **identical config to Conversation** (lighter renderer) | compact conversation |
| **Reply** | Height only (min 400px) | reply box standalone |
| **Influencer Conversation** | Visibility only | influencer thread |
| **Smart Responses** | Height | AI reply suggestions (Loading w/o data) |
| **Smart Assist** | Title, Height | top guided workflows + KB articles + similar cases |
| **Canned Responses** | Visibility only | saved replies list |
| **Outbound Message** | Type | proactive/outbound compose |

### Case data & properties
| Widget | Distinct config | Renders / notes |
|---|---|---|
| **Properties** (= Case Details) | Columns Count + **Fields to display** (drag-reorder / per-field dropdown / add / remove); *also* a Buttons sub-form (Button Type/Name & Icon/Action Type) | case custom fields |
| **CFM Case Properties** | Include Icon, Height, Columns Count | CFM case fields |
| **Highlights With Properties** | **Highlights Entity Type** (Profile) + **Properties Entity Type** (Case) + Fields to display + Columns Count + Upfront Actions Count | combined profile highlights + case props |
| **Universal Case Overview** | Title, Classname, Height | case KPI header (CSAT, Sentiment, AHT) |
| **Universal Case** | Refreshable, Collapsible, polling | "cases assigned to you" list |
| **Case History Summary** | Visibility only | active/total case counts |
| **Linked Cases** | (none) | linked cases list |
| **Timeline** | Buttons sub-form (Name & Icon/Action Type) | case timeline / activity feed |
| **Activity** | Title, Height, Entity Type, Enable Show All | moderation/activity log |
| **Json** | Visibility only | raw case JSON (debug) |
| **Debug Log** | Title, Height | debug counter |

### Collaboration, tasks, to-dos
| Widget | Distinct config | Renders |
|---|---|---|
| **Collaboration** | Title, Height, Entity Type, Enable Show All Button | case/profile notes |
| **Tasks** | Entity Type, Upfront Actions Count, **Task Card Variant**, Show Task Card Actions, Enable Show All | task list |
| **Tasks Summary** | Visibility only | In Progress/Overdue/Completed counts |
| **My Tasks** | Type, Size, Empty Placeholder Title, polling | personal tasks |
| **My Requests** | Refreshable, Collapsible, Enable polling, Refresh Interval | personal requests |
| **Todo** | Collapsible, Hide title left enhancer, Ticket Label/Icon Key, Placeholder Height, Refresh Interval | todo list |
| **Top Actions** | Empty Placeholder Label (+ "Add Top Action") | quick actions |
| **Primary Action** | Primary Action Title, Action Url | single CTA button |

### Controls & navigation
| Widget | Distinct config | Renders |
|---|---|---|
| **Case Controls** | per-button: Button Type / Button Name & Icon / Action Type / Url | top case-control bar (custom buttons) |
| **Agent Controls** | Visibility only | agent presence/controls |
| **Influencer Case Controls** | Visibility only | influencer case bar |
| **Tabs** | Title, Show Header, Height, **Tab Variant** (Segmented default) + **Add Tab** | tabbed container |
| **Horizontal Tabs** | container (errored empty) | horizontal tab container |
| **Layout** | (container, no form) | nested layout region |
| **Quick Search** | Visibility only | universal quick search |

### AI, KB & guidance
| Widget | Distinct config | Renders / gating |
|---|---|---|
| **Guided Workflow** | **Guided Workflow*** (mandatory dropdown), Hide Header, Always Initialize, Should Auto Execute, Custom Execution Context Parameters (`USER.id`/`RECORD`), Execution Restart Parameters, Pinned Guided Workflows, Enable Search, Enable Smart Recommendation | runs GWs (dedicated widget — no JSON hack needed) |
| **Knowledge Base** | **Variant** (Smart Assist Articles List), Collapsible, Sort by creation time, Height (rem) | KB article search |
| **Smart Summary** | Title only | **"Access Denied"** → needs AI enablement |
| **Brand AI insights** | Title | "No AI Insights Found" |
| **Insights** / **Top Insights** | Visibility only | AI insights list |
| **User Guides** | Collapsible, Refreshable, Visible Guides Count | onboarding guides |
| **Checklist** | Refreshable, Collapsible | agent checklist |

### Profile, customer & journey
| Widget | Distinct config | Renders / gating |
|---|---|---|
| **Record Card** | Buttons sub-form | profile card ("Record Card Template not found" w/o template) |
| **Record Card List / …With Tabs / …With Virality / …Table** | Buttons sub-form (most); some Visibility-only | record card collections (need data/template) |
| **Customer Profile Overview** | Visibility only | **errors w/o Profile entity** |
| **Enterprise User** | Visibility only | enterprise user info |
| **User** | Show User Status, Show Assigned Campaigns, Hide Work Queues, Campaign Monitoring Metrics, Auto Refresh Interval | agent/user details |
| **User Widget / User Activity / User Journey** | User Journey: Title | journey/activity (e.g. "Navigated to Live Chat") |
| **Influencer User Profile** | Visibility only | influencer profile |
| **CRM** / **Jira** | Visibility only | external CRM/Jira (Loading w/o integration) |
| **Iframe** | Iframe URL, Iframe Title, Height, Enable Refresh, Allow Copy, **Permissions** | embed external page (see `iframe-widget.md`) |
| **Image** / **Text** | Visibility only | static image / text |

### Channel, paid, influencer, WFM, misc
| Widget | Distinct config | Renders / gating |
|---|---|---|
| **Customer Happiness** | (Properties-style) | **"Access Denied"** w/o permission (CSAT/wait-time AI) |
| **Calendar** | Size, Week Starts On, Refreshable, Show all Status Filter, **Select calendar view***, Height | calendar grid |
| **Appointments** | Collapsible, Height, Refresh Interval | upcoming events |
| **Scheduled Callbacks** | Visibility only | callback queue |
| **Call Overview** | Title, Classname, Height | voice call summary |
| **Contact Us** | Description, Want to show support button (Yes/No), Support Button Text, **Live Chat button action** | help/support panel |
| **Announcements** | Collapsible, Show as banner, Maximum Visible Items, Refresh Interval | announcements feed |
| **Media Asset** | **Type** (Favorite…), Refreshable, Collapsible | DAM assets |
| **Paid Approval** | **Approval Type**, Refreshable, Empty Placeholders | ad approvals |
| **Paid Entity** | **Content Type**, Refreshable, Empty Placeholders | paid campaigns/ads |
| **Ads Campaigns** | Refreshable, Collapsible | ad campaigns |
| **Strategy Group** | Refreshable, Request Payload Type, Empty Placeholders | strategy data |
| **Agent Nudges** | Refresh Interval, Refetch delay, **Type/Theme** (OPPORTUNITY_DETECTED_ALERT…), Nudge Title/Description, Allow Supervisor Escalation, Category | supervisor/AI nudges |
| **QM Case Evaluation** | Collapsible, Variant (errored w/o data) | quality scorecard |
| **QM Case Draft Evaluation** | Collapsible | QM drafts |
| **QM Reporting** | **Standard QM Reporting Widget** picker, Collapsible, Should remove if empty, Placeholder Height, Refresh Interval | QM report embed |
| **Widget with filter selector** | **Standard Reporting Widget** + Dashboard + Widget pickers, Collapsible, Refresh Interval | embeds a reporting widget |
| **CFM Survey Response** / **Extensions** / **Live Monitoring** / **UniversalProfile Thread** / **Influencer All Conversations/Campaigns/Partnerships/Posts/Tasks** | Visibility-only (most) | feature/role-gated panels |
| **WFM:** **Agent Schedule Calender · Agent TimeOff Utilization · Allocated TimeOff · Leave Requests · TimeOff History Preview · Work Queues · My Team · Onboarding Progress · Deactivated Accounts · Favourite Assets/Brands/Reports · Placeholder** | mostly Visibility-only (a few add Title/Collapsible) | WFM/agent-home panels; render data or Loading per permission |

**Gotchas observed:** widgets that need a permission/integration render **"Access Denied"** (Customer Happiness, Smart Summary), an **error** (Customer Profile Overview, QM Case Evaluation, Record Card Table — need the right entity/template), or **"Loading…"/empty** (CRM, Jira, WFM) until configured. Container widgets (**Layout, Tabs, Horizontal Tabs**) hold other widgets rather than render content.

## Per-widget configuration — VERIFIED (right-rail Settings)
Each widget in the builder has **Edit Widget Properties** → opens that widget's config **form in the right rail (Settings tab)**. Common pattern across widgets:
- **Title*** + **Include Icon** toggle; **Height (px)**; **Read Only** toggle/dropdown; **Variant**; **Entity Type*** (Case/Profile).
- **Footer on every widget = "Visibility Condition"** toggle ("this widget will only be visible when the set criteria is met"). Flip ON → reveals **Included Devices*** (Mobile / Desktop / Tablet multi-select) + **Field Based Conditions → "+ Add Visibility Conditions"** (criteria builder). This is how you show/hide a widget by device or case/profile field values.

**Key widget configs captured:**
- **Conversation Widget** (the reply-box engine): Height; **Read Only** (`Read Only` hides the reply box / `Default`); **Message controls to remove from reply box** (multi-select); **Reply box mode** (`Inline` / `Widget`); **Reply box height**; **Smart Responses Mode**; **Canned Responses Mode**; **Default thread display state**; **Initial view state** (Open/Closed radio); **Initial smart responses view state** (Expanded/Collapsed radio); plus ~20 toggles — Hide replyBox properties, Expand replyBox properties, Hide schedule button, Clip Canned Responses, Hide Add Notes Button, Prevent reply box collapse on feed click, Disable bulk selection of messages, Remove engagement/create-case action for brand post, Show translate action upfront, **Make chat feed readonly**, Hide notes in conversation, Load conversation from start, Disable Survey Responses, Enable Range Selection On Notes, Keep CC/BCC open by default, Hide inline text formatting toolbar, Enable channel switching on brand message; **Header Actions to hide** (multi-select).
- **Properties Widget** (= Case Details / custom-field display): Title + Include Icon; Height; Read Only; Variant; Entity Type*; **Columns Count*** (e.g. 2); **Fields to display*** — an ordered list with **drag-reorder handles**, a **per-field dropdown**, **✕ remove**, and **+** to add fields.
- **Case Controls Widget** (the top case-control bar): configure its action buttons — **Button Type**, **Button Name & Icon**, **Action Type** (e.g. URL, Show Macros), **Url**. This is the UI way to add a custom button (e.g. Guided Workflow) without hand-editing JSON.
- **Record Card Widget** (profile card): button config — **Button Type**, **Button Name & Icon**, **Action Type** (e.g. Show Macros → "Apply Profile Macro").

## Notes / gaps
- From the course video transcript + verified live (prod8). Which widgets/fields appear is controlled per role/layout in Care Console Manager. The underlying JSON model (templateIds `@sprinklr/widget/<Type>`) is in `care-console/manager.md`. Related: `care-console/manager.md`, `care-console/agent-assist-ai.md`, `care-console/collaboration-notes.md`.
