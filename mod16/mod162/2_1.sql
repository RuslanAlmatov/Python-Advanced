SELECT customer.full_name      AS "Имя покупателя",
       manager.full_name       AS "Имя продавца",
       "order".purchase_amount AS "Сумма",
       "order".date            AS "Дата"
FROM customer,
     manager,
     "order"
WHERE ("order".customer_id = customer.customer_id)
  AND ("order".manager_id = manager.manager_id);