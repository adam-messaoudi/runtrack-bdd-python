-- Créer la base de données
CREATE DATABASE IF NOT EXISTS job07;

-- Utiliser la base de données créée
USE job07;

-- Créer la table "employe"
CREATE TABLE IF NOT EXISTS employe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

-- Insérer des employés dans la table "employe"
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Dupont', 'Jean', 3500.00, 1),
('Martin', 'Sophie', 2800.00, 2),
('Lefevre', 'Paul', 4000.00, 1),
('Dubois', 'Marie', 3200.00, 3),
('Nouveau', 'Employe', 3500.00, 2);

-- Récupérer les employés avec un salaire supérieur à 3 000 €
SELECT * FROM employe WHERE salaire > 3000;

-- Créer la table "service"
CREATE TABLE IF NOT EXISTS service (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);

-- Insérer des services dans la table "service"
INSERT INTO service (nom) VALUES
('Service A'),
('Service B'),
('Service C');

-- Récupérer tous les employés et leur service respectif
SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service_nom
FROM employe e
JOIN service s ON e.id_service = s.id;

