Select V.customer_id, count(V.customer_id) as count_no_trans
From Visits V left join Transactions T on V.visit_id = T.visit_id
Where T.transaction_id is null
Group by V.customer_id;