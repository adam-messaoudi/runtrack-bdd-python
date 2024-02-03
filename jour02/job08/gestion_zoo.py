# Import des classes nécessaires
from zoodatabase import ZooDatabase
from animal import Animal
from cage import Cage

# Définition de la fonction pour ajouter un animal
def ajouter_animal(db):
    # Saisie des informations de l'animal
    nom = input("Entrez le nom de l'animal: ")
    espece = input("Entrez l'espèce de l'animal: ")
    id_cage = input("Entrez l'ID de la cage: ")
    date_naissance = input("Entrez la date de naissance (YYYY-MM-DD): ")
    pays_origine = input("Entrez le pays d'origine: ")

    # Création d'un objet Animal et sauvegarde dans la base de données
    animal = Animal(nom, espece, id_cage, date_naissance, pays_origine)
    animal.save(db)
    print("Animal ajouté avec succès.")

# Définition de la fonction pour modifier un animal
def modifier_animal(db):
    # Saisie de l'ID de l'animal à modifier
    id_animal = input("Entrez l'ID de l'animal à modifier: ")
    
    # Saisie des nouvelles informations de l'animal
    nom = input("Entrez le nouveau nom de l'animal: ")
    espece = input("Entrez la nouvelle espèce de l'animal: ")
    id_cage = input("Entrez le nouvel ID de la cage: ")
    date_naissance = input("Entrez la nouvelle date de naissance (YYYY-MM-DD): ")
    pays_origine = input("Entrez le nouveau pays d'origine: ")

    # Création d'un objet Animal et mise à jour dans la base de données
    animal = Animal(nom, espece, id_cage, date_naissance, pays_origine)
    animal.update(db, id_animal)
    print("Animal modifié avec succès.")

# Définition de la fonction pour supprimer un animal
def supprimer_animal(db):
    # Saisie de l'ID de l'animal à supprimer
    id_animal = input("Entrez l'ID de l'animal à supprimer: ")
    
    # Suppression de l'animal dans la base de données
    Animal.delete(db, id_animal)
    print("Animal supprimé avec succès.")

# Définition de la fonction pour lister tous les animaux
def lister_animaux(db):
    # Récupération de tous les animaux depuis la base de données
    animaux = Animal.get_all(db)
    
    # Affichage des animaux dans le zoo
    print("Animaux dans le zoo:")
    for animal in animaux:
        print(animal)

# Définition de la fonction pour ajouter une cage
def ajouter_cage(db):
    # Saisie des informations de la cage
    taille = input("Entrez la taille de la cage: ")
    capacite_max = input("Entrez la capacité maximale: ")

    # Création d'un objet Cage et sauvegarde dans la base de données
    cage = Cage(superficie=taille, capacite_max=capacite_max)
    cage.save(db)
    print("Cage ajoutée avec succès.")

# Définition de la fonction pour modifier une cage
def modifier_cage(db):
    # Saisie de l'ID de la cage à modifier
    id_cage = input("Entrez l'ID de la cage à modifier: ")
    
    # Saisie des nouvelles informations de la cage
    superficie = input("Entrez la nouvelle superficie de la cage: ")
    capacite_max = input("Entrez la nouvelle capacité maximale: ")

    # Création d'un objet Cage et mise à jour dans la base de données
    cage = Cage(superficie=superficie, capacite_max=capacite_max)
    cage.update(db, id_cage)
    print("Cage modifiée avec succès.")

# Définition de la fonction pour supprimer une cage
def supprimer_cage(db):
    # Saisie de l'ID de la cage à supprimer
    id_cage = input("Entrez l'ID de la cage à supprimer: ")
    
    # Suppression de la cage dans la base de données
    Cage.delete(db, id_cage)
    print("Cage supprimée avec succès.")

# Définition de la fonction pour lister toutes les cages
def lister_cages(db):
    # Récupération de toutes les cages depuis la base de données
    cages = Cage.get_all(db)
    
    # Affichage des cages dans le zoo
    print("Cages dans le zoo:")
    for cage in cages:
        print(cage)

# Définition de la fonction pour afficher la superficie totale des cages
def afficher_superficie_totale(db):
    superficie_totale = db.calculer_superficie_totale()
    print(f"Superficie totale des cages : {superficie_totale} m²")

# Définition de la fonction principale de gestion du zoo
def gestion_zoo():
    # Connexion à la base de données
    db = ZooDatabase('localhost', 'zoo', 'root', 'A.m.13015')

    while True:
        # Affichage du menu
        print("\n** Menu Gestion du Zoo **\n")
        print("1. Ajouter un animal")
        print("2. Modifier un animal")
        print("3. Supprimer un animal")
        print("4. Lister tous les animaux")
        print("5. Ajouter une cage")
        print("6. Modifier une cage")
        print("7. Supprimer une cage")
        print("8. Lister toutes les cages")
        print("9. Afficher la superficie totale des cages")  # Nouvelle option
        print("10. Quitter")
        
        # Saisie du choix de l'utilisateur
        choix = input("Choisissez une option: ")

        # Traitement en fonction du choix de l'utilisateur
        if choix == '1':
            ajouter_animal(db)
        elif choix == '2':
            modifier_animal(db)
        elif choix == '3':
            supprimer_animal(db)
        elif choix == '4':
            lister_animaux(db)
        elif choix == '5':
            ajouter_cage(db)
        elif choix == '6':
            modifier_cage(db)
        elif choix == '7':
            supprimer_cage(db)
        elif choix == '8':
            lister_cages(db)
        elif choix == '9':
            afficher_superficie_totale(db)  
        elif choix == '10':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution de la fonction principale si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    gestion_zoo()
