# Write your MySQL query statement below
Select t1.employee_id, t1.name, Count(t2.reports_to) as reports_count, round(Avg(t2.age)) as average_age
From Employees as t1 inner join Employees as t2 on t1.employee_id = t2.reports_to
Group by t1.employee_id
Order by t1.employee_id;