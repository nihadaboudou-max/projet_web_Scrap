import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scrapping:
    
    @staticmethod
    def scrape_table(url, columns):
        """
        Web scraping pour récupérer des colonnes sur un site avec option pour enlever l'entête.

        url : str -> l'adresse du site web
        columns : dict -> dictionnaire { "NomColonne": {"class": "NomClasse"} }

        return : DataFrame pandas
        """
        # 1. Télécharger la page
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # 2. Extraire les colonnes
        data = {}
        for col_name, search_args in columns.items():
            tags = soup.find_all(attrs=search_args)
            data[col_name] = [tag.get_text(strip=True) for tag in tags]

        # 3. Créer un DataFrame
        df = pd.DataFrame(data)
        return df
