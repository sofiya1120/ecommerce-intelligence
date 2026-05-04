SELECT p.product_category_name,
       t.product_category_name_english AS category_english,
       SUM(oi.price) AS revenue,
       COUNT(oi.order_item_id) AS units_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN product_category_translation t
  ON p.product_category_name = t.product_category_name
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 10;
