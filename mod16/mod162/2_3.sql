select "order".order_no, manager.full_name, customer.full_name
from "order",
     customer,
     manager
where customer.city != manager.city;