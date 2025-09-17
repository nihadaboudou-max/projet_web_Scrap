import pandas as pd

class Renommer:
    """
    fonction qui renomme des colonnes de la dataframe
    arg: df:dataframe, liste: contenant le nom des nouvelles colonnes
    
    il retour la dataframe avec les colonnes renommés
    """
    
    @staticmethod
    def renommer(df: pd.DataFrame,liste_colonne):
        df.columns = liste_colonne
               
        return df