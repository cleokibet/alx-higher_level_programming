-- This will give lists of number of records with the same score in the table second_table in my MySQL server.
-- And records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
