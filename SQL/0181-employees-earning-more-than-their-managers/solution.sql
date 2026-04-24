# Write your MySQL query statement below
SELECT e.name as Employee
FROM employee e
JOIN employee m ON e.managerId = m.id
WHERE e.salary > m.salary