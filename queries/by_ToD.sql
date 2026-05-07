-- Analysis of crime incidents by Time of Day (ToD) in Atlanta, Georgia.
-- This query counts the number of crime incidents for each unique Time of Day (ToD) 
-- Excludes empty ToD values
select event_watch, COUNT(*) as incident_count
from crimes where event_watch != ''
group by event_watch
order by incident_count desc;
