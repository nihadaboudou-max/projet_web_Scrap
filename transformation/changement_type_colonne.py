import pandas as pd

class ChangementType:
    """
    fonction qui change le type de colonne
    
    arg: df:dataframe, colonne: nom de la colonne à modifier, type_col:type de colonne 
    elle retourne la dataframe modifier
    """
    
    @staticmethod
    def change_type(df: pd.DataFrame, colonne:str, type_col):
        df[colonne] = df[colonne].astype(type_col)
        
        return (df)