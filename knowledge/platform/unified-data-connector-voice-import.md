# Unified Data Connector — Importing Call Recordings (Voice Cases)

**Source:** VERIFIED live on `space-prod3.sprinklr.com` (Qatar Rail dev), 2026-08-16, by stepping through the existing **"Case maker"** connector in edit mode · **Help:** [Configuring a Unified Data Connector](https://www.sprinklr.com/help/articles/configuring-a-unified-data-connector/configuring-a-unified-data-connector/67924595b8b98177d0431c59) · [Voice Cases Single Case Format](https://www.sprinklr.com/help/articles/supported-format-for-file-based-connectors/support-for-import-of-voice-cases-using-single-case-format/65bcfb8f0d89816c5711e654)

> ⚠️ **The help center is wrong in places.** Live UI contradicts the docs on metadata file types and on which fields are mandatory. Trust this file (verified) over the articles.

## What it is
Bulk-import historical call recordings into Sprinklr as **Voice Cases**, so they get transcribed and become available to Quality Management / reporting. Audio + a metadata file are zipped and fed through a Data Connector.

## Navigation
Launchpad → search **"Unified Data Connector"** → lands on `/care/data-connector/import` → **+ Install Connector** (top right).

The wizard has **6 steps**: Entity Selection → Entity Specific Settings → Source Selection → Source Specific Settings → Mapping Configuration → Additional Settings.

## Configuration (verified values)

| Step | Field | Value / options |
|---|---|---|
| 1. Entity Selection | Entity* | `Case` |
| 2. Entity Specific Settings | Account Type* | `Sprinklr Voice` (locked once set) |
| | Account* | the voice account, e.g. `Qatar Rail Test Number` |
| | **Default Language*** | **connector-level, NOT per row** — see gotcha below |
| | Disable Transcription | toggle; OFF = transcription runs |
| 3. Source Selection | Entity Source* | `File Upload` (also S3 / GCS / SFTP / Azure Blob) |
| | Connector Name* | free text |
| | Description | optional |
| 4. Source Specific Settings | Upload Sample File | zip/gz, **max 10 MB** — used only to derive headers |
| | Source File Format* | `Single-Case` \| `Multi-Case` |
| | Metadata File Type* | **`CSV` \| `XLS` \| `XLSX`** ← docs wrongly claim XML/JSON |
| | Recording File Type* | `wav` (also aac, mp3, wma, ogg, opus, m4a, mp4) |
| | Advanced → Is Data Encrypted | toggle |
| 5. Mapping Configuration | header → destination field | see below |
| 6. Additional Settings | sharing / notifications | — |

### Single-Case vs Multi-Case
- **Single-Case** — one zip per call: 1 metadata file + 1 audio file. Metadata has exactly 2 rows (header + one value row).
- **Multi-Case** — one zip for many calls: 1 multi-row metadata file + many audio files. Fewer uploads, but the zip gets large fast.

### Mapping Configuration — the real field list
The destination picker is a **grouped, searchable** menu:
- **Mandatory Case Fields** — only **two** exist, and both must be mapped:
  - **`Unique Call Id`** (Text) — the dedupe key
  - **`Call Recording File Name`** (Text) — points at the audio file in the zip
- Non Mandatory Case Fields (5) · Profile Standard Fields (4) · **Case Custom Fields (251)** · Profile Custom Fields (37)

Each mapping row also offers a **Mandatory** toggle, a **Sample Value** (auto-filled from the sample zip) and an optional **Validation Rule**. **+ Add Field** adds a row. A counter shows Total / Mapped / Unmapped.

**Qatar Rail CRM tagging:** the field to use is **`CRM_Case Number`** (Text, Case Custom Field) — searching `case number` returns exactly one match. Do **not** search just `crm`: that returns **69** fields including **two both named literally "CRM Case"**, most of them Single Select List (picklists that reject free text).

## Running the import (File Upload connectors)
The connector wizard only *defines* the connector. To actually load data: connector row → **⋮ More Actions** → **Edit / Delete / Run / View Activity**.

- **Run** opens a **"Runtime Connector Details"** dialog with an **Upload File(s)** box — this is where the real data zips go. It accepts **ZIP, PGP, GZ, GPG** and, unlike the wizard's sample box, states **no size limit**. Plural "File(s)" — multiple zips per run.
- **View Activity** is the per-file log (records created/updated, success + failure file URLs with reasons).

## Common issues & fixes

- **Mixed-language batches get mis-transcribed.** Default Language is set **per connector**, and there is **no language column in the mapping**. A batch of English + Arabic calls pushed through one Arabic connector transcribes the English calls as Arabic. **Fix: one connector per language.**
- **Stereo channel reversal.** Telephony WAVs are 2-channel (one side agent, one customer). Sprinklr's expected convention can be the opposite of the source recorder's, which silently swaps speaker labels in transcripts and poisons QA scoring. There is **no setting in the connector for this** (checked Entity Specific + Source Specific Settings). Fix on the file side before zipping — see [[voice-recording-channel-swap]].
- **Extension case matters.** `Recording File Type` is lowercase `wav`. Source recordings often arrive as uppercase `.WAV` — rename to lowercase when staging the zip, don't assume the platform is case-insensitive.
- **`File` column must carry the full file name including extension** (`en1.wav`, not `en1`) and must match a real member of the zip exactly. Worth asserting this in the packaging script rather than eyeballing it.
- **Sample file 10 MB cap.** Build a cut-down sample zip (metadata + one short call) just to get through step 4; the real data upload is separate.
- **Large batches.** Multi-Case zips of full-length 8 kHz stereo WAV run ~7 MB/minute of audio. 51 calls ≈ 345 MB. Split into batches, or re-encode to a supported compressed codec (mp3/opus).
- **UI appears frozen / buttons do nothing.** In an embedded browser, a blocking **"Microphone permissions required"** modal swallows clicks, and `getUserInboxNotifications` can spin and trigger HTTP 429s. Dismiss the modal and hard-reload.

## Notes / gaps
- The runtime upload box advertises no size cap, but a real ceiling may still exist server-side — a ~178 MB Multi-Case zip has not yet been confirmed to complete end to end.
- Automation limit: the in-app Browser pane has **no file-upload tool**, so connector creation can't be fully driven from it.
