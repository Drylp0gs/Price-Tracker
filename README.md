Markdown
# Automated Price Tracker & Analytics Dashboard

## Description

**Automated Price Tracker & Analytics Dashboard** is a modular Python command-line and web analytics tool that collects product pricing and availability data, records timestamped snapshots in a local SQLite database, flags price reductions between runs, exports data to CSV, and displays interactive charts and filters through a Streamlit web interface.

Built with a clean separation of concerns across data collection, storage, business logic, testing, and visualization, the project demonstrates end-to-end local data pipeline development using standard Python data libraries.

## Key Features

- **Multi-Page Web Scraping (`scraper.py`):** Fetches product titles, cleaned numeric prices, stock availability, and item URLs with custom request headers, timeout handling, and polite request delays.
- **Historical SQLite Storage (`database.py`):** Stores timestamped price records (`prices.db`) so historical price movements are preserved rather than overwritten, and calculates price drops compared to prior scrapes.
- **CLI Workflow (`main.py`):** Supports command-line flags (`--scrape`, `--pages`, `--drops`, `--export`) for fast terminal execution and automation.
- **Interactive Dashboard (`dashboard.py`):** Provides search filtering, maximum-price sliders, summary metrics, price-drop tables, historical line charts, and full record tables in the browser via Streamlit.
- **Automated Unit Tests (`test_tracker.py`):** Verifies price parsing and SQLite database operations against an isolated temporary test database.

## Project Structure

```text
price-tracker/
├── .gitignore
├── README.md
├── database.py
├── scraper.py
├── dashboard.py
├── main.py
└── test_tracker.py


Setup (Windows / PowerShell)
Navigate to the project folder:

PowerShell
cd price-tracker
Create and activate a virtual environment:

PowerShell
python -m venv venv
venv\Scripts\activate
Install required packages:

PowerShell
pip install requests beautifulsoup4 pandas streamlit
Usage
Run unit tests:

PowerShell
python -m unittest discover -v
Scrape catalog pages into SQLite (prices.db):

PowerShell
python main.py --scrape --pages 2
Check detected price drops from the terminal:

PowerShell
python main.py --drops
Export records to CSV (price_report.csv):

PowerShell
python main.py --export
Launch the interactive Streamlit dashboard:

PowerShell
python -m streamlit run dashboard.py

Save `README.md` (`Ctrl + S`).

---

### Step 2: Commit the Updated `README.md`
In your VS Code terminal inside `C:\Users\YourName\Projects\price-tracker`, stage and commit your changes:

```powershell
git add README.md
git commit -m "Expand README.md with detailed project description and features"
git status
