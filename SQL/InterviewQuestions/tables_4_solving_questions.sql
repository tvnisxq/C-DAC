CREATE TABLE Department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(50) NOT NULL
);

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    salary DECIMAL(10,2) NOT NULL,
    department_id INT,
    manager_id INT,
    joining_date DATE NOT NULL,

    FOREIGN KEY (department_id)
        REFERENCES Department(department_id),

    FOREIGN KEY (manager_id)
        REFERENCES Employee(emp_id),

    CHECK (salary >= 0)
);


CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    signup_date DATE NOT NULL
);


CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,

    CHECK (price >= 0)
);


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(30) NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id),

    CHECK (amount >= 0),

    CHECK (status IN (
        'Placed',
        'Shipped',
        'Delivered',
        'Cancelled',
        'Returned'
    ))
);



CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES Orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES Products(product_id),

    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);



CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    signup_date DATE NOT NULL
);



CREATE TABLE API_Usage (
    request_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    input_tokens INT NOT NULL,
    output_tokens INT NOT NULL,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    CHECK (input_tokens >= 0),
    CHECK (output_tokens >= 0)
);


CREATE TABLE API_Requests (
    request_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    request_date DATETIME NOT NULL,
    status VARCHAR(30) NOT NULL,
    response_time_ms INT,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    CHECK (status IN (
        'Success',
        'Failed',
        'Timeout'
    )),

    CHECK (response_time_ms IS NULL OR response_time_ms >= 0)
);


CREATE TABLE User_Limits (
    user_id INT PRIMARY KEY,
    monthly_limit INT NOT NULL,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    CHECK (monthly_limit >= 0)
);




CREATE TABLE GPU_Usage (
    gpu_id INT NOT NULL,
    usage_date DATE NOT NULL,
    total_active_minutes DECIMAL(10,2) NOT NULL,
    total_available_minutes DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (gpu_id, usage_date),

    CHECK (total_active_minutes >= 0),
    CHECK (total_available_minutes > 0),
    CHECK (total_active_minutes <= total_available_minutes)
);



CREATE TABLE Activity (
    activity_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    activity_date DATE NOT NULL,
    activity_type VARCHAR(50),

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id)
);



CREATE TABLE Logins (
    login_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    login_date DATE NOT NULL,

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id)
);




CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_date DATETIME NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(30),

    FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    CHECK (amount >= 0)
);



SHOW TABLES;