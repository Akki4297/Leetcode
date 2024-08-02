Select P.product_id, ifnull(Round(sum(price*units)/sum(units),2),0) As average_price
from Prices P left join UnitsSold U on P.product_id = U.product_id And (U.purchase_date BETWEEN P.start_date AND P.end_date)
Group by P.product_id;