# Knowledge Base — CSV import & HTML export

Source: https://www.sprinklr.com/help/articles/import-and-export/import-external-content-to-sprinklr-knowledge-base-csv-import/66d961994fd1f856894fc0bd
Verified against a real QRail export (Sep 2026).

## Import CSV — columns

Order below matches Sprinklr's own `Article_Import_Template_CSV` template.

| Column | Mandatory | Notes |
|---|---|---|
| `Export Import Id` | yes | Unique per row. Doubles as the handle other rows point at. |
| `Folder Id` | yes | The category. Take it from the KB URL of the folder, or from `Folder Id` in an export's `metadata.csv`. Null → import error. |
| `Locale` | yes | Use exactly what the environment already uses (`en`, `en_US`, `ar`, …) — an export's `metadata.csv` shows the live values. |
| `Base Article Id` | no | **How translations are linked — but it will not resolve against another row in the same file.** It must be the base article's *real Sprinklr article id* (24-hex, as seen in an export's `metadata.csv`). Pointing it at an `Export Import Id` from the same upload fails with _"Base Article Id is invalid. Base content cannot be null."_ — even when that base row imports successfully in the same batch. **So a bilingual load is two passes:** import the base language first, re-export the folder to read the new article ids from `metadata.csv`, then import the translations keyed on those ids. |
| `Title` | yes | |
| ~~`Country`~~ | **do not send** | The help article lists it and the official template ships it, but the importer **rejects the file**: _"I couldn't process your Articles import request because Country column is not supported. Remove and retry."_ (QRail env, Sep 2026). Omit the column entirely — a blank one still fails. |
| `Content` | yes | **Plain text or HTML.** Media must be public URLs — images get pulled to the Sprinklr CDN at import. SVG unsupported. |
| `Status` | yes | `Draft` / `Published`. Null → import error. Import as `Draft` when the content still needs review. |
| `Tags` | no | |
| `Migrated From`, `Migration Id` | no | Source system + original id, for traceability. |

Also documented but not in the template: `Language Setting ID` (a predefined localization config).

Send only the columns you actually populate. Unused optional columns add nothing and each one is another chance for the validator to refuse the file. A 7-column header — `Export Import Id, Folder Id, Locale, Base Article Id, Title, Content, Status` — imported cleanly.

No documented row-count or file-size limit. Write the file as **UTF-8 without a BOM** — and don't round-trip it through Excel, which mangles Arabic and re-quotes embedded HTML.

## Export side (what you get back out)

An export drops one folder containing:
- `metadata.csv` — columns `Export Import Id, Folder Name, Folder Id, Locale, Country, Base Article Id, Title, Modified On, Created On, Created By, Hierarchy`. This is the map from file → article, and the place to read real Folder Ids and Locale values.
- One HTML file per article per locale, named `SPR_KB_<exportImportId>π<title-slug>.html`. Body content sits in `<div id="spr-kb-article-content">`; the editor leaves `export-block__parent` / `doc-editor__marks__*` classes and heavy inline styles behind, which re-import fine.
- Translations appear as separate files; the non-base one carries `Base Article Id` in `metadata.csv` (its slug is often just `-`, since the Arabic title doesn't transliterate).

## Splitting a monolithic article into granular ones

Sprinklr's editor gives no structural heading markup, so a big FAQ article's question boundaries are only visible as **bold runs**. In the QRail export the same document used all of: bold `<li>` inside `<ul>`, bold `<p>`, `<h3>`, and a bold question inline with a plain-text answer in one `<p>`. A reliable rule set:
1. whole block ≤250 chars, ends with `?`/`؟`, bold ratio ≥0.6 → title, no body;
2. leading bold run ends with `?`/`؟` → title = that run, body = the rest of the same block;
3. heading tag or fully-bold short block → section title;
4. fold sub-labels (`Terms & Conditions`, `Purchase:`, `For Personal:`, table headers) and any heading whose parent article still has no body.

Watch for bold runs broken mid-sentence by a plain word — a strict "all bold" test silently loses those questions.

**Normalise images before re-importing.** The exporter wraps every image in its own asset placeholder — `<span data-type="spr-social-media-asset-photo" data-resolvable-asset="false"><img …></span>`. The importer's sanitiser throws the `<img>` away and re-emits the leftover attributes as visible text, so the picture silently vanishes. Unwrap the span and reduce the tag to a bare `<img src="…" alt="…">`; keep only public URLs (a private CRM host or a relative `/api/...` path cannot be fetched to the CDN).

**Don't auto-link translations by position.** Verify the two locales actually contain the same sections first; a partially-translated article (QRail: 460 EN vs 306 AR) will mis-pair, attaching Arabic bodies to the wrong English base article.
