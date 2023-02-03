USE `car_rental`;

CREATE TABLE `categories`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `category` VARCHAR(30),
    `dayly_rate` DOUBLE,
    `weekly_rate` DOUBLE,
    `montly_rate` DOUBLE,
    `weekend_rate` DOUBLE
);

INSERT INTO `categories`(`category`)
	VALUES
		("Category 1"),
		("Category 2"),
		("Category 3");

CREATE TABLE `cars`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `plate_number` VARCHAR(20),
	`make` VARCHAR(30),
    `model` VARCHAR(30),
    `car_year` INT,
    `category_id` INT,
    `doors` INT,
    `picture` BLOB,
    `car_condition` VARCHAR(30),
    `available` BOOLEAN
);

INSERT INTO `cars`(`plate_number`)
	VALUES
		("AA 1111 AA"),
		("BB 2222 B"),
		("C 3333 CC");

CREATE TABLE `employees`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(30),
    `last_name` VARCHAR(30),
    `title` VARCHAR(30),
    `notes` TEXT
);

INSERT INTO `employees`(`first_name`, `last_name`)
	VALUES
		("First 1", "Last 1"),
		("First 2", "Last 2"),
		("First 3", "Last 3");

CREATE TABLE `customers`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `driver_licence_number` VARCHAR(30),
    `full_name` VARCHAR(30),
    `address` VARCHAR(30),
    `city` VARCHAR(30),
    `zip_code` VARCHAR(30),
    `notes` TEXT
);

INSERT INTO `customers`(`driver_licence_number`, `full_name`)
	VALUES 
		("Number 1", "Test Testov 1"),
		("Number 2", "Test Testov 2"),
		("Number 3", "Test Testov 3");

CREATE TABLE `rental_orders`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `employee_id` INT,
    `customer_id` INT,
    `car_id` INT,
    `car_condition` VARCHAR(30),
    `tank_level` VARCHAR(30),
    `kilometrage_start` DOUBLE,
    `kilometrage_end` DOUBLE,
    `total_kilometrage` DOUBLE,
    `start_date` DATE,
    `end_date` DATE,
    `total_days` INT,
    `rate_applied` DOUBLE,
    `tax_rate` DOUBLE,
    `order_status` VARCHAR(30),
    `notes` TEXT
);

INSERT INTO `rental_orders`(`employee_id`, `customer_id`, `car_id`)
	VALUES
		(1, 4, 7),
		(2, 5, 8),
		(3, 6, 9);


