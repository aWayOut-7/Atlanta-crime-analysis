-- Analysis of crime trends by month in Atlanta, Georgia.
-- This query counts the # of crime incidents for each month, excluding empty month values, and in descending order.
--strftime(format, date) is used to extract the month & year from the occuredFromDate column

-- ========== pruned lines below ==========
-- select strftime('%Y-%m', OccurredFromDate) as Monthly_Count, COUNT(*) AS monthly_crime_count
-- from crimes where OccurredFromDate != '' 
-- group by strftime('%Y-%m', OccurredFromDate) 
-- order by Monthly_Count desc;

-- SELECT OccurredFromDate FROM crimes WHERE OccurredFromDate != '' LIMIT 5;
-- ========== pruned lines above ==========

SELECT     
    substr(OccurredFromDate, instr(OccurredFromDate, ' ') - 4, 4 ) as YEAR,
    substr(OccurredFromDate, 1, instr(OccurredFromDate, '/') - 1) as MONTH,
    COUNT(*) AS monthly_crime_count
FROM crimes WHERE OccurredFromDate != ''
GROUP BY year, month 
HAVING CAST(year as INTEGER) >= 2021
ORDER BY year DESC, CAST(month AS INTEGER) DESC;
-- LIMIT 10;