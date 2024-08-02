# Write your MySQL query statement below
Select teacher_id, Count(Distinct Subject_id) as cnt From Teacher
Group by teacher_id 