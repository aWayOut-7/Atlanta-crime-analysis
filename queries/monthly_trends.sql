-- Analysis of crime trends by month in Atlanta, Georgia.
-- This query counts the # of crime incidents for each month, excluding empty month values, and in descending order.
--strftime(format, date) is used to extract the month & year from the occuredFromDate column
select DISTINCT strftime('%Y-%m', OccurredFromDate) as Monthly_Count, COUNT(*) as monthly_crime_count
from crimes where OccurredFromDate != '' 
group by Monthly_Count 
order by monthly_crime_count desc;

