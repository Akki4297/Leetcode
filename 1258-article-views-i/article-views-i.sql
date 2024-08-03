# Write your MySQL query statement below
Select distinct viewer_id id From Views
where viewer_id = author_id
order by viewer_id;