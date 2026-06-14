# Records Manipulation — Get / Update / Create (GW 118)
**Source:** Product Foundation Courses → Guided Workflow - Records manipulation (Create Get Update) (118, video transcript) · **Help:** search `site:sprinklr.com/help guided workflow get records update records create record node entity`

## Entities & records (the data model)
- An **entity** = objects stored inside a database. Every object inside an entity is a **record**.
- **Three entity types:**
  1. **System entity** — Sprinklr's own internal objects.
  2. **Standard entity** — common across all profiles (e.g. **Case**, **Profile**).
  3. **Custom entity** — custom-made per the client's requirement.
- Guided workflows can **fetch, update, and create** records via three dedicated nodes.

## When to use
- **Fetch** all open cases for a client → **Get Records**.
- **Update** custom fields in bulk for a set of cases → **Update Records**.
- **Create** a new case in Sprinklr → **Create Record**.

---

## Get Records node — fetch
Fetches data from the database. Can fetch a **single** record or **multiple** (max **100 at a time**).
1. Add the **Get Records** node → **name** it.
2. **Select the entity** (e.g. Case).
3. Define the **variable** to store the fetched records.
4. **Number of records to get** → Single or Multiple. (Selecting Multiple shows a disclaimer: *max 100 records*.)
5. Apply **filters/conditions** to narrow the data (e.g. *Account containing <account>*). Add **multiple conditions** if needed.
6. Optionally **sort** (e.g. case creation time, descending).
7. **Save.**

## Update Records node — modify
Updates field values in single or multiple records of an entity. The updated object(s) are stored in a variable for later use.
1. Add the **Update Record** node → **name** it.
2. **Select the entity** (e.g. Case).
3. **Number of records** → Single / Multiple.
4. Define the **condition** that selects which records to update (e.g. *Account containing <account>*; multiple conditions allowed).
   - ⚠️ **The filter value must not be null at runtime** — if it's null, the node **breaks**.
5. Choose the **field(s) to update** and set the new **value** (e.g. set **case status = Closed** for all matched records).
6. **Store the result in a variable** → **Save**. Use that variable anywhere later in the workflow.

## Create Record node — create
Creates records of an entity type, stored in the database. Fields can be tagged with **values from GW variables** or **static data**.
1. Add the **Create Record** node → **name** it → **select entity type**.
2. On the **left**, select the **field** to set; on the **right**, set its **value**.
3. **Name a variable** to store the created record → **Save**.
- **Demo (create a Case):** needs social network, case creation time, customer email, full name, etc.
  - Some values are **static** (e.g. social network = `Sprinklr Voice`).
  - Others come **from variables** (phone number, email captured on a previous screen, stored in a variable, then mapped to the field).
  - Once all required fields are mapped, the result is stored in a variable (demo: `profile created`).

## Notes / gaps
- The 100-record ceiling on Get Records (multiple) is a hard limit — design around it for large datasets.
- Update Records fetches-then-updates by condition; null filter values at runtime are the main failure mode — validate inputs before this node.
- All three nodes output to a **variable**, so chain them with [[api-node]], [[groovy-scripts]], and screen components downstream.
