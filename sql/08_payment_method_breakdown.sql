SELECT 
    payment_type,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_value)::numeric, 2) AS total_revenue,
    ROUND(AVG(payment_value)::numeric, 2) AS avg_payment_value,
    ROUND(AVG(payment_installments)::numeric, 2) AS avg_installments
FROM order_payments
GROUP BY 1
ORDER BY 3 DESC;