SELECT 
    s.seller_id,
    s.seller_state,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    ROUND(SUM(oi.price)::numeric, 2) AS total_revenue,
    ROUND(AVG(r.review_score)::numeric, 2) AS avg_review_score,
    ROUND(AVG(
        DATE_PART('day', o.order_delivered_customer_date::timestamp
        - o.order_purchase_timestamp::timestamp)
    )::numeric, 2) AS avg_delivery_days
FROM sellers s
JOIN order_items oi ON s.seller_id = oi.seller_id
JOIN orders o ON oi.order_id = o.order_id
LEFT JOIN order_reviews r ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
AND o.order_delivered_customer_date IS NOT NULL
GROUP BY 1, 2
ORDER BY 4 DESC
LIMIT 50;