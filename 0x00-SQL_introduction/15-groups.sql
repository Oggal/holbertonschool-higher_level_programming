-- Displace Scores and how often they occure
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;