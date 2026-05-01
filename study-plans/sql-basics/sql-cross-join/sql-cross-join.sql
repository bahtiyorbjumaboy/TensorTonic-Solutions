SELECT
    s.segment_name,
    m.metric_name
FROM segments s
CROSS JOIN metrics m
ORDER BY 1, 2