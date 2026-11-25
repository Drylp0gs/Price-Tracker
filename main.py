import argparse
from database import init_db, insert_items, export_to_csv
from scraper import scrape_pages

def main():
    parser = argparse.ArgumentParser(description="Automated E-Commerce Price Tracker CLI")
    parser.add_argument("--scrape", action="store_true", help="Run web scraper and store results")
    parser.add_argument("--pages", type=int, default=2, help="Number of pages to scrape (default: 2)")
    parser.add_argument("--export", action="store_true", help="Export database records to CSV")

    args = parser.parse_args()
    init_db()

    if args.scrape:
        items = scrape_pages(max_pages=args.pages)
        if items:
            insert_items(items)
        else:
            print("[WARNING] No items scraped.")

    if args.export:
        export_to_csv()

    if not args.scrape and not args.export:
        parser.print_help()

if __name__ == "__main__":
    main()
