SELECT
    c.name,
    c.city,
    COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
    LEFT JOIN orders o
        ON c.id = o.customer_id
GROUP BY 1, 2
ORDER BY 3 DESC, 1