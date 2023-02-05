USE `book_library`;

SELECT ROUND(SUM(`cost`), 2) AS "Total cost"
FROM `books`;