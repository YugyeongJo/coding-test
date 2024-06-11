WITH RECURSIVE cte AS
(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1 AS HOUR
    FROM cte 
    WHERE HOUR < 23
)

SELECT cte.HOUR, COUNT(HOUR(ANIMAL_OUTS.DATETIME)) AS COUNT
FROM cte
LEFT JOIN ANIMAL_OUTS 
ON cte.HOUR = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR
;