-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: books_libraries
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `email_address` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'johnhelldiver@gmail.com','1234'),(2,'marc_lamont@gmail.com','marc321');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `address_id` int NOT NULL AUTO_INCREMENT,
  `street` varchar(45) NOT NULL,
  `city` varchar(50) NOT NULL,
  `zip_code` varchar(45) NOT NULL,
  `province` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES (1,'San Jose','Puerto Princesa City','5300','Palawan','Philippines'),(2,'245 Anthony Trafficway Suite 526','Scottbury','46525','Ohio','Iraq'),(3,'15301 Stewart Cove','Valeriechester','02492','Minnesota','Slovakia (Slovak Republic)'),(4,'17071 Jessica Gateway Apt. 865','Port Brian','05268','Indiana','Equatorial Guinea'),(5,'5056 Hinton Springs','Tiffanytown','76014','Illinois','Albania'),(6,'07803 Karen Ways','Georgehaven','14657','Oregon','Wallis and Futuna'),(7,'40161 Clifford Road Apt. 168','East Kimberly','11531','Wyoming','Korea'),(8,'028 Miller Trail','Phillipstown','58400','North Carolina','Colombia'),(9,'36584 Maria Street','New Annechester','10335','Wyoming','Belize'),(10,'3092 Holly Fall Suite 287','Ashleyberg','34380','New Jersey','Afghanistan'),(11,'80183 Estrada Cliff','Christinaport','22164','New Mexico','Hungary'),(12,'76235 Rebekah Inlet Suite 901','Lake Patriciamouth','11155','California','Bhutan'),(13,'50157 Melissa Course','South Jonathanton','95323','Tennessee','Western Sahara'),(14,'7378 Simmons Expressway','East Hector','69003','Colorado','Dominica'),(15,'7825 Laura Neck Apt. 088','Mcbrideside','21445','Massachusetts','China'),(16,'51897 Victor Harbors','North Jay','58990','Connecticut','Russian Federation'),(17,'099 Conner Fall','Millerland','29614','Minnesota','Uruguay'),(18,'18863 Catherine Trafficway','New Brooke','67918','Idaho','Niger'),(19,'57000 Walters Green Suite 584','New Robertville','47521','Kansas','Sudan'),(20,'38800 Pugh Mews','Charleshaven','31977','Kentucky','South Africa'),(21,'26378 Walker Locks','Lake Ian','17146','West Virginia','El Salvador'),(22,'79173 Jacob Wall Suite 458','Devinmouth','89723','Massachusetts','New Caledonia'),(23,'79979 Davis Skyway','Jamesport','96438','Alabama','Faroe Islands'),(24,'562 Barnes Wall','South Robert','88106','Indiana','Honduras'),(25,'8369 Michael Knoll Apt. 784','South Kelly','11174','Maryland','Niue'),(26,'19359 Sims Lights','East Kathleen','48320','Kansas','Taiwan');
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `isbn` varchar(45) NOT NULL,
  `book_title` varchar(100) NOT NULL,
  `date_of_publication` date NOT NULL,
  `category_id` int DEFAULT NULL,
  `author_name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `fk_BOOKS_CATEGORIES1_idx` (`category_id`),
  CONSTRAINT `fk_BOOKS_CATEGORIES1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'458-8-450-89090-5','Forever','1999-01-01',10,'Monica Lopez'),(2,'295-38-398-52159-5','Southern forward especially.','1990-06-06',5,'Jesus Wolfe'),(3,'894-90-941-73878-5','Life record capital.','2018-10-23',2,'Nicole Rogers'),(4,'201-96-572-44622-5','Physical.','2007-09-09',1,'Deborah Griffin'),(5,'224-39-983-28815-3','North have.','2001-11-27',3,'Brooke Figueroa'),(6,'798-22-613-24220-6','Draw.','2020-10-13',15,'Gloria Mitchell'),(7,'479-31-609-15560-9','Provide song yes.','1974-03-24',2,'Eric Miller'),(8,'603-52-619-56441-8','Quality me.','1972-03-15',16,'Harold Campos'),(9,'568-99-376-45657-2','Different car radio.','1986-05-21',4,'Julie Taylor'),(10,'530-52-369-76371-9','Personal could radio.','2022-09-26',7,'Michael Scott'),(11,'923-41-465-98264-8','Smile truth.','1991-02-16',13,'Paul Gutierrez'),(12,'654-93-286-95996-6','Course.','2001-08-20',1,'Jessica Glass'),(13,'590-66-482-71110-8','Much do property main.','1972-06-26',15,'Maria Perry'),(14,'967-81-744-21042-8','There agency top.','2002-03-25',11,'Martin Baker DVM'),(15,'296-96-155-63972-7','Manage radio.','2005-02-01',5,'Kathleen Marshall'),(16,'661-6-617-63395-7','National free field wall Democrat.','1999-04-15',14,'Dr. Aaron Castro DDS'),(17,'618-72-372-71474-6','Conference final.','2002-11-15',11,'Ray Young'),(18,'811-15-92-95994-4','Hotel number.','1985-09-24',7,'Laura Miller'),(19,'238-12-320-73357-8','Set change.','1982-12-17',5,'Michael Wang'),(20,'549-44-21-87626-1','Off most.','2002-02-10',13,'Lisa Smith'),(21,'780-32-998-20210-5','Us which.','1996-12-09',8,'Laurie Davis'),(22,'307-71-81-55377-3','Current box dark.','2009-12-16',15,'Rachel Brennan'),(23,'250-89-359-56658-7','Set alone.','1995-08-01',13,'Matthew Hill'),(24,'201-19-358-74080-2','Firm management page.','1987-01-27',15,'Meghan Fox'),(25,'645-41-978-95410-5','Sea.','2017-11-07',1,'Kelly Gray'),(26,'407-32-531-45519-9','Behavior send.','2007-04-20',NULL,NULL),(27,'111-21-333-12411-9','The Wild Melodies','2022-01-01',2,'Mob Miller'),(30,'888-12-91-32131-9','The Last Stand','2024-01-01',4,'House Patch');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_at_libraries`
--

DROP TABLE IF EXISTS `books_at_libraries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_at_libraries` (
  `library_id` int DEFAULT NULL,
  `book_id` int DEFAULT NULL,
  `quantity_in_stock` int NOT NULL,
  KEY `fk_LIBRARIES_has_BOOKS_BOOKS1_idx` (`book_id`),
  KEY `fk_LIBRARIES_has_BOOKS_LIBRARIES1_idx` (`library_id`),
  CONSTRAINT `fk_LIBRARIES_has_BOOKS_BOOKS1` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`),
  CONSTRAINT `fk_LIBRARIES_has_BOOKS_LIBRARIES1` FOREIGN KEY (`library_id`) REFERENCES `libraries` (`library_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_at_libraries`
--

LOCK TABLES `books_at_libraries` WRITE;
/*!40000 ALTER TABLE `books_at_libraries` DISABLE KEYS */;
INSERT INTO `books_at_libraries` VALUES (1,1,85),(1,2,84),(1,3,84),(1,4,90),(1,5,3),(1,6,36),(1,7,55),(1,8,22),(1,9,97),(1,10,4),(1,11,57),(1,12,83),(1,13,2),(1,14,54),(1,15,89),(1,16,46),(1,17,75),(1,18,16),(1,19,51),(1,20,65),(1,21,7),(1,22,98),(2,1,98),(2,2,87),(2,3,90),(2,4,94),(2,5,66),(2,6,5),(2,7,89),(2,8,20),(2,9,92),(2,10,6),(2,11,69),(2,12,73),(2,13,91),(2,14,46),(2,15,98),(2,16,24),(2,17,16),(2,18,87),(2,19,53),(2,20,20),(3,1,12),(3,2,54),(3,3,42),(3,4,11),(3,5,81),(3,6,35),(3,7,97),(3,8,21),(4,1,89),(4,2,36),(4,3,74),(4,4,27),(4,5,32),(4,6,97),(4,7,47),(4,8,11),(4,9,94),(4,10,69),(4,11,49),(4,12,1),(4,13,95),(4,14,93),(4,15,86),(4,16,96),(5,1,0),(5,2,13),(5,3,60),(5,4,25),(5,5,70),(5,6,4),(5,7,20),(5,8,65),(5,9,90),(5,10,24),(5,11,89),(5,12,49),(5,13,21),(5,14,59),(6,1,37),(6,2,48),(6,3,53),(6,4,74),(7,1,92),(7,2,87),(7,3,17),(7,4,89),(7,5,40),(7,6,26),(7,7,42),(7,8,38),(7,9,71),(7,10,39),(7,11,94),(7,12,64),(7,13,1),(8,1,5),(8,2,22),(8,3,27),(8,4,3),(8,5,7),(8,6,60),(8,7,92),(8,8,44),(8,9,58),(9,1,5),(9,2,47),(9,3,92),(9,4,33),(9,5,48),(9,6,26),(9,7,25),(9,8,63),(9,9,24),(9,10,93),(9,11,18),(9,12,47),(9,13,44),(10,1,80),(10,2,40),(10,3,18),(10,4,63),(10,5,23),(10,6,59),(10,7,95),(10,8,1),(10,9,87),(10,10,81),(10,11,36),(10,12,67),(10,13,87),(10,14,70),(11,1,13),(11,2,99),(11,3,72),(11,4,24),(11,5,79),(11,6,90),(11,7,81),(11,8,28),(11,9,70),(11,10,4),(11,11,33),(11,12,36),(11,13,76),(11,14,81),(11,15,49),(11,16,4),(11,17,42),(12,1,65),(12,2,8),(12,3,54),(12,4,67),(12,5,40),(12,6,37),(12,7,57),(12,8,41),(12,9,98),(12,10,25),(12,11,10),(12,12,70),(12,13,94),(12,14,41),(12,15,73),(12,16,14),(12,17,49),(12,18,71),(12,19,13),(12,20,76),(12,21,48),(12,22,60),(13,1,49),(13,2,42),(13,3,69),(13,4,95),(13,5,37),(13,6,59),(13,7,83),(13,8,46),(13,9,92),(13,10,42),(13,11,19),(13,12,86),(13,13,38),(13,14,13),(14,1,62),(14,2,42),(14,3,48),(14,4,16),(14,5,11),(14,6,72),(14,7,67),(14,8,47),(14,9,25),(14,10,76),(14,11,62),(14,12,48),(14,13,30),(14,14,48),(14,15,35),(14,16,97),(14,17,32),(14,18,2),(14,19,47),(14,20,99),(14,21,9),(14,22,91),(14,23,33),(14,24,84),(15,1,77),(15,2,20),(15,3,58),(15,4,10),(15,5,2),(15,6,50),(15,7,9),(15,8,79),(15,9,75),(15,10,74),(15,11,66),(15,12,77),(15,13,22),(15,14,24),(15,15,83),(15,16,56),(15,17,22),(15,18,39),(15,19,70),(15,20,36),(15,21,89),(15,22,7),(16,1,77),(16,2,5),(16,3,91),(16,4,41),(16,5,27),(16,6,4),(16,7,49),(16,8,80),(16,9,54),(16,10,97),(16,11,68),(16,12,91),(16,13,11),(16,14,93),(16,15,7),(16,16,92),(17,1,22),(17,2,47),(17,3,93),(17,4,43),(17,5,38),(17,6,48),(17,7,73),(18,1,10),(18,2,3),(18,3,66),(18,4,76),(18,5,7),(18,6,17),(18,7,47),(18,8,29),(18,9,34),(18,10,31),(18,11,6),(18,12,36),(19,1,94),(19,2,60),(19,3,81),(19,4,40),(19,5,37),(19,6,76),(19,7,88),(19,8,49),(19,9,38),(19,10,85),(19,11,58),(19,12,87),(19,13,75),(20,1,57),(20,2,13),(20,3,75),(20,4,82),(20,5,97),(20,6,52),(20,7,89),(20,8,87),(21,1,86),(21,2,84),(21,3,24),(21,4,82),(21,5,29),(21,6,95),(21,7,26),(21,8,85),(21,9,70),(21,10,48),(21,11,86),(21,12,73),(21,13,4),(21,14,19),(21,15,61),(21,16,89),(21,17,48),(21,18,77),(21,19,56),(21,20,98),(21,21,12),(21,22,57),(21,23,89),(21,24,28),(21,25,16),(21,26,66),(22,1,86),(22,2,74),(22,3,5),(22,4,42),(22,5,66),(22,6,5),(22,7,7),(22,8,91),(22,9,68),(22,10,10),(22,11,34),(22,12,38),(22,13,98),(22,14,47),(22,15,69),(22,16,39),(22,17,18),(23,1,86),(23,2,82),(23,3,73),(23,4,27),(23,5,74),(23,6,52),(23,7,85),(24,1,18),(24,2,46),(24,3,40),(24,4,78),(24,5,32),(24,6,89),(24,7,93),(24,8,97),(24,9,7),(24,10,13),(24,11,7),(24,12,28),(24,13,12),(24,14,96),(24,15,37),(24,16,19),(24,17,63),(25,1,99),(25,2,62),(25,3,50),(25,4,13),(25,5,94),(25,6,23),(25,7,66),(25,8,84),(25,9,60),(25,10,71),(25,11,16),(25,12,46),(25,13,90),(25,14,12),(25,15,83),(25,16,74),(25,17,26),(25,18,63),(25,19,80),(25,20,7),(25,21,88),(25,22,9),(25,23,28),(25,24,17);
/*!40000 ALTER TABLE `books_at_libraries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Horror'),(2,'fiction'),(3,'non-fiction'),(4,'mystery'),(5,'fantasy'),(6,'science fiction'),(7,'biography'),(8,'romance'),(9,'history'),(10,'self-help'),(11,'children\'s literature'),(12,'poetry'),(13,'thriller'),(14,'adventure'),(15,'cookbooks'),(16,'graphic novels');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries`
--

DROP TABLE IF EXISTS `libraries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libraries` (
  `library_id` int NOT NULL AUTO_INCREMENT,
  `address_id` int NOT NULL,
  `library_name` varchar(100) NOT NULL,
  `library_details` text NOT NULL,
  PRIMARY KEY (`library_id`),
  KEY `fk_LIBRARIES_ADDRESSES1_idx` (`address_id`),
  CONSTRAINT `fk_LIBRARIES_ADDRESSES1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries`
--

LOCK TABLES `libraries` WRITE;
/*!40000 ALTER TABLE `libraries` DISABLE KEYS */;
INSERT INTO `libraries` VALUES (1,22,'Gonzalez-Martinez library','Current leave unit degree shoulder alone.'),(2,10,'Banks-Torres library','Enough thought interest there while wait create individual world next science where data.'),(3,15,'Guerra and Sons library','Keep south must guy north citizen.'),(4,23,'Anderson-Ortega library','Seven coach strong time book writer father force.'),(5,19,'Nguyen and Sons library','Follow quality hundred area money owner.'),(6,7,'Russell, Wallace and Ward library','Teach reason keep run matter of low food house feeling mouth.'),(7,20,'Mcconnell-Wright library','Tonight parent deep follow town their figure newspaper meet baby.'),(8,6,'Lopez LLC library','Forward yard at short young whatever soon speech soldier left wife.'),(9,8,'Huang, Humphrey and Riley library','Bill community mouth reduce outside level.'),(10,6,'Manning, Stark and Morris library','Happen fill need reality white agent us go cell item especially walk.'),(11,24,'Carter-Oliver library','Same explain break citizen official success strong natural area house hospital professor meet.'),(12,6,'Garcia, Perkins and Myers library','Push experience image during miss pay someone stock reality budget sure movement smile foot.'),(13,24,'Gordon Inc library','Ground series why enjoy collection fear whose factor.'),(14,7,'Poole LLC library','At serious try animal community personal growth but vote travel.'),(15,12,'Lewis, Curtis and Ryan library','Here radio price crime book result side here clearly wrong mission doctor of.'),(16,6,'Turner, Walker and Odom library','To reason fly at yet news in year until wide cold theory.'),(17,3,'Sanchez PLC library','Structure knowledge environment training news true.'),(18,6,'Williams, Clark and Carrillo library','Bit they upon effort strong ready billion firm consumer thank.'),(19,10,'Brown-Mathis library','Difference next middle travel director law father born not technology himself should.'),(20,3,'Adkins-Smith library','Certainly than less single computer pressure range stop upon.'),(21,20,'Jackson PLC library','Health treat teach article wait similar when bank loss or prevent.'),(22,21,'Russell-Collins library','Wonder voice morning trip million feeling environment race might class rest.'),(23,16,'Suarez-Lang library','Nearly garden ten house staff game effect artist management better share around mind.'),(24,19,'Miles, Thomas and Lewis library','Range word season state lot smile.'),(25,7,'Valencia-Clark library','For idea themselves maybe Mrs reach third risk career executive discussion.'),(26,9,'Adkins, Brown and Byrd library','Kitchen build economic radio it mention purpose range someone line many central others.');
/*!40000 ALTER TABLE `libraries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_request`
--

DROP TABLE IF EXISTS `member_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_request` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `book_id` int NOT NULL,
  `date_requested` date NOT NULL,
  `date_located` date NOT NULL,
  `other_request` text,
  PRIMARY KEY (`request_id`),
  KEY `fk_MEMBERS_has_BOOKS_BOOKS1_idx` (`book_id`),
  KEY `fk_MEMBERS_has_BOOKS_MEMBERS1_idx` (`member_id`),
  CONSTRAINT `fk_MEMBERS_has_BOOKS_BOOKS1` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`),
  CONSTRAINT `fk_MEMBERS_has_BOOKS_MEMBERS1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_request`
--

LOCK TABLES `member_request` WRITE;
/*!40000 ALTER TABLE `member_request` DISABLE KEYS */;
INSERT INTO `member_request` VALUES (1,13,20,'1975-10-14','1975-10-14','Mouth who here possible leave budget bed old fish southern teach involve.'),(2,11,4,'2024-04-13','2024-04-13','Write people quality machine against speak establish apply note magazine personal.'),(3,16,3,'1982-07-18','1982-07-18','Center no discussion common design whatever wait who sort think long.'),(4,15,3,'1999-06-25','1999-06-25','Spring forward key deal nothing study sign situation study.'),(5,21,25,'1984-11-17','1984-11-17','Forget protect road without large or every image talk maintain here.'),(6,15,22,'1989-10-05','1989-10-05','Apply role participant rule yourself language big theory little.'),(7,20,26,'2005-08-09','2005-08-09','Watch consider lead exist media it support million field doctor service between kid.'),(8,23,8,'2006-09-15','2006-09-15','Process brother population seem television voice this hold war.'),(9,6,2,'2005-02-23','2005-02-23','Early experience subject keep discussion meet yourself current thousand beat throughout.'),(10,4,10,'2003-12-28','2003-12-28','Environment little month energy inside parent.'),(11,22,9,'2007-03-30','2007-03-30','Job because understand where there safe think they mention.'),(12,15,7,'1976-05-14','1976-05-14','Common oil prepare memory tough response.'),(13,12,4,'2014-03-11','2014-03-11','Behavior type group pick entire second ten available tree town.'),(14,16,3,'2014-11-27','2014-11-27','Coach stay across base sing similar agent fill drive tend.'),(15,5,18,'1973-01-13','1973-01-13','Across religious draw reach price front involve road.'),(16,1,2,'1993-07-26','1993-07-26','Example say onto sure happy his develop five between stay.'),(17,25,24,'2013-03-26','2013-03-26','Space commercial popular kind miss prove father me realize oil parent.'),(18,24,26,'2021-06-13','2021-06-13','Choose population value data discover watch yard food almost participant account visit.'),(19,6,9,'2008-07-28','2008-07-28','Which since seem whole training serious big threat staff.'),(20,13,22,'1981-11-11','1981-11-11','Choice under stay shake reach summer develop detail wife.'),(21,25,4,'2015-02-12','2015-02-12','Condition fight us cold phone itself book set stuff voice light serve involve.'),(22,20,1,'2018-10-27','2018-10-27','Gas receive cold why it shoulder occur.'),(23,16,21,'1989-08-27','1989-08-27','Rock since hold situation international know animal society stock truth too some job.'),(24,23,19,'2023-02-09','2023-02-09','Pass suddenly growth goal ground either station itself television.'),(25,13,5,'1971-07-08','1971-07-08','Subject before term agency watch would north only agent defense prepare.'),(26,3,9,'1982-11-09','1982-11-09','Grow husband never machine operation run right.'),(27,2,5,'2024-01-01','2024-01-01','Make sure it\'s the 4th edition'),(28,2,4,'2024-02-02','2024-02-02','Make sure to keep it nice and warm'),(29,3,3,'2022-03-03','2022-03-03','GIvEEEE');
/*!40000 ALTER TABLE `member_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `member_address_id` int NOT NULL,
  `gender` tinyint NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `email_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`),
  KEY `fk_MEMBERS_ADDRESSES_idx` (`member_address_id`),
  CONSTRAINT `fk_MEMBERS_ADDRESSES` FOREIGN KEY (`member_address_id`) REFERENCES `addresses` (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,16,1,'Nicholas','Rosario','935.494.4571x2842','hmueller@example.org'),(2,4,0,'Dalton','Pierce','441-465-6799x04008','ngay@example.net'),(3,20,0,'William','Campbell','615.488.1647x7044','derek08@example.com'),(4,15,1,'Travis','Williams','8083676714','ldickson@example.org'),(5,5,0,'Brenda','Hebert','329-321-1368x8765','osbornemadison@example.org'),(6,19,1,'Paul','Kelly','001-256-449-2654x0730','jameskimberly@example.org'),(7,2,1,'Michael','Ruiz','8399382728','yhunter@example.com'),(8,13,0,'Andrew','Ward','5544154906','debra62@example.org'),(9,15,1,'John','Keller','(942)566-8044x639','catherinepowell@example.net'),(10,26,0,'Deborah','Pruitt','001-617-627-9238x0836','georgewalter@example.net'),(11,20,1,'Jennifer','Price','+1-991-674-6197x71113','wmahoney@example.net'),(12,13,0,'Bradley','Valdez','001-344-202-1696x2494','upollard@example.com'),(13,15,1,'Dale','Obrien','001-764-552-5086','nelsontimothy@example.net'),(14,24,0,'Joann','Reese','956-654-3632','michelle80@example.com'),(15,23,0,'Aaron','Benitez','(973)727-1404x8091','murphyjackie@example.org'),(16,17,0,'Lindsey','Evans','(775)517-4532','shepherdkaren@example.com'),(17,20,1,'Anthony','Jones','+1-796-598-8222x66951','qrobinson@example.net'),(18,22,1,'Mary','Lucero','320.529.1822','ksoto@example.net'),(19,2,1,'David','Stanley','+1-958-926-6528x79463','joshuapatel@example.org'),(20,19,0,'Lisa','Watson','886.998.0344','hardingjeremy@example.net'),(21,5,0,'Katherine','Reynolds','815-848-1046','michelle60@example.org'),(22,22,0,'Tony','Medina','001-327-827-4806','jacksonduran@example.com'),(23,3,0,'Amanda','Green','620.404.9481','washingtonkevin@example.net'),(24,8,0,'Jennifer','Hays','(339)489-6545','elizabeth12@example.net'),(25,24,0,'John','Thompson','969-311-4278','schmittmichael@example.org'),(26,24,0,'Ralph','Mitchell','(246)964-1345','smithmichael@example.org');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-14 11:40:11
