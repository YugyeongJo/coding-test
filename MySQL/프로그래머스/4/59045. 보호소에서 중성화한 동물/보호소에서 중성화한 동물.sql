-- 코드를 입력하세요


WITH A AS (SELECT ANIMAL_ID
            FROM ANIMAL_OUTS
            WHERE SEX_UPON_OUTCOME LIKE ('Spayed%')
            OR SEX_UPON_OUTCOME LIKE ('Neutered%'))

SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME
FROM ANIMAL_INS
INNER JOIN A
ON A.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE SEX_UPON_INTAKE LIKE ('Intact%')
;