import streamlit as st
from intro import intro_page
from main import main_page
from cv import canned_page

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ("Introduction", "Main Dashboard","Anomaly Detection for Canned Goods"))

# Show the selected page
if page == "Introduction":
    intro_page()
elif page == "Main Dashboard":
    main_page()
elif page == "Anomaly Detection for Canned Goods":
    canned_page()

