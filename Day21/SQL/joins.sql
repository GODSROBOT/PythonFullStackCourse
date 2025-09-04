-- INNER JOIN
SELECT s.student_name, c.course_name
FROM school.student s
INNER JOIN school.enrollments e ON s.id = e.student_id
INNER JOIN school.courses c ON e.course_id = c.course_id;


-- LEFT JOIN
SELECT s.student_name, c.course_name
FROM school.student s
LEFT JOIN school.enrollments e ON s.id = e.student_id
LEFT JOIN school.courses c ON e.course_id = c.course_id;



-- RIGHT JOIN
SELECT s.student_name, c.course_name
FROM school.student s
RIGHT JOIN school.enrollments e ON s.id = e.student_id
RIGHT JOIN school.courses c ON e.course_id = c.course_id;


-- FULL JOIN
SELECT s.student_name, c.course_name
FROM school.student s
LEFT JOIN school.enrollments e ON s.id = e.student_id
LEFT JOIN school.courses c ON e.course_id = c.course_id

UNION

SELECT s.student_name, c.course_name
FROM school.student s
RIGHT JOIN school.enrollments e ON s.id = e.student_id
RIGHT JOIN school.courses c ON e.course_id = c.course_id;
