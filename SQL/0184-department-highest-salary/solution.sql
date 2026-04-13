# Write your MySQL query statement below
WITH SalRank as (
    SELECT d.name as Department, e.name as Employee, 
    e.salary as Salary,
    RANK() OVER(partition by d.id ORDER BY e.salary DESC) as ran
    FROM employee e
    JOIN department d ON d.id = e.departmentId
)

SELECT Department, Employee, Salary
FROM SalRank
WHERE ran = 1
