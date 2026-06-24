-- Top 10 Products by Sales

SELECT product_name,
       ROUND(SUM(sales),2) AS total_sales
FROM cleaned_sales_data
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- Top 10 Customers by Sales

SELECT customer_name,
       ROUND(SUM(sales),2) AS total_sales
FROM cleaned_sales_data
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;

-- Sales by Region

SELECT region,
       ROUND(SUM(sales),2) AS total_sales
FROM cleaned_sales_data
GROUP BY region
ORDER BY total_sales DESC;

SELECT category,
       ROUND(SUM(profit),2) AS total_profit
FROM cleaned_sales_data
GROUP BY category
ORDER BY total_profit DESC;


SELECT month,
       ROUND(SUM(sales),2) AS total_sales
FROM cleaned_sales_data
GROUP BY month;


SELECT ROUND(AVG(sales),2) AS avg_order_value
FROM cleaned_sales_data;
