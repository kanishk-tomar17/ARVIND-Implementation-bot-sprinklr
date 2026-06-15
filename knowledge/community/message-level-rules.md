# Community-specific Message-level Rules (Community 182)
**Source:** Product Foundation Courses → Community / 182 Community specific Message level Rules (video transcript + demo) · **Help:** search `site:sprinklr.com/help community moderation rules mark as private spam`

## What it is
Message-level rules (inbound/message rules — see [[inbound-rules]]) configured for **community moderation**. Three use cases:
1. **Spam & profanity identification**
2. **Attachment-based moderation** (image/video)
3. **Masking personally identifiable information (PII)** of a community user/customer

## The standard rules

### 1. Spam / profanity rule
- Standard spam identification rule: message passes through; conditions match against a **predefined keyword list** (profanity/spam keywords).
- If matched → action **Mark as Spam** (a message-level **Care Community action**) → the message is marked spam.

### 2. PII masking rule
- Users may (un)knowingly post personal info (SSN, Aadhaar, bank records) in posts/replies/comments.
- Rule uses **regex checks** for email address, bank account number, customer ID, SSN/Aadhaar, etc.
- If any matches → action **Mark as Private** → the post is hidden. A further action can **send the message to a moderation board** where admins/moderators review and, if appropriate, **Mark as Public** (another message action) to make it visible again.

### 3. Attachment-based moderation rule
- Standard rule checks if a message has an **image/video attachment**.
- If yes → **Mark as Private** + **assign to a moderation queue**. Moderators review via the **Engagement Dashboard**, scan the image/video, and **Mark as Public** if it meets community guidelines (catches obscene/inappropriate attachments).

## Community-specific message actions
Found under **Care Community actions** when editing a rule:
- **Mark as Private** (set Yes → post hidden)
- **Mark as Spam**
- **Mark as Public**

## Notes / gaps
- These are message/inbound rules ([[inbound-rules]], [[queue-rules]]) specialized with **Care Community actions** + a **moderation queue** reviewed in Engagement Dashboards. Spam detail also in [[spam-model]].
- Part of Community: [[community-builder]], [[global-workspace-roles]], [[spam-model]], [[case-management-for-community]], [[live-chat-on-community]], [[guided-workflow-on-community]], [[social-sso]], [[survey-on-community]], [[support-ticket]], [[community-reporting]].
