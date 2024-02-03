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

# Affichage des résultats en console avec alignement
print("{:<20}{}".format("Nom", "Capacité"))
print("-" * 28)
for resultat in resultats:
    nom, capacite = resultat
    print("{:<20}{}".format(nom, capacite))

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
