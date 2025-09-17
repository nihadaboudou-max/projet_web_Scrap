import pandas as pd

class ValeurManquante:
    """cette classe permet de calculer le nombre de valeur manquante
    """
    
    @staticmethod
    def calcul_valeur_manquante(df:pd.DataFrame):
        """
        .Que fais la fonction
        La fonction calcul le nombre de valeur manquante
        
        .les arguments
        df: la base de donnée (dataframe) à analyser
                
        .return
        res:(int) retourne la somme des valeurs manquantes
                
        """ 
        if not isinstance(df,pd.DataFrame):
            raise ValueError("La donnée reçu n'est pas un dataframe") # si df n'est pas un dataframe
        
        if df.empty:
            return pd.DataFrame() # pour verifier si df est null
        
        res = df.isnull().sum()
        
        return res