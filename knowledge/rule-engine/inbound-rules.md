# Inbound Rules (Rule Engine 009)
**Source:** Product Foundation Courses → Sprinklr Services - Rule Engine / 009 Inbound rules (video transcript + demo; rule canvas observed) · **Help:** search `site:sprinklr.com/help inbound rules universal inbox rule engine`

## What it is
**Inbound rules** are configurations applied to **inbound messages** entering Sprinklr. They **automate/streamline** handling of incoming content (social mentions, DMs, enquiries) using **conditions + actions** to tag custom fields/properties or route based on attributes (keywords, language, sentiment).
- **Any message entering Sprinklr passes through inbound rules first** — they are the **first course of action**. (E.g. you DM a brand on Instagram → that account is in Sprinklr → the message is grabbed → inbound rules run first.)

## The rule canvas (what it looks like)
Rules are built on a **visual canvas** (URL `…/social/rule-engine/canvas/…`) of connected nodes:
- **START → MESSAGE** entry, then **CONDITION** nodes (if/else) each with a **Yes path** and **No (N) path**, and **ACTION** nodes.
- Example seen (Language Detection): CONDITION "Message is in Universal Inbox / Universal Inbox Exclusions queues" → CONDITION "Exclude messages that contain only fan mentions/images/emojis" → ACTION "Set Language to English for messages with no text" (Language CF = replace all with [English]).

## Create an inbound rule
1. **Rule Engine home → Create new rule.**
2. Top-right, set: **Name**, **Scope** (customer-level or workspace-level), **Context** = **Inbound**, **Activation date**, **Rule batch**, **Rule type**.
   - **Rule types:** **Standard** = triggered **automatically**; **On-demand** = triggered only on a **manual user action**. (Detail in [[batches-triggers]], [[on-demand-rules]].)
3. On the canvas, add **conditions** and **actions**. Each condition is a simple **if/else** (Yes path / No path).
   - Example: CONDITION source = account "all live chat accounts" → if Yes, ACTION **Change properties of the message → custom field Priority = High**. Result: all messages from that account group are tagged high priority.
- You can build complex logic and do all property/custom-field tagging on inbound messages this way.

## Standard/critical inbound rules (common in implementations)
- **Universal Inbox (master) rule** — the **backbone / first filter**. Typically starts with an **account-level check** (filter out accounts not meant to be handled). Then conditions exclude certain message subtypes (e.g. **sticker**, or **Instagram DMs** if the brand doesn't want cases from them) → those go to the **Universal Inbox Exclusion queue** (excluded from the case workflow). Everything else goes to the **Universal Inbox queue** → processed by further rules. So it sorts messages into **two queues: Universal Inbox vs Universal Inbox Exclusion**.
- **Language Detection rule** — if Universal-Inbox = Yes and message-content conditions match, the back-end **language model** detects the language and tags a **message-level custom field** (e.g. Arabic). Used downstream to route (e.g. Arabic cases → Arabic agents). Carrying the language tag from message → case is why inbound tagging matters.
- **Channel Detection rule** — **copies** account properties (**Social Network**, **Channel Type**) onto the message via a **Copy action source** (e.g. Instagram account → message social-network CF = Instagram).
- **Message Category Detection rule** — keyword sets per category (complaint / compliment / inquiry); if matched, tag **message category** (e.g. Complaint) on the Yes path → used to route to the team that handles that category.

## Why inbound rules are critical (messages vs cases)
- **Message** = an individual interaction (post, comment, DM, chat) from a profile. **Case** = multiple messages from a single profile **bundled** into one entity for tracking/management.
- Example: a customer DMs + comments + mentions about one laptop issue → Sprinklr **bundles them into one case** (by profile), so the brand handles **one** case, not three. Simplifies engagement.
- All **basic property tagging** (message type, category, language, account type, privacy, content) is done by inbound rules **before the case is created**, then carried forward to the case → enables granular routing/workflow.

## Best practices
- Always include **account-level safety checks** so only messages from the intended account groups pass through.

## Notes / gaps
- A ~1:23–5:01 segment (extended "why/intro") wasn't captured in the scrape; the setup + standard-rules content above is complete.
- Built on [[queues]] (Universal Inbox / Exclusion) and [[custom-fields]] (tagging); rule types/batches in [[batches-triggers]]; case creation rules in [[case-update-creation]].
- Part of Rule Engine: [[batches-triggers]], [[queue-rules]], [[case-update-creation]], [[on-demand-rules]], [[scheduler-engine]], [[login-logout-rule]].
