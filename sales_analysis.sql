
-- 1. Calculate total revenue and profit
SELECT
    SUM(units_sold * unit_price) AS total_revenue,
    SUM(units_sold * (unit_price - unit_cost)) AS total_profit
FROM sales;

-- 2. Compare revenue and profit by category
SELECT
    category,
    SUM(units_sold * unit_price) AS revenue,
    SUM(units_sold * (unit_price - unit_cost)) AS profit
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 3. Find the best-selling products by units sold
SELECT
    product,
    SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY product
ORDER BY total_units_sold DESC;

-- 4. Find the lowest recorded inventory levels
SELECT
    product,
    MIN(stock_remaining) AS lowest_recorded_stock
FROM sales
GROUP BY product
ORDER BY lowest_recorded_stock ASC;
