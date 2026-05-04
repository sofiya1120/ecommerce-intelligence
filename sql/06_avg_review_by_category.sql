SELECT 
    t.product_category_name_english AS category,
    ROUND(AVG(r.review_score)::numeric, 2) AS avg_review_score,
    COUNT(r.review_id) AS total_reviews
FROM order_reviews r
JOIN order_items oi ON r.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN product_category_translation t 
    ON p.product_category_name = t.product_category_name
GROUP BY 1
ORDER BY 2 DESC;