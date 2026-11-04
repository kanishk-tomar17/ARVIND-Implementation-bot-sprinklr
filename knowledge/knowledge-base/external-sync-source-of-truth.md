# Keeping Sprinklr KB in sync with an external source of truth (SharePoint, CMS, etc.)

**Sources:** [Article Ingestion through External API](https://www.sprinklr.com/help/articles/import-and-export/article-ingestion-through-external-api/69dfa62e7a9df23df080f16d) · [SharePoint & Sprinklr DAM Integration](https://www.sprinklr.com/help/articles/integration-guides/sharepoint-and-sprinklr-dam-integration/67812b50c1294a49e14186bf) · [Import/Migrate your CMS data](https://www.sprinklr.com/help/articles/migrate-existing-content/importmigrate-your-cms-data-to-sprinklr-knowledge-base/63d518522c015d03d4e7fed8) · [Zendesk Connector for External Content Management](https://www.sprinklr.com/help/articles/import-and-export/configure-zendesk-connector-for-external-content-management/6862406d6862622c540eb0d2) · [AI Agent — Website URL content sources](https://www.sprinklr.com/help/articles/knowledge-content/add-content-sources-website-urls/69720226c836550ff8592b9c)

## The answer
**Ongoing sync is possible, but there is no out-of-the-box SharePoint→Sprinklr KB connector.** The only *productised* external-content connector for KB is **Zendesk**. Everything else is built on **Article Ingestion through External API**.

## The supported architecture (External API ingestion)
Documented flow — an event-driven pipeline, not a file import:

**Custom Entity → Entity Triggers → Groovy script → KB article create/update**

- Auth via **`Endpoint ID`** + **`Credentials ID`** passed to the **`HTTP_UTILS`** utility function in the Groovy script.
- The external API returns **KB article IDs and related metadata**; the script **creates or updates** the Sprinklr article (**upsert is supported**).
- **Scheduling is built in** — "define when and how often the connector runs". This is what makes it *continuous sync* rather than a migration.

### What it does NOT do
- **No documented delete.** An article removed from the source will **not** disappear from Sprinklr on its own. Handle it in the script (flip `Status` to unpublished/archived on a tombstone flag) or it silently rots. This is the single biggest gap.
- No published rate limits, no published payload schema — both are customer-specific and need confirming during build.

## Why the SharePoint integration doesn't solve this
The shipped **SharePoint ↔ Sprinklr** integration is **DAM only**:
- Scope: documents, presentations, Excel, images, video into **Asset Manager** — **Knowledge Base is out of scope.**
- **One-time manual** uploads, user-initiated. No scheduled or continuous sync.
- **Unidirectional** SharePoint → Sprinklr, Microsoft-account auth ("Authenticate" → SharePoint login).
- Marketing-attached files are **referenced by link**, not migrated.

So it's useful for hosting the *files*, useless as the article sync mechanism.

## Why website-URL crawling doesn't solve it either
AI Agent supports **Website URL** content sources (Knowledge Content → **Add Website URLs** → **Add Sources** → **Save**), but:
- **No documented re-crawl or refresh schedule** — treat it as a point-in-time sync, not live.
- **No documented authentication support** for gated sites. SharePoint is auth-gated, so a crawler generally can't reach it.
- No documented sitemap support or URL/content limits.
- It feeds the **AI Agent store**, not KB articles. See [[pdf-document-ingestion]].

## Design decisions to force early on a SharePoint-as-truth build
1. **One-way, and make Sprinklr read-only by policy.** If authors can edit in Sprinklr too, the next sync overwrites them and the client loses trust in the whole thing. Agree this in writing.
2. **Stable unique key.** Map the SharePoint item id → the Sprinklr dedupe key (`Export Import Id` on CSV, Entity ID on the API path). Never key on title.
3. **Change detection.** Use the SharePoint `Modified` timestamp or a Graph **delta query** so each run only pushes what changed. Full re-push every cycle is slow and churns article version history.
4. **Format conversion is on you.** SharePoint holds PDF/DOCX; KB articles need HTML. The pipeline must convert, and PDFs need a real text layer.
5. **Deletion policy.** Decide up front: unpublish, archive, or leave stale. There is no automatic path.
6. **Translations.** `Base Article Id` only resolves against a real 24-hex Sprinklr article id, so multilingual sync is inherently two-phase. See [[csv-import-export]].

## Cheaper fallback if the client won't fund the API build
Scheduled **CSV import** on a cadence (nightly/weekly) driven by an external job that reads SharePoint and emits the KB import CSV. Loses near-real-time and still has no delete, but it is far less build and uses a fully documented import path.

## Gotchas
- "Always in sync" usually means *scheduled*, not real-time. Set that expectation before scoping.
- Sprinklr KB and the AI Agent/FAQ+ content stores are **separate** — syncing SharePoint into KB does not feed the bot unless you also enable **Sync from Knowledge Base** as a bot content source.
