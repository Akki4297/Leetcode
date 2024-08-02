Select P.product_id, ifnull(Round(sum(price*units)/sum(units),2),0) As average_price
from Prices AS P left join UnitsSold AS U on P.product_id = U.product_id 
Where (U.purchase_date BETWEEN P.start_date AND P.end_date) or U.purchase_date is null
Group by P.product_id;