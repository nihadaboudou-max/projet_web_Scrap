import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scrapping:
    @staticmethod
    def scrape_table(url, columns, skip_header=True):
        """
        Web scraping pour récupérer des colonnes sur un site avec option pour enlever l'entête.
        url : str -> l'adresse du site web
        columns : dict -> dictionnaire { "NomColonne": {"class": "NomClasse"} }
        skip_header : bool -> True pour enlever la première ligne (souvent l'entête)
        return : DataFrame pandas
        """
        try:
            # Ajout des headers pour éviter les blocages
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            data = {}
            
            for col_name, search_args in columns.items():
                tags = soup.find_all(attrs=search_args)
                
                # définir values même si tags est vide
                values = [tag.get_text(strip=True) for tag in tags] if tags else []
                
                # Supprimer le header si demandé ET si values n'est pas vide
                if skip_header and values:
                    values = values[1:]
                    
                data[col_name] = values
            
            # Vérifier que toutes les colonnes ont la même longueur
            max_length = max(len(values) for values in data.values()) if data else 0
            
            # Égaliser la longueur des colonnes (remplir avec des valeurs vides)
            for col_name in data:
                current_length = len(data[col_name])
                if current_length < max_length:
                    data[col_name].extend([''] * (max_length - current_length))
            
            return pd.DataFrame(data)
            
        except requests.RequestException as e:
            print(f"Erreur de requête: {e}")
            return pd.DataFrame()
        except Exception as e:
            print(f"Erreur lors du scraping: {e}")
            return pd.DataFrame()