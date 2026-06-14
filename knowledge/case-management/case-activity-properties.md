# Case Management — Checking Case Activity & Properties (3rd pane)

**Source:** Product Foundation Courses → `Sprinklr Services - Case Management / 021_… Checking Case Activity & Properties` (video transcript) · **Cross-check:** `site:sprinklr.com/help case activity`

How to inspect a **message / case / profile** in the **third pane** — the diagnostic view for "what happened and why."

## The third pane
- Double-click a message in an engagement dashboard column → the **third pane** opens on the right.
- A **dropdown** switches between **Message / Case / Profile** context.

## Sections (Message context)
- **Overview** — quick summary: who it's from, message text, basic properties, current queues/work queues, the associated case, and notes.
- **Properties** — all properties of the **Universal Message**: message ID (copyable), system fields (e.g. Channel Type = "Sprinklr Live Chat"), and **all message-level custom fields** with their values (blank if unset). Values can be edited manually here, but normally the automated rules set them.
- **Cases** — the case(s) associated to this message (e.g. case #2850).
- **Collaborate** — notes (from rules or manually added).
- **Tasks** — tasks created on the message.
- **Activity** (three-dot → Activity) — **the audit log**: every action/update on the message, sortable asc/desc, with timestamps.

## Reading the Activity log (debugging gold)
- Shows the exact rule pipeline that ran, in order, e.g.:
  1. **Inbound rules** (first to run after grab) → set engageable null→true, message category not-set→inquiry, privacy→private, priority→medium → push to **Case Maker queue**.
  2. **Case Maker rule** → removed from Case Maker queue, added to Bot Trigger queue, "case created = yes" (first message of the case).
  3. **Bot Rule** → bot status "handled by bot".
- **Case Activity** works the same for case-level actions/updates.
- This is the primary tool to diagnose **why a case routed/behaved a certain way** — read which rule made which change and when.

## Switching context & previewing
- Switch the dropdown to view **Case** or **Profile** properties/activity instead of message.
- You can also **preview** messages/cases against your **rules** (test how a rule evaluates a given message/case) — the video's final segment.

## Notes / gaps
- From the course video transcript. This pane is the consultant's main debugging surface — pair with `case-management/assignment-rules.md` / `bot-rule.md` to trace behaviour. Related: `care-console/case-third-pane.md`.
