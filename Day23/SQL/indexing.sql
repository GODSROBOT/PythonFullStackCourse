-- Creating an index on the email column for faster searches
CREATE INDEX idx_email ON school.student(email);
SELECT * FROM school.student WHERE email = 'manoj@example.com';

-- after everything we need to delete that index to not slow our DB

-- DROP INDEX idx_email;