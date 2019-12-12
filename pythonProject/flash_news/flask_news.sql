# Host: localhost  (Version: 5.5.53)
# Date: 2019-12-12 10:17:43
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "news"
#

DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` varchar(200) NOT NULL,
  `types` varchar(10) NOT NULL,
  `image` varchar(300) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `view_count` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_valid` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4;

#
# Data for table "news"
#

/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'1','1','推荐','/static/img/news/01.png','张三',87,'2019-12-12 09:48:03',1),(2,'2','2','百家','/static/img/news/02.png','张三',40,'2019-12-12 09:48:14',1),(3,'3','3','本地','/static/img/news/03.png','王五',46,'2019-12-12 09:48:28',1),(4,'4','4','图片','/static/img/news/04.png','王五',55,'2019-12-12 09:49:36',1),(5,'5','5','推荐','/static/img/news/05.png','路人甲',56,'2019-12-12 09:49:47',1),(6,'6','6','百家','/static/img/news/06.png','张三',23,'2019-12-12 09:50:13',1);
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
