CREATE OR REPLACE VIEW higher_age_students AS
SELECT s.id, s.student_name, s.age
FROM school.student s
WHERE s.age > 20;

-- SELECT * FROM higher_age_students;a
