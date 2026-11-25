## Automated Price Tracker & Analytics Dashboard

## Description

Automated Price Tracker & Analytics Dashboard** is a modular Python command-line and web analytics tool that collects product pricing and availability data, records timestamped snapshots in a local SQLite database, flags price reductions between runs, exports data to CSV, and displays interactive charts and filters through a Streamlit web interface.

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

## How to Install
Open the project folder in VS Code and launch the terminal (Ctrl + ~), then navigate to the project directory:PowerShell
cd
price-tracker
Create a virtual environment:PowerShellpython -m venv venv
Activate the virtual environment in PowerShell:PowerShell.\venv\Scripts\Activate.ps1
(If PowerShell blocks script execution, run Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser once, then run
.\venv\Scripts\Activate.ps1 again.)

Install the required Python packages:PowerShellpip install requests beautifulsoup4 pandas streamlit
How to RunMake sure your terminal is inside C:\Users\esgue\Webbrowser\price-tracker and (venv) is active before running any command:   Run unit tests:PowerShellpython -m unittest discover -v
Scrape product listings into SQLite (prices.db):PowerShellpython main.py --scrape --pages 2
Check detected price drops from the terminal:PowerShellpython main.py --drops
Export scraped records to CSV (price_report.csv):PowerShellpython main.py --export
Start the interactive Streamlit dashboard in your browser:PowerShellpython -m streamlit run dashboard.py
(Press Ctrl + C in the terminal when you want to stop the Streamlit server.)
