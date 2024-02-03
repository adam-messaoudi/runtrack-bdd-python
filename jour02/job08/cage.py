# Définition de la classe Cage
class Cage:
    # Initialisation de l'objet avec les attributs
    def __init__(self, superficie, capacite_max):
        self.superficie = superficie
        self.capacite_max = capacite_max
        self.animaux = []

    # Méthode pour sauvegarder la cage dans la base de données
    def save(self, db):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        db.execute_query(query, (self.superficie, self.capacite_max))

    # Méthode pour mettre à jour les informations de la cage dans la base de données
    def update(self, db, id_cage):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
        db.execute_query(query, (self.superficie, self.capacite_max, id_cage))

    # Méthode pour supprimer la cage de la base de données
    @staticmethod
    def delete(db, cage_id):
        db.execute_query("DELETE FROM cage WHERE id = %s", (cage_id,))

    # Méthode statique pour récupérer toutes les cages de la base de données
    @staticmethod
    def get_all(db):
        return db.execute_query("SELECT * FROM cage")
