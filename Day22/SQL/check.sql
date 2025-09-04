-- This ensure the table to check weather the age is above the given rule 
CREATE OR REPLACE VIEW student_view AS
SELECT s.id, s.student_name, c.course_name, s.age
FROM school.student s
JOIN school.courses c ON s.id = c.course_id
WHERE s.age > 18
WITH CHECK OPTION;
-- This ensures the table to check whether the age is above the given rule
SELECT * 
FROM student_view 
WHERE age >= 19;
