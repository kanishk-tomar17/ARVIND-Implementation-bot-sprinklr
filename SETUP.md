# ARVIND — Setup

One-time setup to give ARVIND its browser hands and confirm its knowledge sources. Do this on the consultant's machine.

---

## 1. Browser MCP (inspection, learning + automation, inside Claude Code)

Lets ARVIND navigate Chrome, read config/DOM and transcript text, and drive the UI from the CLI — attaching to **your own logged-in Chrome** so no passwords are shared. Config is already in `.mcp.json` (`chrome-devtools`).

Launch (see `LEARNING.md` for the full runbook):
1. Fully quit Chrome.
2. `& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222`
3. Sign into Lyearn / Sprinklr in that window.
4. Requires Node.js. Restart Claude Code, run `/mcp`, confirm `chrome-devtools` is connected.

**Use it for:** learning from Lyearn courses + the live platform, inspecting what's actually configured, reading rule/queue state, automated steps.

---

## 2. Claude for Chrome extension (live SSO session takeover)

Operates the consultant's **own logged-in** Chrome — so it acts inside the real, SSO-authenticated Sprinklr session with the consultant's permissions. This is the path for the actual fix in their environment.

Manual one-time steps (ARVIND can't install this for you):
1. Get access to **Claude for Chrome** (Anthropic's browser extension; requires an eligible Claude plan/access).
2. Install the extension in the Chrome profile the consultant uses for Sprinklr.
3. Sign in to Claude in the extension.
4. Open the client's Sprinklr environment and log in as normal (SSO).
5. When ARVIND escalates to takeover, drive the fix through the extension in that tab.

**Use it for:** changes that must happen in the consultant's authenticated session / production-or-sandbox environment.

---

## 3. Which path when

| Situation | Path |
|---|---|
| Read/inspect current config | Browser MCP |
| Automated repetitive steps | Browser MCP |
| Fix in the consultant's live, logged-in Sprinklr | Claude for Chrome extension |
| Anything destructive (delete/publish/bulk/prod) | Either — but confirm first, prefer sandbox |

The `sprinklr-takeover` skill encodes this decision.

---

## 4. Knowledge sources (verify they're reachable)

- **Local KB:** `knowledge/INDEX.md` and topic files in this project.
- **`sprinklr.com/help`:** ARVIND uses WebFetch/WebSearch — no setup, just internet access.
- **RaptorCX SharePoint** (Product Foundation Courses): via the Microsoft 365 MCP. Confirm it's connected with `/mcp`. If not, re-authenticate the Microsoft 365 connector.

Quick check after setup: ask ARVIND "How do assignment rules work in Unified Routing?" — it should answer from the KB / `sprinklr.com/help` with a source link.
