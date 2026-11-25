USE CompanyDB;

-- READ: Display all employees
SELECT * FROM Employee;

-- CREATE: Insert a new Employee
INSERT INTO Employee
VALUES (111, 'Pooja', 52000, 'Bengaluru', '2024-01-10', 1);

-- Filter Salary
SELECT * 
FROM Employee 
WHERE salary > 50000;

-- IN Operator
SELECT * 
FROM Employee
WHERE city IN ('Bengaluru', 'Mumbai');

-- BETWEEN
SELECT * 
FROM Employee
WHERE salary BETWEEN 40000 AND 60000;

-- LIKE 
SELECT * 
FROM Employee
WHERE emp_name LIKE '%A';

-- NULL Check
SELECT * 
FROM Employee
WHERE city IS NULL;

-- UPDATE
UPDATE Employee 
SET salary = 58000 
WHERE emp_id = 101;

-- DELETE 
DELETE FROM Employee
WHERE emp_id = 111;