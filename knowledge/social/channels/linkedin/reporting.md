# LinkedIn — Reporting & Insights (Sprinklr Social — LinkedIn)
**Source:** sprinklr.com/help — LinkedIn channel (multiple articles; see links below)

## What it is
- A set of LinkedIn analytics surfaces in Sprinklr that let you visualize and track LinkedIn KPIs so you can understand and grow your audience. See [[reporting]].
- Covers three reporting layers: **Account/Page Insights** (brand presence — reach, engagement, conversions, CTR), **Post Insights** (per-post performance), and **Audience Understanding** (demographics: age/gender, location, industry, function, seniority, company size).
- Available for two LinkedIn account types: **Company Pages** and **Profiles** (some profile metrics only apply to "Distributed" type accounts).
- Data is pulled directly from LinkedIn Insights via the LinkedIn API, then refreshed on fixed sync schedules and backfilled within fixed historical windows (both governed by LinkedIn API limits, not Sprinklr).

## Key features & how to use

### Standard Reporting Dashboard — LinkedIn
- A prebuilt dashboard that visualizes your key LinkedIn KPIs in (near) real time, fed directly from LinkedIn Insights. Build/edit it in Sprinklr's reporting module (see [[reporting]] and [[engagement-dashboards]]).
- Use it to: track KPIs live, demonstrate campaign value to clients/executives, and show results in an accessible visual format.
- Organized around three reporting categories:
  - **Account Insights** — measures brand presence: reach, engagement, conversions, click-through rates.
  - **Post Insights** — analyzes individual post performance.
  - **Audience Understanding** — examines demographics (age, gender, location, interests, etc.).

### LinkedIn Company Page Insights
- Reports available specifically for LinkedIn **Company Page** accounts.
- **Follower metrics:** total members following the Page, broken down by employee vs non-employee, and by organic vs paid acquisition.
- **Page view metrics:** views by page section — All Pages, Careers, Jobs, Life At, and Overview pages. Mobile-specific views tracked separately for Jobs, Life At, and Overview pages.
- **Engagement metrics (status updates):** organic impressions, unique impressions, clicks, comments, likes, shares.
- **Career page interactions:** banner promotion clicks, employee-section clicks, job-section clicks.
- **Dimensional breakdowns** available on supported metrics: Company Size, Country (top 100), Function, Industry, Region, Seniority. Targeted-post dimensions: geography, industry, function, seniority.

### LinkedIn Profile Insights
- Reports for LinkedIn **Profile** accounts (used for market research, demographics, and targeted-campaign planning).
- **Account Insights:**
  - **LinkedIn Profile Followers** — number of followers of the profile.
  - **LinkedIn Profile Connections** — connection count; available only for **Distributed**-type accounts.
- **Post Insights (per-post measures):**
  - **Impressions** — number of times a profile post is viewed.
  - **Reach** — number of unique viewers of a profile post.
  - **Likes & Reactions** — aggregate positive interactions.
  - **Aggregated Comments** — total comments across all reply levels.
  - **First Level Comments** — direct responses to the original post.
  - **Reshares** — number of times content was redistributed.
  - **Video Views** — play counts (minimum ~2-second engagement).
  - **Unique Video Views** — distinct engaged viewers.
  - **Video Watch Time** — duration, measured in milliseconds.
- Note: executive/profile visibility metrics depend on LinkedIn API release; some are pending.

### LinkedIn Dimensions
- Dimensions you can slice LinkedIn metrics by (use these as group-by / breakout fields in widgets):
  - **LinkedIn Country** — country name; applies only to metrics that provide country-specific insights.
  - **LinkedIn Seniority** — experience level of followers (Unpaid -> ... -> CXO, Partner, Owner).
  - **LinkedIn Industry** — industry your followers work in.
  - **LinkedIn Function** — job function of followers (e.g. Marketing, Sales, Engineering, HR).
  - **LinkedIn Region** — region associated with the follower's profile.
  - **LinkedIn Company Size** — employee-count bands (coded B-I, from 1-10 up to 10,000+).
- **Event dimensions** (for LinkedIn Events): Event Title, Event Description, Event Start Date/Time, Event End Date/Time, Event Type (VIRTUAL or IN_PERSON), Event Organizer, External Event Link.

### LinkedIn Data Sync Frequency
- How often Sprinklr refreshes LinkedIn data from the API:

