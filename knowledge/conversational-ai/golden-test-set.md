# Golden Test Set & Version Control (Conversational AI 107)
**Source:** Product Foundation Courses → Conversational AI / 107 Golden Test Set & Version Control (video transcript) · **Help:** search `site:sprinklr.com/help golden test set intent model version deploy classification report`

## What a Golden Test Set is
A **golden test set** (golden standard / benchmark set) is a **predetermined collection of unseen test expressions**, hand-crafted by experts, covering a **diverse range of inputs/scenarios**. It gives a **standardised, objective** measure to compare **different versions** of an intent model fairly — using metrics like **accuracy, precision, recall, F1 score**. This lets you decide which version performs best and should be deployed.

## Setting up a Golden Test Set
1. **Conversational AI → application → Intent Models** (under **AI Tools**).
2. Hover the model → **View version**.
3. Under the **Golden Test Set classification report** panel → **Manage Set**.
4. For each intent, click the **edit icon** → select the **language** → add **test expressions** (singly or in **bulk**) → **Save**. Repeat per intent.
5. On the View version landing page, click **Calculate Performance**.

## Validating a model against the Golden Test Set
- On the **View version** landing page, once predictions are **processed**, click **Review Predictions**.
- See the **classification report** + predictions for each test expression; **apply filters** to customise the view; **download** the classification report.

## Managing versions & deployment
- The **model version window** shows the **live, previous, and new** versions.
- **Deploy** the best-performing version — clicking **Deploy** on a version makes it **live instantly**.
- Create a **new version** by **modifying the training data**.
- Compare performance by **toggling between versions** in the Golden Test Set classification report panel.

## Notes / gaps
- Golden test set = the objective gate before deploying a model trained/validated via [[intents]] (097) and [[message-validation]] (106).
- Keep the test expressions **unseen** (not in training data) so the benchmark stays honest across versions.
- Deployment is instant and reversible (re-deploy the previous version) — safe to roll back if a new version regresses.
