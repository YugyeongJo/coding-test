-- 코드를 입력하세요
# PATIENT, DOCTOR 그리고 APPOINTMENT 테이블에서 
# 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요. 
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성해주세요. 
# 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.
WITH A AS (SELECT *
            FROM APPOINTMENT
            WHERE DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
            AND MCDP_CD = 'CS'
            AND APNT_CNCL_YN = 'N')
            
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM A
LEFT JOIN PATIENT AS P
ON P.PT_NO = A.PT_NO
LEFT JOIN DOCTOR  AS D
ON D.DR_ID = A.MDDR_ID
ORDER BY APNT_YMD ASC

;