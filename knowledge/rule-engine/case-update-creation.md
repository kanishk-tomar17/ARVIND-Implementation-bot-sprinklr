# Case Creation & Case Update Rules (Rule Engine 012)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 012 Case update and creation rules (video transcript + demo) · **Help:** search `site:sprinklr.com/help case creation rule case update rule`

## Case Creation rules
Triggered **whenever a new case is created** (after the **case maker** queue rule makes the case — see [[queue-rules]]). Used to **auto-tag / assign / queue** every new case immediately.
- Examples: assign cases from different accounts to different teams; set **priority**; tag a custom field; add the case to a queue.
- Demo: CONDITION source = a specific **account** → Yes path: **priority = High**; No path: priority = Low → then **add all cases to the Universal Case Inbox**.
  - **Best practice:** all cases pass through the case creation rule, so use it for **universal tagging/assignment** regardless of team/account, and add every case to the **Universal Case Inbox** queue → handy to count created cases and to drill down (language/priority/CF) in **reporting**.
- Conditions here should use **case-level** properties (account, **case channel type**, any **case-level custom field**) — not message-level. E.g. tag priority High on all **Facebook** cases (via a channel custom field), then use that in the **assignment** setup so high-priority cases are catered to first.

## Case Update rules
Run/execute on cases **based on a trigger** (or a case-update event). They carry **most case-management actions**: **assigning, auto-closing, sending surveys**, and custom workflow actions.
- **Key difference from case creation rules:** creation rules fire **as soon as the case is created**; update rules require **your own trigger + conditions** defining **when/how** they run, **further down** the workflow.
- Demo: a case update rule with a **time-agnostic trigger** (source = **CGB assignment engine processing** queue — see [[batches-triggers]]). Sequencing trick: in the **case creation rule**, add the case to the "CGB assignment engine processing" queue → the time-agnostic trigger **auto-picks it up** → the update rule runs and checks further conditions (case queue, status, custom fields). This is how you **order** when each rule executes.

## Creation vs Update — when to use which
- Want to tag/assign **at the instant of creation** → **case creation rule**.
- Want actions **later / on updates / on a trigger** → **case update rule** (you can technically do creation-style tagging in an update rule too, but it needs a trigger that fires downstream).

## Notes / gaps
- Sits downstream of [[queue-rules]] (case maker) and uses [[batches-triggers]] (esp. time-agnostic) + [[queues]]. Deep case mechanics also in the Case Management module ([[case-creation-logic]], [[assignment-rules]], [[survey-rules]]).
- Part of Rule Engine: [[inbound-rules]], [[batches-triggers]], [[queue-rules]], [[on-demand-rules]], [[scheduler-engine]], [[login-logout-rule]].
