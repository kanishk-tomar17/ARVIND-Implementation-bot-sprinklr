# Queues (Governance 008)
**Source:** Product Foundation Courses → Sprinklr Services - Governance / 008 Understanding Queues (video transcript + demo) · **Help:** search `site:sprinklr.com/help queues case queue subscribers permissions`

## What it is
A **queue** is storage for assets — like an **invisible folder** that houses **cases, messages, tasks**, etc. (same idea as a queue data structure). Queues are filled **manually** or via **automation** (macros, Rule Engine, Workflow Engine).

## Why queues matter
When a message is grabbed in Sprinklr (because the brand's account is added and a customer messaged it natively), you run it through workflows **via queues** — for case creation, assignment, etc. Queues are the backbone of routing/workflow (near-infinite use cases).

## Workspace vs Customer queues
**Settings → All Settings → Queues** appears under both **Workspace** and **Customer**:
- **Workspace queues** — visible only within that workspace; support **message-level** queues only.
- **Customer queues** — visible **across all workspaces** in the partner; support **multiple queue/asset types**: **Inbound Message, Suggestion, Approval, Case, Task**.

## Creating a queue
- **Add Queue** → **Name**; (customer level) **Queue type / asset type**, **Description**, **Owner** (yourself or someone else).
- **Subscribers** — get an **in-platform notification** when an asset is added to the queue (available for **inbound message** queues; **not** for case queues).
- **Smart alerts** — case queues can enable smart alerts, managed in the separate **Care Alert Manager** module (define which notifications trigger and to which users).

## Permissions / sharing
- To use queues you need the **Queues permission** via [[roles-permissions]].
- Share a queue (⋯ → **Permissions**) with users / user groups: **provisioned** users can **add** assets to the queue; **view** users can only **see** it (not add/remove).
- In workflows you can only **see/use a queue if it's shared** with you or a user group you're in.
- **Edit / Delete** existing queues.

## Adding/removing assets to a queue
- **Manually:** open a case → Overview/properties → see which global queues it's in → **add/remove** queues there.
- **Via automation:** macros / Rule Engine. Common example: when an agent **closes** a case, a macro adds it to the **Closed queue** so all closed cases are viewable in one dashboard.

## Notes / gaps
- Queues are consumed by [[macros]] (add-to-queue action), the Rule Engine ([[rule-engine]] family — e.g. [[queue-rules]]), and routing. Care Alert Manager is a separate module.
- Completes Governance: [[users-user-groups]], [[roles-permissions]], [[accounts-account-groups]], [[customer-vs-workspace]], [[custom-fields]], [[macros]].
