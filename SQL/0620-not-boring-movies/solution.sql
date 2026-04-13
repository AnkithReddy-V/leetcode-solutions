# Write your MySQL query statement below
SELECT * FROM cinema
WHERE description != 'boring'
AND id & 1 = 1
ORDER BY rating DESC
