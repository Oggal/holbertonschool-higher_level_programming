-- Displace Scores and how often they occure
SELECT score, COUNT(*) AS score,number FROM second_table GROUP BY score;