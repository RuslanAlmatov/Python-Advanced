select customer.full_name
from customer, "order"
where customer.customer_id != "order".customer_id;