# Other Modules — KB, Guided Workflow, Smart Response (Reporting 073)
**Source:** Product Foundation Courses → Reporting / 073 Other Modules - KB, Guided Workflow, Smart Response (video transcript + KB reporting use-case table screenshot) · **Help:** search `site:sprinklr.com/help knowledge base reporting content count event count web analytics`

## What it is
Reporting use cases for **Knowledge Base** (and, by extension, Guided Workflow and Smart Response). KB Builder creates a content repository — **customer-facing** (self-help across digital channels) or **agent-facing** (reduces response/handle time). Reporting measures KB performance.

## KB reporting use cases & metrics
| # | Use case | Parameter | Data Source | Metrics / Dimensions |
|---|---|---|---|---|
| 1 | **Content Management** | Total content created | Social Analytics | **Content Count** |
| | | Content by creation status | Social Analytics | Content Count × **Content Status** (draft/approved/waiting/completed/closed) |
| | | Usage events | Social Analytics | **Event Count (Comprehend)** × **Event Type** (cloned/deleted/unpublished/marked helpful/not helpful/moved) |
| | | Article marked **Helpful** | Social Analytics | Content × Event Count (Comprehend) = Helpful |
| | | Article marked **Not Helpful** | Social Analytics | Content × Event Count (Comprehend) = Not Helpful |
| | | Feedback on "not helpful" articles | **Community** | Activity Object (= KB article), Community User, **Activity Reason** (feedback text), Date, Activity Count |
| 2 | **Knowledge Portal Web Analytics** | Top URLs | Community | **Community Page Title** (= article URL), **Activity Count** (page views), **Unique Visit Count**, **Session Duration** (time on page), **Bounce Rate** (filter activity = website visit) |
| | | Most searched queries | Community | **Search Query** (keyword), **Search Hits**; Activity Count = times searched, Unique User Count (filter activity type = search) |
| 3 | **User Adoption Report** | Article usage summary | Social Analytics | User × Event Type (Comprehend) × Event Count — e.g. "User Rima read 488 articles, 35 helpful, 17 not helpful" |
| 4 | **Article Recommendation Summary** | Articles recommended per inbound message | Social Analytics | Case, Inbound Message, Content, User × **Event Type = Intuition Recommended** |
| 5 | **Article Usage Summary** | Article usage per inbound message | Social Analytics | Case, Inbound Message, Content, User × Event Type/Event Count (Comprehend) |

## Notes / gaps
- KB content/builder covered in the Knowledge Base module ([[enablement]], [[reporting]] there); built via [[creating-widget]] using Social Analytics + Community data sources. Guided Workflow + Smart Response reporting follow similar event-count patterns (transcript focuses on KB).
- Part of Reporting (Digital): [[live-reporting-digital]], [[agent-performance-digital]], [[volume-sla]], [[survey-reports]], [[backend-structure-digital]].
