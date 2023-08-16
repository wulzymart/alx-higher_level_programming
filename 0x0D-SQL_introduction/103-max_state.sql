-- script that displays the max temperature of each state (ordered by State name).
-- gets table of states and max temp using select, MAX and group by
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
