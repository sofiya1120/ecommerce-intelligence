# E-Commerce Sales Intelligence Dashboard

An end-to-end data analytics project analysing 100,000+ real Brazilian e-commerce orders from the Olist dataset. Built to demonstrate skills across data engineering, data analysis, data science, and AI/ML engineering.

## Live Demo

- **AI Chat App** — https://ecommerce-intelligence-xtw4bbdmbsx5fm9yzgswap.streamlit.app/
- **Tableau Dashboard** — https://public.tableau.com/app/profile/sofiya.mohammed6217/viz/E-commerceSalesIntelligenceDashboard/Dashboard2#1

## What This Project Does

Business users can type questions in plain English like "which state had the highest revenue?" and get instant AI-powered answers backed by real data. The project also includes a 4-page interactive Tableau dashboard covering revenue trends, customer geography, product performance, and payment analysis.

## Key Business Insights Found

1. **Revenue grew 7,000x in 14 months** — from R$143 in August 2016 to R$1.15M in November 2017, with a clear Black Friday peak
2. **São Paulo dominates** — SP accounts for 41% of total revenue, with SP + RJ + MG accounting for over 60% of all orders
3. **Late deliveries kill satisfaction** — early deliveries score 4.1+ stars on average while late deliveries drop to 2.5 stars
4. **Health & beauty leads revenue** — top category by total revenue with 9,670 units sold
5. **75% of customers only buy once** — high churn rate is the #1 business problem, with less than 5% classified as loyal customers

## Tech Stack

| Tool | Purpose |
|---|---|
| Python + Pandas | Data cleaning and EDA |
| PostgreSQL + SQL | Database and 10+ analytical queries |
| Neon | Cloud PostgreSQL hosting |
| Tableau Public | 4-page interactive dashboard |
| Streamlit | Public web app |
| Groq + Llama 3 | Natural language to SQL AI layer |
| Git + GitHub | Version control |

## Project Structure

ecommerce-intelligence/
├── notebooks/          # Jupyter EDA notebook with 5 business insights
├── outputs/            # Chart PNG files from EDA
├── scripts/            # Python scripts for data loading
├── sql/                # 10 SQL queries (churn, RFM, revenue, etc)
├── streamlit/          # AI-powered web app
└── requirements.txt    # Python dependencies

## SQL Queries Written

1. Monthly revenue trend
2. Revenue by Brazilian state
3. Top 15 product categories
4. Customer churn rate (90-day window)
5. RFM customer segmentation
6. Average review score by category
7. Delivery delay analysis
8. Payment method breakdown
9. Seller performance ranking
10. Repeat buyer analysis

## Dashboard Pages

- **Executive Summary** — Revenue KPIs, monthly trend with Black Friday annotation
- **Customer Analysis** — Brazil geographic heatmap, revenue by state
- **Product Performance** — Top categories, review scores with target line
- **Payment Analysis** — Payment method distribution and revenue breakdown

## Dataset

Olist Brazilian E-Commerce dataset from Kaggle — 100,000+ real orders placed between 2016 and 2018 across 9 relational tables.

## Author

Built by Sofiya Mohammed | May 2026
