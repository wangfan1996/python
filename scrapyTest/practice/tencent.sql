# Host: localhost  (Version: 5.5.53)
# Date: 2019-12-17 17:00:00
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "tencent"
#

DROP TABLE IF EXISTS `tencent`;
CREATE TABLE `tencent` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `RecruitPostName` varchar(255) DEFAULT NULL,
  `PostId` varchar(255) DEFAULT NULL,
  `RecruitPostId` varchar(255) DEFAULT NULL,
  `CountryName` varchar(255) DEFAULT NULL,
  `LocationName` varchar(255) DEFAULT NULL,
  `BGName` varchar(255) DEFAULT NULL,
  `ProductName` varchar(255) DEFAULT NULL,
  `CategoryName` varchar(255) DEFAULT NULL,
  `Responsibility` varchar(255) DEFAULT NULL,
  `LastUpdateTime` varchar(255) DEFAULT NULL,
  `PostURL` varchar(255) DEFAULT NULL,
  `SourceID` varchar(255) DEFAULT NULL,
  `IsCollect` varchar(255) DEFAULT NULL COMMENT '0false  1true',
  `IsValid` varchar(255) DEFAULT NULL COMMENT '0false 1true',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4143 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;
