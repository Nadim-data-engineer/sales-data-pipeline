-- Create a sales table
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    total_sales DECIMAL(12,2)
);

-- Calculate total sales by product
SELECT
    product,
    SUM(total_sales) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- Calculate total revenue
SELECT
    SUM(total_sales) AS total_revenue
FROM sales;

-- Find products with sales above 30000
SELECT *
FROM sales
WHERE total_sales > 30000;
