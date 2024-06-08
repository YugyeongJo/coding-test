-- 코드를 작성해주세요
SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
FROM ITEM_INFO AS A
LEFT JOIN ITEM_TREE AS B
ON B.ITEM_ID = A.ITEM_ID
WHERE B.PARENT_ITEM_ID IN (SELECT ITEM_ID 
                           FROM ITEM_INFO 
                           WHERE RARITY='RARE')
ORDER BY A.ITEM_ID DESC
;