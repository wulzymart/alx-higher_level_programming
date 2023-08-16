-- script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT month, city, AVG(value) as avg_temp FROM temperatures GROUP BY month ORDER BY avg_temp DESC;
