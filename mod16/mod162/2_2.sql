SELECT customer.full_name
FROM customer
         LEFT JOIN "order" o on customer.customer_id = o.customer_id
WHERE o.customer_id IS NULL