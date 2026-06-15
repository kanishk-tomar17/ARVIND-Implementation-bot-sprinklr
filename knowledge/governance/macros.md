# Macros (Governance 007)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 007 Understanding Macros (video transcript + demo) · **Help:** search `site:sprinklr.com/help macros automated manual actions`

## What it is
A **macro** executes **multiple actions on an entity in a single click** — clubbing repetitive agent steps. Example: moving a case from one queue to an agent normally means remove from current queue → add to assigned queue → set status to Assigned; a macro does all three at once.
- Supports **bulk actions** — apply one macro to e.g. 1000 cases at once instead of repeating manually.

## Entity-specific macros
Each entity type has its own macros, usable **only** on that entity (can't reuse a case macro at message level):
- Inbound message, Outbound message, Case, Asset, Profile, plus User, Event, Universal Product Catalog, etc.

## Where / managing
- **Settings → (Workspace) → Macros.** Lists existing macros with **activity** (created when, changes, by whom). **Edit / Clone / Delete**.

## Creating a macro
**Create Macro** → form:
- **Name**, **Description**.
- **Entity** — the macro is visible only on the selected entity.
- Two checkboxes:
  - **Prompt on apply** — ask the user for confirmation when they apply the macro (guards accidental application).
  - **Mark as favorite** — for all users it's shared with, the macro appears as **favorite** (pinned at top when applying) and they can't un-favorite it.

### Action types
- **Automated actions** — no user input needed. E.g. **Add case to case queue** (auto-adds to the chosen queue when applied), add a comment, add to a profile list, **assign to agent / assign to me / unassign** (e.g. a "Close" macro unassigns from self), and **set case properties** (= set a case **custom field** value).
- **Manual actions** — require input at apply time. E.g. set a custom field whose value the user must fill — a dialog appears on apply; mark **Required** to make it mandatory.

### Related macros & sharing
- **Related macros** — running this macro triggers **another macro** (chain multiple macros simultaneously).
- **Sharing permissions** — control who the macro is shared with.

## Notes / gaps
- Macros sit on top of [[custom-fields]] (set field values), [[queues]] (move between queues), and case assignment — a core agent-productivity governance entity. Also surfaced as Care Console shortcuts/macros.
- Part of Governance: [[users-user-groups]], [[roles-permissions]], [[accounts-account-groups]], [[customer-vs-workspace]], [[custom-fields]], [[queues]].
