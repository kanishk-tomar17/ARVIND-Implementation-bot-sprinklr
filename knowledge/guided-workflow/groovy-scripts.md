# Groovy Scripts (GW 116)
**Source:** Product Foundation Courses → Guided Workflow - Groovy Scripts (116, video transcript) · **Help:** search `site:sprinklr.com/help guided workflow groovy library`

## What it is
**Groovy** is an object-oriented programming language. In guided workflows it's used to:
- Write the **logic of the flow**, and
- **Manipulate data** the workflow is already receiving (most common use).

## When to use — typical cases
- **Reformat API data:** e.g. API returns time in **epoch** format → use Groovy to convert it to a readable format for the agent screen.
- **Combine data from multiple APIs** into a single variable, then show it as a **dynamic table**.
- **Reshape gathered input before sending to an API:** info collected from the customer isn't in the format the API accepts → Groovy converts it to the accepted format.
- **Common small ops:** difference between two dates; convert/format dates; string changes (upper/lower case, **split string**); number formatting. More are documented in the **Groovy library**.

## Writing Groovy in the GW builder
- Example shown: API response returns `total amount` with many decimal places, but the agent should see only **two decimals**.
  - In the Groovy field you **define a variable**, **specify the path** to fetch `total amount` from the response, then append a **formatting/rounding expression** so only two decimals are displayed.
- This is where you type Groovy; the returned result is **stored in a variable**.

## Groovy library (your starting point)
- Click the **"Groovy library"** icon to open the library link.
- It contains:
  1. A **link to an online editor** to test the Groovy you've written.
  2. A **list of operations** with **ready-made Groovy** for each — e.g. *convert date string format*, *convert date to epoch*, *difference between two dates*, and many more.
- Find the operation matching your use case and **copy its script**.

## Testing in the online editor
1. Open the editor link (from the Groovy library).
2. **Paste** your Groovy script.
3. Change the output call to **`println`** (print) and hit **Execute**.
4. Read the output (demo showed a date/time, in **UTC** — you can write further Groovy to convert to the timezone/format you need).

## If you can't write it yourself
- If you're not proficient and the library has no script for your case, **ask ChatGPT** to generate it (e.g. *"groovy script to split a string"*).
- Copy the generated script → **test it in the online editor** → if it works, use it in the workflow.

## Storing & using the result
1. Write the Groovy and **return** the result.
2. **Store it in a variable.**
3. Use that variable in **display components** or as **inputs to an API**, per your requirement.

## Notes / gaps
- Always **test in the online editor first** before trusting a script in a live workflow — especially ChatGPT-generated code.
- Groovy is the "adapt the response" mechanism referenced in [[input-components]] and [[api-node]] when API output isn't already in key–value pairs.
- Exact Groovy syntax for each operation lives in the Groovy library, not memorised here — point consultants there.
