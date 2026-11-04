# PII Masking & Redaction (Audit and Compliance)

**Help:** https://www.sprinklr.com/help/articles/masking-templates/pii-masking-and-data-protection/679097bc37f1fe2470ea3f09 · https://www.sprinklr.com/help/articles/pii-masking/hard-masking-of-pii-content/64b03f1cc834a85bda8ca153

## What it is
Templates that detect and obfuscate personal data (names, emails, phone numbers, card details, SSN…) across universal case messages, transcripts and voice recordings — for GDPR/CCPA-style compliance. Masking markers show on the recording timeline at the matching message timestamp in the case analytics view.

## When to use
- Client wants PII scrubbed from case history but **not** while the conversation is live or being transferred.
- Regulated data (PCI/PII) must never sit unmasked in the database.
- QA/legal need a controlled path back to the original values.

## Configuration steps
1. **All Settings → General → Audit and Compliance** → choose masking type (**Universal Message Masking**, **Survey**, or **AI Data Masking**) → **+Add Masking Template**.
2. Fill the template:
   - **Name / Description**
   - **Enable for voice Channels** toggle
   - **Message Conditions** — Account, message type, channel, fan/brand post filters
   - **User / User Groups** sharing
   - **Approach** — **AI Based** (50+ built-in entities: email, phone, username, card number, CVV, account number, SSN, DOB, passport, VIN, IP, MAC, URL…) or **Regex Based** (custom patterns)
   - **Mask after time** — see the timing table below
   - **Masking Character** — the replacement symbol
   - **Type** — **Permanent** (irreversible) or **Conditional** (masked by default, authorised users e.g. legal can view unmasked)
   - **Additional Settings** — **Mask Audio** toggle (voice only)

### Mask after time — the three timing modes
| Mode | Fires when |
|---|---|
| Message Creation Time | Immediately as each message is received |
| Call Disconnect Time | When the call ends (voice only) |
| **Trigger On-Demand** | **Only when a rule executes it — nothing automatic** |

### Redact only after the conversation ends (and keep PII through transfers)
1. Create the template with **Mask after time = Trigger On-Demand**.
2. Rule Engine → **Case Update rule**.
3. **Add Action → Action on Universal Case → "Execute Masking Configuration"** → pick the template. *Only* Trigger-On-Demand templates appear in this dropdown.
4. Condition the rule on **case status → Closed / Resolved**.

**Why transfers stay unmasked:** with On-Demand the masking runs *only* when that rule fires. A transfer is an assignment change, not a status change, so the rule never triggers and the receiving agent sees the full unredacted history. Message Creation Time would mask up front and break the transfer use case.

## Related: hard masking via Rule Engine (regex, immediate)
Separate older path for immediate regex masking (credit cards, OTPs, SSNs):
- Rule Engine → **Inbound** or **Queue** rule → Condition **Account** → Action **"Search Pattern and take action"** → **"Mask matched terms"**.
- Applies to the database and agent-visible messages. **One-way — the original cannot be restored.** No closure-based or delayed trigger on this path; use the Trigger On-Demand template route for that.
- There is also **Hard Masking of Case/Profile Notes via Rules** (`/help/articles/pii-masking/hard-masking-of-caseprofile-notes-via-rules/65047547923c104940d19235`).

## Common issues & fixes
- **Template missing from the rule action dropdown** → its *Mask after time* isn't set to Trigger On-Demand.
- **Transferred agent sees masked history** → template is on Message Creation Time (or a queue/inbound hard-masking rule is doing it), not On-Demand.
- **Legal/QA can't retrieve originals** → template Type is **Permanent**. Permanent is unrecoverable; use **Conditional** if any authorised read-back is needed.
- **Reopened case has no PII** → expected with Permanent masking on close. Decide the reopen policy up front; the agent must re-collect.

## Notes & gaps
- The help article doesn't enumerate which Case Update conditions are supported for this action — status change is the standard/intended one; verify in the client's rule builder.
- Reporting on masking activity: **Reporting of PII Masking** (`/help/articles/masking-templates/reporting-of-pii-masking/685d1fac20753412ba7083a4`). Dry-run: **Test Masking Template** (`/help/articles/masking-templates/test-masking-template/6790940137f1fe2470ea3beb`).
- Adjacent, different features: **Mask PII data in Collaboration widget**, **Anonymize Agent Names on Care Console**, **Restrict Agent Performance Data in Service Reporting**, Co-browsing **Data Masking**, Insights CFM **Scheduled PII Redaction** / **Anonymize Profile Data** / survey response masking, AI+ Studio **PII Masking Template**.
