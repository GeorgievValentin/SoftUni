USE `book_library`;

SELECT `title` 
FROM `books`
WHERE `title` LIKE "harry potter%"
ORDER BY `id`;