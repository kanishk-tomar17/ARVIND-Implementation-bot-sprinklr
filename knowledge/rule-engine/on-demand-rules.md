# On-Demand Rules (Rule Engine 013)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 013 On demand rules (video transcript + demo) · **Help:** search `site:sprinklr.com/help on demand rule standard rule macro rule runner`

## On-demand vs Standard rules
The core distinction is **how they're triggered**:
- **Standard rules** — execute **automatically** in the background on a **trigger** + conditions; continuously monitored, no user intervention.
- **On-demand rules** — **manually triggered by a user** (via a **macro**) on specific cases/messages only.

| Dimension | On-demand | Standard |
|---|---|---|
| Trigger | Manual (macro) | Automatic (trigger condition) |
| Scope | Limited / selected entities | Runs across all matching, continuously |
| Real-time | Acts only when user executes | Runs in background on predefined logic |
| Use | Ad-hoc / custom one-offs | Backbone of case workflow |

## When to use which
- **On-demand:** apply an action to a **limited set** (e.g. update a custom field on only 10 of 100 cases) — build the logic in an on-demand rule, then apply a **macro** selectively on those cases.
- **Standard:** the **basics of the case-management workflow** — assignment rule, preassignment processing rule, survey delivery rule, etc. — all standard rules with triggers, running continuously to pull cases from queues and update status/custom fields.
- **Retro-tagging** can be done either way: on-demand (filter cases + apply macro) **or** standard (a **one-time retrospective trigger** on a differentiating property). Depends on how well you can filter the target cases.

## How it works (demo)
- When creating any rule (e.g. a **case update rule**) you choose **Standard** or **On-demand**.
- **Standard:** you're prompted to select a **trigger** (e.g. a **time-agnostic** trigger running every 2 sec, searching the preassignment processing queue) → runs in a background loop once enabled. See [[batches-triggers]].
- **On-demand:** executed via a **macro**. In **Macros**, an automated action **"Rule Runner" / "Rules to execute"** lets a (case-level) macro run a chosen rule — so applying that macro on a case executes the on-demand rule **only on those cases**. See [[macros]].

## Notes / gaps
- On-demand = macro-driven (Rule Runner); standard = trigger-driven. Pairs with [[macros]] and [[batches-triggers]].
- Part of Rule Engine: [[inbound-rules]], [[batches-triggers]], [[queue-rules]], [[case-update-creation]], [[scheduler-engine]], [[login-logout-rule]].
