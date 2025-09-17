Projet de Web Scraping & (ETL)

Un projet de scraping intelligent qui permet d’extraire des données depuis le web, de les transformer (nettoyage, analyse) et de les charger dans différents formats (CSV, visualisations).  

Objectif : automatiser la collecte et l’exploitation des données pour créer de la valeur à partir de n’importe quel site.

Fonctionnalités
- Scraping de données à partir de pages HTML
- Nettoyage et transformation des données
- Export en **CSV / Excel**
- Visualisations interactives avec **Matplotlib / Pandas**
- Architecture **ETL (Extract – Transform – Load)** réutilisable

Technologies utilisées
- Python 3.11.9
- Requests
- BeautifulSoup4
- Pandas
- Matplotlib
- Seaborn
- Sqlite3

Installation

Clonez le projet et installez les dépendances :

bash
git clone https://github.com/<TON-USERNAME>/<TON-REPO>.git
cd <TON-REPO>
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
