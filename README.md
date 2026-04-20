# Vault Take-Home Exercise - AWS QuickSight Processing

### What This Is ->
- Python script that logs into the AWS QuickSight dashboard
- Downloads the table as CSV, converts it to **`output.json`**

### What You Need
Make sure you have Python 3 installed, then clone this repo and run the following commands:

    python -m venv .venv
    .venv/Scripts/activate
    pip install -r requirements.txt
    playwright install chromium

### Running It ->
Stay in the project root and run:

    python main.py

### Output
- A browser window opens while Playwright runs
- When it's done, open **`output.json`** — each row has `date`, `code`, `registrations`, `ftds`, `state`
- The download is saved as `quicksight_export.csv` locally (gitignored so it doesn’t get committed by accident)

### Why I Did It This Way
- QuickSight is a normal site: log in → use **Export to CSV**
- Playwright drives a real browser to do those clicks for you
- Used **sync** Playwright so it’s just a straight line: open → sign in → export, no `async`/`await` noise

### If This Were More "Production":
I'd probably focus more on these things :

- **Wait on real elements** instead of fixed `sleep`s
- **Retries** when the UI is slow
- Handle **weird CSV layouts** or **bad/missing cells**
- **Validate types / ranges** before writing JSON
- **Credentials from env vars**, not hardcoded in the file
- **Headless** runs for CI if you need that
- **Fallback if CSV breaks:** parse rows from the **table in the DOM** (scroll + wait so rows show up, then read cells),annoying because QuickSight often only keeps **visible** rows mounted, so you can miss data; CSV avoids that

But for the sake of not over-engineering the solution, none of the above was required for this exercise, so it’s not in the script
