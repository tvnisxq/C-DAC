CREATE DATABASE IF NOT EXISTS CompanyDB;
USE CompanyDB;

CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) UNIQUE NOT NULL,
    location VARCHAR(50)
);

CREATE TABLE Employee(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    city VARCHAR(50),
    hire_date DATE,
    dept_id INT,
    CONSTRAINT  chk_salary CHECK (salary > 0),
    CONSTRAINT fk_dept
        FOREIGN KEY (dept_id)
        REFERENCES Department(dept_id)
);


INSERT INTO Department VALUES
(1, 'IT', 'Bengaluru'),
(2, 'HR', 'Mumbai'),
(3, 'Finance', 'Delhi'),
(4, 'Sales', 'Pune');

INSERT INTO Employee VALUES
(101, 'Amit', 55000, 'Bengaluru', '2022-01-15', 1),
(102, 'Priya', 75000, 'Mumbai', '2021-03-10', 1),
(103, 'Neha', 45000, 'Delhi', '2023-06-10', 2),
(104, 'Rahul', 80000, 'Mumbai', '2022-11-05', 3),
(105, 'Sneha', 35000, NULL, '2024-05-18', 3),
(106, 'Anjali', 60000, 'Pune', '2022-09-25', 4),
(107, 'Anjali', 60000, 'Pune',      '2022-09-25', 4),
(108, 'Karan',  60000, 'Delhi',     '2020-03-14', 4),
(109, 'Meera',  50000, 'Mumbai',    '2023-12-01', 1),
(110, 'Rohit',  30000, 'Bengaluru', '2025-01-10', 2);


