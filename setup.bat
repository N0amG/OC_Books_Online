@echo off
chcp 65001 > nul
echo ==========================================
echo    Books Online Scraper - Installation
echo ==========================================
echo.

echo [1/7] Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou pas dans le PATH
    echo Telechargez Python depuis https://www.python.org/downloads/
    echo N'oubliez pas de cocher "Add Python to PATH" lors de l'installation
    pause
    exit /b 1
)
echo ✓ Python detecte

echo.
echo [2/7] Suppression ancien environnement virtuel...
if exist ".venv" (
    rmdir /s /q ".venv"
    echo ✓ Ancien .venv supprime
) else (
    echo ✓ Aucun ancien environnement trouve
)

echo.
echo [3/7] Creation environnement virtuel...
python -m venv .venv
if errorlevel 1 (
    echo ERREUR: Impossible de creer l'environnement virtuel
    pause
    exit /b 1
)
echo ✓ Environnement virtuel cree

echo.
echo [4/7] Activation environnement virtuel...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERREUR: Impossible d'activer l'environnement virtuel
    pause
    exit /b 1
)
echo ✓ Environnement active

echo.
echo [5/7] Installation des dependances...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERREUR: Installation des dependances echouee
    pause
    exit /b 1
)
echo ✓ Dependances installees

echo.
echo [6/7] Creation des dossiers necessaires...
if not exist "data" mkdir data
if not exist "data\images" mkdir data\images
echo ✓ Dossiers crees

echo.
echo ==========================================
echo     LANCEMENT DU SCRAPING COMPLET
echo ==========================================
echo.
echo Cette etape va prendre environ 10 minutes...
echo Scraping de tous les produits en cours...

echo.
echo [7/7] Execution scrap_all_products.py...
python src\scrap_all_products.py
if errorlevel 1 (
    echo ERREUR: Scraping echoue
    pause
    exit /b 1
)
echo ✓ Scraping termine avec succes

echo.
echo ==========================================
echo     TELECHARGEMENT DES IMAGES
echo ==========================================
echo.
echo Cette etape va prendre environ 10-12 minutes...
echo Telechargement des images en cours...

echo.
echo [8/8] Execution download_all_images.py...
python src\download_all_image.py
if errorlevel 1 (
    echo ATTENTION: Telechargement des images partiellement echoue
    echo Les donnees CSV sont neanmoins disponibles
)

echo.
echo ==========================================
echo           INSTALLATION TERMINEE !
echo ==========================================
echo.
echo ✓ Environnement virtuel: .venv\
echo ✓ Donnees extraites:     data\books.csv
echo ✓ Images telechargees:   data\images\
echo.

if exist "data\books.csv" (
    for /f %%i in ('find /c /v "" ^< data\books.csv') do set /a lines=%%i-1
    echo 📊 Nombre de livres scrapes: !lines!
)

if exist "data\images" (
    for /f %%i in ('dir /b data\images ^| find /c ".jpg"') do echo 🖼️  Nombre d'images telechargees: %%i
)

echo.
echo 💡 Pour reactiver l'environnement plus tard:
echo    .venv\Scripts\activate.bat
echo.
echo 💡 Pour lancer un scraping manuel:
echo    python src\scrap_all_products.py
echo.
echo 💡 Pour telecharger les images:
echo    python src\download_all_image.py
echo.
echo Appuyez sur une touche pour fermer...
pause >nul