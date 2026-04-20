# vault interview.

import csv
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

username = "vault-network-inteview"
email = "candidate@vaultsportshq.com"
password = "Vault!nterview1"
dashboard_url = "https://us-east-1.quicksight.aws.amazon.com/sn/account/vault-network-inteview/dashboards/3b1cdcb4-3d00-4612-9ff3-4940982b2e99"

# set our root path for organizing our files.
root = Path(__file__).resolve().parent

# -- paths.
csv_path = root / "quicksight_export.csv"
out_path = root / "output.json"

main_table = "Sum of Ftds and Sum of Registrations by Code, Date, and State"


def records_from_csv(path):

    # initialize our output list.
    out = []

    # open the csv file and read the rows.
    with path.open(newline="", encoding="utf-8-sig") as f:

        # iterate over the rows and append to our output list.
        for row in csv.DictReader(f):
            out.append(
                {
                    "date": row["Date"].strip()[:10],
                    "code": row["Code"].strip(),
                    "registrations": int(row["Registrations"].replace(",", "")),
                    "ftds": int(row["FTDs"].replace(",", "")),
                    "state": row["State"].strip(),
                }
            )
            
    return out


def main():
    # start the playwright browser.
    with sync_playwright() as p:

        # launch it.
        browser = p.chromium.launch(headless=False)

        # create our fresh page.
        page = browser.new_context(accept_downloads=True).new_page()

        # head over to the dashboard url.
        page.goto(dashboard_url)

        # wait for the page to load.
        page.wait_for_load_state("networkidle")

        # fill in the username and submit w/ 'next' button.
        page.locator('input[type="email"], input[name="username"], input[type="text"]').fill(email)
        page.locator('button, input[name="Next"]').first.click()

        # fill in the password and submit w/ 'sign in' button.
        page.locator('input[type="password"], input[name="password"]').first.fill(password)
        page.get_by_role("button", name="Sign in").click()

        # wait for the page to load.
        page.wait_for_timeout(5000)

        # find the visual and hover over it.
        v = page.get_by_text(main_table).first
        v.wait_for(state="visible", timeout=60_000)

        # hover over the visual and click the 'more' button.
        v.hover()
        page.get_by_role("button", name="Menu options").click()

        # wait for the download to start.
        with page.expect_download() as dl:
            page.get_by_text("Export to CSV").first.click()

        # save the download to the csv path.
        dl.value.save_as(str(csv_path))

        # close the browser.
        browser.close()

    # write the records to the output path.
    out_path.write_text(json.dumps(records_from_csv(csv_path), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
