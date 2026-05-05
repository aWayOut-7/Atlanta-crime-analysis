-- Analysis of crime incidents by Zone and Time of Day (ToD) in Atlanta, Georgia.
-- This query counts the number of crime incidents for each unique combination of Zone and ToD.
select zone_int, event_watch, COUNT(*) as incident_count
from crimes where zone_int != '' and event_watch != ''
group by event_watch, zone_int order by incident_count desc;
