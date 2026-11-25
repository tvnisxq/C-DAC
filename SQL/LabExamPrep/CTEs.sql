-- Create a CTE for department statistics.
--  Display departments with average salaries
-- above ₹50,000, classify employees into salary 
-- categories, and count each category by department.

WITH DeptStats AS ( 
    SELECT 
        dept_id,
        COUNT(*) AS employee_count,
        AVG(salary) AS avg_salary,
        MAX(salary) AS max_salary
    FROM Employee
    GROUP BY dept_id
)

SELECT * 
FROM DeptStats
WHERE avg_salary > 50000;