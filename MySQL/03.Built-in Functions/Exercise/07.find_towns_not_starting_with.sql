USE `soft_uni`;

SELECT * FROM `towns`
WHERE `name` REGEXP "^[^rbd].*"
ORDER BY `name`;   


SELECT * FROM `towns`
WHERE `name` NOT LIKE ("r%")
	AND `name` NOT LIKE ("b%") 
    AND `name` NOT LIKE ("d%")
ORDER BY `name`;