# Telephony Integration (Inbound Voice 153)
**Source:** Product Foundation Courses → Inbound Voice / 153 Telephony Integration (video transcript + demo; Create Voice Account form screenshot) · **Help:** search `site:sprinklr.com/help voice care voice account voice application telephony provider`

## What it is
**Telephony integration** = integrating telecom systems (traditional phone lines or **VoIP**) with Sprinklr → seamless communication, efficient call handling, better CX.

## Supported providers
Sprinklr supports **5 telephony providers**: **Twilio (Tulio), Ozonetel, Amazon Connect, SignalWire, Vonage (Wuenach)**. Each offers **phone numbers (DIDs)** to add to the platform. Customers either **route their toll-free number (TFN)** to the platform phone number, or **publish the platform phone number** on their website/portals.

## Configure a telephony provider (demo)
### 1. Voice Account
**Sprinklr Service → Voice Care → Voice Accounts** → add an account using the provider's **native details** (varies by provider):
- **Twilio:** API Key, Account SID.
- **Ozonetel:** API Key, Username, API Base URL, Domain, Port.
- **SignalWire:** API Key, Account SID, API Base URL.
- (Form fields seen: **Account Name, Number of Outbound Channels, Provider** (dropdown), **API Key, Account SID, API Base URL**.) → **Save**.

### 2. Voice Application (the phone numbers / DIDs)
**Voice Care → Voice Application** — phone numbers/DIDs live here. Add the number from the provider's native account. Mandatory fields (e.g. for Twilio): **phone number, application name, default country, the voice account** (created above), and an **IVR to route the call to**. Other fields per requirement → **Save**.
- When a customer calls that number → the **linked IVR plays**. Once saved, you can dial out / the number lands calls to the connected IVR.

## Real customers
- **Ozonetel:** Port, HDFC, Lenskart, KYO fit. **Twilio:** Montclair, Salt Bay, etc. (provider chosen by region).

## Notes / gaps
- Voice Account = provider credentials; Voice Application = DID + routing to an IVR ([[ivr]] / IVR module). See KB article for full field list.
- Part of Inbound Voice: [[voice-connectivity]], [[custom-fields]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[disposition-plan]], [[acw-builder]].
