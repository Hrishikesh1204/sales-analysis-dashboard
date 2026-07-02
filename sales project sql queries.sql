CREATE DATABASE sales_analysis;
USE sales_analysis;

CREATE TABLE sales (...);

LOAD DATA INFILE '...';

SELECT * FROM sales;

SELECT SUM(Sales) AS Total_Sales FROM sales;

SELECT SUM(Profit) AS Total_Profit FROM sales;

SELECT Region, SUM(Sales)
FROM sales
GROUP BY Region;

SELECT Category, SUM(Sales)
FROM sales
GROUP BY Category;

SELECT Year, Month, SUM(Sales)
FROM sales
GROUP BY Year, Month;

SELECT Product_Name, SUM(Sales) AS Sales
FROM sales
GROUP BY Product_Name
ORDER BY Sales DESC
LIMIT 10;