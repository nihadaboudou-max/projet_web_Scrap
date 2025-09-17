import pandas as pd
class ExportationCsv:
    @staticmethod
    def charger_csv(df,chemin):
        """
        Sauvegarde les données dans un fichier CSV
        
        args: df->dataframe, chemin-> chemin de stockage du fichier
        
        """
        
        df.to_csv(chemin, index=False, encoding="utf-8")
        print(f"Données enregistrées dans {chemin}")
