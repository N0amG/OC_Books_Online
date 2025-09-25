import requests
import re
import csv
from bs4 import BeautifulSoup
from scrap_a_category import scrap_category

def scrap_all_categories(base_url="https://books.toscrape.com/"):
    page = requests.get(base_url)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, "html.parser")
    category_links = soup.select("div.side_categories ul.nav-list ul li a")
    category_urls = [
        requests.compat.urljoin(base_url, a["href"]) for a in category_links
    ]
    print(f"Found {len(category_urls)} categories.")
    all_books = []
    for category_url in category_urls:
        all_books.extend(scrap_category(category_url))
    return all_books

def save_csv(rows, path="data/books.csv"):
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

save_csv(scrap_all_categories())