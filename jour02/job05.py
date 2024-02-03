import mysql.connector

# Informations de connexion à la base de données

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'A.m.13015',
    'database': 'LaPlateforme'
}

# Tentative de connexion à la base de données
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Connexion à la base de données réussie.")

        # Création d'un curseur pour exécuter des requêtes SQL
        cursor = connection.cursor()

        # Exécution de la requête pour calculer la superficie totale des étages
        query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
        cursor.execute(query)

        # Récupération des résultats
        result = cursor.fetchone()

        # Affichage du résultat en console
        superficie_totale = result[0]
        print(f"La superficie de La Plateforme est de {superficie_totale} m2.")

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données: {err}")

finally:
    # Fermeture du curseur et de la connexion
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée.")
