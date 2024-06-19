-------------------------------------------------

-- 1378. Replace Employee ID With The Unique Identifier
-- Write your MySQL query statement below
SELECT EmployeeUNI.unique_id, Employees.name FROM EmployeeUNI RIGHT JOIN Employees
ON Employees.id = EmployeeUNI.id;

-------------------------------------------------

-- 1068. Product Sales Analysis I
-- Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price FROM Product RIGHT JOIN Sales
ON Sales.product_id = Product.product_id;

-------------------------------------------------
