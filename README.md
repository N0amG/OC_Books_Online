# Books Online Scraper

Projet de scraping du site Books to Scrape pour extraire les informations des livres et télécharger leurs images.

## Structure du projet

```
Books_Online/
├── src/
│   ├── scrap_a_page.py            # Scraping d'une page produit
│   ├── scrap_a_category.py        # Scraping d'une catégorie
│   └── scrap_all_products.py      # Scraping de tous les produits
├── data/                          # (créé automatiquement)
│   ├── books.csv                  # Données extraites (généré)
│   └── images/                    # Images téléchargées (généré)
├── requirements.txt               # Dépendances Python
└── README.md                     # Ce fichier
```

## Installation et lancement

### Étape 1 : Créer l'environnement virtuel
```powershell
python -m venv .venv
```

### Étape 2 : Activer l'environnement virtuel
```powershell
.\.venv\Scripts\Activate.ps1
```

### Étape 3 : Installer les dépendances
```powershell
pip install -r requirements.txt
```

### Étape 4 : Lancer le scraping complet
```powershell
python src\scrap_all_products.py
```

**Durée estimée** : 15-20 minutes selon votre connexion

> ℹ️ **Note** : Les dossiers `data` et `data\images` sont créés automatiquement si ils n'existent pas lors du scraping.

## Utilisation

### Scraping complet (recommandé)
```powershell
python src\scrap_all_products.py
```
*Cette commande unique lance le scraping complet de toutes les catégories, télécharge les images et sauvegarde les données dans le CSV au fur et à mesure.*

### Scripts individuels (pour développement/debug)
```powershell
# Scraper une catégorie spécifique
python src\scrap_a_category.py

# Scraper une page produit individuelle  
python src\scrap_a_page.py
```

## Données extraites

Le fichier `data/books.csv` contient les colonnes suivantes :

| Colonne | Description |
|---------|-------------|
| `product_page_url` | URL de la page produit |
| `universal_product_code` | Code UPC unique du livre |
| `title` | Titre complet du livre |
| `price_including_tax` | Prix TTC (avec £) |
| `price_excluding_tax` | Prix HT (avec £) |
| `number_available` | Nombre d'exemplaires en stock |
| `product_description` | Description complète du produit |
| `category` | Catégorie du livre |
| `review_rating` | Note sur 5 étoiles (1-5) |
| `image_url` | URL absolue de l'image de couverture |

## Images téléchargées

- **Emplacement** : `data/images/`
- **Format** : JPG
- **Nommage** : `[timestamp]-image.jpg` (horodatage unique)
- **Résolution** : Format original du site
- **Téléchargement** : Automatique lors du scraping

## Performance et statistiques

- **Nombre de livres** : ~1000 livres
- **Scraping + téléchargement** : 15-20 minutes
- **Taille totale images** : ~45 MB
- **Processus** : Intégré (CSV et images traités simultanément)

### Encodage
- Support UTF-8 complet
- Correction automatique des symboles monétaires
- Nettoyage des espaces et caractères spéciaux

## Respect des sites web

Ce projet est destiné à des fins **éducatives** sur le site [Books to Scrape](http://books.toscrape.com/) qui est spécifiquement conçu pour l'apprentissage du web scraping.


## Dépendances

- **Python** 3.7+
- **requests** : requêtes HTTP
- **beautifulsoup4** : parsing HTML  

## Licence

Projet éducatif - OpenClassrooms Python Developer Path
