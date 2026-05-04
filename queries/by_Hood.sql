select nhoodname, COUNT(*) as nhood_crime_count from crimes where nhoodname != '' 
group by nhoodname order by nhood_crime_count desc;