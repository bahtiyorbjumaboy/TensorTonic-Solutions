SELECT
    category,
    COUNT(*) AS total_sales,
    SUM(amount) AS total_revenue,
    ROUND(AVG(discount), 2) AS avg_discount
FROM sales
GROUP BY 1
ORDER BY 3 DESC, 1