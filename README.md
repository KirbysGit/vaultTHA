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

### If This Were More "Production"
In a real product I'd tighten things up. Here's the kind of stuff I would add:

- **Wait for the actual button or table to appear** instead of “pause for 5 seconds and hope.” **Pauses** (`sleep`s) are easy to write but flaky if the site is slow or fast.
- **Try again automatically** if a click fails or the page is still loading (**retries**).
- **Deal with messy exports:** the download is a **CSV** (spreadsheet-style text: comma-separated values). A production script might handle renamed columns, empty cells, or weird number formats.
- **Sanity-check the numbers** before writing **JSON** (a standard text format for structured data, that's what `output.json` is used for).
- **Put secrets in environment variables** (**env vars**, settings the app reads from the machine, not from the source file) instead of pasting the password in the code.
- **Run the browser in the background with no window** (**headless**) when you run automated checks on a server.
- **Backup plan if CSV export breaks:** read the table straight off the web page. The DOM is messy on QuickSight because it often only keeps visible rows in memory, so you can miss rows unless you scroll and wait a lot, exporting CSV is the reliable path, thats why i did it.

##  What I Did
I didn't build all of what I just listed. I **patched the symptoms** of issues I ran into, for example QuickSight’s “welcome” popup blocks the chart until you click its **X**, which doesn’t have a normal label, so the script clicks the button Amazon marks with `welcome-modal-close-btn`. 
I also assume the CSV headers stay **`Code`, `Date`, `State`, `FTDs`, `Registrations`** (**FTDs** = first-time depositors in this dataset). 


None of the heavier production list was required for a proper output for this exercise, so I didn't add it to the script.
