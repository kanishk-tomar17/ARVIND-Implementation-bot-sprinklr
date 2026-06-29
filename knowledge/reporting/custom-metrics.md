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

## Counting by a combination of fields (e.g. two custom fields) — VERIFIED live (prod, 2026-06)
A "count per combination of field A × field B" is **not a custom-metric formula** — it's a **Table widget**: put the two fields as **two row dimensions** (nested) and plot **Case Count**. Each unique (A,B) pair becomes one row with its count; rows where B is empty (single-level cases) show B blank. Custom fields appear in the metric/dimension picker as **"Custom Dimension"** named `<Field> (Case)`.
- To count only cases where the field was actually filled, add a widget **Filter** on that field with operator **`exists`** — and **you MUST set the value in the next column: `True` = field has a value (drops the blank/empty rows), `False` = field is empty.** (There is no separate "is not empty" operator — `exists = True` IS the "is not empty" filter.) Verified: `exists=True` removed the empty-Ebene-1 rows and kept all populated ones.
- **Always set the `exists` value** — an `exists` filter left **without a True/False value is silently dropped on save** (this is why it "won't persist"). Set the value, then it saves in both the Edit Widget → Filters definition and the widget "Apply Filters" (Number of filters) panel.
- Filter operator dropdowns and value lists are **virtualized** (options don't render in the a11y tree): type-to-filter, then `ArrowDown`→`Enter`.

## Notes / gaps
- Custom metrics plug into [[creating-widget]]; metric/dimension building blocks in [[common-metrics-dimensions]] and [[backend-structure-digital]]; filter mechanics in [[filtering]].
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[filtering]], [[export-schedule-export]], [[backend-structure-digital]], [[common-metrics-dimensions]].
