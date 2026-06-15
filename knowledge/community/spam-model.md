# Spam Model (Community 185)
**Source:** Product Foundation Courses → Community / 185 Spam Model (video transcript) · **Help:** search `site:sprinklr.com/help community spam AI model rate limit`

## What spam is / why prevent it
**Spam** = content irrelevant to the community forum, usually trying to **sell something fishy** unrelated to the brand; disrupts normal business. Common on **large communities (100k–200k+ users)** where moderators can't manually moderate. Preventing spam is a **health measure** — a spammed community drives away real users.

## Prevention measures
1. **Keyword / regex-based rules** (message-level rules — see [[message-level-rules]]).
2. **Manually block/ban** users (moderator permission).
3. **Rate limit** — restrict new users (e.g. first 24–48h: max 2–5 messages/hour). Spammers create new users to post spam, so rate limits curb them.
4. **AI spam model** (most effective).

## AI spam model
- An **out-of-the-box model** is pre-trained on default community data — usable for any community.
- For a use-case-specific model, **reach out to the AI Team** with a **dataset** (spam + non-spam messages, exported from reporting) to **custom-train** it.

### Deploy the AI model — 3 rules
1. **Inbound rule** → sends all inbound messages to the **spam queue**.
2. **Queue rule #1** → sends messages to the **spam AI model** and gets back a **classification (spam / non-spam)**.
3. **Queue rule #2** → based on the model's feedback, **marks the message as spam or not spam**.

Once deployed, spam is filtered automatically for months without moderator action.

### Retraining
- Spammers eventually find loopholes → **retrain** the AI model with the **new** spam message types so it keeps performing. Do this whenever there's a **surge** in spam.

## Notes / gaps
- Uses the [[inbound-rules]] + [[queue-rules]] pattern with an AI classification step; ties to moderation actions in [[message-level-rules]].
- Part of Community: [[community-builder]], [[global-workspace-roles]], [[message-level-rules]], [[live-chat-on-community]], [[guided-workflow-on-community]], [[case-management-for-community]], [[social-sso]], [[survey-on-community]], [[support-ticket]], [[community-reporting]].
