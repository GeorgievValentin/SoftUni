CREATE DATABASE `gamebar`;

CREATE TABLE `gamebar`.`employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(30) NOT NULL,
    `last_name` VARCHAR(30) NOT NULL
);

CREATE TABLE `gamebar`.`categories` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL
);

CREATE TABLE `gamebar`.`products` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL,
    `category_id` INT NOT NULL
);

