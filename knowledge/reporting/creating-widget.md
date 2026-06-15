# Creation of a Widget (Reporting 063)
**Source:** Product Foundation Courses → Reporting / 063 Creation of a Widget (video transcript + Custom Widget builder screenshot) · **Help:** search `site:sprinklr.com/help reporting create widget data source visualization metric dimension`

## What it is
How to create a reporting widget — from the pre-built library or a fully custom widget — and what each builder option means.

## Add a widget
Click **Add Widget** → two options:
- **Widget Library** — pre-configured widgets; pick one that fits and add directly, or customize further.
- **Create Custom Widget** — build from scratch.

## Custom widget builder
1. **Widget Name** (e.g. "Test Widget") + **Description** (e.g. "Social Network vs Case Count"). Optionally upload a **video tutorial** explaining the widget.
2. **Data Source** — what you plot against. Key sources:
   - **Social Analytics** — channel data + **case**-related info (covers most use cases).
   - **Inbound Analytics** — **message-level** details.
   - These two cover ~90% of use cases; others used as needed.
3. **Visualization** — choose chart type (Bar, stacked bar, table, etc.).
4. **What to plot (Metric / Dimension):**
   - **X-Axis** — a **metric** (e.g. **Case Count**) with an aggregation: **Sum, Average, Min, Max, Change, % Change, Percentile, Variance**.
   - **Y-Axis** — a **dimension** (e.g. **Social Network** = channel).
   - *Example:* Case Count (Sum) by Social Network = cases received per channel in the dashboard's time range. Or Case Processing SLA (= **case handle time**) plotted as Min / Max / top-5 percentile across channels.
5. **Configuration:** Label Axis, **Include Data Labels** (show numbers without hovering), Hide Legend, Start Y-Axis from Zero, Auto Refresh, Define Y/X-Axis Scale, Enable Threshold. Axes can be **renamed** (e.g. Case Count → "Tickets", Social Network → "Channel").
6. **Advanced Options** — apply **filters** (Select Filter / Type / Value, Add New Filter), additional properties, personalised targets.

## Notes / gaps
- Data sources/metrics detailed in [[backend-structure-digital]] and [[common-metrics-dimensions]]; custom metrics in [[custom-metrics]]; widget/dashboard filtering in [[filtering]].
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[filtering]], [[custom-metrics]], [[export-schedule-export]], [[backend-structure-digital]], [[common-metrics-dimensions]].
