import requests
import re
from bs4 import BeautifulSoup
from scrap_a_page import scrap_book


def scrap_category(category_url):
    page = requests.get(category_url)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, "html.parser")
    books_urls = []
    page_count = soup.select_one("li.current")
    if page_count:
        page_count = page_count.get_text(strip=True)
        _, _, total_pages = page_count.rpartition("of ")
        total_pages = int(total_pages)

        for page_num in range(1, total_pages + 1):
            page_url = requests.compat.urljoin(category_url, f"page-{page_num}.html")
            page = requests.get(page_url)
            page.raise_for_status()
            soup = BeautifulSoup(page.content, "html.parser")
            for h3 in soup.select("h3 a"):
                book_relative_url = h3.get("href")
                book_url = requests.compat.urljoin(category_url, book_relative_url)
                books_urls.append(book_url)

    else:
        for h3 in soup.select("h3 a"):
            book_relative_url = h3.get("href")
            book_url = requests.compat.urljoin(category_url, book_relative_url)
            books_urls.append(book_url)

    category_name = (
        re.search(r"books/(.*?)_(\d+)/index\.html", category_url)
        .group(1)
        .replace("-", " ")
        .title()
    )
    print(f"Found {len(books_urls)} books in category '{category_name}'")
    all_books_data = [scrap_book(book_url) for book_url in books_urls]
    return all_books_data
