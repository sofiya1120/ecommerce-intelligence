import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ecommerce')
os.makedirs('tableau_data', exist_ok=True)

monthly = pd.read_sql("""
    SELECT DATE_TRUNC('month', o.order_purchase_timestamp::date) AS month,
           SUM(oi.price + oi.freight_value) AS revenue,
           COUNT(DISTINCT o.order_id) AS order_count
    FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY 1 ORDER BY 1""", engine)
monthly.to_csv('tableau_data/monthly_revenue.csv', index=False)

state = pd.read_sql("""
    SELECT c.customer_state, SUM(oi.price) AS revenue,
           COUNT(DISTINCT o.order_id) AS orders
    FROM customers c JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY 1 ORDER BY 2 DESC""", engine)
state.to_csv('tableau_data/revenue_by_state.csv', index=False)

products = pd.read_sql("""
    SELECT t.product_category_name_english AS category,
           SUM(oi.price) AS revenue,
           COUNT(oi.order_item_id) AS units_sold
    FROM order_items oi JOIN products p ON oi.product_id = p.product_id
    LEFT JOIN product_category_translation t ON p.product_category_name = t.product_category_name
    GROUP BY 1 ORDER BY 2 DESC LIMIT 15""", engine)
products.to_csv('tableau_data/top_products.csv', index=False)

reviews = pd.read_sql("""
    SELECT t.product_category_name_english AS category,
           ROUND(AVG(r.review_score)::numeric, 2) AS avg_score,
           COUNT(r.review_id) AS total_reviews
    FROM order_reviews r JOIN order_items oi ON r.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    LEFT JOIN product_category_translation t ON p.product_category_name = t.product_category_name
    GROUP BY 1 ORDER BY 2 DESC""", engine)
reviews.to_csv('tableau_data/reviews_by_category.csv', index=False)

payments = pd.read_sql("""
    SELECT payment_type, COUNT(DISTINCT order_id) AS total_orders,
           ROUND(SUM(payment_value)::numeric, 2) AS total_revenue
    FROM order_payments GROUP BY 1 ORDER BY 3 DESC""", engine)
payments.to_csv('tableau_data/payment_methods.csv', index=False)

print("All CSV files exported to tableau_data/ folder")