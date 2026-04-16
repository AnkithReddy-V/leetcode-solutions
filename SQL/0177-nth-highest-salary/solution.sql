CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH Nhigh AS (
        SELECT DISTINCT e.salary as getNthHighestSalary,
        DENSE_RANK() OVER(ORDER BY e.salary DESC) as ranks
        FROM Employee e
      )

      SELECT MAX(getNthHighestSalary) as getNthHighestSalary
      FROM Nhigh
      WHERE ranks = N
  );
END
