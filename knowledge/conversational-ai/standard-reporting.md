# Standard Bot Reporting Dashboard (Conversational AI 110)
**Source:** Product Foundation Courses → Conversational AI / 110 Standard Reporting Dashboard (video transcript) · **Help:** search `site:sprinklr.com/help standard bot reporting dashboard metrics care reporting`

## What it is
An **out-of-the-box dashboard** giving an overview of the bot's **performance and activity** over a selected time range — bot activity, cases handled by the bot, handle-time stats, and deflection stats.

## Data sources
- **Inbound Analytics** — **message-based** reporting: message volume, response time, user sentiment.
- **Social Analytics** — **case-based** reporting: case resolution and CSAT on social channels.
- **Universal Profile** — **profile-based** reporting: user preferences, demographics, behaviour patterns.

## Metric categories
- **Volumetric** — total messages received by the bot, total unique customers, etc.
- **Bot metrics** — distribution of **bot status** at message/case level (**handled by bot / handled by agent / fallback**).
- **Intent distribution** — intents detected by the bot (matched-intent distribution, cases with no intent detected).
- **Deflection & SLA analysis** — cases handled by the bot, **bot-to-agent handoff**.
- **Survey reporting** — survey clicks, survey click rate, survey sent count.
- **Smart clusters** (for spam messages) — top co-occurring keywords with message sentiment and count per keyword.
- **Bot abandoned case count / abandonment rate** — number / percentage of cases that **leave the bot interaction before the bot finishes** the conversation.

## Accessing & configuring
1. **Sprinklr Service → Analyze → Care Reporting.**
2. Search for the **Standard Reporting Dashboard** (offered OOTB).
3. Set the **account name** and a **date/time range** (demo: *Energy Australia*).
4. The dashboard renders all the metrics above.

### Add a custom widget
- Click **Add widget** → name it → select the **data source** → choose the **entity** → choose the **custom field** to plot.
- Example: a **Daily summary** tab mapping multiple custom fields.

## Notes / gaps
- Abandonment rate + bot-to-agent handoff are the headline health metrics — high values signal flows that need work (tie back to [[discovery-run]] for new workflows and [[message-validation]] for accuracy).
- OOTB dashboard; custom widgets extend it with client-specific custom fields.
- Three data sources map to three lenses: message (Inbound), case (Social), profile (Universal Profile).
