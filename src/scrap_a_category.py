import requests
import re
from bs4 import BeautifulSoup
from scrap_a_page import scrap_book


def scrap_category(category_url, progress=None):
    books_urls = []
    current_url = category_url
    
    # Pagination basée sur le bouton "next"
    while current_url:
        # Scraper la page courante
        page = requests.get(current_url)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Extraire tous les liens de livres de cette page
        for h3 in soup.select("h3 a"):
            book_relative_url = h3.get("href")
            book_url = requests.compat.urljoin(current_url, book_relative_url)
            books_urls.append(book_url)
        
        # Chercher le bouton "next"
        next_button = soup.select_one("li.next a")
        if next_button and next_button.get("href"):
            # Construire l'URL de la page suivante
            next_url = requests.compat.urljoin(current_url, next_button["href"])
            current_url = next_url if next_url != current_url else None
        else:
            # Plus de page suivante, on arrête
            current_url = None

    category_name = (
        re.search(r"books/(.*?)_(\d+)/index\.html", category_url)
        .group(1)
        .replace("-", " ")
        .title()
    )
    print(f"Found {len(books_urls)} books in category '{category_name}'")
    for index, book_url in enumerate(books_urls):
        scrap_book(book_url)
        print(f"Saved {index + 1} / {len(books_urls)}")
    if progress:
        print(f"Category '{category_name}' completed ({progress[0]} / {progress[1]})")
