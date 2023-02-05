USE `book_library`;

SELECT REPLACE(`title`, "The", "***") 
AS "Title"
FROM `books`
WHERE `title` LIKE "The%"
ORDER BY `id`;