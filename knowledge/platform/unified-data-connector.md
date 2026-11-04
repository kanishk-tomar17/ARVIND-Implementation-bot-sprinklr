# Unified Data Connector (UDC) — overview

**Sources:** [What is Unified Data Connector](https://www.sprinklr.com/help/articles/what-is-unified-data-connector/what-is-unified-data-connector/67924290aac7641fe720dbdd) · [Supported Entity Types](https://www.sprinklr.com/help/articles/supported-entity-types/supported-entity-types/67924671aa528e2b338c4a02) · [Integration Types](https://www.sprinklr.com/help/articles/integration-types/integration-types/67925047aa528e2b338c51bf) · [Configuring a UDC](https://www.sprinklr.com/help/articles/configuring-a-unified-data-connector/configuring-a-unified-data-connector/67924595b8b98177d0431c59)

For the hands-on voice/call-recording import flow (verified live), see [[unified-data-connector-voice-import]].

## What it is
The platform-level pipe for moving data **into and out of** Sprinklr from external systems — files, cloud storage, SFTP, SQL, and a few vendor connectors. Replaces one-off custom integrations for bulk/migration work. Free platform feature, but **access must be switched on by the Success Manager**.

## Navigation & permissions
- Launchpad → **"Migrate Your Data From/To Sprinklr"** → Unified Data Connector (`/care/data-connector/import`).
- Record page lists all connectors; filter by Status, Name, Entity, Source, Last Synced On, Added On, Modified Time, Modified By.
- **+ Install Connector** creates one. Row → **⋮ More Actions** → Edit / Delete / **Run** / **View Activity**.
- Permissions: View, View Audit Logs, Create, Edit, Delete.

## Wizard — 6 steps
Entity Selection → Entity Specific Settings → Source Selection → Source Specific Settings → **Mapping Configuration** → Additional Settings.

## Entity types and which connectors they support

| Entity type | Supported connectors |
|---|---|
| Standard entities | SFTP, S3, GCS, Azure Blob, File Upload, SQL |
| Custom entities | SFTP, S3, GCS, Azure Blob, File Upload, SQL |
| Live Chat Cases (system) | SFTP, S3, GCS, Azure Blob, File Upload, Zendesk |
| Voice Cases (system) | SFTP, S3, GCS, Azure Blob, File Upload, Zendesk (ticket data only), Genesys |
| Email Cases (system) | SFTP, S3, GCS, Azure Blob, File Upload, Zendesk, Freshdesk |
| Source Agnostic Cases (system) | SFTP, S3, GCS, Azure Blob, File Upload, Zendesk, Freshdesk |

**Cases are the only system entity supported.** SQL is available for standard/custom entities only — not for system Case entities.

## Connection types (each has its own setup article)
File Upload · SFTP · Amazon S3 (incl. IAM-role auth) · Google Cloud Storage · Azure Blob · SQL · Zendesk · Genesys (voice). File-based connectors support **encryption** (PGP/GPG — runtime upload accepts ZIP, PGP, GZ, GPG).

## Integration types (write behaviour) — pick deliberately
| Type | What it does |
|---|---|
| **Insert** | Adds new records; silently ignores rows whose unique id already exists. |
| **Upsert** | Updates if the id exists, inserts if not. The usual safe default. |
| **Update** | Only modifies existing records; never creates. |
| **Sync** | Makes destination exactly match source — **deletes destination records absent from the source file.** Destructive; never point it at a partial file. |
| **Patch** | Only touches columns present in the file/query; unmapped columns are left alone. |
| **Insert or Patch** | Patches existing, inserts new. |

## Mapping Configuration
Source header → destination field, with a per-row **Mandatory** toggle, auto-filled **Sample Value**, and optional **Validation Rule**. The destination picker is grouped and searchable (Mandatory Case Fields, Non-Mandatory, Profile Standard, Case Custom, Profile Custom). A counter shows Total / Mapped / Unmapped. Entity-specific mapping screens exist for **Email**, **Live Chat**, and **Standard/Custom Entities**.

The sample file uploaded at step 4 only derives the headers — the real data goes in via **Run**.

## Export side
**Data Connector Export Module** pushes Sprinklr data out to the same destination types (e.g. exporting voice recordings). Same connector record page, export direction.

## Monitoring
**View Activity** / Data Connector Activity Log — per-run and per-file: records created/updated, plus downloadable success and failure files with per-row reasons. Always read the failure file rather than guessing why a load short-landed.

## Also runnable from Record Manager
A connector can be triggered from **Record Manager** against a selected record set, not only from the connector page.

## Knowledge Base articles through UDC — unverified
The **documented** system entities in UDC are **Cases only** (Live Chat / Voice / Email / Source-Agnostic). Knowledge Base articles are **not listed** as a UDC system entity.

Sprinklr's documented KB ingestion paths are separate from UDC:
- **KB CSV import** (`Export Import Id / Folder Id / Locale / Base Article Id / Title / Content / Status`) — see [[csv-import-export]]
- **KB HTML import**
- **Article Ingestion through External API**
- **Zendesk connector for External Content Management**

Whether "Knowledge Base Article" appears in UDC's **Entity** picker as a *standard* entity has **not been verified in a live tenant** — the picker is searchable, so check it there before promising a client a UDC-based KB migration. WARNING: open question.

If it is available, it behaves like any standard entity: file-based source (CSV/XLS/XLSX), one row per article, a mandatory **Entity ID** as the unique dedupe key, and **source header -> destination field** mapping. Source header names are arbitrary - they only need to be mappable.

## Gotchas
- Sample file at step 4 is capped at **10 MB**; the runtime upload advertises no cap.
- **Sync** is the only integration type that deletes. Treat it as a production-changing action.
- Success Manager enablement is a real gate — if the launchpad entry is missing, that's why.
- File-based connectors are case-sensitive on file names/extensions (see the voice-import notes).
