import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Neon connection
neon_engine = create_engine(os.getenv("NEON_DATABASE_URL"))

# Local connection
local_engine = create_engine("postgresql://postgres:postgres@localhost:5432/ecommerce")

tables = ["orders", "order_items", "customers", "products", 
          "sellers", "order_reviews", "order_payments", 
          "product_category_translation"]

for table in tables:
    print(f"Copying {table}...")
    df = pd.read_sql(f"SELECT * FROM {table}", local_engine)
    df.to_sql(table, neon_engine, if_exists="replace", index=False)
    print(f"Done: {table} — {len(df)} rows")

print("All tables loaded to Neon!")