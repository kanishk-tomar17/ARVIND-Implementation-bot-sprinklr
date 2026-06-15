# Community Reporting (Community 190)
**Source:** Product Foundation Courses → Community / 190 Community Reporting (video transcript + demo) · **Help:** search `site:sprinklr.com/help community reporting dashboard data source`

## What it is
The **standard Community Reporting dashboard** in Sprinklr. Top-level **filters**: **date range** (custom or predefined), **quick filters** (Account = the community being reported on, e.g. "Sprinklr Community"), **Workspace, Social Network**, plus additional filters.

## The 4 tabs
1. **Overview** — high-level community functioning: total **posts, comments, replies, likes**, content type, **most viewed posts**, activity breakdown.
2. **Content Analysis** — deep dive into content: **conversations by day/week/month**, **sentiment** of community posts (neutral/positive/negative), what users **search**, popular posts.
3. **User Analysis** — the users interacting: **new users** (daily/weekly/monthly), total users, new-user trend (last 30 days), activity trend, **DAU/MAU** (daily/monthly active users).
4. **Website Analytics** — website behaviour: **page views, unique visitors, average session duration, bounce rate, exit/landing pages**, breakdowns by **device** and **OS**.

## Key concept — data sources (important when building widgets)
The standard community dashboard uses **3 data sources**, chosen per widget (Edit Widget → Data Source):
- **Inbound Analytics** — for **content** widgets (conversations by day/month). Every community post is grabbed as an **inbound message** in Sprinklr, so content data comes from inbound analytics.
- **Universal Profile** — for **user** widgets (to fetch user details / who's interacting).
- **Community** — for **website** widgets (actions / how the site functions — e.g. average session duration).

## Notes / gaps
- Standard OOTB dashboard with 4 tabs; the **data-source choice** (Inbound Analytics / Universal Profile / Community) is the key build consideration. Mirrors the KB reporting pattern ([[reporting]] in KB).
- Completes Community: [[community-builder]], [[global-workspace-roles]], [[message-level-rules]], [[live-chat-on-community]], [[guided-workflow-on-community]], [[spam-model]], [[case-management-for-community]], [[social-sso]], [[survey-on-community]], [[support-ticket]].
