# Write your MySQL query statement below
WITH ConsecVal as (
    SELECT num,
    LAG(num) OVER (ORDER BY id) as prev,
    LEAD(num) OVER (ORDER BY id) as next 
    FROM Logs
)

SELECT DISTINCT num as ConsecutiveNums 
FROM ConsecVal
WHERE prev = num AND num = next
