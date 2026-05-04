SELECT DATE_TRUNC('month', o.order_purchase_timestamp::date) AS month,
       SUM(oi.price + oi.freight_value) AS revenue,
       COUNT(DISTINCT o.order_id) AS order_count
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY 1
ORDER BY 1;