# Rule Batches & Triggers (Rule Engine 010)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 010 Rule Batches & Triggers (video transcript + demo) · **Help:** search `site:sprinklr.com/help rule batch rule trigger retrospective time agnostic`

## Rule Batches
**Rule batches** categorize/organize rules so they run in a defined **sequence**. A batch stacks multiple rules in order.
- View: Rule Engine home → (case update rules at customer level) → **⋯ → Rule Batch**. The grey-background tags at the top are the **rule batches** (e.g. **Bot**, **Default**, **Preassignment**…); the entities beneath each are the **rules** in that batch.
- **Execution order:**
  - **Rule batches run left → right** (Bot batch first, then Default, then Preassignment…).
  - **Rules within a batch run top → down.**
- **Why ordering matters:** even correctly-configured rules break the workflow if mis-ordered. Example: **survey rules** must be in a **later** batch — a case must first pass **preassignment → assignment → status tagging** and only be surveyed **after the agent closes it**. Putting surveys first would fire them before the case is even assigned.

## Rule Triggers
**Triggers** automate *when* a rule runs — they have their own conditions deciding when/how the rule executes. Example: an assignment rule should fire only once a case is in the **Awaiting Assignment** queue → set that queue as the trigger so those cases run through the assignment rule.

### The 3 trigger types
1. **One-time trigger for retrospective & ongoing use** — runs on an entity **once** per the trigger **frequency**. It picks each message/case **only once**, regardless of whether the action happened; if the entity didn't match at that iteration, it's **never reconsidered**, though the trigger keeps scanning for **new** entities in future iterations.
   - Config: name, type, **trigger frequency** (e.g. 5 sec), **trigger conditions** (e.g. case queue = preassignment processing). Best for cases **not** needing loops/retro-tagging of old entities.
2. **Time-agnostic trigger** — runs on an entity an **unlimited** number of times per frequency until the entity **stops meeting** the trigger condition. **Most common** in case workflows.
   - **Critical:** you **must define an exit path** — remove the case/message from the **source queue / custom field** the trigger watches, or it loops **indefinitely**. (If not removed, the trigger can't even be enabled.) Demo: assignment rule with trigger source = "CGB assignment engine processing" queue; the final action **removes the case from that queue** to prevent an infinite loop.
3. **One-time trigger for retrospective use** — for **processing older entities** (retro-tagging). Use case: you add a new custom field tagged on new cases but want older cases to get a **default** value — this trigger runs the rule on the **old** cases once.
   - **No source queue required** and **no frequency to define** (frequency is set back-end). Picks entities **once**; never reconsiders them (even if conditions weren't met).

## Notes / gaps
- Triggers + batches + [[queues]] are how the Rule Engine sequences work; ties directly to [[inbound-rules]] and [[case-update-creation]] / [[queue-rules]].
- Part of Rule Engine: [[inbound-rules]], [[queue-rules]], [[case-update-creation]], [[on-demand-rules]], [[scheduler-engine]], [[login-logout-rule]].
