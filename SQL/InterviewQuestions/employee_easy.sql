show databases;
use interview_questions;
show tables;

CREATE TABLE Emplopyee(
	emp_id INT PRIMARY KEY,
    emp_name VARCHAR(20),
    salary INT
);

INSERT INTO Emplopyee (emp_id, emp_name, salary)
VALUES(1, 'Rahul', 45000),
(2, 'Priya', 65000),
(3, 'Aman', 80000),
(4, 'Neha', 40000);

SHOW TABLES;
SELECT * FROM Emplopyee;

SELECT * FROM Emplopyee WHERE salary > 50000;