# Outbound Voice — Ingestion / Upload Inventory Report (Reporting 083)
**Source:** Product Foundation Courses → Reporting / 083 Outbound Voice Use Cases - Ingestion Report (video transcript + Inventory Report widget screenshot) · **Help:** search `site:sprinklr.com/help upload inventory report lead count coverage record type lead event`

## What it is
The **Upload Inventory Report** — key for dialer admins to see, per uploaded file: how many records uploaded, how many called/connected, and conversion to leads.

## Sample report fields
File attributes + per-file: **Lead Count** (total uploaded), **Unique Attempted**, **Uncalled**, **Coverage** (= Unique Attempted ÷ Total Lead Count), **Churn**, **Unique Connect %**, **Unique RPC% (Right Party Contact)**, **Unique Attempted Connects**, follow-ups scheduled. Filter by **file attributes** (file name, data type, product, segment, subsegment, hub location, etc. — vary per client workflow). Tabs: Overall Inventory DB, Upload Summary - Product, Upload Summary - Subsegment, Metric Definitions.

## Key dimensions & metrics
- **File Upload Time**, **File Name** — self-explanatory.
- **Lead Event ID** — identifier per uploaded record.
- **Record Type** — a record can be a **Lead** or a **Voice Conversation**; for this report filter **Record Type = Lead**.
- **Count** — with **Record Type = Lead** filter → **Total Leads** (records uploaded; e.g. 100 customers = 100).
- **Call Attempted** / **Call Contacted** — boolean (yes/no) flags. On Count, filter:
  - Call Attempted = yes → **unique leads attempted**.
  - Call Contacted = yes → **unique leads connected**.
- **Total Attempts** — total calls made on the leads (100 records could be 200–300 calls).
- **Total Contacts** — total successful contacts.
- **Call Disposition / Disposition Plan** — filter leads by whether a particular disposition was filled.
- **File Attributes** (from the upload file: product, city, etc.) — aggregate e.g. leads uploaded per city/hub location.

## Notes / gaps
- First report in the outbound chronology ([[outbound-voice-overall]]); combines the upload file with calling data (Voice report records). Metrics built via [[custom-metrics]] + [[filtering]] on Record Type / Call Attempted / Call Contacted.
- Part of Reporting (Voice/Outbound): [[outbound-voice-overall]], [[outbound-voice-campaign-management]], [[outbound-voice-agent-performance]], [[outbound-voice-schedule-callback]].
