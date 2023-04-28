select "order".order_no, m.full_name, c.full_name
from "order"
         INNER JOIN customer c on c.customer_id = "order".customer_id
         INNER JOIN manager m on m.manager_id = "order".manager_id
WHERE c.city != m.city
