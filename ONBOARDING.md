# ARVIND — Onboarding

**ARVIND is RaptorCX's all-in-one Sprinklr expert** — an AI agent that helps our product consultants implement client use cases, diagnose issues, and find the fastest, cleanest path to a fix. This guide gets you set up and running.

> Built by Kanishk Tomer. Ping me to get access or if anything below sticks.

---

## What ARVIND does for you

- **Answers any Sprinklr config question** — from a distilled knowledge base plus live `sprinklr.com/help` articles, and always cites its source. If it doesn't know, it says so.
- **Implements use cases end to end** — assignment rules, Care Console, IVR, ACW/disposition plans, Unified Routing, bots, reporting widgets & custom metrics, and more (requirements → config mapping → ordered steps → verify).
- **Diagnoses from a screenshot** — triage → clarify → plan → guide, so you get unblocked fast.
- **Takes over the browser** — when guidance isn't landing, it drives Sprinklr directly and safely: states each change, confirms before anything risky, works in sandbox where possible, hands control back with a summary.
- **Learns as a team** — every path it works out and every best practice you teach it is saved to shared memory, so the whole team gets faster over time.

---

## One-time setup (~15 min)

### 1. Get the agent
Clone the ARVIND project repo and open it in **Claude Code**. That gives you its instructions, skills, and the full knowledge base.

Clone the ARVIND repo:

```
git clone https://github.com/kanishk-tomar17/ARVIND-Implementation-bot-sprinklr.git
```

Then `cd` into the folder and open it in Claude Code. Pull regularly (`git pull`) to stay in sync as the KB grows. *(You'll need access to the repo — ping Kanishk if the clone is denied.)*

### 2. Browser MCP — inspection & automation (in Claude Code)
Lets ARVIND read and drive Chrome from the CLI, attached to **your own logged-in Chrome** (no passwords shared). Config ships in `.mcp.json`.
1. Fully quit Chrome.
2. Launch with remote debugging: `& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222`
3. Sign into Sprinklr in that window.
4. Needs Node.js. Restart Claude Code → run `/mcp` → confirm `chrome-devtools` is connected.

### 3. Claude for Chrome extension — live SSO takeover
For changes that must happen in your **own authenticated** Sprinklr session.
1. Get access to **Claude for Chrome** (eligible Claude plan).
2. Install it in the Chrome profile you use for Sprinklr and sign in.
3. Open the client's Sprinklr environment, log in via SSO as normal.

### 4. Microsoft 365 MCP — RaptorCX training library
For the Product Foundation Courses on SharePoint. In claude.ai → Settings → Connectors, connect **Microsoft 365**. Confirm with `/mcp`.

### 5. Supabase MCP — shared macro ledger (team hive-mind)
ARVIND stores reusable, generalized "how to do this in Sprinklr" paths in a shared Supabase table. Once connected, you read/write the same paths everyone else does.
1. claude.ai → Settings → Connectors → connect **Supabase**, authorizing the account that's a member of the shared RaptorCX Supabase org (the one holding the `arvind-macros` project).
2. Confirm with `/mcp` that Supabase is connected.
- **Security:** access is via your own Supabase connector auth — no service key or secret lives in the repo.

---

## Quick check
Ask ARVIND: *"How do assignment rules work in Unified Routing?"* — it should answer from the KB / `sprinklr.com/help` with a source link. If it does, you're good.

## Help ARVIND get smarter
Use it on real client work and **teach it**: when you give a correction or a "do it this way" best practice, it records it for the whole team. Your feedback is the training.

**Need a hand? Reach out to Kanishk — happy to set it up with you live.**
