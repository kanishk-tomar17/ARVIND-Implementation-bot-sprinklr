# Spelling & Grammar Check (native, outbound messages) — Platform-wide

**Source:** https://www.sprinklr.com/help/articles/platform-modules/support-for-spelling-and-grammar-check-in-outbound-messages/633c5c2b59534970b26f96d9
**Related (Social flavor, same underlying feature):** https://www.sprinklr.com/help/articles/advanced-capabilities/spelling-and-grammar-check/63fee0be32d12b63c5f55c3c

Non-generative, real-time proofing as an agent types — different from the Sprinklr AI+ "Fix Spelling & Grammar" rewrite in [[reply-assistance-ai-plus]].

## What it does
- **Red underline** = spelling error. **Green underline** = grammar error. (Docs don't call out punctuation as a separate underline color — grammar checking covers it.)
- Double-click an underlined word to see fix suggestions and apply one.
- Right-click a flagged word to **add to personal dictionary** (so it stops flagging brand terms, jargon, names).

## Coverage
- Works across **all Sprinklr publishers**: Care Console, Agent Console, Engagement dashboards, Social publishing composer.
- **17 languages**: English (US), Spanish, Portuguese, French, German, Catalan, Dutch, Italian, Greek, Persian, Polish, Romanian, Russian, Slovak, Ukrainian, Galician, Khmer.

## Configuration
- Must be **enabled by a Success Manager** (not a self-serve toggle).
- Admins can **restrict the "Add to Dictionary" permission** by user/role.
- **Rule Engine**: can build a pre-publish rule that **blocks sending** if a message has more than N spelling/grammar errors.
- **Reporting**: build an **Outbound Message widget** in reporting with these metrics (source: Social flavor article, applies platform-wide) —
  - `Grammar Violations Count`
  - `Grammar Suggestions Visited Count`
  - `Grammar Suggestions Used Count`
  - `Spell Check Violations Count`
  - `Spellcheck Suggestions Visited Count`
  - `Spellcheck Suggestions Used Count`
  - `Add To Dictionary Used Count`
  - No punctuation-specific metric — punctuation is folded into "Grammar."

Related: [[agent-assist-ai]], [[reply-assistance-ai-plus]].
