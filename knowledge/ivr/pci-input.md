# PCI Input in IVR (IVR 151)
**Source:** Product Foundation Courses → IVR / 151 PCI input in IVR (architecture **slide captured via screenshot**; Stream transcript not yet generated) · **Help:** search `site:sprinklr.com/help PCI IVR CDE DTMF`

## What it is
Securely collecting **PCI-sensitive data** (e.g. card details) from a customer **in the IVR**, so the sensitive data **never touches Sprinklr's normal system** — it goes to an isolated **CDE** (Cardholder Data Environment). **All data in motion is over TLS 1.2 with AES-256 encryption.**

## High-level PCI architecture (Scenario 1 — customer connected through IVR, IVR taking PCI data)
Components: **Customer → Telephony provider → Sprinklr's System (Process Engine) → Sprinklr PCI Environment (CDE, with Redis Cache).**

Numbered flow:
1. **Customer calls** the number and connects to the **telephony provider**.
2. Telephony provider **patches the call to Sprinklr IVR**.
3. When **PCI data is required**, the **Sprinklr process engine sends an instruction** to the telephony provider to collect the information — **along with the webhook of the CDE** — so the telephony provider can send that data **directly to the CDE** (bypassing Sprinklr's normal system).
4. **Customer enters the PCI-sensitive data via DTMF** (Dual-Tone Multi-Frequency keypad input).
5. Telephony provider **sends the PCI data over an encrypted transport (TLS 1.2, AES-256)** and submits it to the **Sprinklr PCI Environment (CDE)**; the CDE **retains the data in memory, in the Redis cache**.

## Why it matters
PCI compliance requires sensitive cardholder data to be isolated. Routing it **direct telephony-provider → CDE** (never through the main Sprinklr platform) plus **TLS1.2/AES-256** + **in-memory Redis** storage keeps the brand PCI-compliant while still capturing the input mid-call.

## Notes / gaps
- **Written from the architecture slide (screenshot); the Stream transcript for 151 had not finished generating** — re-scrape to enrich step detail / any second scenario (the slide was labelled "Scenario 1", implying more scenarios in the video).
- Uses IVR DTMF input ([[communication-nodes]] gather response) routed to the CDE. Part of IVR: [[communication-nodes]], [[disconnect-journey]], [[transaction-reporting]], [[api-integration]], [[system-nodes]].
