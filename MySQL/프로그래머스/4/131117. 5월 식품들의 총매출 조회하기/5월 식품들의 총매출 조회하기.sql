-- 코드를 입력하세요
# FOOD_PRODUCT와 FOOD_ORDER 테이블에서 
# 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 
# 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 
# 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.
WITH A AS (
            SELECT PRODUCT_ID, PRODUCE_DATE, AMOUNT
            FROM FOOD_ORDER 
            WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
            ) 
            
SELECT A.PRODUCT_ID, FP.PRODUCT_NAME, (SUM(AMOUNT)*FP.PRICE) AS TOTAL_SALES
FROM A
INNER JOIN FOOD_PRODUCT AS FP  
ON FP.PRODUCT_ID = A.PRODUCT_ID
GROUP BY PRODUCT_ID 
ORDER BY TOTAL_SALES DESC, PRODUCT_ID
;