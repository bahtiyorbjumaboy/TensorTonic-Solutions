SELECT
    product,
    revenue,
    sale_date
FROM sales
ORDER BY revenue DESC, sale_date
LIMIT 3
OFFSET 1