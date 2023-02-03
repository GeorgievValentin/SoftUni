USE `soft_uni`;

CREATE TABLE `towns`(
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

INSERT INTO `towns`(`name`)
	VALUES
		("Sofia"),
		("Plovdiv"),
		("Varna"),
		("Burgas");

CREATE TABLE `addresses`(
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `address_text` VARCHAR(255) NOT NULL,
    `town_id` INT NOT NULL
);

CREATE TABLE `departments`(
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);

INSERT INTO `departments`(`name`)
	VALUES
		("Engineering"),
		("Sales"),
		("Marketing"),
		("Software Development"),
		("Quality Assurance");
		
CREATE TABLE `employees`(
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(30) NOT NULL,
    `middle_name` VARCHAR(30) NOT NULL,
    `last_name` VARCHAR(30) NOT NULL,
    `job_title` VARCHAR(30) NOT NULL,
    `department_id` INT NOT NULL,
    `hire_date` DATE,
    `salary` DECIMAL(10,2),
    `address_id` INT
);

INSERT INTO `employees`(`first_name`, `middle_name`, `last_name`, `job_title`, `department_id`, `hire_date`, `salary`)
	VALUES
		("Ivan", "Ivanov", "Ivanov", ".NET Developer", 4, "2013-02-01", 3500.00),
		("Petar", "Petrov", "Petrov", "Senior Engineer", 1, "2004-03-02", 4000.00),
		("Maria", "Petrova", "Ivanova", "Intern", 5, "2016-008-28", 525.25),
		("Georgi", "Terziev", "Ivanov", "CEO", 2, "2007-12-09", 3000.00),
		("Peter", "Pan", "Pan", "Intern", 3, "2016-08-28", 599.88);