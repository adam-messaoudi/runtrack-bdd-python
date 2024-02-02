import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",      # Adresse du serveur MySQL
    user="root",           # Nom d'utilisateur MySQL
    password="A.m.13015",  # Mot de passe MySQL
    database="LaPlateforme" # Nom de la base de données
)

# Création d'un curseur pour exécuter des requêtes SQL
mycursor = mydb.cursor()

# Requête SQL pour sélectionner tous les enregistrements de la table "etudiant"
sql_query = "SELECT * FROM etudiant"

# Exécution de la requête SQL
mycursor.execute(sql_query)

# Récupération de tous les résultats de la requête
results = mycursor.fetchall()

# Affichage des résultats
for row in results:
    print(row)

# Fermeture du curseur pour libérer les ressources
mycursor.close()

# Fermeture de la connexion à la base de données
mydb.close()
