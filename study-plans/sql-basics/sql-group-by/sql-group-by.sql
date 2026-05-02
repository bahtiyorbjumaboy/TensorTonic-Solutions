SELECT
    customer,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_spent
FROM orders
GROUP BY 1
ORDER BY 3 DESC