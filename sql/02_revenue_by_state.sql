SELECT c.customer_state,
       SUM(oi.price) AS revenue,
       COUNT(DISTINCT o.order_id) AS orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY 1
ORDER BY 2 DESC;