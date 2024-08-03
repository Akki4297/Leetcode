# Write your MySQL query statement below
Select viewer_id id From Views
where viewer_id = author_id
group by viewer_id
order by viewer_id;