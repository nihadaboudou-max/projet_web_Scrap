import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualisation:
    @staticmethod
    def visualiser_donnees(df, x=None, y=None, kind="bar", title="Visualisation"):
        """
        Fonction pour visualiser des données avec Matplotlib et Seaborn.
        
        Paramètres :
        ------------
        df : pandas.DataFrame
            Le DataFrame contenant les données.
        x : str, optionnel
            Colonne à mettre en abscisse.
        y : str, optionnel
            Colonne à mettre en ordonnée.
        kind : str, optionnel
            Type de graphique ("bar", "line", "scatter", "hist", "box", "pie").
        title : str, optionnel
            Titre du graphique.
        """

        plt.figure(figsize=(8, 5))

        if kind == "bar":
            sns.barplot(data=df, x=x, y=y)
        elif kind == "line":
            sns.lineplot(data=df, x=x, y=y, marker="o")
        elif kind == "scatter":
            sns.scatterplot(data=df, x=x, y=y)
        elif kind == "hist":
            sns.histplot(data=df[x], bins=20, kde=True)
        elif kind == "box":
            sns.boxplot(data=df, x=x, y=y)
        elif kind == "pie":
            if y is None:
                counts = df[x].value_counts()
            else:
                counts = df.groupby(x)[y].sum()
            plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
        else:
            raise ValueError("Type de graphique non reconnu !")

        plt.title(title)
        plt.tight_layout()
        plt.show()
