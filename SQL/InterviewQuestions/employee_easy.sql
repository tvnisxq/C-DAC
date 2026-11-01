create database interview_questions;
USE interview_questions;
CREATE TABLE Employee(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(20),
    salary INT
);
SHOW TABLES;

INSERT INTO Employee (emp_id, emp_name, salary)
VALUES (1, 'Priya', 65000),
(2, 'Aman', 80000),
(3, 'Neha', 40000);

SHOW TABLES;
SELECT * FROM Employee;
SELECT * FROM Employee WHERE salary > 50000;