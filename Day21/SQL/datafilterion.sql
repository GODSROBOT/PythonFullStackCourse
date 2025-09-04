-- Filtering Data
SELECT student_name, age 
FROM `school`.`student` 
WHERE age > 18 
ORDER BY age DESC 
LIMIT 5;

-- Get courses with credits >= 3 AND course_name contains 'Data'
SELECT course_name, credits
FROM `school`.`courses`
WHERE credits >= 3 AND course_name LIKE '%Data%';

-- Get credits with 3 or 4
SELECT course_name, credits
FROM `school`.`courses`
WHERE credits =3 OR credits=4;

-- Get courses whose credits are not 3
SELECT course_name, credits
FROM `school`.`courses`
WHERE NOT credits =3 ;

-- Get Courses with credits between 2 and 4
SELECT course_name, credits
FROM `school`.`courses`
WHERE credits BETWEEN 2 AND 4;

-- Get courses with credits 2,3,4
SELECT course_name, credits
FROM `school`.`courses`
WHERE credits IN(2,3,4);

-- courses starting with ‘Data’
SELECT course_name
FROM `school`.`courses`
WHERE course_name LIKE 'Data%';

-- Courses ending with 'ics'
SELECT course_name
FROM `school`.`courses`
WHERE course_name LIKE '%ics';

-- Courses with 'a' as the second character
SELECT course_name
FROM `school`.`courses`
WHERE course_name LIKE '_a%';