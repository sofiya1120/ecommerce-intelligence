import streamlit as st
import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCHEMA = """
Tables available:
- orders(order_id, customer_id, order_status, order_purchase_timestamp, order_delivered_customer_date)
- order_items(order_id, product_id, seller_id, price, freight_value)
- customers(customer_id, customer_unique_id, customer_city, customer_state)
- products(product_id, product_category_name)
- order_reviews(order_id, review_score, review_comment_message)
- order_payments(order_id, payment_type, payment_value)
- product_category_translation(product_category_name, product_category_name_english)
- sellers(seller_id, seller_city, seller_state)
"""

def nl_to_sql(question):
    prompt = f"""You are a PostgreSQL expert. Convert this question to a SQL query.
Only use these tables: {SCHEMA}
Return ONLY the SQL query, no explanation, no markdown backticks.
Question: {question}"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def run_query(sql):
    conn = psycopg2.connect(os.getenv("NEON_DATABASE_URL"))

    df = pd.read_sql(sql, conn)
    conn.close()
    return df

st.set_page_config(page_title="Sales Intelligence", page_icon="📊")
st.title("E-Commerce Sales Intelligence")
st.caption("Ask business questions in plain English — powered by Llama 3 AI")
st.markdown("**Try asking:** Which state had the highest revenue? | What are the top 5 product categories? | What is the average review score?")

question = st.text_input("Your question:", placeholder="Which region had the most orders?")

if question:
    with st.spinner("Generating SQL and fetching data..."):
        try:
            sql = nl_to_sql(question)
            st.subheader("Generated SQL")
            st.code(sql, language="sql")
            df = run_query(sql)
            st.subheader("Results")
            st.dataframe(df)
            if len(df.columns) >= 2:
                st.bar_chart(df.set_index(df.columns[0])[df.columns[1]])
        except Exception as e:
            st.error(f"Error: {e}")