select "order".order_no, customer.full_name, manager.full_name, "order".purchase_amount, "order".date
from customer,
     manager,
     "order"
where "order".customer_id = customer.customer_id
  and "order".manager_id = manager.manager_id;