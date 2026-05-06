WITH customer_agg AS (
    SELECT
        customer,
        COUNT(order_date) AS order_count,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY 1
)
SELECT
    *
FROM customer_agg
WHERE order_count > 1
ORDER BY 3 DESC, 1