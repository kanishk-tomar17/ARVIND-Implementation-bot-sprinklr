# PCI Input in IVR (IVR 151)
**Source:** Product Foundation Courses → IVR / 151 PCI input in IVR (video transcript + "Gather Customer's Response" node screenshot showing Sensitive Data → PCI option) · **Help:** search `site:sprinklr.com/help PCI input IVR gather customer response sensitive data CDE`

## What it is
How to capture **PCI / sensitive data** (e.g. card number) from the customer in an IVR without storing it in normal Sprinklr databases — it goes to an isolated **CDE** (Cardholder Data Environment).

## What is PCI data
**PCI DSS** = a set of security standards from Visa, MasterCard & global financial leaders (governed by the **PCI SSC**) for handling sensitive data. A vendor/brand storing such data must be **PCI DSS certified** — requires restricted access, antivirus, strong **encryption** (transmission + retention), firewalls.
- **Examples:** complete card number, expiry, CVV, card PIN, OTP. (Brands may classify other sensitive customer data as PCI too.)
- **Requirements:** never stored on normal servers; encrypted at rest + in transit; retained only in cache; access restricted to PCI-DSS-trained people.

## How Sprinklr solves it (data flow)
1. Customer calls the brand → telephony provider connects to the normal Sprinklr environment (process engine, IVR, guided workflow).
2. When PCI data is needed, the **process engine / IVR instructs the telephony provider** to take the input (e.g. a 14-digit card number), flagged as **sensitive** — **do NOT send it back** to Sprinklr; instead send it to the special **CDE** provisioned to retain such data.
3. Telephony provider securely transmits the data with **AES-256 encryption** to the secure **PCI environment (CDE)**.
4. The CDE returns an **ID** (identifier) for that data → passed back to the process engine.
5. The **normal environment only ever holds the identifier**, never the sensitive data. In the CDE the data is **encrypted** and **auto-discarded after a defined time** (held in a **Redis cache**).

## Configuration steps (demo)
1. In the IVR flow, at the point you need PCI data, add a **Gather Customer's Response** node.
2. Set **Name**, **Number of Input Digits** (e.g. **14** for a card number), **Process Variable** (stores the returned identifier), and the prompt text (language tabs: English/Dutch/German/Finnish/French).
3. Tick the **Sensitive Data** checkbox → choose the **PCI data** radio option (or **PII data**). Also configurable: wait for end of prompt, end key, number of times to play the message.
4. **Save.** That input then automatically routes to the **CDE** — provided the **PCI environment is enabled** for the partner (**contact Support** to enable PCI for a partner).

## Notes / gaps
- Built on the **Gather Customer's Response** node ([[communication-nodes]]); customer enters data via DTMF keypad. IVR runs through the process/guided-workflow engine; PCI/sensitive flows reported via [[inbound-voice-ivr]].
- Part of IVR: [[communication-nodes]], [[disconnect-journey]], [[transaction-reporting]], [[api-integration]], [[system-nodes]].
