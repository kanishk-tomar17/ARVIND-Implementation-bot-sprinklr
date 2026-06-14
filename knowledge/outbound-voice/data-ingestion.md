# Outbound Voice — Data Ingestion (Outbound Voice 163)
**Source:** Product Foundation Courses → Outbound Voice / 163 Data Ingestion (video transcript) · **Help:** search `site:sprinklr.com/help outbound voice data ingestion connector lead schema mapping`

## What Outbound Voice is
A channel where a business/org/political campaign **calls out** to customers/supporters/voters — to deliver a message at scale, generate leads, promote a product/service, or increase engagement (an **agent calls a customer**).
- **Use cases:** personalised communication (bill due, thank-you), relationship building (e.g. "did you make this transaction?"), **real-time feedback/insights** (product feedback), **lead generation & sales conversion**, customer support/issue resolution (callbacks, follow-ups), market research/surveys, trust-building.

## What Data Ingestion is
The process of **acquiring + integrating lead/customer data** into Sprinkler so outbound calls can be made (the **lead list** to call for a campaign).
- **Steps:** identify data source → data collection → **validation & cleansing** (errors, duplicates, inconsistencies; can use rules) → formatting → integration → **segmentation & filtering** (a subset per campaign).
- **Why it matters:** ensures **data quality/accuracy** — validating, cleansing, standardising; removing duplicates, correcting errors, standardising formats → data integrity.

## Connectors (data sources)
Sprinkler supports multiple ingestion sources — **API**, **CSV/Excel file upload**, and **CRM** (e.g. Salesforce). *(The detailed connector-type walkthrough at ~6:00–12:40 of the video wasn't fully captured in the transcript scrape — confirm the per-connector setup on the KB if needed.)*

## File-upload connector — schema & profile mapping
1. Fill the connector info → **Next** → **Schema mapping**:
   - Column 1 = the **file's column header**; Column 2 = the **Sprinkler attribute** it maps to (selecting an existing attribute updates that lead attribute).
   - Set **character limits**; add **validations** (e.g. valid email/phone; admins can create **custom validations**). An attribute that exceeds the limit or fails validation lands **empty** in the lead.
   - Mark attributes **mandatory** → a missing mandatory field **fails** record creation.
   - If a lead with the **unique identifier already exists** → it's **updated**; otherwise a **new lead** is created.
2. **Next → Profile mapping:** map lead attributes to **customer profile fields**; map identifier columns to the **User ID** field. Existing profile → updated; else a **new profile** is created.
3. **Save** → the file-upload data connector is created.

## Managing connectors (Data Collection screen)
Lists **active/inactive** connectors. **Three dots → View Details** → uploaded files (file name, timestamp, total records).
- **Records created / updated / unchanged** counts per upload.
- **Successful file URL** (download created leads) and **Failed file URL** (download failed records + **reasons** → fix the source attributes → re-upload).
- Top options: **refresh**, **sort** (chrono/reverse), **export activity** by time range.
- **Edit connector** — upload another file with the same/additional attributes (reuse the connector instead of recreating).
- **Uninstall connector** — confirmation prompt → removed from all connector screens.

## Notes / gaps
- The unique-identifier rule (update vs create) governs whether re-uploads dedupe or duplicate — get the identifier mapping right.
- Failed-file URL + reasons is the debugging path for ingestion errors.
- Connector-type specifics (API/CRM) are a transcript gap — first Outbound Voice topic; feeds [[campaign-creation]].
