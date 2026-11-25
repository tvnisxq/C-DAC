USE CompanyDB;

-- subqueries and correlated subqueries
-- 1. Employees earning more than the company average(Scakar subquety)
SELECT emp_name, salary
FROM Employee
WHERE salary > (
    SELECT AVG(salary)
    FROM Employee
);

-- 2. Employees earning more than their departments average(Correlated subquery)
SELECT e.emp_name, e.salary, e.dept_id
FROM Employee e 
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM Employee e2
    WHERE e2.dept_id = e.dept_id
);

-- 3. Finding the Employee tied fort the highest salary in their department

SELECT e.emp_name, e.salary, e.dept_id
FROM Employee e 
WHERE e.salary = ( 
    SELECT MAX(e2.salary)
    FROM Employee e2
    WHERE e2.dept_id = e.dept_id
);

-- 4. EXISTS 
SELECT d.dept_name
FROM Department d 
WHERE EXISTS ( 
    SELECT 1
    FROM Employee e 
    WHERE e.dept_id = d.dept_id
); 

