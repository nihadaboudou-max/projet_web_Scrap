import sqlite3
class ExportationDB:
    @staticmethod
    def charger_sqlite(df, db_path, table_name):
        """Charge les données dans une base SQLite."""
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print(f"Données enregistrées dans la table '{table_name}' de {db_path}")