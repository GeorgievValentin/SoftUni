USE `movies`;

CREATE TABLE `directors`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`director_name` VARCHAR(30) NOT NULL,
	`notes` TEXT
);

INSERT INTO `directors`(`director_name`, `notes`)
VALUES
	("director 1", "note 1"),
	("director 2", "note 2"),
	("director 3", "note 3"),
	("director 4", "note 4"),
	("director 5", "note 5");
	

CREATE TABLE `genres`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `genre_name` VARCHAR(30) NOT NULL,
    `notes` TEXT
);

INSERT INTO `genres`(`genre_name`, `notes`)
VALUES
	("genre 1", "note 1"),
	("genre 2", "note 2"),
	("genre 3", "note 3"),
	("genre 4", "note 4"),
	("genre 5", "note 5");

CREATE TABLE `categories`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `category_name` VARCHAR(30) NOT NULL,
    `notes` TEXT
);

INSERT INTO `categories`(`category_name`)
VALUES
	("category 1"),
	("category 1"),
	("category 1"),
	("category 1"),
	("category 1");

CREATE TABLE `movies`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(50) NOT NULL,
    `director_id` INT, 
    `copyright_year` INT,
    `length` DOUBLE(6,2),
    `genre_id` INT,
    `category_id` INT,
    `rating` INT,
    `notes` TEXT
);

INSERT INTO `movies`(`title`)
VALUES
	("title 1"),
	("title 2"),
	("title 3"),
	("title 4"),
	("title 5");
