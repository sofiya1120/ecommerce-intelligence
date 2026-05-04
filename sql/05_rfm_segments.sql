SELECT 
    c.customer_unique_id,
    DATE_PART('day', NOW() - MAX(o.order_purchase_timestamp::timestamp)) AS recency_days,
    COUNT(DISTINCT o.order_id) AS frequency,
    ROUND(SUM(oi.price)::numeric, 2) AS monetary
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY 1
ORDER BY 4 DESC
LIMIT 1000;