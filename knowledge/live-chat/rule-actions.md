# Live Chat Rule Actions (Live Chat 089)
**Source:** Product Foundation Courses → Live Chat / 089 Live chat rule actions (video transcript) · **Help:** search `site:sprinklr.com/help live chat rule conditions actions` + Sprinklr Live Chat handbook "WUC / workflow use cases"

## Rules basics
Rules automate workflows, assignments, properties, and more — an **if-then**: *if* an asset (message/profile) meets a **condition**, *then* an **action** runs.
- **Rule Engine** lives under **Collaborate**.
- Rules run on different **entities**: queues (queue rules), **case update** rules, **inbound message** rules, etc.
- Two kinds: **Standard** (auto-triggered per config/triggers) and **On-demand** (manual, via **macro** or scheduler engine).

## Live-chat-specific CONDITIONS
(Under "conditions of live chat conversation associated to this case")
- **Case IP address** — match a set of IPs via **CIDR** (an IP-range group). Use: block/act on a set of IPs.
- **Last active fan profile duration** — time since the user was last active on the **browser tab** where the chat is happening.
- **Last updated fan profile status duration** — time since the tab was last opened.
  - Together: **auto-close** cases by active/inactive status, and **set priorities** so agent capacity serves **active** customers first (reduces load).
- **Survey last sent to case IP address before duration** — act based on a survey already sent to an IP (e.g. don't resend a survey to a returning user within a window).

## Live-chat-specific ACTIONS
(Under "actions on chat conversation associated to the case")
- **Block IP of the conversation** — block abusive/malicious users; agent must **unblock** to restore access.
- **Close chat conversation** — makes the conversation **read-only** for the customer (can't reply). Mirrors the customer's own close action.
- **Delete chat conversation** — delete for the customer after a period (privacy; e.g. public computer left open).
- **Enable / disable video calls** — turn audio/video on/off for a user (e.g. disable camera on spam).
- **Expire chat conversations** — expire templates (cards, carousels, quick-reply assets) so the customer can't act after close; run in a **case-closed macro**; templates show "this attachment has expired".
- **Expire chat user session** — clear session so a new conversation is treated as a **brand-new user** (useful on public spaces/networks).
- **External actions** — call an **API** / wire a **third-party bot** into live chat.
- **Forward live chat conversation as email** — send the full **transcript + attachments** to the customer's email (captured via the contact form).
- **Handover live chat conversation** — hand the conversation from agent to a bot, or to an **external bot** mid-conversation.

## Calling rules from the Live Chat Builder
In **Personalize your live chat → Conversation screen**, chat actions can trigger rules:
- **Close chat action** — select rules to run when the customer clicks close (e.g. trigger a survey, set a custom field, unassign the case). Configure an **on-demand rule** and call it here. Same for **Delete chat**.
- **Advanced settings** — two more hooks:
  - Rule on **New Conversation CTA** — applied to **all previous cases** (e.g. unassign/delete prior cases when the customer starts a new conversation).
  - Rule on **case association** — runs before the message is processed.

## Notes / gaps
- Active/inactive duration conditions are the key levers for not wasting agent capacity on idle chats — pair with priority/auto-close.
- "Expire chat conversations" must run in the **case-closed macro** to clean up interactive templates.
- The **Live Chat handbook's WUC (workflow use cases)** section has ready-made rule configs for common scenarios — point consultants there.
- Same Rule Engine as [[../conversational-ai/bot-rule-setup]] and [[../case-management/assignment-rules]].
