SELECT customer.full_name
FROM customer
         INNER JOIN "order" o on customer.customer_id != o.customer_id
GROUP BY full_name;