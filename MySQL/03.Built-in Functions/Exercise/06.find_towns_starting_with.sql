USE `soft_uni`;

SELECT * FROM `towns`
WHERE `name` REGEXP "^[mkbe].*"
ORDER BY `name`;   

SELECT * FROM `towns`
WHERE `name` LIKE "m%" 
	OR `name` LIKE "k%" 
    OR `name` LIKE "b%" 
    OR `name` LIKE "e%"
ORDER BY `name`;

