-- Displace Scores and how often they occure
SELECT score, COUNT(*) FROM second_table GROUP BY score;