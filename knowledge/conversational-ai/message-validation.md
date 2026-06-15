# Message Validation & Intent Test Projects (Conversational AI 106)
**Source:** Product Foundation Courses → Conversational AI / 106 Message Validation & Intent Test Projects (video transcript) · **Help:** search `site:sprinklr.com/help message validation intent test project model accuracy feedback`

## What they are
Tools to **measure and improve intent-model accuracy**:
- **Message Validation** — test **individual** messages for intent prediction and give the model feedback.
- **Intent Test Project** — test **bulk/historical** messages and validate predictions at scale.
Both feed a **machine-learning loop**: the more validated feedback you give, the closer the model gets to target accuracy.

## Test an individual message (Message Validation)
1. **Conversational AI → application → Message Validation** (under the **Test** panel).
2. Click **Validate Message** (top-right).
3. Enter the **message/phrase**, select the **intent model**, select the **language** → **Test message**.
4. **Intents tab** shows the predicted intent + **confidence score**; **Entities tab** shows any captured entities.
5. **Save** → stored in the **Record Manager**.

## Give feedback on a wrong prediction
- Example: customer wants to *link* their account but the model predicts **Account closure**.
1. Open the **dropdown** → select the **expected intent**.
2. To inculcate it into the model you must **approve** it: click the **view-details icon** for that message in the **Record Manager** → **approve the feedback** to append it into the model.

## Intent Test Project (bulk)
Evaluate a built model against **historical data** in bulk; validating + approving predictions refines the model over time.
1. Application homepage → **Intent Test Project** (under **Test**) → **Add Test Project** (top-right).
2. **Name**, **description**, select the **intent model**.
3. Data source: **existing Sprinklr data** or **upload an Excel**.
4. Add **filters**; select **language**, **time range**, **sample size** → **Create**.
5. Status goes **Processing → Processed**.
6. **Review:** click the **(i) icon** → see predictions per message. If good → **Save progress** and view the next set; if wrong → provide feedback (select expected intent) and save.
7. **Approve feedback:** three-dot menu near the test project → **Review validated predictions** → approve.

## Notes / gaps
- This is the accuracy-improvement loop referenced in [[intents]] (097) — predictions → human validation → approved feedback → retrain.
- Confidence score on the Intents tab is the quick signal for whether a model is sure; low/incorrect → feedback candidate.
- Approval is a required second step — selecting the expected intent alone doesn't update the model until approved.
