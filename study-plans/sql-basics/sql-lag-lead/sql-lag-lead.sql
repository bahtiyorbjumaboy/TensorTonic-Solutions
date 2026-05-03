SELECT
    month,
    revenue,
    LAG(revenue, 1, 0) OVER (ORDER BY month) AS prev_revenue,
    revenue - LAG(revenue, 1, 0) OVER (ORDER BY month) AS revenue_change
FROM monthly_revenue
ORDER BY 1