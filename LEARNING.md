# ARVIND — Learning from Lyearn & the Sprinklr platform

How ARVIND studies the foundational courses and the live product, using your own logged-in browser. **No passwords are shared** — ARVIND attaches to a Chrome session *you* have already logged into.

## One-time: let ARVIND attach to your Chrome

ARVIND uses the `chrome-devtools` MCP (see `.mcp.json`), which connects to a Chrome started with remote debugging.

1. Double-click **`Start-ARVIND-Chrome.bat`** on your Desktop. It closes Chrome and reopens it with debugging on, using a **dedicated ARVIND profile** (`C:\ARVIND-Chrome-Profile`).
   - Why a separate profile: Chrome 136+ refuses to expose the debug port on your normal profile for security. The dedicated profile is a real on-disk profile, so logins persist — you sign in once.
2. In the Chrome window it opens, sign into **Lyearn** (`sprinklr.lyearn.com`) and your **Sprinklr** environment. **One time only** — this profile remembers it.
3. Restart Claude Code and run `/mcp` — confirm `chrome-devtools` is connected.

That's it. ARVIND now sees the tabs in the ARVIND profile. (Your normal Chrome profile is untouched and separate.)

## How ARVIND learns a course
For each Product Foundation Course (map in `knowledge/INDEX.md`):
1. Open the course in Lyearn.
2. Read every text surface the player exposes — **transcript/caption panel**, on-screen slide text, course notes, attached docs.
3. Distill into the matching `knowledge/<area>/<topic>.md` file (template in `INDEX.md`), citing the Lyearn course + any `sprinklr.com/help` article.
4. Flag in the file's **Notes / gaps** if the course was audio-only with no readable transcript.
5. Mark the topic `✅` in `INDEX.md`.

## Researching the live platform
With your Sprinklr environment open, ARVIND can navigate real config screens to learn exact navigation paths, field names, and behaviour — then bake those into the KB and into diagnoses. It treats your environment as read-only while learning; it follows the `sprinklr-takeover` safety rules before changing anything.

## Honest limit
ARVIND reads **text**. A video with spoken narration and **no captions/transcript** can't be consumed by any tool here — those courses get flagged as gaps, and ARVIND falls back to `sprinklr.com/help` for that topic.
