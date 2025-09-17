import pandas as pd

class Doublons:
    """Fonction qui determine les valeurs doubles

        df: la dataframe
        
        res: retourne le nombre de valeur double
    """
    @staticmethod
    def valeur_double(df:pd.DataFrame):
        if not isinstance(df,pd.DataFrame):
            raise ValueError("la donnée envoyer n'est pas une dataframe") # verifie si la df envoyer est un dataframe
        if df.empty:
            return pd.DataFrame() # verifie si la df n'est pas null
        
        res = df.duplicated().sum()
        
        return res