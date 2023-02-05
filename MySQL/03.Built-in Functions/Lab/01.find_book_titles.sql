USE `book_library`;

SELECT `title`
FROM `books`
WHERE `title` LIKE 'The%'
ORDER BY `id`;

SELECT `title`
FROM `books`
WHERE SUBSTRING(`title`, 1, 3) = "The";