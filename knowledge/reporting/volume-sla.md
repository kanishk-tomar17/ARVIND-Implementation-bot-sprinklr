# Volume & SLA (Reporting 071)
**Source:** Product Foundation Courses → Reporting / 071 Volume & SLA (digital) (video transcript + date-filter discrepancy slide screenshot) · **Help:** search `site:sprinklr.com/help reporting case count unique case count response SLA date filter`

## Volume use cases
### Case Count vs Unique Case Count (most common confusion)
- **Case Count** = number of cases **created** in the selected time range.
- **Unique Case Count** = number of cases on which **activity** took place in the range — activity = brand response, queue removal, assignment change, custom-field change (and configured custom-field changes).
- **Why Unique Case Count > 1 per case:** it counts the case once per **action type recorded** (a case can have multiple brand responses, queue assignments, user assignments, etc., so it appears across multiple queues). When filtered to a single case action type, unique case count = 1 per record.

### Date/time filter discrepancy (common mistake)
Date filters are at the **widget level** and sort data by the metric/dimension in the filter.
- *Example:* Two widgets both plot **Macro vs Unique Case Macro Usage Count** but show different numbers because of different date filters:
  - Widget 1 uses **Case Creation Time** (the dashboard default) → macros applied on cases **created** in the range.
  - Widget 2 uses **Case Macro Apply Time** → macros **applied** in the range, regardless of when the case was created (could be a case from August/October).
- Choosing the right date filter is critical to avoid data discrepancies — pick per the client's use case.

## SLA metrics
- **Case Response SLA** — time between the **brand response** and the **last unresponded (first) fan message**; includes auto + agent responses; messages ordered by their time on the case. **Always** plot with **Case Action Type = Brand Response** and filter **Ignore Multiple Queues = true**.
- **Case Action SLA**, **User SLA**, **Processing SLA**, **Macro SLA**, **Case Queue SLA** — other SLA metrics for response/action/handling/queue timing.

## Notes / gaps
- Metrics derive from records in [[backend-structure-digital]]; built via [[creating-widget]] with [[filtering]] (Ignore Multiple Queues) and date filters from [[dashboard-feature-overview]].
- Part of Reporting (Digital): [[live-reporting-digital]], [[agent-performance-digital]], [[survey-reports]], [[other-modules-reporting]], [[backend-structure-digital]], [[common-metrics-dimensions]].
