# -- 코드를 입력하세요

SELECT CRCC.CAR_ID, CRCC.CAR_TYPE, ROUND((CRCC.DAILY_FEE*CRCDP.RATE*30), 0) AS FEE
FROM (SELECT CAR_ID, CAR_TYPE, DAILY_FEE
        FROM CAR_RENTAL_COMPANY_CAR 
        WHERE CAR_TYPE IN ("세단", "SUV")) AS CRCC
JOIN (SELECT CAR_ID
           FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
           WHERE CAR_ID NOT IN (SELECT CAR_ID
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                    WHERE START_DATE <= '2022-11-30'
                    AND END_DATE >= '2022-11-01')) AS CRCRH
ON CRCC.CAR_ID = CRCRH.CAR_ID
JOIN (SELECT CAR_TYPE, 1-DISCOUNT_RATE*0.01 AS RATE
            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
            WHERE DURATION_TYPE = "30일 이상") AS CRCDP
ON CRCDP.CAR_TYPE = CRCC.CAR_TYPE
WHERE (CRCC.DAILY_FEE*CRCDP.RATE*30) >= 500000
AND (CRCC.DAILY_FEE*CRCDP.RATE*30) < 2000000
GROUP BY CRCC.CAR_ID
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC

;