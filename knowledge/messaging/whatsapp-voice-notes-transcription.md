# WhatsApp Voice Notes Transcription — does the AI Agent bot get it?

**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/whatsapp-voice-notes-transcription/whatsapp-voice-notes-transcription/695f11d1f0afa271d1bf668d
**Verified:** 2026-10-27

## What it is
- Sprinklr auto-transcribes **WhatsApp voice notes to text**, surfaced **in Care Console only** — the transcript appears alongside the original voice note so a **human agent** doesn't have to listen to it.
- This is a different feature from **Voice AI Agent** (the telephony voicebot with STT/TTS for phone calls — see `ai-agent-voice` category). Voice *notes* (chat attachments) and Voice *calls* (telephony) are unrelated features in Sprinklr's docs — don't conflate them.

## Important — not confirmed for AI Agent Builder bots
- The entire article is scoped to **Care Console / human agents**. There is **no mention anywhere of an AI Agent Builder task/bot reading or acting on the transcription**.
- So: as documented, a conversational AI Agent (e.g. the Zain bot) has **no confirmed way to "hear" an inbound voice note** on WhatsApp, Instagram, or Facebook. If the customer sends a voice note, what the bot sees (ignored attachment vs. some fallback) isn't stated — this needs to be tested live in the channel, or confirmed with your Sprinklr Success Manager / a ticket.

## Channel support
- **WhatsApp only** (nothing on Instagram/Facebook in this article). Config is done **per WhatsApp phone number**.

## Configuration steps (Care Console transcription — not bot-facing)
1. Feature is gated by a **Dynamic Property (DP)** — not on by default. Ask your Success Manager, or raise a ticket at tickets@sprinklr.com to get DPs enabled for the account.
2. Launchpad (+) icon → search **"WhatsApp Business Accounts"** → find the account → **⋮ → View Numbers** → **⋮** on the specific number → **Enable Voice Note Transcription**.
3. Language modal: set a **mandatory Primary Language**, optionally add more **Possible Languages**. If you don't add any, **only the primary language gets transcribed** — it does not auto-detect everything.
4. **Save and Enable**. Once on, the same menu shows **Modify Language Preferences** / **Disable Voice Note Transcription** (toggle any time, per number).

## Common issues & fixes
- Transcription isn't guaranteed to succeed — reporting tracks a **"Voice Message Transcription Status"** dimension (`SUCCESS` / `FAILED`).
- A voice note in a language not listed under Primary/Possible Languages likely won't transcribe correctly (not stated as auto-detect).

## Notes & gaps
- No numeric audio-length/file-size limit stated.
- Reporting: Care Reporting → **Inbound Analytics** source → dimensions `Voice Message Transcription Detected Language`, `Voice Message Transcription Status`; metrics `Voice Message Transcription Audio Duration`, `...E2E Latency`, `...ML Latency`.
- Related ARVIND topics: [[channels-overview]], [[whatsapp-account-addition]], [[ai-agents]].
