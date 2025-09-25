import csv
import requests
import time

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Vérifie que la requête a réussi
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image téléchargée et sauvegardée sous {save_path}")
    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement de l'image {image_url}: {e}")

def get_csv_image_urls(csv_file_path):
    image_urls = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'image_url' in row:
                image_urls.append(row['image_url'])
    return image_urls

if __name__ == "__main__":
    start = time.time()
    csv_file_path = 'data/books.csv'  # Chemin vers votre fichier CSV
    image_urls = get_csv_image_urls(csv_file_path)
    
    for idx, image_url in enumerate(image_urls):
        save_path = f'data/images/image_{idx + 1}.jpg'  # Nom de fichier pour sauvegarder l'image
        download_image(image_url, save_path)
    end = time.time()
    print(f"Temps total d'exécution: {end - start} secondes")
