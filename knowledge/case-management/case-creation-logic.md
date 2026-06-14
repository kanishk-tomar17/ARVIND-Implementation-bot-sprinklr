# Case Management — Case Creation Logic & Case Maker Rule

**Source:** Product Foundation Courses → `Sprinklr Services - Case Management / 016_… Case Creation Logic & Case Maker Rule` (video transcript) · **Cross-check:** `site:sprinklr.com/help case maker rule`

How Sprinklr decides whether an inbound message **creates a new case** or **associates to an existing one** — and the **Case Maker rule** that automates it.

## What a case is
- A **case** = a collection of related messages/interactions/inquiries around one customer issue.
- **Lifecycle:** Creation → Routing → Prioritisation → Assignment → Resolution → Closed. All updates/notes/actions are documented in the case.

## Sprinklr architecture (entities)
- A message from any channel is grabbed as a **Universal Message**; its source is a **Universal Profile**.
- The message passes **message enrichment + data-tagging rules** → enters the **Case Management system**.
- There, **case creation logic** decides: create a new **Universal Case** or associate to an existing one.
- After creation, the case flows on: **bot** (Bot Rule) or **assignment queues** (Assignment Rules) → resolution → **survey** for feedback.

## Why case management matters
- **Organisation & efficiency** — cluster high-volume messages by issue/profile → streamlined workflows.
- **Better CX** — comprehensive interaction history → faster, accurate responses → higher CSAT.
- **Collaboration** — documented actions; assign to the right agent; reduce duplicate effort.
- **Monitoring & reporting** — interaction-level insights: response times, SLAs, resolution rates, CSAT.

## Case creation logics (vary by channel/client)
- **Conversational channels:** single case for all messages in the same conversation from the **same profile**; OR single case for all messages in the same conversation from **any profile**.
- **Social channels (profile-based):** single case for all messages from the **same profile on a given account**; OR same profile on a **given channel** (across multiple accounts on that channel).
- **Generic modifiers:** create a new case (vs associate) based on **inactivity** of the previous case beyond a set time, or based on the **status/properties** of the previous case.

## Case Maker rule (automates creation/association)
1. Check the message is in the **Case Maker queue** (it passed basic criteria — an engageable message needing a case).
2. Check for an **existing case** this message belongs to (channel-specific checks).
3. If no existing case → **create a new case**; else **associate** to the existing case.
- (Walked through on the platform in the video; exact checks differ per channel/client.)

## Notes / gaps
- From the course video transcript. Related: `case-management/bot-rule.md`, `case-management/assignment-rules.md`, `case-management/survey-rules.md` (pending).
