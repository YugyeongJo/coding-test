-- 코드를 입력하세요
# SELECT CAR_ID, 
#     CASE
#         WHEN START_DATE > '2022-10-16' THEN '대여 가능'
#         WHEN START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16' THEN '대여중'
#         WHEN END_DATE < '2022-10-16' THEN '대여 가능'
#     END AS AVAILABILITY
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# GROUP BY 1
# ORDER BY 1 DESC

# with shortlist as (
# select car_id
# from car_rental_company_rental_history
# where '2022-10-16' between start_date and end_date)

# SELECT distinct car_id,
# case
# when car_id in (select car_id from shortlist) then '대여중'
# else '대여 가능'
# end availability
# from car_rental_company_rental_history
# order by 1 desc;

WITH SORT_LIST AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE
    )
    
SELECT CAR_ID, 
    CASE
        WHEN CAR_ID IN (SELECT CAR_ID FROM SORT_LIST) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY 1
ORDER BY 1 DESC
;