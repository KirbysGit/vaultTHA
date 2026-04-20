# Vault Network — QuickSight export

Fetches affiliate performance data from the QuickSight dashboard (login + **Export to CSV**), normalizes it, and writes **`output.json`** in the format required by the technical exercise.

## Setup

Python 3.10+ recommended.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run

```bash
python main.py
```

This saves `quicksight_export.csv` (download) and **`output.json`** (array of objects with `date` as `YYYY-MM-DD`, integer `registrations` and `ftds`).

The script opens a visible Chromium window so you can complete any interactive login if the flow changes.

## Output

- `output.json` — JSON array, each object: `date`, `code`, `registrations`, `ftds`, `state`.
