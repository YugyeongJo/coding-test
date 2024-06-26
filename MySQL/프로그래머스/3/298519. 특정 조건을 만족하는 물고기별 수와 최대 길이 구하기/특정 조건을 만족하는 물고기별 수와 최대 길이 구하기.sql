# -- 코드를 작성해주세요
WITH FISH_INFO_NOTNULL AS (
                            SELECT ID, FISH_TYPE, IFNULL(LENGTH, 10) AS LENGTH, TIME
                            FROM FISH_INFO)
                            
SELECT COUNT(FISH_TYPE) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM FISH_INFO_NOTNULL
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE 
;