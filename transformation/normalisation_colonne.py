import pandas as pd

class Normalisation:
    
    """
    Cette fonction mets à la même échelle les colonnes de la dataframe
    la foction retoune la datframe avec la colonne normaliser  
    
    args: df, nom_colonne: la colonne à normaliser
    
    return df
    """
    
    @staticmethod
    def normalisation_par_min_max(df: pd.DataFrame, nom_colonne):
        df[nom_colonne] = (df[nom_colonne] - df[nom_colonne].min())/(df[nom_colonne].max() - df[nom_colonne].min())
        return df