# Write your MySQL query statement below
WITH Sal as (
    SELECT DISTINCT salary as SecondHighestSalary,
DENSE_RANK() OVER(ORDER BY salary DESC) as rnk
FROM Employee
)

SELECT MAX(SecondHighestSalary) as SecondHighestSalary
FROM Sal
WHERE rnk = 2 
