# Write your MySQL query statement below
SELECT t2.id FROM Weather AS t2
JOIN Weather as t1 on DATEDIFF(t2.recordDate, t1.recordDate) = 1
WHERE t2.temperature > t1.temperature
