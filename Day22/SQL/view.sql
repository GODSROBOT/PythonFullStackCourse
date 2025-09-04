-- Creating a View Table in SQL
CREATE OR REPLACE VIEW student_view AS
SELECT s.id, s.student_name, c.course_name,
FROM school.student s
JOIN school.courses c ON s.id = c.course_id;
-- Now for Viewing that table in the SQLs
SELECT * FROM student_view;

-- This is to select a particular student or data
SELECT * FROM student_view WHERE student_name = 'Rahul';

