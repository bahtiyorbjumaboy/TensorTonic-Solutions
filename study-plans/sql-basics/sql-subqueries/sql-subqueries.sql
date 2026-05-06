SELECT
    p.name,
    p.price,
    ROUND(p.price - (SELECT AVG(price) FROM products), 2) AS vs_avg
FROM products p
WHERE EXISTS (
    SELECT 1
    FROM sales s
    WHERE s.product_id = p.id
)
ORDER BY 3 DESC, 1