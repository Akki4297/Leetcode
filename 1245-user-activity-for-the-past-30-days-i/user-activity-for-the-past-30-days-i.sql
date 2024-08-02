# Write your MySQL query statement below
#Select*
Select activity_date as day, Count(Distinct user_id) as active_users
from Activity
#where activity_date = '2019-06-28'
where activity_date between '2019-06-28' and '2019-07-27'
Group by activity_date;