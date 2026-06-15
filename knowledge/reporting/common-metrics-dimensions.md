# Most Common Metrics and Dimensions (Reporting 068)
**Source:** Product Foundation Courses → Reporting / 068 Most Common Metrics and Dimensions (video transcript + metric-aggregation dropdown screenshot) · **Help:** search `site:sprinklr.com/help reporting metrics dimensions aggregation glossary`

## Definitions
- **Metric** — any **measurable value** (e.g. Total Number of Calls, Call Count).
- **Dimension** — a **field that categorizes** the measurable value into segments (e.g. **Agent**, **Direction**). Plotting Call Count against Direction splits it into incoming vs outgoing.

## Metric aggregation options
When you plot a metric in a widget, you choose how to aggregate it:
**Sum, Cumulative Sum, Average, Time Aggregated Average, Min, Max, Change, Percentage, % Change, Percentile, Standard Deviation, Variance.**

## Rules & behaviours
- **At least one metric is mandatory** to build any widget (so data populates).
- **Table (No Metrics)** — a special visualization; you still plot one metric to populate data, but that metric **column won't appear** in the final table.
- Metrics can be **sorted** (ascending/descending) and have **conditional formatting**.
- **Drill-down:** on a final widget, **hover on a metric value** to drill down into the dimensions (fields) relevant to that metric.
- Each metric/dimension is **fetched from a specific data source**; an elaborate **glossary** in the Knowledge Base defines each metric, its calculation, and each dimension.

## Notes / gaps
- Aggregations apply in [[creating-widget]] and [[custom-metrics]]; data sources/records in [[backend-structure-digital]]. Standard digital + voice metrics covered in later sessions ([[volume-sla]], [[agent-performance-digital]], voice reports).
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[filtering]], [[custom-metrics]], [[export-schedule-export]], [[backend-structure-digital]].
