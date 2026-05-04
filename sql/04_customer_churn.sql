SELECT COUNT(DISTINCT customer_unique_id) AS churned_customers,
  ROUND(COUNT(DISTINCT customer_unique_id) * 100.0 /
    (SELECT COUNT(DISTINCT customer_unique_id) FROM customers), 2) AS churn_rate_pct
FROM (
  SELECT c.customer_unique_id,
         MAX(o.order_purchase_timestamp::date) AS last_order
  FROM customers c
  JOIN orders o ON c.customer_id = o.customer_id
  GROUP BY 1
  HAVING MAX(o.order_purchase_timestamp::date) < CURRENT_DATE - INTERVAL '90 days'
) t;