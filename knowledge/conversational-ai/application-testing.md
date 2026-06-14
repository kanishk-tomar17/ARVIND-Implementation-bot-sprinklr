# Application Testing (Conversational AI 108)
**Source:** Product Foundation Courses → Conversational AI / 108 Application Testing (video transcript) · **Help:** search `site:sprinklr.com/help conversational AI application testing debug logs`

## What it is
**Application Testing** lets brands run **comprehensive in-platform testing** of their conversational AI bots before/after go-live — a seamless way to build robust, reliable bots without external tooling.

## Using Application Testing
1. **Conversational AI → application** (search bar) → **Application Testing** (under the **Test** panel).
2. Choose **Chat** or **Call** application.
3. Select the **testing account**.
4. A testing window pops up (bottom-right) — start chatting to test the bot.

## Debug logs
Debug logs give admins insight into the bot's **performance, areas of improvement, and shortcomings** by:
- documenting **all user activity** (actions and dialogs),
- keeping a **history** of the bot's operation/interactions,
- **monitoring** over time, and
- letting admins **adjust/enhance** the bot.

### Viewing debug logs
1. Application Testing → select testing account → **start a new conversation** (bottom).
2. Send a test message (demo: *"I'd like to have some more time to pay my energy bills"*) → bot replies.
3. Click the **debug log icon** in the Chat Application Testing toolbar → view the **dialogue and actions** that produced the reply.
4. Click **View node** to jump to the **dialogue tree that was triggered** (demo confirmed the *payment extension* dialogue tree fired — correct in context).

## Notes / gaps
- This is how you confirm the right [[dialogue-tree-basics]] / [[bot-rule-setup]] fired for a given utterance — the debug log → View node is the key troubleshooting path when a bot replies wrongly.
- Test both **chat** and **call** application types separately.
- Pairs with [[message-validation]] (intent-level testing) and [[golden-test-set]] (model-level) — application testing is the end-to-end conversation check.
