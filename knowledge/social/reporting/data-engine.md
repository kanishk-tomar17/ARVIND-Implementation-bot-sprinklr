# Data Engine (Data Flow) (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- The Data Engine merges data from multiple sources into a **pipeline** that transforms the combined data into a single report.
- Lets organizations capture and consolidate all the data streaming into their business, then turn it into one unified report.
- Accessed in Sprinklr Social via the **Data Pipeline** section, managed through a centralized **Pipeline manager**.
- Two pipeline types: **Normal Pipelines** (standard consolidation) and **Live Dataset Pipelines** (real-time processing).
- A pipeline is built by: adding one or more data sources, then applying transformations (create/remove columns, joins, group by, execution-time snapshots) to produce the final report. See [[reporting]] and [[engagement-dashboards]].

## Key features & how to use

### About the Data Engine (Pipeline manager)
- Open via the **Data Pipeline** section in Sprinklr Social.
- Pipeline manager supports: **create, view, edit, deactivate, clone, share, delete** pipelines.
- **Run History** tracks: the user who initiated the pipeline, source files, execution status, date, record counts, and output files.
- Record limits:
  - **Normal Pipelines** — default **150,000** records, extendable to **500,000**.
  - **Live Dataset Pipelines** — default **5,000–10,000** records.
  - Limit increases require coordination with your Success Manager / support team.

### Data sources in the Data Engine
Three categories of data source:
- **From File** — Excel and CSV files. Can be auto-refreshed via an **FTP connection**; otherwise a manual upload is required each time the pipeline runs.
- **From Sprinklr** — internal Sprinklr data: Social Analytics (owned), Listening (earned), Paid, Inbound Analytics, Benchmarking, etc. Supports automatic data **refresh frequency** configuration. Now exposes **all** data sources the user has permission to access (previously a limited preset).
- **Generic Source** — external sources such as Facebook Leads and third-party APIs. Supports automatic data refresh frequency.

### Select Widget — add metrics/dimensions in a source
- Navigate: **+ New Page > Platform Modules > Manage Pipelines** (under "Listen to Data from other Internal Systems").
- Click **Create Normal Pipelines**.
- Click **+ Add Data Source** and choose **From Sprinklr**.
- Complete the **Add Data Source from Sprinklr** form:
  - **Data Source Name** — meaningful identifier for the source.
  - **Data Source** — selection from available options.
  - **Columns** — choose metrics and dimensions, including column labels.
  - **Time Zone** — location-based selection.
  - **Time Range** — date-range filter.
  - **Date Filters** — customize data filters.
  - **Advanced Filters** — add additional conditions.
- Click **Save**.
- **Import from Widget** — alternative that auto-imports metrics and dimensions from a selected widget. Applies **only to table widgets**. When importing, the selected **time range and time zone do NOT transfer** to the pipeline data source.
- Prerequisite: user must have **Data Engine** permission.

### Create / remove columns in a pipeline
- Purpose of columns: (1) calculate new metrics across unified data sources; (2) define data structure — column name, data type (string, integer, date), length constraints, default values, required flag; (3) ensure data is correctly transformed/mapped through the pipeline.
- Requires at least one data source already configured.
- **Create a column:** click the **Addition (+) icon** > **Create Column(s)** > choose a **simple formula** or **conditional formula**.
- **Remove a column:** click the **Addition (+) icon** > **Remove Column(s)**.

### Group By in the pipeline
- Use when joining data sources: organize data by specific columns and aggregate values in others to achieve the desired join result.
- Steps: with at least one data source added, click the **Addition (+) icon** > **GROUP BY**, configure aggregation functions per column data type, apply.
- Aggregation functions for **numerical** columns: **AVG**, **COUNT**, **MAX**, **MIN**, **SUM**, **ROUND** (round to a specified precision).
- Aggregation function for **character/text** columns: **CONCAT** (join two or more text strings into one).

### Joins in a pipeline
- Joining combines data from two datasets on a common field (or set of fields). Ensure the common field has the **same data type and format** in both datasets, with no duplicates.
- Join types:
  - **Outer Join** — keeps only the unique columns from each side; excludes unwanted columns from both tables.
  - **Inner Join** — keeps matching columns only from both tables.
  - **Left Join** — preserves all columns in the left table; filters the right table's columns.
  - **Right Join** — keeps all columns from the right table; excludes unwanted columns from the left.
  - **Left Anti Join** — returns all rows from the left table that have **no** matching row in the right table.
- Always review the joined data to confirm the merge succeeded and the result makes sense.

### Set execution time for pipelines
- Captures **snapshot values for metrics at specific execution intervals** so you can track how a metric evolves over time.
- Steps: open an existing pipeline with a **From Sprinklr** data source > **Edit** > **Vertical Ellipses** > **Edit** on the final Sprinklr Report > toggle **Unique Pipeline Execution Time** to stamp each record with a unique timestamp.
- A toggle adds execution-frequency options: **End of Day (EOD), hourly, or weekly**. Frequency selection is **mandatory** once enabled.
- Each run stamps records with the execution timestamp for its window; new records **append** to the existing report rather than overwrite, preserving historical data.
- Reporting: **"Records by execution time"** lets you view metric snapshots per interval and aggregate metrics such as open/closed cases and closure rates.

## Common issues & fixes
- **Pipeline execution paused:** if records cross **30,000** in any single execution (execution-time pipelines), the pipeline execution is paused.
- **Record-limit ceilings:** Normal Pipelines cap at 150,000 (extendable to 500,000); Live Datasets cap at 5,000–10,000. To raise a limit, work with your Success Manager / support team.
- **From File source not refreshing:** without an FTP connection, the file must be manually re-uploaded on every pipeline run.
- **Widget import missing time settings:** Import from Widget does not carry over time range or time zone — set these manually; also only table widgets are supported.

## Notes & gaps
- Prerequisite/permission: **Data Engine** access permission is required; "From Sprinklr" sources are limited to what the user has permission to access.
- The Create/Remove Columns article does **not** specify formula syntax, exact field-naming conventions, supported expressions, or operational limits beyond the data-type list.
- The Joins article does **not** give step-by-step click paths, key field names, or limits for configuring each join type.
- Exact refresh-frequency options for File/Sprinklr/Generic sources are not enumerated in the source articles.
- Related GROOT topics: [[reporting]], [[engagement-dashboards]], [[data-engine]], [[rule-engine]], [[care-console]].

## Sources
- About the Data Engine — https://www.sprinklr.com/help/articles/data-flow/about-the-data-engine/63f84bfc9b334f7283b4dc8d
- Data Sources in the Data Engine — https://www.sprinklr.com/help/articles/data-flow/data-sources-in-the-data-engine/63f850b59b334f7283b4dc91
- Data Engine: Select Widget to add metrics/dimension in source — https://www.sprinklr.com/help/articles/data-flow/data-engine-select-widget-to-add-metrics-dimension-in-source/67e53868906b9016978adaf6
- Create / Remove Columns in a Pipeline — https://www.sprinklr.com/help/articles/data-flow/create-remove-columns-in-a-pipeline/63f84d80e02459133724b0c9
- Group By in the Pipeline — https://www.sprinklr.com/help/articles/data-flow/group-by-in-the-pipeline/63f84fad9b334f7283b4dc90
- Joins in a Pipeline — https://www.sprinklr.com/help/articles/data-flow/joins-in-a-pipeline/63f84ec49b334f7283b4dc8f
- Ability to Set Execution Time for Pipelines — https://www.sprinklr.com/help/articles/data-flow/ability-to-set-execution-time-for-pipelines/67e5343fc10b2770b72c09a7
