import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("postgresql://postgres:postgres@localhost:5432/ecommerce")

tables = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "product_category_translation": "product_category_name_translation.csv",
}

for table, filename in tables.items():
    df = pd.read_csv(f"data/{filename}")
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"Loaded {table}: {len(df)} rows")

print("Done! All tables loaded.")