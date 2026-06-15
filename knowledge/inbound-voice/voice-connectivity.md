# Voice Connectivity (Inbound Voice 154)
**Source:** Product Foundation Courses → Inbound Voice / 154 Voice connectivity (video transcript) · **Help:** search `site:sprinklr.com/help voice connectivity CPaaS bring your own carrier`

## What it is
**Voice connectivity** = establishing/maintaining audio communication (real-time conversation) using telephony, **VoIP**, and mobile networks. Sprinklr's **dynamic voice connectivity** benefits: seamless integration (phone calls, voice messages, IVR), enhanced/personalized CX, efficient **omni-channel** management, and **actionable analytics** from voice interactions.

## Architecture
Each connectivity option interacts with the **CPaaS** layer → lands in Sprinklr's back-end → connects to the **agent** and/or **IVR** workflow depending on the use case.

## The 4 voice connectivity options
- **Option A — New phone numbers / port existing number.** Get customized local/toll-free numbers from Sprinklr, or **port** an existing number to the **Sprinklr CPaaS** partner (simplified pricing, centralized). *Live example: Salt Pay (Saltpi).*
- **Option B — Bring Your Own Carrier (BYOC).** Integrate the customer's **preferred carrier** into the platform; customer keeps full **ownership/control** of carrier relationships while using Sprinklr's connectivity. *Live example: (a customer named "possible").*
- **Option C — BYOC with On-Premise.** Tailored local connectivity supporting **IP trunk**, terminating at the **customer's location** via **SBC / gateway** — keeps existing carrier with local termination. *Live example: Montclair (Monkle).*
- **Option D — Sprinklr hardware deployment (on-premise).** Secure on-prem deployment keeping **voice traffic internal** — for regions/countries with strict telecom/data regulations (data integrity/compliance). *Live example: HDFC.*

## Notes / gaps
- Connectivity feeds the telephony providers/accounts in [[telephony-integration]] and routes to [[ivr]]. See KB article for more.
- Part of Inbound Voice: [[telephony-integration]], [[custom-fields]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[disposition-plan]], [[acw-builder]].
