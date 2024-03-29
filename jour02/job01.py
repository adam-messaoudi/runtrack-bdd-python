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

        # Exécution de la requête pour récupérer l'ensemble des étudiants
        query = "SELECT * FROM etudiant"
        cursor.execute(query)

        # Récupération des résultats
        students = cursor.fetchall()

        # Affichage des résultats en console
        for student in students:
            print(student)

except mysql.connector.Error as err:
    print(f"Erreur de connexion à la base de données: {err}")
finally:
    # Fermeture de la connexion
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connexion fermée.")
