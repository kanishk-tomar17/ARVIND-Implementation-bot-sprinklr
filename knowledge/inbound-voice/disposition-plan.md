# Disposition Plan (Inbound Voice 161)
**Source:** Product Foundation Courses → Inbound Voice / 161 Disposition plan (video transcript + demo; ACW/disposition builder screenshot) · **Help:** search `site:sprinklr.com/help disposition plan SCW callback schedule`

## What it is
A **disposition plan** is a **form the agent fills at the end of a call** to capture the **primary business outcome, secondary (sub) outcome**, and related info — enriching the conversation data. Filled in the **SCW** (Summary/Smart Call Window) that pops up after the call.

## Disposition builder
- Build the disposition plan (a set of **fields**). Each field can be **mandatory/optional**, have **error messages** (shown in SCW on invalid input), **business-hours** rules, and **advanced conditions**:
  - **Future-date condition** for callback date/time (time selected must be in the future; "within … next … future").
  - **Visibility conditions** — show a field only based on the **disposition / sub-disposition** selected (e.g. show "callback date & time" only when **disposition = Connected** AND sub-disposition = **Follow up** OR **Primary customer not available**), and based on prior field selections.
- **Add Field** → add any number of fields.

## Use in the SCW
- **SCW Builder** → field component **Call Disposition** → select the disposition plan to show (e.g. "Acme disposition plan"). Plus 3 natively-built SCW fields.
- **Schedule-callback workflow** (in SCW builder, via update-properties / assignment node):
  - A **Groovy** script reads the callback date/time field from the disposition plan (fields stored in an **array** → `[0]` = first element; reference by `field_<id>`) into a local variable.
  - A **decision box** checks the callback time exists → only then create the **Scheduled Callback** node.
  - Scheduled Callback fields: **callback number** (usually the customer's **Caller ID**), **callback date/time** (from disposition), and **agent** (the agent who took the call → callback triggers to the **same agent**).

## Agent experience
After the call disconnects, the **SCW pop-up** appears bottom-right. If one disposition plan is configured it's prefilled. Agent selects **disposition** (e.g. Connected) + **sub-disposition** (e.g. Follow up). Visibility conditions then reveal fields (e.g. callback date/time); mandatory fields + future-date validation block submit until satisfied.

## Reporting
A widget on **Call Disposition / Disposition / Callback date-time** + **Call Count**, filtered by the disposition plan (e.g. Acme) → counts per disposition selection (note: a few minutes' latency after a call before it reflects).

## Live example — HDFC (banking)
Disposition plan "Banking": dispositions = **Debit card, Bank account, Fixed deposits, Recurring deposits, Dream deposits**; sub-dispositions = **FCR, Non-FCR, Partial FCR**; ~**30+ fields** (banking has many products/departments — banking, credit card, loans, etc.).

## Notes / gaps
- Disposition is the ACW form; the SCW + schedule-callback flow ties to [[acw-builder]] and [[call-controls]]; callback feeds the dialer/callback flow. Uses Groovy ([[groovy-scripts]]).
- Part of Inbound Voice: [[telephony-integration]], [[voice-connectivity]], [[custom-fields]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[acw-builder]].
