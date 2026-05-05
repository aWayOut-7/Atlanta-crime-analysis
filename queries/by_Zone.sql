SELECT Zone_int, COUNT(*) AS crime_count 
FROM crimes WHERE Zone_int != '' 
GROUP BY Zone_int ORDER BY crime_count DESC;   