import pandas as pd

class Zscore:

    @staticmethod
    def calcul_zscore(df: pd.DataFrame) -> pd.DataFrame:
        """
        Détecte les valeurs aberrantes (Z-score > 3 ou < -3)
        pour toutes les colonnes numériques du DataFrame.
        """
        numeric_cols = df.select_dtypes(include='number').columns

        if len(numeric_cols) == 0:
            return pd.DataFrame()  

        mask = pd.Series(False, index=df.index)

        for col in numeric_cols:
            mean_val = df[col].mean()
            std_val = df[col].std()

            if std_val == 0:  # éviter division par zéro
                continue  

            upper_limit = mean_val + 3 * std_val
            lower_limit = mean_val - 3 * std_val

            mask |= (df[col] < lower_limit) | (df[col] > upper_limit)

        return df[mask]   # retourne uniquement les valeurs aberrantes
