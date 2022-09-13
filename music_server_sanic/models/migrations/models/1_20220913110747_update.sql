-- upgrade --
CREATE TABLE IF NOT EXISTS `singer` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL,
    `sex` BOOL,
    `pic` VARCHAR(255),
    `birth` DATETIME(6),
    `location` VARCHAR(45),
    `introduction` VARCHAR(255)
) CHARACTER SET utf8mb4;;
CREATE TABLE IF NOT EXISTS `comment` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `song_id` INT NOT NULL,
    `song_list_id` INT NOT NULL,
    `content` VARCHAR(255),
    `create_time` DATETIME(6),
    `type` BOOL NOT NULL,
    `up` INT NOT NULL
) CHARACTER SET utf8mb4;;
CREATE TABLE IF NOT EXISTS `song` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `singer_id` INT NOT NULL,
    `name` VARCHAR(45) NOT NULL,
    `introduction` VARCHAR(255),
    `create_time` DATETIME(6) NOT NULL  COMMENT '发行时间',
    `update_time` DATETIME(6) NOT NULL,
    `pic` VARCHAR(255),
    `lyric` LONGTEXT,
    `url` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;;
CREATE TABLE IF NOT EXISTS `admin` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45) NOT NULL UNIQUE,
    `password` VARCHAR(45) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='管理员';;
CREATE TABLE IF NOT EXISTS `consumer` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(100) NOT NULL,
    `sex` BOOL,
    `phone_num` VARCHAR(15)  UNIQUE,
    `email` VARCHAR(50)  UNIQUE,
    `birth` DATETIME(6),
    `introduction` VARCHAR(255),
    `location` VARCHAR(45),
    `avator` VARCHAR(255),
    `create_time` DATETIME(6) NOT NULL,
    `update_time` DATETIME(6) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='普通用户';;
CREATE TABLE IF NOT EXISTS `collect` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `type` BOOL NOT NULL,
    `song_id` INT NOT NULL,
    `song_list_id` INT NOT NULL,
    `create_time` DATETIME(6) NOT NULL
) CHARACTER SET utf8mb4;;
CREATE TABLE IF NOT EXISTS `list_song` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `song_id` INT NOT NULL,
    `song_list_id` INT NOT NULL
) CHARACTER SET utf8mb4;;
CREATE TABLE IF NOT EXISTS `rank_list` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `songListId` BIGINT NOT NULL,
    `consumerId` BIGINT NOT NULL,
    `score` INT NOT NULL,
    KEY `idx_rank_list_songLis_9c7b52` (`songListId`),
    KEY `idx_rank_list_consume_4a9906` (`consumerId`)
) CHARACTER SET utf8mb4;;
CREATE TABLE IF NOT EXISTS `song_list` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `pic` VARCHAR(255),
    `introduction` LONGTEXT,
    `style` VARCHAR(10)   DEFAULT '无'
) CHARACTER SET utf8mb4;-- downgrade --
DROP TABLE IF EXISTS `singer`;
DROP TABLE IF EXISTS `comment`;
DROP TABLE IF EXISTS `song`;
DROP TABLE IF EXISTS `admin`;
DROP TABLE IF EXISTS `consumer`;
DROP TABLE IF EXISTS `collect`;
DROP TABLE IF EXISTS `list_song`;
DROP TABLE IF EXISTS `rank_list`;
DROP TABLE IF EXISTS `song_list`;
