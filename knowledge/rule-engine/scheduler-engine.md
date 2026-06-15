# Scheduler Engine (Rule Engine 014)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 014 Scheduler Engine (video transcript + demo) · **Help:** search `site:sprinklr.com/help scheduler engine scheduler queue`

## What it is
**Scheduler Engine** schedules actions in a workflow at a **predefined time** — **singular or recurring** per the configured schedule. It uses **scheduler queues** instead of a trigger, which is **simpler/shorter** than building a queue + configuring a trigger.

## How it compares to a rule trigger
Functionally like a **rule trigger** ([[batches-triggers]]): both execute a rule on messages/cases. Difference:
- **Trigger:** picks up cases/messages by config and runs the rule.
- **Scheduler engine:** you **add** messages/cases into a **scheduler queue**, and the engine **automatically executes the configured rule** on them — no trigger to build.

## Configuration (demo)
- **Sprinklr Service home → Triaging and Route → Scheduler Engine** — lists configured scheduler engines.
- **Create a scheduler queue:** choose **asset/queue type** (e.g. Case queue), **name** it, set the **execution interval** (like trigger frequency, e.g. every 2 sec), and define the **action** = **apply a rule** (select the rule). All messages/cases dropped into that scheduler queue are picked up and the rule runs on them.
- **Add items to the scheduler queue:** in a (queue) rule, use the action **"Add to scheduler engine queue"** (under **Schedule actions**) → pick the queue name. Those messages/cases are then auto-processed by the scheduler.
- Example: condition language = English → "Add to scheduler engine queue" → that scheduler queue runs the chosen rule on all English messages.

## Scheduler engine vs trigger (when to use)
To execute rules in sequence you have **two options**:
1. Add cases/messages to a **case/message-level queue** → define a **trigger** on the next rule. (More setup; with time-agnostic triggers you must remember to **remove** items from the source queue to avoid loops.)
2. Add them to a **scheduler engine queue** → the scheduler config runs the rule directly. **Simpler/easier** (no trigger to build).

## Notes / gaps
- A lightweight alternative to triggers for sequencing rule execution; pairs with [[queues]], [[queue-rules]], [[batches-triggers]].
- Part of Rule Engine: [[inbound-rules]], [[batches-triggers]], [[queue-rules]], [[case-update-creation]], [[on-demand-rules]], [[login-logout-rule]].
