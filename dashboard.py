import streamlit as st
from database import init_db, fetch_all_data

st.set_page_config(page_title="Price Tracker Analytics", layout="wide")
init_db()

st.title("Automated Price Tracker & Analytics")
st.markdown("Monitor scraped product prices, filter deals, and inspect historical trends.")

df = fetch_all_data()

if df.empty:
    st.warning("No data found in database yet. Run `python main.py --scrape` in your terminal first.")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filter Controls")
max_price_limit = float(df["price"].max())
selected_max_price = st.sidebar.slider(
    "Maximum Price (£)",
    min_value=0.0,
    max_value=max_price_limit,
    value=max_price_limit
)
search_query = st.sidebar.text_input("Search Product Title", "")

# Apply Filters
filtered_df = df[df["price"] <= selected_max_price]
if search_query:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(search_query, case=False, na=False)
    ]

# Top Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(filtered_df))
col2.metric("Average Price", f"£{filtered_df['price'].mean():.2f}")
col3.metric("Lowest Price", f"£{filtered_df['price'].min():.2f}")

# Price History Line Chart for a Specific Product
st.subheader("Product Price Trend")
product_list = sorted(df["title"].unique())
selected_product = st.selectbox("Select a product to track over time:", product_list)

product_history = df[df["title"] == selected_product].sort_values("scraped_at")
if len(product_history) > 1:
    st.line_chart(product_history, x="scraped_at", y="price")
else:
    st.info("Run the scraper multiple times to see price changes plotted over time.")

# Data Table
st.subheader("Scraped Product Records")
st.dataframe(filtered_df, use_container_width=True)