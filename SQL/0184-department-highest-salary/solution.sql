# Write your MySQL query statement below
WITH DeptHighestSal AS (
    SELECT d.name as Department, e.name as Employee, e.salary as Salary,
    DENSE_RANK() OVER(partition by d.id ORDER BY e.salary DESC) as ranks
    FROM Employee e
    JOIN Department d ON d.id = e.departmentId
)

SELECT Department, Employee, Salary
FROM DeptHighestSal
WHERE ranks = 1
