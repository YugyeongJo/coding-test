-- 코드를 입력하세요
SELECT FIRST_HALF.FLAVOR
FROM FIRST_HALF 
LEFT OUTER JOIN JULY
ON FIRST_HALF.FLAVOR = JULY.FLAVOR
GROUP BY FLAVOR
ORDER BY SUM(FIRST_HALF.TOTAL_ORDER) DESC
LIMIT 3
;