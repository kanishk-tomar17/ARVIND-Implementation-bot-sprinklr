# Care Console — Iframe Widget

**Source:** Product Foundation Courses → `Care Console - Iframe Widget` (video `041_…`, transcript read) · **Cross-check:** `site:sprinklr.com/help iframe widget`

Render a **third-party / KB / website URL** inside a widget or a full tab in Care Console, so agents reference external info without leaving the platform.

## What it is
- Embeds an external URL (KB portal, website, dashboard) in a **widget** or a **dedicated tab** in the case view.
- Agents reference that info (offers/coupons, KB articles, dashboards) and reply without extra clicks or switching browsers/tabs.

## Prerequisite & configuration
- **Prerequisite:** the URL must be **whitelisted on the sprinklr.com domain** so its content renders inside Sprinklr.
- **Configure in Care Console Manager:** add a tab or widget → enter the URL → set a name and **height**. (Exact steps in the KB article.)

## Limitations
- The widget **relies on the URL's native functionality** — Sprinklr only renders it; if the site doesn't work natively, it won't work here (Sprinklr can't control it).
- **No state retention** — closing/reopening the widget restarts the session (agent searches from the beginning), which can mean repetitive actions. Still faster than juggling separate browser tabs.

## Examples (from real client configs)
- A **website** rendered in the console (e.g. request-a-demo, native live-chat widget — starting a chat there flows back into Sprinklr).
- A **Power BI dashboard** in a dedicated tab (churn performance, unit recommendations, churn engines) — agent flips between case details and dashboard in one browser.
- A **KB portal/article** rendered so a stuck agent searches, opens, and copies the answer into the reply without leaving the console.

## Notes / gaps
- From the course video transcript. Whitelisting is the key gate. Related: `care-console/manager.md`, `care-console/widgets.md`.
