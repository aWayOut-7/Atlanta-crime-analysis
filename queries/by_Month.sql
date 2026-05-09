
SELECT     
    substr(OccurredFromDate, 1, instr(OccurredFromDate, '/') - 1) as MONTH,
    COUNT(*) AS monthly_count
FROM crimes WHERE OccurredFromDate != ''
GROUP BY MONTH 
ORDER BY CAST(MONTH AS INTEGER) ASC;