-- 코드를 입력하세요
WITH A AS (SELECT BOARD_ID
            FROM USED_GOODS_BOARD
            ORDER BY VIEWS DESC
            LIMIT 1)
            
SELECT CONCAT("/home/grep/src/", USED_GOODS_FILE.BOARD_ID, "/", USED_GOODS_FILE.FILE_ID, USED_GOODS_FILE.FILE_NAME, USED_GOODS_FILE.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE 
INNER JOIN A 
ON USED_GOODS_FILE.BOARD_ID = A.BOARD_ID
ORDER BY USED_GOODS_FILE.FILE_ID DESC
;