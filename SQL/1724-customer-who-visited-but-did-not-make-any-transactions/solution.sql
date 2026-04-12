# Write your MySQL query statement below
SELECT ip.customer_id, COUNT(ip.visit_id) AS count_no_trans
FROM Visits AS ip
LEFT JOIN Transactions AS t on t.visit_id = ip.visit_id
WHERE t.transaction_id is NULL
GROUP BY ip.customer_id
