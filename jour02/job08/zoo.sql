/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE IF NOT EXISTS zoo;
USE zoo;
DROP TABLE IF EXISTS animal;
CREATE TABLE `animal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `race` varchar(255) NOT NULL,
  `id_cage` int DEFAULT NULL,
  `date_naissance` date NOT NULL,
  `pays_origine` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS cage;
CREATE TABLE `cage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `superficie` float NOT NULL,
  `capacite_max` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;