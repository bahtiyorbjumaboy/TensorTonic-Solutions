SELECT
    account,
    txn_date,
    amount,
    SUM(amount) OVER (PARTITION BY account ORDER BY txn_date, id) AS running_total
FROM transactions
ORDER BY account, txn_date, id