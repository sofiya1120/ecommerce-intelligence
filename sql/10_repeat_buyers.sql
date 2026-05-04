SELECT 
    repeat_category,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM (
    SELECT 
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS order_count,
        CASE 
            WHEN COUNT(DISTINCT o.order_id) = 1 THEN 'one-time buyer'
            WHEN COUNT(DISTINCT o.order_id) BETWEEN 2 AND 3 THEN 'repeat buyer'
            WHEN COUNT(DISTINCT o.order_id) > 3 THEN 'loyal customer'
        END AS repeat_category
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY 1
) t
GROUP BY 1
ORDER BY 2 DESC;