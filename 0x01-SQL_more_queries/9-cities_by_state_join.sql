-- Select cities from cities where statie_id = (select id from states where name = 'california')
SELECT id, name, (Select name from states WHERE id = state_id) as name FROM cities;