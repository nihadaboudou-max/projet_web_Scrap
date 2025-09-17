import pandas as pd

class Imputation:
    """
    Classe pour l'imputation des valeurs manquantes par la médiane, moyenne et mode.
    """

    @staticmethod
    def imputation_par_mediane(df: pd.DataFrame) -> pd.DataFrame:
        """
        Cette fonction selectionne les colonnes numériques et détermine si elle comporte de valeur manquante

        Args:
            df (pd.DataFrame): df

        Returns:
            pd.DataFrame: df
        """
        
        # Sélectionner uniquement les colonnes numériques
        colonnes_numeriques = df.select_dtypes(include=["number"]).columns

        # Parcourir les colonnes numériques et remplacer les NaN par la médiane
        for col in colonnes_numeriques:
            if df[col].isnull().sum() > 0:  # Vérifie s'il y a au moins une valeur manquante
                mediane = df[col].median()
                df[col] = df[col].fillna(mediane)

        return df
    
    def imputation_par_mode(df: pd.DataFrame) -> pd.DataFrame:
        # On sélectionne toutes les colonnes (numériques + catégorielles)
        colonnes = df.columns

        for col in colonnes:
            if df[col].isnull().sum() > 0:  # Si la colonne contient des NaN
                mode = df[col].mode()[0]     # mode()[0] donne la première valeur la plus fréquente
                df[col] = df[col].fillna(mode)

        return df

    def imputation_par_moyenne(df: pd.DataFrame) -> pd.DataFrame:
        # Sélectionner uniquement les colonnes numériques (inclure toutes les variantes)
        colonnes_numeriques = df.select_dtypes(include=["number"]).columns

        # Parcourir les colonnes numériques et remplacer les NaN par la moyenne
        for col in colonnes_numeriques:
            if df[col].isnull().sum() > 0:  # ✅ Vérifie le nombre de NaN 
                moyenne = df[col].mean()
                df[col] = df[col].fillna(moyenne)

        return df