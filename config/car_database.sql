-- MySQL dump 10.13  Distrib 5.7.14, for Win64 (x86_64)
--
-- Host: localhost    

DROP DATABASE IF EXISTS `car_database`;
CREATE DATABASE `car_database`;
USE `car_database`;
--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
CREATE TABLE `car` (
  `registration` varchar(15) NOT NULL,
  `make` varchar(20) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `colour` varchar(10) DEFAULT NULL,
  `mileage` int(11) DEFAULT NULL,
  `engineSize` float(2,1) DEFAULT NULL,
  PRIMARY KEY (`registration`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES ('05-MO-17931','Toyota','Highlander','Green',253789,1.6),('10-G-2334','Toyota','Corolla','Green',123389,1.3),('10-WH-17931','Toyota','Corolla','Silver',130389,1.4),('11-MO-23431','Toyota','Corolla','Black',1234123,1.3),('12-WH-123','Ford','Ka','Black',125882,1.0),('132-G-9923','Ford','Ka','Silver',325883,1.0),('132-MO-19323','Ford','Galaxy','Silver',2343,1.5),('171-G-39532','Toyota','Corolla','Silver',55882,1.3),('171-MO-12533','Ford','Fiesta','Black',25882,1.0),('99-G-300','Toyota','Corolla','Green',599339,1.3);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

