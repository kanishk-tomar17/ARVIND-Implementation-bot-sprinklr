# Queue Rules (Rule Engine 011)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 011 Queue Rules (video transcript + demo) · **Help:** search `site:sprinklr.com/help queue rules intuition case maker`

## What it is
**Queue rules** run on a **segregated group** of messages/cases that sit in a particular queue. (Queues = invisible buckets housing one asset type — see [[queues]].) Use queue rules to **automatically** act on a filtered subset without manual action.

## Workspace vs Global queues (recap for rules)
- **Workspace queues** — asset type **inbound messages** only.
- **Global queues** — used in case workflows; can store **cases, messages, tasks, approvals, suggestions**.

## How queue rules relate to inbound rules
- **Inbound rules tag in real time** as messages are grabbed, and **add messages into queues**.
- **Queue rules then execute on only the messages in those queues** (picked up by a **trigger** whose source condition = that queue). So you **drill down**: inbound rules filter/tag/route into queues → queue rules apply higher-level logic to each group.
- **Best practice:** the queue rule's **source condition** should be **in sync** with its **trigger's source condition** (same queue).

## Primary use case — segregating the workflow
Example: thousands of messages arrive. **DMs** on Twitter/Instagram should create a case **directly** (skip AI filtering), so inbound rules send DMs straight to the **case maker** and send all **other** message types into a queue where a queue rule runs the AI/Intuition setup.

## The two key queue rules in case workflows
1. **Intuition rules** — AI/ML logic that filters messages and categorizes them (complaint, feedback, appreciation…), marking **engageable vs non-engageable**. Non-engageable messages are **dropped from case creation** (efficient at high volume — agents only engage where needed).
2. **Case Maker rule** — **where cases are actually created.** As a blueprint best practice, **cases are created on queue rules (case maker), not on inbound messages.** (Detail in case-creation/case-management videos.)

## Typical end-to-end flow
Inbound rules (tag + add to queues) → **Intuition queue rule** (filter engageable) → eligible messages → **Case Maker queue rule** (create case). Within a queue rule, after conditions, messages can be **added to a different (downstream) message-level queue** for the next stage.

## Notes / gaps
- Queue rules are triggered (see [[batches-triggers]]) and depend on [[queues]] + [[inbound-rules]] upstream tagging. Case creation specifics → [[case-update-creation]] and the Case Management module.
- Part of Rule Engine: [[inbound-rules]], [[batches-triggers]], [[case-update-creation]], [[on-demand-rules]], [[scheduler-engine]], [[login-logout-rule]].
