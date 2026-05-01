SELECT
    e.name,
    e.salary,
    d.dept_name
FROM employees e
    JOIN departments d
        ON e.dept_id = d.id
ORDER BY e.name