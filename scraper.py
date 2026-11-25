import time
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def clean_price(raw_price):
    """Extracts numeric float value from strings like '£51.77'."""
    match = re.search(r"[\d\.]+", raw_price)
    return float(match.group()) if match else 0.0

def scrape_pages(max_pages=2):
    """Scrapes product listings across multiple pages with rate limiting."""
    results = []

    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        print(f"[SCRAPER] Fetching page {page}: {url}")

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title_tag = article.find("h3").find("a")
            title = title_tag["title"].strip()
            relative_url = title_tag["href"]
            full_url = urljoin(url, relative_url)

            price_tag = article.find("p", class_="price_color")
            price = clean_price(price_tag.text) if price_tag else 0.0

            stock_tag = article.find("p", class_="instock availability")
            availability = stock_tag.text.strip() if stock_tag else "Unknown"

            results.append({
                "title": title,
                "price": price,
                "availability": availability,
                "url": full_url
            })

        # Polite delay between requests
        time.sleep(1.5)

    return results