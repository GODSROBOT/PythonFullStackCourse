-- Aggregate Functions
-- COUNT(): Number of records
-- SUM(): Total value
-- AVG(): Average value
-- MIN(): Minimum value
-- MAX(): Maximum value

SELECT COUNT(*) FROM `school`.`student`; 
SELECT AVG(age) FROM `school`.`student`;

-- GROUP BY & HAVING

SELECT grade, COUNT(*) AS total_students 
FROM `school`.`student`
GROUP BY grade 
HAVING COUNT(*) > 2;