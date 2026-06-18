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

## Live — VERIFIED (prod8, 2026-06-18)
**Voice Settings hub** = Launchpad → *Sprinklr Service › Resolve › Voice* → **Voice Care** → `/care/voice/settings/`. Left nav (12): **Voice Applications · Voice Accounts · Disposition Plan · Call Retry Strategy · Dial Plan · Caller ID Settings · Dialer Profiles · Suppression List · Threshold Settings · Speech Profiles · Voice Configurator · AMD Policy**. (VoiceConnect moved to Launchpad.)

**Voice Accounts** (`/settings/accounts`) — list cols: Voice Account · Provider · SIP Extension Range · Domain · Port · Number of Outbound Channels. **Create Voice Account** form: **Account Name\***, Number of Outbound Channels, **Provider** (dropdown — the 5 providers; drives which creds show), **API Key + Account SID** (Twilio), toggles **Enable Mobile Push Notifications / Delete Provider Call Records / Enable Network Traversal Service / Enforce Auth to access media**, Android & iOS Push Credentials SID, Region.

**Voice Applications** (`/settings/applications`) — the DID→IVR binding. List cols: Application · Status · Type · Active Connection · Provider · **Active Phone Number** · **IVR Process** · Voice Application ID · dates. Row actions: View Audit Trail · Validate configuration · **Edit** · Deactivate · Export · View Usages. **Create/Edit = 4-step wizard:**
- **1. Overview:** Application name\*, **Provider\*** (Twilio…), **Phone Number Based / SIP Domain Based** (radio), **Phone number\***, **Country\***, **Voice Account\***, **IVR Process\*** (the IVR the number routes to), **Fallback ACW**, **Fallback IVR Process**, App SID, API Key SID, Groups, **Share across workspaces** (Visible-in-all / Workspaces / Users), **Permission Settings** (per user/group: action All…, Add New Permission).
- **2. Caller IDs:** pick which phone number(s) act as caller ID (search list).
- **3. Audio and Voice Settings:** **Audio Language & Voice** (language + voice + sample), **Add Wait/Waiting Music**, **Ringtone Config** (+ conditions + Disable Ringtone Loop), **Agent Whisper Tone Config**, **Recording Announcement**.
- **4. Advanced Settings:** External Case URL, Contact/Caller **SIP Domain**, **After Call Work (ACW) Assignment** (e.g. *Trigger ACW for Each Primary Agent*), **Supervisor Eligible for ACW on Barge In**, **Highlighted Fields for Warm/Blind Transfer**, **Call Event Workflow IVR**, From Number SIP header Key, **BYOC Trunk SID**, Outbound Wait Message, **DTMF / Speech Timeout**, **Enable SIP Credentials** (→ Contact SIP Auth Username/Password), Subscribers (share), Custom Properties.

**Safety:** binding a phone number is a real telephony action — don't Create/Save a Voice Application against a live DID in a shared env; **edit an existing one** to inspect tabs, then Cancel.

## Notes / gaps
- Voice Account = provider credentials; Voice Application = DID + routing to an IVR ([[ivr]] / IVR module). Macros: `create_voice_account`, `create_voice_application` (ledger).
- Part of Inbound Voice: [[voice-connectivity]], [[custom-fields]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[disposition-plan]], [[acw-builder]].
