# Reporting Backend Structure — Digital (Reporting 067)
**Source:** Product Foundation Courses → Reporting / 067 Reporting Backend Structure - Digital (video transcript + record-structure Excel screenshot) · **Help:** search `site:sprinklr.com/help reporting digital data sources case SLA macro availability occupancy`

## What it is
The backend record architecture of the main digital reports — how each report stores records and what its **primary metric** is. Understanding this explains why metrics behave the way they do.

## Reports & primary metrics
| Report | Deals with | Primary metric(s) | How records are stored |
|---|---|---|---|
| **Inbound Case Report** | Case properties vs **case count**; case-level custom fields (priority, social network, sentiment, etc.) | **Case Count** | One record per case — e.g. #123 (Facebook, Priority Low) → Case Count = 1 |
| **SLA Report** | Custom + case SLA metrics to monitor service-level agreements / time requirements | **Case Response SLA**, **Count Case SLA** | Stores a record per **action** (user assignment/unassignment, queue removal, prime response). **SLA Index = 1** for the brand response to the oldest fan response; e.g. case #124 user assigned 9:10, brand response 9:25 → Case Response SLA 20 min |
| **Macro Report** | Macro/action usage by agents (close, no-response-required, custom-field actions) | **Case Macro Usage Count**, **Case Macro SLA** | Per macro record — e.g. Close macro on #123 (FB) at 9:10; **Case Macro SLA** = time between case creation and macro applied (15 min) |
| **Case Processing SLA Report** | Performance from the processing-clock records (a backend clock runs while a case is open in the 3rd pane / agent console) | **Case Processing SLA** (= handle time) | Unique counts + handling-time properties per processing session |
| **Availability Report** | Agent hygiene — status assigned/removed times | **Time in Status** (status remove − status assigned), **Time in Login Status** | On login/status select → status-assigned time captured; on removal → status-remove time captured |
| **Occupancy Report** | Agent occupancy per hour | **Time Spent in Status** | An hourly clock captures statuses — e.g. Break 2:15–3:15, clock at 2 processes to 3 → 45 min recorded in that hour |

## Notes / gaps
- These reports map to the data sources used in [[creating-widget]] (Social Analytics, Inbound Analytics); metrics surfaced in [[common-metrics-dimensions]]; live versions in [[live-reporting-digital]]. SLA/handle-time underpins [[volume-sla]] and [[agent-performance-digital]].
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[filtering]], [[custom-metrics]], [[export-schedule-export]], [[common-metrics-dimensions]].
