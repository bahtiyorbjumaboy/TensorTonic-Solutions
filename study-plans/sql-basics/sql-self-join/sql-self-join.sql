SELECT
    ur.username,
    COALESCE(urb.username, 'organic') AS referrer_name
FROM user_referrals ur
LEFT JOIN user_referrals urb
    ON ur.referred_by = urb.id
ORDER BY 1