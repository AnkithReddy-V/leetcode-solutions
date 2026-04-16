# Write your MySQL query statement below
WITH TopThree AS (
    SELECT 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC)
        as ranks
        FROM Employee e
        JOIN Department d
        ON d.id = e.departmentId
)

SELECT 
    Department, 
    Employee, 
    Salary
FROM TopThree
WHERE ranks <= 3
