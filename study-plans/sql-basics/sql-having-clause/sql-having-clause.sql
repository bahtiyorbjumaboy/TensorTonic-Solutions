SELECT
    customer,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_spent
FROM orders
GROUP BY 1
HAVING total_orders >= 2
ORDER BY 3 DESC