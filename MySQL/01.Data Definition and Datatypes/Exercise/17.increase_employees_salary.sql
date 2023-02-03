USE `soft_uni`;

UPDATE `employees`
SET `salary` = `salary` * 1.10;
SELECT `salary` FROM `employees`;