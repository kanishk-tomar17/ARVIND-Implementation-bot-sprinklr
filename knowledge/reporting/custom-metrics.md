# Custom Metrics (Reporting 065)
**Source:** Product Foundation Courses → Reporting / 065 Custom Metrics (video transcript + Create Custom Metric dialog screenshot) · **Help:** search `site:sprinklr.com/help reporting custom metrics widget builder formula color coding`

## What it is
**Custom metrics** are unique measurements beyond standard metrics — built by combining API-based metrics with math operators to track exactly what matters to your business, then plotted in widgets.

## Access the Custom Metrics Widget Builder
**+** icon → **Care Reporting** (under Analyze, Sprinklr Service) → Reporting dashboard → **Settings** icon → **Custom Metrics** → **Add Custom Metric** (top-right).

## Builder fields (Create Custom Metric)
- **Name** — descriptive name.
- **Description** — brief purpose.
- **Data Source** — e.g. **Social Analytics**.
- **Metric Type** — how the value is presented: **Numeric, Percentage, Currency, Date, Time, SLA**, and more.
- **Metric** — choose from API-based metrics and **combine with math operators `+ - / *`** to build a formula.
- **Filters** — optional (Select Filter / Type / Value; Add New Filter) — e.g. case time or priority.
- **Color Coding** — assign colours to value ranges (metric start/end value → colour, e.g. red/yellow/green for CSAT) to aid interpretation in tables/widgets.
- **Create Metric**.

## Worked example — Average Case Handle Time
- **Name:** Average Case Handle Time; **Description:** average time taken to handle a case.
- **Data Source:** Social Analytics; **Metric Type:** Numeric (time in minutes).
- **Metric formula:** **Case Processing SLA ÷ Unique Processing Case Count**.
- No filters / no colour coding → **Create Metric**.

## Use the custom metric in a widget
On a dashboard, create a widget → Data Source = Social Analytics → visualization (e.g. inline) → **X-Axis** = a standard dimension (e.g. **Time of the Day**) → plot the **custom metric** (Average Case Handle Time) → **Create/Update Widget**.

## Notes / gaps
- Custom metrics plug into [[creating-widget]]; metric/dimension building blocks in [[common-metrics-dimensions]] and [[backend-structure-digital]].
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[filtering]], [[export-schedule-export]], [[backend-structure-digital]], [[common-metrics-dimensions]].
