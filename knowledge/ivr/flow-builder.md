# IVR Flow Builder — manager, create flow & full node catalog

**Source:** Verified live (prod8, 2026-06-18) by building a throwaway `Kanishk Agent Test IVR` + help center `Introduction to IVR Components → How to Create and Manage All Your IVR`. This is the **how-it-actually-works** companion to the concept files: `ivr/communication-nodes.md`, `ivr/system-nodes.md`, `ivr/api-integration.md`, `ivr/disconnect-journey.md`, `ivr/transaction-reporting.md`, `ivr/pci-input.md`, `inbound-voice/ivr.md`.

## Access
- **Launchpad → Sprinklr Service › Resolve › Voice → Voice IVR** (or Voice Admin persona → *Tools › Configuration › IVR*).
- Lands on the **IVR Flow Manager** at **`/care/voice/ivr-flow`** (don't guess other slugs — `/care/ivr` 404s).

## IVR Flow Manager (the list)
- Sub-tabs: **IVR Flows Manager** | **Test Cases**.
- A **Manual / Standard** dropdown (builder mode — manual node flow vs standard templated).
- Toolbar: Search, Refresh, **More Actions**, **Create IVR Flow**, **Import IVR Prompt(s)**, **Select Quick Filter**, Create Folder.
- Columns: **Name · Status · Date Created · Last Modified**. Status e.g. **Paused** (not deployed) / live.
- **Row More Actions (⋮):** Edit · Edit Settings · **Activate** · Clone · Move To Folder · Share · **Delete** (confirm: "You cannot undo this action") · View Reports · Export IVR Prompt · Get Usages.

## Create IVR Flow (the dialog → opens the builder)
Mandatory `*`: **IVR Name**, **IVR Type**, **Language**, **Default Language**.
- **IVR Name*** + **Description**.
- **IVR Type*** (11): **Inbound IVR · Wait Time Queue IVR · Early Media Inbound IVR · IVR Transfer · IVR Transfer – End Call · IVR Transfer – Connect Back · IVR Conference · System IVR · Outbound Dialer · Call Another Flow – IVR · Call Event IVR**.
- **Language*** — multi-select from the full language list; **+ Add Language** for more; **Default Language*** (auto-set when only one). Each language can attach a **Timeout Message** and **Invalid Message** (typed prompt + **Add Recording**).
- **Speech Profile** (optional), **Disconnect Journey** (optional — see `ivr/disconnect-journey.md`).
- **Share Settings:** **Visible in all workspaces** (checkbox) → else pick **Workspaces** / **Users / User Groups**.
- **Save** creates the flow (Status = Paused, *not* live) and opens the builder.

## The builder (canvas)
- Header: **Back**, flow name, Last Modified, **Search node**, **Activity** (needs a save first), **Manage Resources** (prompts/recordings/variables/APIs).
- Canvas starts with a **"Received a Call"** trigger node; **zoom %** control.
- **+ Add Element** opens the **node palette** (a *Search node* box + the categorized node list). Clicking a node **adds it to the canvas and opens its config modal** (Name + node-specific fields + Cancel/Save/Close Modal). Nodes connect into the flow; **Go To Node** is an on-canvas target picker (no modal).
- Footer: **Close · Save as Draft · Save & Deploy** (**Save & Deploy = publish/make live** — only after the flow is wired to a number/entry point).

## Node palette — full catalog (52 nodes, 4 categories) + verified config
Every node has a **Name**; most expose **Dynamic Input Type** (drive the value from a variable) and a `${x}` resource/variable picker. Listed below are the *distinctive* fields.

### COMMUNICATION (11)
| Node | Key config |
|---|---|
| **Operator Says** | Prompt(s) — text editor + **Say As / Add Recording / Audio Variable / Sprinklr AI+**; per-prompt **Add Conditions**, Hide Message; Add Another Prompt |
| **Get Customer's Language** | prompt; **Always Ask Language**; Valid Digits for Input; Timeout (s); number of times to play; wait for end of prompt |
| **Gather Customer's Response** | **Response Type (DTMF)**; Number of Input Digits; Process Variable; prompt; **Enable Recording** (Sensitive / **PCI** / **PII** data); Timeout; End Key; repeat count; **Add Timeout / Add Invalid Input** messages |
| **Record Voicemail** | Max duration; end-recording key; store variable; **beep before recording**; **text transcription** |
| **Send SMS/Email/Whatsapp** ("Send Message") | **Channel** (SMS…); Sender's account; Mobile Number (w/ country code); **Time to send** (Epoch, blank=immediate); Message Content Type/Content; set Outbound Message custom fields; **Wait for Message to be Sent** |
| **Send Survey** | Survey Name; Channel; Sender's Account; URL Shortener; Expiry Duration; Language; **Survey Asset** |
| **Deflect** | **Deflection Channel**; Sender's Account; **Asset** (deflect to digital channel) |
| **VXML Connect** | VXML URL; **Input** params (var/value, Add More); **Output** params (var → store var); handover settings; VXML Timeout |
| **Confirmed Appointment** | Email/SMS/Whatsapp notification; **Customer & Agent Reminder Schedule** (Notify Before + unit); **Appointment Mode** |
| **Cancel Appointment** | Email/SMS/Whatsapp notification |
| **Fetch Appointment slots** | **Slot Definition** (Dynamic Input); **Assignment Type** (Queue) + Work Queue; Timezone; Start/End time to fetch; **Slots Batch Size**; slot date/time voice format; prompts; DTMF timeout; Next Batch Navigation Key |

### SYSTEM ACTIONS (33)
| Node | Key config |
|---|---|
| **Decision Box** | **Paths** — each Path: name + conditions (**Where** field / **Operator** / Values), **Add Condition / Condition Group**, Add Another Path; **Default Path** |
| **Set Language** | Language (Dynamic Input) |
| **Configure API** | **Select API** (from APIs registered in Manage Resources) — see `ivr/api-integration.md` |
| **Custom Fields Action** | **Set Fields** (Profile / Case custom fields: field/operator/values) + **Copy Fields** (copy to field) |
| **Set Priority Rank** | Priority Rank 1–100 (Dynamic Input) |
| **User Task** | Task Label; Description; **Task Type**; Priority; **Assign to Agent** |
| **Set Skills** | **Manage Required Skill** = **Merge** / replace; **Dynamic skill and proficiency**; Skill + **Proficiency Score** |
| **Add or Remove from Queues** | **Input Type** (Static…); **Add to Case Queue** / **Remove from Case Queue** |
| **Profile List Change** | **Add to** / **Remove from** Profile List(s) |
| **Add to Suppression List** | Suppression List; Customer Name; Contact Number; **Evergreen** / **Expiry Time** |
| **Merge Profile** | Channel; **Profile SnId** |
| **Add Auth Profile To Case** | Channel SnId; Case ID; **Add Contact Details** (Contact Type/Tag/Details e.g. Email) |
| **Business Hours** | Business Hours set (Dynamic Input); **Is in Business Hours** var; **Start/End of Next Business Hour**; format |
| **Work Queue Properties** | per property: Work Queue; **Consider Current Case Skill**; Skills + Proficiency Score; store variable; Add more |
| **Add Note** | **Asset** (where to add note); Notes text; Media variable |
| **Start / Stop Stream Activity** | (no config modal — marker nodes for activity streams) |
| **Execute Action** | **Select action** |
| **Add Loop** | **Collection Variable**; Loop Direction; Loop Variable Name — see `ivr/system-nodes.md` |
| **Break Loop** | (no config — exits the loop) |
| **Go To Node** | on-canvas **target node picker** (no modal) — jump flow control |
| **Call Another Flow** | **Enable Route to IVR from Voice bot**; **Select IVR** to call |
| **Embed IVR Flow** | **Select IVR** (Dynamic Input) to embed inline |
| **Schedule Callback** | Callback Number; **Time for Callback** (Epoch); **Use Callback Campaign**; Callback Campaign; **Assign to**: Work Queue / Journey / Agent; Assign Skills; Note; Priority Rank; Preview Time; Expire Timeout; Advanced Settings |
| **Reschedule Callback** | Task id; Priority Rank; Callback Number; Time; Note; reassign Work Queue/Agent |
| **Cancel Callback** | **Callback Type** |
| **Update Properties** | Select/Create fields → **operator** → value mapping; Add Another Mapping |
| **Get / Update / Create / Count Records** | **Entity Type** + record query/fields (CRUD over Sprinklr records) |
| **Create Customer Session** | Asset; Asset ID; **Expiry Duration**; Variables (name → value) |

### TRANSFER ACTIONS (5)
| Node | Key config |
|---|---|
| **Assign Agent** | **Enable Route to Agent from Voice bot**; **Work Queue** (Dynamic); **Wait Time IVR**; **Timeout Duration** + unit; **Preferred agent** (+ try-only-preferred); **Disable Recordings / Transcripts**; Entity Type + highlighted fields; **Wait Music** |
| **External Assignment** | **Assignment Provider**; Timeout Duration; Disable Recordings/Transcripts; Wait Music |
| **Assign Case** | **Queue** |
| **DID Transfer** | **Enable Sip Dial**; **Record Call**; Enable Transcripts; **Answering Machine Detection**; **Transfer Destination**; **Caller Id**; Max Ring Time + unit; **Send Digits to External Transfer**; Music on hold — see help "Call Forwarding & Dial External Number using DID Transfer Node" |
| **Redirect to Voicebot** | **Voicebot**; **Set Incoming Mapping** / **Set Outgoing Mapping** (var ↔ voicebot in/out) |

### FLOW ACTIONS (3)
| Node | Key config |
|---|---|
| **Resume Previous IVR** | (no config — returns to the prior IVR, e.g. after a transfer/bot) |
| **Hang up** | (no config — drops the call; cf. End Connection, see help "Difference between End Call and Hangup node") |
| **End Connection** | (no config — ends the leg/connection) |

## Notes / gotchas
- **Manage Resources** holds reusable prompts, recordings, audio variables, **APIs** (for Configure API), and process variables — define once, reference across nodes.
- Many inputs accept a **`${x}` resource/variable** instead of a literal, and most config values support **Dynamic Input Type** (variable-driven).
- **PCI/PII** capture is via **Gather Customer's Response → Enable Recording → Sensitive/PCI/PII data** (see `ivr/pci-input.md`).
- Status stays **Paused** until **Save & Deploy**; building + exploring never affects live call routing. Cite `sprinklr.com/help` IVR articles for node-specific deep dives.
