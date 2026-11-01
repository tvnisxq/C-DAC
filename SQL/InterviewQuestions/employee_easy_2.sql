SHOW TABLES;
SELECT * FROM Employee;

SELECT MAX(salary) as second_highest_salary 
FROM Employee 
WHERE
salary < (SELECT MAX(salary) 
FROM Employee);
