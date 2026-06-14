# Live Chat Specific Reporting Metrics (Live Chat 090)
**Source:** Product Foundation Courses → Live Chat / 090 Live chat specific reporting metrics (video transcript) · **Help:** search `site:sprinklr.com/help live chat reporting KPI funnel audience activity`

## KPIs
Key performance indicators = quantifiable metrics for product performance. For Live Chat: **message volume, case volume, response time, CSAT, agent performance metrics, abandonment rate**, etc.

## Building a reporting dashboard
1. **Launchpad → Care Reporting** (under **Sprinklr Service → Analyze**) → folders/dashboards.
2. **Create a dashboard** → **Add widget** (custom reporting widget).
3. Configure: **name**, **data source**, **visualization**, **filters**.
   - **Data sources:** **Social Analytics** = case data · **Inbound Analytics** = message data · **Audience Activity** = funnel / audience-activity data.
   - **Visualisations:** counter, table, pie, bar, etc.
   - **Filters:** e.g. case status = assigned / awaiting assignment.
   - Demo: a **Counter** widget for **case count**, optionally filtered by case status.

## Funnel reporting
Tracks the user journey from first contact → conversion, broken into stages, to make data-driven decisions about website initiatives.
- **Live chat funnel stages:** **Prospects** (all website visitors) → **Exposures** (saw the live chat) → **Unique click count** (clicked the trigger icon) → **Unique conversation started** (clicked the new-conversation CTA).
- **Data source = Audience Activity** (has a built-in **funnel** visualisation).
- Exposed **events** for reporting include **conversation started**, **conversation window opened**, plus click counts and other standard events. (SDK-specific events covered separately.)

## Website visitor demographics
At the **start of a conversation**, live chat captures channel details **by default**: **browser, device, local IP, country, locale**.
- Report on these under **Social Analytics** — e.g. case count by browser/device/country/locale.
- Demo: a **bar** widget, X-axis = case count, Y-axis = browser; add account/channel filters.

## Example (Samsung America dashboard)
- KPIs: total cases, abandoned cases, handled by agent, currently assigned, awaiting assignment.
- Funnel reporting split across pages/apps (samsung.com, Members app, Shop app, support/contact pages) → shows **which page drives more live-chat interactions** → informs business decisions.

## Notes / gaps
- Pick the data source deliberately: **case** metrics → Social Analytics; **message** metrics → Inbound Analytics; **funnel/visitor** → Audience Activity. Wrong source is the common reporting mistake.
- Demographics (browser/device/country) are captured automatically — no extra config needed to report on them.
- Funnel (prospects→exposure→click→conversation) is the deflection/adoption story for live chat rollouts.
