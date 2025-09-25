# Books Online Scraper

Projet de scraping du site Books to Scrape pour extraire les informations des livres et télécharger leurs images.

## Structure du projet

```
Books_Online/
├── src/
│   ├── main.py                    # Scraping d'une page produit
│   ├── scrap_a_category.py        # Scraping d'une catégorie
│   ├── scrap_all_products.py      # Scraping de tous les produits
│   └── download_all_image.py      # Téléchargement des images
├── data/
│   ├── books.csv                  # Données extraites (généré)
│   └── images/                    # Images téléchargées (généré)
├── requirements.txt               # Dépendances Python
├── setup.bat                     # Script d'installation automatique
└── README.md                     # Ce fichier
```

## Installation automatique (Recommandé)

Exécutez simplement le script batch :
```powershell
setup.bat
```

Ce script va automatiquement :
1. ✅ Vérifier Python
2. 🗂️ Créer l'environnement virtuel (.venv)
3. 📦 Installer les dépendances
4. 📁 Créer les dossiers nécessaires
5. 🕷️ Lancer le scraping complet de tous les produits
6. 🖼️ Télécharger toutes les images automatiquement

**Durée estimée** : 10-15 minutes selon votre connexion

## Installation manuelle

### 1. Créer l'environnement virtuel
```powershell
python -m venv .venv
```

### 2. Activer l'environnement
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances
```powershell
pip install -r requirements.txt
```

### 4. Créer les dossiers
```powershell
mkdir data
mkdir data\images
```

## Utilisation manuelle

### Scraper une page produit
```powershell
python src/main.py
```

### Scraper une catégorie
```powershell
python src/scrap_a_category.py
```

### Scraper tous les produits
```powershell
python src/scrap_all_products.py
```

### Télécharger toutes les images
```powershell
python src/download_all_image.py
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
- **Nommage** : `image_1.jpg`, `image_2.jpg`, etc.
- **Résolution** : Format original du site

## Performance et statistiques

- **Nombre de livres** : ~1000 livres
- **Scraping complet** : 5-10 minutes
- **Téléchargement images** : 2-5 minutes  
- **Taille totale images** : ~50-100 MB
- **Total estimé** : 10-15 minutes

## Dépannage

### ❌ Erreur PowerShell Execution Policy
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
setup.bat
```

### ❌ Python non reconnu
Vérifiez l'installation :
```powershell
python --version
```
Si échec, essayez :
```powershell
py --version
```
Sinon, installez Python depuis [python.org](https://www.python.org/downloads/)

### ❌ Environnement virtuel corrompu
```powershell
rmdir /s .venv
setup.bat
```

### ❌ Erreur réseau / timeout
Relancez simplement le script, il reprendra où il s'est arrêté.

## Fonctionnalités avancées

### Throttling automatique
- Délai de 1 seconde entre chaque requête
- Respect des bonnes pratiques de scraping

### Gestion d'erreurs
- Retry automatique sur erreur réseau
- Journalisation des erreurs
- Continuation même en cas d'échec partiel

### Encodage
- Support UTF-8 complet
- Correction automatique des symboles monétaires
- Nettoyage des espaces et caractères spéciaux

## Respect des sites web

Ce projet est destiné à des fins **éducatives** sur le site [Books to Scrape](http://books.toscrape.com/) qui est spécifiquement conçu pour l'apprentissage du web scraping.

**⚠️ Important** : 
- Ne pas utiliser sur des sites commerciaux sans autorisation
- Respecter les `robots.txt` et conditions d'utilisation
- Limiter la fréquence des requêtes
- Ne pas surcharger les serveurs

## Dépendances

- **Python** 3.7+
- **requests** : requêtes HTTP
- **beautifulsoup4** : parsing HTML  
- **lxml** : parser rapide et robuste

## Licence

Projet éducatif - OpenClassrooms Python Developer Path

---

📧 Pour toute question : consultez les logs ou relancez `setup.bat`