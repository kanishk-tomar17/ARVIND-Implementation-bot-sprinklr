# Proactive Prompt Builder & Rule Configuration (Live Chat 095)
**Source:** Product Foundation Courses → Live Chat / 095 Proactive Prompt Builder and Rule Configuration (video transcript + demo) · **Help:** search `site:sprinklr.com/help proactive prompt creative intercept AB testing`

## What proactive prompts are
**Cues/pop-ups** shown to website visitors to **encourage/initiate** a specific action — the brand makes the **first move**, anticipating user preferences.
- **Use cases:** provide assistance/resolve issues, **increase conversion** (targeted product prompt), promote **special offers**, **upsell/cross-sell**, **reduce cart abandonment** (prompt when a purchase stalls), and **gather feedback** (survey as an overlay).

## Creatives (the UI shown)
- **Position prompt** — appears at any screen position; the website stays accessible.
- **Chat prompt** — appears above the chat trigger icon.
- **Pop-up / overlay** — a modal pop-up with actions.

## Intercepts (the triggers)
**Intercepts** = the conditions that decide when/who sees a creative (e.g. "user spends 5 min on a URL → show on second visit"). Condition buckets:
- **User details** (personalised prompts) and **browser/device type**.
- **Browsing session** — time on page, time in session, **scroll depth**, current URL.
- **Intercept triggered** — whether the customer already engaged with the same/another intercept (avoid re-prompting).
- **Survey details** — saw/completed a survey in chat, etc.
- **External API** — trigger off a signal the website sends via API.
- **Agent availability** — number of agents available + pending cases in queue (workforce management).
- **User activity.**

## Configuration
1. **Create a creative:** choose a **layout** (e.g. headline + content + one target button); customise **headline text, button/border colours, padding, pop-up background, overlay background** → Create.
2. **Create an intercept:** toggle to **Intercept → New intercept** → add **display conditions** (the buckets above).
   - Add **multiple variants** in one intercept (e.g. mobile → chat pop-up, browser → overlay).
   - **A/B testing** — show different pop-ups to a chosen set of visitors to compare engagement.
   - **Target button actions:** open a survey (inline / new tab), open chat (with actions), **snooze** the prompt, redirect to a URL, or close.
   - **Additional settings:** **schedule** the prompt (campaigns), and set the **percentage of visitors** to show it to (e.g. 100% / 50%).
3. **Embed:** once the live chat code is on the website, prompts **trigger automatically** — no extra brand action needed.

## Proactive prompt rules
Tag **custom fields** on messages/cases created via prompts (for **routing logic** or **reporting** — e.g. volume generated per intercept):
- **Case-level:** create a **Case Update rule** → select source (live chat account) → search **"prompt"** → conditions like **prompt variant**, creative type, intercept triggered are exposed → tag the relevant custom fields.
- **Message-level:** same via an **Inbound rule** (source → message properties → "prompt" conditions).

## Notes / gaps
- Creative (the look) and intercept (the trigger) are separate objects — build the creative first, then attach it to one or more intercepts.
- Agent-availability + queue conditions let prompts respect **workforce capacity** (don't invite chats you can't staff).
- Prompt-tagging rules are the only way to **attribute volume/outcomes** to specific prompts in [[reporting-metrics]].

---
## Help-center additions (fetched 2026-10-27)
**Sources:** [Proactive Messaging](https://www.sprinklr.com/help/articles/proactive-messaging/proactive-messaging/6544925afd555b390dfed360) · [User Journey](https://www.sprinklr.com/help/articles/user-journey/user-journey/63ed2616f6e2cc7d18fac964) · [Proactive Prompts Report](https://www.sprinklr.com/help/articles/detailed-report-glossary/proactive-prompts-report/674dc54e974a651ec2f68f82)

### User journey of a prompt
- Conditions met → prompt shows. User can **click a CTA button**, **close it via "X"** (appears on hover on every prompt), or **ignore** it.
- You can configure **limits on repeat triggering** so users aren't spammed.
- On interaction, a custom journey can: **redirect to a webpage**, **start a bot journey**, **start a survey**, or **trigger an external action**.

### Proactive Messaging (different feature — agent/API-initiated outbound, not rule-based prompts)
1. Call the **Create Profile** API (Universal Profile API) to create a **blank case**; it returns the case number → open it in Care Console.
2. Agent sends an outbound message → the live chat widget **pops up** on the visitor's site and starts a new conversation. Rich message templates are supported.
3. **Fallback to Email/WhatsApp** when the visitor is inactive: **Rule Engine → Case Update rule** → section "Conditions on live chat conversation associated to the case" → **"Last active fan profile duration greater than 'x'"** → action **"Send SMS To"** or **"Send Auto Response To"**.

### Reporting — Proactive Prompts Report
Dashboard widget → data source **Service Analytics** → **Live Chat Additional Report Group** in Widget Builder.
- **Metrics:** Intercept Triggered / Engaged / Completed / Closed Count, Intercept Snooze Triggered Count, Snooze Count.
- **Dimensions:** Intercept Name, Activity Type, Activity Actor, Proactive Prompt, **Variant AB Testing** (boolean), Snooze Count, Prompt Intercept Triggered Time, Prompt Creative ID / Name / Type, Trigger Image Url, plus standard time dimensions (Date, Day of Year, Week of Year, Month, Day of Week, 15/30/60-min time of day).
- Help-center pages have **no** step-by-step builder config; the course note above is the only config source. Category page: https://www.sprinklr.com/help/categories/proactive-prompts/63bc4e2b24627514aaa2305a
