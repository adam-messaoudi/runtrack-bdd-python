-- Création de la base de données
CREATE DATABASE IF NOT EXISTS zoo;

-- Utilisation de la base de données
USE zoo;

-- Création de la table "animal" pour MySQL
CREATE TABLE IF NOT EXISTS animal (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_cage INTEGER,
    date_naissance DATE,
    pays_origine VARCHAR(255)
);

-- Création de la table "cage" pour MySQL
CREATE TABLE IF NOT EXISTS cage (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    superficie INTEGER,
    capacite_max INTEGER
);
