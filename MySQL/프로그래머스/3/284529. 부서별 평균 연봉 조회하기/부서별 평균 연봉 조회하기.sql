-- 코드를 작성해주세요
SELECT HR_EMPLOYEES.DEPT_ID, HR_DEPARTMENT.DEPT_NAME_EN, ROUND(AVG(SAL), 0) AVG_SAL
FROM HR_EMPLOYEES 
LEFT JOIN HR_DEPARTMENT 
ON HR_DEPARTMENT.DEPT_ID = HR_EMPLOYEES.DEPT_ID
GROUP BY DEPT_ID
ORDER BY AVG_SAL DESC
;