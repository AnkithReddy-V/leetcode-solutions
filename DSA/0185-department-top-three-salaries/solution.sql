# Write your MySQL query statement below
WITH Sal as (
    SELECT e.name as Employee, d.name as Department, e.salary as Salary,
    DENSE_RANK() OVER (partition by d.name ORDER BY Salary DESC) as rnk
    FROM Employee e
    JOIN Department d
    ON d.id = e.departmentId
)

SELECT Department, Employee, Salary
FROM Sal
WHERE rnk < 4
