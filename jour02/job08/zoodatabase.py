# Import de la bibliothèque MySQL Connector pour la gestion de la base de données MySQL
import mysql.connector

# Définition de la classe ZooDatabase
class ZooDatabase:
    def __init__(self, host, database, user, password):
        # Initialisation des paramètres de connexion à la base de données
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        # Méthode pour établir une connexion à la base de données
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def calculer_superficie_totale(self):
        # Méthode pour calculer la superficie totale de toutes les cages dans le zoo
        query = "SELECT SUM(superficie) FROM cage"
        result = self.execute_query(query)
        # Retourne le résultat du calcul ou 0 si le résultat est None ou la première valeur est None
        return result[0][0] if result and result[0][0] is not None else 0

    def execute_query(self, query, params=()):
        # Méthode pour exécuter une requête SQL sur la base de données
        connection = self.connect()  # Établit la connexion à la base de données
        cursor = connection.cursor()  # Crée un objet curseur pour exécuter des requêtes
        cursor.execute(query, params)  # Exécute la requête SQL avec les paramètres fournis

        if query.strip().upper().startswith("SELECT"):
            # Si la requête commence par SELECT, récupère toutes les lignes du résultat
            result = cursor.fetchall()
        else:
            # Sinon, commit les modifications à la base de données et définit le résultat à None
            connection.commit()
            result = None

        connection.close()  # Ferme la connexion à la base de données
        return result  # Retourne le résultat de la requête
