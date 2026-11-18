
-- ==========================================
-- SETUP FOR QUESTION 1: Customers & Orders
-- ==========================================
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2)
);

INSERT INTO customers (id, name) VALUES
(1, 'Arjun'),
(2, 'Meera'),
(3, 'Rahul'),    -- Edge case: Rahul has 0 orders!
(4, 'Sneha');

INSERT INTO orders (id, customer_id, order_date, amount) VALUES
(101, 1, '2026-10-01', 250.00),
(102, 1, '2026-10-05', 150.00),
(103, 2, '2026-10-03', 500.00),
(104, 4, '2026-10-10', 300.00);


-- ==========================================
-- SETUP FOR QUESTION 2: Transactions
-- ==========================================
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    category VARCHAR(50),
    sale_amount DECIMAL(10, 2)
);

INSERT INTO transactions (transaction_id, category, sale_amount) VALUES
(1, 'Electronics', 6000.00),
(2, 'Electronics', 5500.00),
(3, 'Electronics', 50.00),    -- Should be ignored (<= 100)
(4, 'Furniture', 8000.00),
(5, 'Furniture', 2500.00),    -- Total > 10,000 (10,500)
(6, 'Clothing', 4000.00),
(7, 'Clothing', 3000.00),     -- Total < 10,000 (7,000)
(8, 'Accessories', 90.00),    -- Should be ignored (<= 100)
(9, 'Accessories', 12000.00); -- Valid, total 12,000


-- ==========================================
-- SETUP FOR QUESTION 3: Employees
-- ==========================================
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (emp_id, emp_name, department, salary) VALUES
(1, 'Devika', 'AI Engineering', 95000.00),
(2, 'Nikhil', 'AI Engineering', 82000.00), -- 2nd highest in AI
(3, 'Aswathy', 'AI Engineering', 70000.00),
(4, 'Rohan', 'Data Science', 90000.00),
(5, 'Ananya', 'Data Science', 85000.00),   -- 2nd highest in Data Science
(6, 'Karthik', 'Data Science', 65000.00),
(7, 'Priya', 'Cloud Ops', 88000.00),
(8, 'Siddharth', 'Cloud Ops', 79000.00);   -- 2nd highest in Cloud Ops
