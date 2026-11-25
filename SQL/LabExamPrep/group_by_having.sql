-- Question: Find department-wise employee count, 
-- average salary, and departments 
-- having more than two employees. 
-- Display employee names with department names, 
-- and show departments even if they have no employees.

USE CompanyDB;

SELECT 
    dept_id,
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary,
    SUM(salary) AS total_salary
FROM Employee
GROUP BY dept_id;


SELECT 
    dept_id,
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary
FROM Employee
GROUP BY dept_id
HAVING COUNT(*) > 2
    AND AVG(salary) > 40000;
