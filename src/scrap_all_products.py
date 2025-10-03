import requests
from bs4 import BeautifulSoup
from scrap_a_category import scrap_category
import time


def scrap_all_categories(base_url="https://books.toscrape.com/"):
    start = time.time()
    page = requests.get(base_url)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, "html.parser")
    category_links = soup.select("div.side_categories ul.nav-list ul li a")
    category_urls = [
        # Vérifie la validité de l'url et renvoie l'url absolue
        requests.compat.urljoin(base_url, a["href"]) for a in category_links
    ]
    print(f"Found {len(category_urls)} categories.")
    for index, category_url in enumerate(category_urls):
        scrap_category(category_url, (index + 1, len(category_urls)))

    # Afficher le temps écoulé en minutes et secondes
    end = time.time()
    duration = end - start
    minutes = int(duration // 60)
    seconds = duration % 60
    print(f"Scraping completed in {minutes}m {int(seconds)}s.")

scrap_all_categories()