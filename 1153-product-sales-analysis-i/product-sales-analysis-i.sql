# Write your MySQL query statement below
Select product_name, year, price From Sales S left join Product P
On S.product_id = P.product_id
