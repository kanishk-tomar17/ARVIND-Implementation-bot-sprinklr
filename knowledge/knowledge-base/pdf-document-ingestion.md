# Uploading PDFs / documents as knowledge

**Sources:** [FAQ+ (RAG) — Add Content Sources: Upload Documents](https://www.sprinklr.com/help/articles/setting-up-faq-bot/add-content-sources-upload-documents/665718c5b35fa9007da7248e) · [AI Agent — Add Content Sources: Documents](https://www.sprinklr.com/help/articles/knowledge-content/add-content-sources-documents/685d184820753412ba6fed21) · [Agent Copilot — Add Documents](https://www.sprinklr.com/help/articles/data-management/add-documents-for-agent-copilot/69c556e83d2bda6aa77074bb)

## The headline
**The Knowledge Base article module does not accept PDFs.** KB articles are HTML/rich-text records — the documented ingestion paths (CSV import, HTML import, External API, Zendesk connector) all carry article *markup*, not binary documents. See [[csv-import-export]].

PDFs are ingested through the **AI content-source** surfaces instead, where they're chunked and indexed for retrieval. Three separate destinations, and they are **not the same store** — uploading to one does not populate the others:

| Destination | Path | What it powers |
|---|---|---|
| **Generative AI FAQ Bot (RAG)** | Training Content → Documents → **View All** → **Add Documents** → upload → **Save** | Customer-facing FAQ+ bot answers |
| **Sprinklr AI Agent** | AI Agent dashboard → Training Content → Documents → **View All** → **Add Documents** → upload → **Save** | AI Agent responses |
| **Agent Copilot** | Agent Copilot → Data Management → Documents → **Configure** → **Add Document** → drag/Browse → **Save** | Agent-facing Copilot suggestions |

## Supported formats and limits (FAQ+ bot — the only place Sprinklr states them)
- **`pdf, txt, html, docx, xlsx, pptx, zip`**
- **25 MB per file**
- `zip` is accepted, so a batch of PDFs can go up in one upload.

The AI Agent and Agent Copilot articles don't publish their format/size lists. Agent Copilot's article names "PDFs, slide decks, and internal documentation". Treat the FAQ+ list as the working assumption elsewhere, and confirm in the tenant before committing a client to a large migration. WARNING: unverified for AI Agent / Copilot.

## Behaviour
- **Save triggers the sync with the model** — the document isn't live until sync finishes. No published refresh interval or incremental-indexing controls.
- After syncing: manage content, validate against a **Golden Test Set**, then deploy in the Conversational AI dialogue tree.
- No chunking configuration is exposed.

## If the content must live as a KB *article*
Convert first — the PDF's text becomes article HTML, imported via the KB CSV route. Two options for the original file:
- Host the PDF at a **public URL** and link to it from the article body. Sprinklr pulls images to its CDN at import, but a link stays a link; a private CRM host or a relative `/api/...` path can't be fetched.
- Keep the PDF only in the AI content source, and write a short KB article covering the same ground for agents/customers.

## Gotchas
- **Scanned PDFs are dead weight.** Retrieval needs an extractable text layer. Image-only scans index as nothing — OCR them first.
- **Three separate stores.** A client saying "the bot doesn't know this" when the PDF was loaded to Copilot is the usual cause.
- **25 MB per file** — split large handbooks rather than zipping one oversized file.
- Chunking is opaque, so a 300-page monolith retrieves worse than the same content split into topic-sized documents.
