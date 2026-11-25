-- Inner Join
USE CompanyDB;

SELECT * FROM Employee;
SELECT * FROM Department;

SELECT
    e.emp_name,
    e.salary,
    d.dept_name,
    d.location
FROM Employee e
INNER JOIN Department d
    ON e.dept_id = d.dept_id;


SELECT 
    d.dept_name,
    e.emp_name,
    e.salary
FROM Department d
LEFT JOIN Employee e 
    ON d.dept_id = e.dept_id;

