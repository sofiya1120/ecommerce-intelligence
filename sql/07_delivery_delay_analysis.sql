SELECT 
    c.customer_state,
    ROUND(AVG(
        DATE_PART('day', o.order_delivered_customer_date::timestamp 
        - o.order_estimated_delivery_date::timestamp)
    )::numeric, 2) AS avg_delay_days,
    COUNT(o.order_id) AS total_orders,
    SUM(CASE 
        WHEN o.order_delivered_customer_date > o.order_estimated_delivery_date 
        THEN 1 ELSE 0 
    END) AS late_deliveries
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_delivered_customer_date IS NOT NULL
AND o.order_estimated_delivery_date IS NOT NULL
AND o.order_status = 'delivered'
GROUP BY 1
ORDER BY 2 DESC;