-- number by score
SELECT score AS 'score', COUNT(*) AS 'number' FROM second_table GROUP BY score ORDER BY score DESC;