| Level | What | Sync frequency | Window |
|-------|------|----------------|--------|
| Account | Account/Page metrics | Once daily | While the LinkedIn account and linked page stay active |
| Post | Posts aged 0-10 days | Every 4 hours | First 10 days after publish |
| Post | Posts aged 11-60 days | Once daily | Days 11-60 |
| Stories | Story metrics | Every 4 hours | ~24-hour story lifespan |

- Practical takeaway: brand-new posts update fast (every 4h) for the first 10 days, then slow to daily until day 60; after 60 days posts are no longer routinely re-synced (see backfill below).

### Historical Backfill — Capabilities & Limitations
- **Backfill** = updating data for posts published before the account was added to Sprinklr, or older than 60 days.
- **Default window:** a 60-day backfill range activates automatically when an account is added.
- **Account-level data:** not available for backfill.
- **Post-level:** trend metrics cannot be backfilled; only posts published within the **last 6 months** are eligible.
- **By message type** (defaults are configurable for "posts" types unless noted):

| Message type | Default backfill depth | Edit sync | Delete sync |
|--------------|------------------------|-----------|-------------|
| Company Status Updates | 5,000 posts (configurable) | No | No |
| Company Status Comments | comments from 1,000 most recent posts | Yes | Yes |
| Company Status Replies | replies from 1,000 latest comments | Yes | Yes |
| Company Status Mentions | Not available (API limit) | Yes | No |
| Company Status Shares | Not available (API limit) | Yes | No |
| Company Private Messages | last 500 conversations x 500 messages each | Yes | Yes |
| Profile Network Updates | 5,000 posts (configurable) | No | No |
| Profile Comments | 1,000 posts | No | No |
| Profile Replies | 1,000 comments | No | No |

## Common issues & fixes
- **"Old post metrics aren't updating."** Posts older than 60 days are not routinely re-synced; days 11-60 sync only once daily. Use backfill (within the 6-month eligibility window) rather than expecting live refresh.
- **"Mentions/Shares aren't backfilling."** Company Status Mentions and Shares cannot be backfilled — LinkedIn API constraint, not a config error.
- **"Account-level history is missing."** Account-level data has no backfill; only forward-looking daily syncs from when the account was added.
- **"Profile Connections metric is empty."** It only populates for **Distributed**-type profile accounts.
- **"Numbers lag behind LinkedIn native."** Expected — account metrics sync once daily; reconcile against the sync schedule above before raising a data-discrepancy ticket.

## Notes & gaps
- **Prerequisites/permissions:** the LinkedIn account (Company Page or Profile) must be added/authenticated in Sprinklr via [[asset-manager]] / account management, and stay active for account-level data to keep flowing. Reporting access depends on the user's role/permissions in [[reporting]].
- All sync and backfill limits are imposed by the LinkedIn API; some metrics (e.g. certain executive/profile visibility data) are pending LinkedIn API release.
- **Gaps in source articles:** the Standard Reporting Dashboard article gives categories/benefits but no step-by-step build instructions, widget names, or required permissions; none of the six articles contain UI screenshots (pages carry only marketing/spotlight imagery), so exact button labels and menu paths for building the dashboard are not documented here — confirm in-product. Story backfill specifics and exact configurable maximums for the "5,000 post" defaults are unspecified.

## Sources
- Standard Reporting Dashboard - LinkedIn — https://www.sprinklr.com/help/articles/report-on-linkedin-activities/standard-reporting-dashboard-linkedin/6454a114f65d86626c82b909
- LinkedIn Company Page Insights — https://www.sprinklr.com/help/articles/report-on-linkedin-activities/linkedin-company-page-insights/6406c53932d12b63c5f57287
- LinkedIn Profile Insights — https://www.sprinklr.com/help/articles/report-on-linkedin-activities/linkedin-profile-insights/6406c37332d12b63c5f57286
- LinkedIn Dimensions — https://www.sprinklr.com/help/articles/report-on-linkedin-activities/linkedin-dimensions/6406c66b7a695d65a1606e72
- LinkedIn Data Sync Frequency — https://www.sprinklr.com/help/articles/report-on-linkedin-activities/linkedin-data-sync-frequency/6406c8807a695d65a1606e73
- Historical Backfill Capabilities and Limitations — https://www.sprinklr.com/help/articles/report-on-linkedin-activities/historical-backfill-capabilities-and-limitations/6406c90c32d12b63c5f57288

Related: [[reporting]] - [[engagement-dashboards]] - [[publishing]] - [[asset-manager]] - [[rule-engine]]
