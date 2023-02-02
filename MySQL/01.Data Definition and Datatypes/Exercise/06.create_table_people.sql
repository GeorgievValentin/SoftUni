USE `level_2`;

CREATE TABLE `people` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL ,
    `picture` BLOB,
    `height` DOUBLE(5, 2),
    `weight` DOUBLE(5, 2),
    `gender` CHAR(1) NOT NULL,
    `birthdate` DATE NOT NULL,
    `biography` TEXT
);

INSERT INTO `people` (`name`, `height`,  `gender`, `birthdate`)
VALUES
	("Ivan", 1.71, "m", "1980-12-17"),
	("Asen", 1.82, "m", "1996-07-21"),
	("Peter", 1.69, "m", "2002-01-07"),
	("Maria", 1.73, "f", "1993-03-03"),
	("Gergana", 0.52, "f", DATE(NOW()));