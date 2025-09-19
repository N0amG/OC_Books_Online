import requests

def fetch_page(url):
    page = requests.get(url)
    page.raise_for_status()
    return page.text


url = "https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html"

page = fetch_page(url)
print(page)