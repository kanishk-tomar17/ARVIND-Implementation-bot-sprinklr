# Bot Rule Setup (Conversational AI 105)
**Source:** Product Foundation Courses → Conversational AI / 105 Bot Rule Setup (video transcript) · **Help:** search `site:sprinklr.com/help bot rule case maker rule inbound rule rule batch`

## Goal
Set up the rules that **enable bots on social/messaging accounts** — covering rule execution order, why the Case Maker runs before the Bot Rule, how the Bot Rule is triggered, and the scenarios it handles.

## Rule batch (execution order)
- Rules of a given type **don't run simultaneously** — a **rule batch** defines their **sequential execution** within an environment.
- **Each rule type has its own dedicated rule batch** (queue rules, case update rules, inbound rules, etc.).
- Within a batch, rules run **top → bottom, then left → right**.

## Message flow (order of execution with bots)
1. **Inbound rules** (first) — process incoming messages by **social channel, account, message type**. They automate tagging and **direct messages to the Universal Inbox queue / Case Maker**.
   - Example *"add eligible messages to Case Maker"*: conditions like *account in account group?*, *message age?*, *from Universal Inbox?* → action: send to Case Maker via the **scheduler engine queue**.
2. **Case Maker** — decides whether to **create a new case, attach to an existing case**, close, or route to agent. Then forwards the processed message to the **Bot Rule**.
3. **Bot Rule** — activates the **bot application** (dialogue tree, intents, entities, issue types, FAQ bots). The dialogue tree + CA entities determine the response (which **intent** is captured, which **bot** is configured against it). The bot **publishes the reply**.

## Why Case Maker runs before Bot Rule
Case Maker handles **new case creation** and **associating the message to a case**, plus: checking case status, **copying properties message→case and profile→case**, and sending the case to the right bot rule.
- It runs first so the Bot Rule/application has **all relevant info** to decide.
- **If a message goes straight to the Bot Rule**, and the bot's decisions depend on **profile-level properties not present at message level**, the bot **can't decide and throws an error**.

## How the Bot Rule is triggered (two ways)
1. **Preferred:** inside the Case Maker rule, place the message in the appropriate **scheduler engine queue** → this triggers the Bot Rule.
2. **Not preferred:** add messages to a **partner queue** and make the Bot Rule **trigger-based** on messages in that partner queue.

## Five scenarios handled in a Bot Rule
1. **Error state** — has the application hit an error?
2. **Routed to agent** — is the case routed to an agent?
3. **Fallback.**
4. **Conversation with the bot** — is the conversation still with the bot?
5. **Conversation ended.**
These let the Bot Rule run different actions per situation for good CX with fewer errors.

## Setup checklist (summary)
1. **Inbound rule** → ensure all messages from your accounts go to the **Case Maker** via the scheduler engine.
2. **Case Maker rule** → after preprocessing, call the **right Bot Rule** (via case queue or scheduler engine queue).
3. **Bot Rule** → ensure it calls the **correct application** (where your bots are configured).
4. **Conversational application → Deployment settings** → confirm the **bots are deployed**.

## Notes / gaps
- This ties Conversational AI to the broader [[../case-management/case-creation-logic]] (Case Maker) and [[../case-management/bot-rule]] — same rule-engine machinery.
- The profile/message-level property dependency is the classic "bot throws an error" root cause — check Case Maker is copying the needed properties first.
- "Scheduler engine queue" trigger is preferred over "partner queue + trigger-based" — default to the former.
