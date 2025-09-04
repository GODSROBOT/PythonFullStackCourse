-- Active: 1750844122550@@127.0.0.1@3306
CREATE TABLE `school`.`student` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0),
    grade VARCHAR(10) DEFAULT 'NA'
);

CREATE TABLE `school`.`courses` ( 
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL UNIQUE, 
    credits INT CHECK (credits > 0)
);