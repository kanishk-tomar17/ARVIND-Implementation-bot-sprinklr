# Email Collaboration — Forward Case as Email (Email Care 135)
**Source:** Product Foundation Courses → Email Care / 135 Email collaboration (Forward as email) (video transcript + demo) · **Help:** search `site:sprinklr.com/help forward case as email associate case rule`

## What it is
**Forward Case as Email** lets a user **forward a whole case to another person/team via email** without leaving Sprinklr — for collaboration with a supervisor or someone outside the team. The forwarded email carries the case conversation (from any channel).

## How an agent forwards
From the **Agent Console / Care Console**, open a case → **Forward as Email** → a dialog opens → pick the **From account** (which Sprinklr account to send from), enter the **recipient email**, add details/message → **Send**. The case shows as "forwarded" to that email.

## Required rule configuration (so replies thread back)
For the **recipient's subsequent replies to associate back to the original case**, set up an **inbound rule** with **2 conditions + 1 action**:
1. **Account condition** — the account used to forward the case.
2. **Message-has-associated-case condition** — does any message in the conversation already have a case associated (from any channel)? → **Yes**.
3. **Action: Associate Case** — associates the recipient's subsequent replies to the **original case**.

Once this rule is enabled, replies from the forwarded recipient land in the **same case**.

## Notes / gaps
- Depends on an inbound rule with an **Associate Case** action ([[inbound-rules]]); forwarding happens from Care/Agent Console.
- Part of Email Care: [[account-types]], [[webforms-external-gw]], [[email-signature]], [[manual-case-merge]], [[ignore-duplicate-autoresponse]], [[email-templates]].
