import requests
import bs4
import re
import csv
from urllib.parse import urljoin
import os
import time

def fetch_page(url):
    page = requests.get(url, timeout=10)
    page.raise_for_status()
    # Forcer un encodage correct si pas détecté
    if not page.encoding:
        page.encoding = page.apparent_encoding or "utf-8"
    text = page.text
    # Correction des artefacts courants de double-encodage 'Â£'
    text = text.replace("Â£", "£")
    return text


def scrap_book(url):
    page = fetch_page(url)
    soup = bs4.BeautifulSoup(page, "html.parser")
    # Récupération du titre
    title = soup.find("h1").get_text(strip=True)

    # Tableau des caractéristiques produit: chaque ligne <tr> contient un <th> (libellé) et un <td> (valeur)
    data_table = {}
    for row in soup.select("table.table.table-striped tr"):
        header = row.find("th")
        value_cell = row.find("td")
        if not header or not value_cell:
            continue
        label = header.get_text(strip=True)
        value_text = value_cell.get_text(separator=" ", strip=True)
        data_table[label] = value_text

    # Association des libellés -> clés normalisées
    keys = {
        "UPC": "universal_product_code",
        "Product Type": "product_type",
        "Price (excl. tax)": "price_excluding_tax",
        "Price (incl. tax)": "price_including_tax",
        "Tax": "tax",
        "Availability": "availability_raw",
        "Number of reviews": "num_reviews",
    }

    # Normalisation des données extraites
    normalized = {}
    for label, key in keys.items():
        if label in data_table:
            normalized[key] = data_table[label]

    number_available = None
    if "availability_raw" in normalized:
        avail_text = normalized["availability_raw"]
        match = re.search(r"\((\d+) available\)", avail_text)

        if match:
            number_available = int(match.group(1))

    # Conversion nombre de reviews en int
    if "num_reviews" in normalized:
        try:
            normalized["num_reviews"] = int(normalized["num_reviews"])
        except ValueError:
            pass

    # Description produit: le paragraphe suivant l'ancre #product_description
    product_description = None
    desc_anchor = soup.find(id="product_description")
    if desc_anchor:
        p = desc_anchor.find_next("p")
        if p:
            product_description = p.get_text(strip=True)

    # Catégorie: dans le chemin d'accès, la 3ème li > a (index -1 avant le livre)
    category = None
    breadcrumb_links = soup.select("ul.breadcrumb li a")
    # Structure: Home > Books > Category > Book Title (sans lien)
    if len(breadcrumb_links) >= 3:
        category = breadcrumb_links[2].get_text(strip=True)

    # Review rating: basé sur la classe star-rating
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    review_rating = None
    rating_tag = soup.find(class_=re.compile(r"\bstar-rating\b"))
    if rating_tag:
        for cls in rating_tag.get("class", []):
            if cls in rating_map:
                review_rating = rating_map[cls]
                break

    image_url = None
    img_tag = soup.select_one(
        "div.thumbnail img"
    )  # image dans une div de class 'thumbnail'
    if img_tag and img_tag.get("src"):
        image_url = urljoin(url, img_tag["src"])  # gère ../../

    # Construire le dict final et le retourner
    result = {
        "product_page_url": url,
        "universal_product_code": normalized.get("universal_product_code"),
        "title": title,
        "price_including_tax": normalized.get("price_including_tax"),
        "price_excluding_tax": normalized.get("price_excluding_tax"),
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url,
    }
    download_image(image_url)
    save_book(result)
    return result


def save_book(book, path="data/books.csv"):
    if not book:
        return
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Check if file exists and is not empty before opening
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    
    fieldnames = list(book.keys())
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            w.writeheader()
        w.writerow(book)

def download_image(image_url, save_dir="data/images/"):
    try:
        if not image_url:
            return
            
        # Créer le répertoire s'il n'existe pas
        os.makedirs(save_dir, exist_ok=True)
        
        # Créer le nom du fichier unique
        filename = str(time.time()) + '-image.jpg' 
        
        # Chemin complet du fichier
        file_path = os.path.join(save_dir, filename)
        
        # Télécharger l'image
        response = requests.get(image_url)
        response.raise_for_status()  # Vérifie que la requête a réussi
        
        # Sauvegarder l'image
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
        
    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement de l'image {image_url}: {e}")
        return None
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de l'image: {e}")
        return None