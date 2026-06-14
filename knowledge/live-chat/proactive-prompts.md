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
