-- Updating a view to include course names for students older than 18, ordered by age in descending order
CREATE OR REPLACE VIEW student_view AS
SELECT s.id, s.student_name, c.course_name
FROM school.student s
JOIN school.courses c ON s.id = c.course_id
WHERE s.age > 18
ORDER BY s.age DESC;

SELECT * FROM student_view ;
