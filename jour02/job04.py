import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='A.m.13015',
    database='LaPlateforme'
)

# Création d'un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécution de la requête pour récupérer les noms et les capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

# Récupération des résultats
resultats = cursor.fetchall()

# Affichage des résultats en console
print("Nom\t\tCapacité")
print("---------------------")
for resultat in resultats:
    nom, capacite = resultat
    print(f"{nom}\t\t{capacite}")

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
