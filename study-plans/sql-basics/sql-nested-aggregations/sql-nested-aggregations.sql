WITH daily_orders AS (
    SELECT
        order_date,
        COUNT(*) AS total_orders,
        SUM(amount) AS total_revenue
    FROM orders
    GROUP BY 1
)
SELECT
    ROUND(AVG(total_orders), 2) AS avg_daily_orders,
    ROUND(AVG(total_revenue), 2) AS avg_daily_revenue,
    MAX(total_orders) AS busiest_day_orders
FROM daily_orders