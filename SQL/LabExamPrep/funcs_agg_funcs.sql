USE CompanyDB;

-- string numeric and date functions
SELECT
    emp_name,
    UPPER(emp_name) AS uppercase_name,
    CHAR_LENGTH(emp_name) AS name_length,
    salary * 12 AS annual_salary,
    ROUND(salary, 2) AS rounded_salary,
    YEAR(hire_date) AS joining_year
FROM Employee;

-- aggregate functions
SELECT 
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary,
    SUM(salary) AS total_salary
FROM Employee;

