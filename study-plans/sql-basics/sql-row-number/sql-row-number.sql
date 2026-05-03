SELECT
    username,
    segment,
    engagement_score,
    ROW_NUMBER() OVER (PARTITION BY segment ORDER BY engagement_score DESC, username) AS activity_rank
FROM user_activity
ORDER BY 2, 4