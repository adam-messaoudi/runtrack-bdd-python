import mysql.connector

# Fonction de connexion à la base de données
def connection():
    try:
        # Création de la connexion à la base de données
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="A.m.13015",
            database="job07"
        )
    except mysql.connector.Error as err:
        # Gestion des erreurs lors de la connexion
        print(f"Erreur de connexion à la base de données: {err}")
        raise

# Fonction pour récupérer les employés avec un salaire supérieur à 3000
def employeriche(conn):
    try:
        # Création du curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()
        # Exécution de la requête SQL pour récupérer les employés avec un salaire supérieur à 3000
        cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
        # Affichage des résultats
        for employe in cursor.fetchall():
            print(employe)
    except mysql.connector.Error as err:
        # Gestion des erreurs lors de l'exécution de la requête
        print(f"Erreur lors de la récupération des employés avec salaire > 3000: {err}")
        raise
    finally:
        # Fermeture du curseur pour libérer les ressources
        cursor.close()

# Fonction pour récupérer les employés et leur service respectif
def employeservice(conn):
    try:
        # Création du curseur pour exécuter des requêtes SQL
        cursor = conn.cursor()
        # Exécution de la requête SQL pour récupérer les employés et leur service respectif
        cursor.execute("""
        SELECT e.nom, e.prenom, s.nom AS service_name
        FROM employe e
        INNER JOIN service s ON e.id_service = s.id
        """)
        # Affichage des résultats
        for employe in cursor.fetchall():
            print(employe)
    except mysql.connector.Error as err:
        # Gestion des erreurs lors de l'exécution de la requête
        print(f"Erreur lors de la récupération des employés et de leur service: {err}")
        raise
    finally:
        # Fermeture du curseur pour libérer les ressources
        cursor.close()

# Connexion à la base de données
conn = connection()

# Exécution des opérations
print("Employé avec un salaire plus de 3000:")
employeriche(conn)

print("\nEmployés et leur service:")
employeservice(conn)

# Fermeture de la connexion à la base de données
conn.close()
