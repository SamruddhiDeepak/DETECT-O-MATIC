import pandas as pd
import random
import time
from datetime import datetime
import streamlit as st


def main_page():
    # Load product data
    df = pd.read_excel('product_data.xlsx')

    # Function to generate random values
    def generate_random_values(product_name):
        product_data = df[df['product_name'] == product_name]
        if product_data.empty:
            st.warning(f"No data found for product: {product_name}")
            return None

        optimal_temp = product_data['optimal_temperature'].values[0]
        optimal_humidity = product_data['optimal_humidity'].values[0]
        optimal_weight = product_data['optimal_weight'].values[0]

        # Introduce a chance to generate anomalous values
        if random.random() < 0.3:  # 20% chance of generating an anomalous value
            temp = round(random.uniform(optimal_temp - 10, optimal_temp + 10), 2)
            humidity = round(random.uniform(optimal_humidity - 20, optimal_humidity + 20), 2)
            weight = round(random.uniform(optimal_weight - 0.5, optimal_weight + 0.5), 2)
        else:
            temp = round(random.uniform(optimal_temp - 5, optimal_temp + 5), 2)
            humidity = round(random.uniform(optimal_humidity - 10, optimal_humidity + 10), 2)
            weight = round(random.uniform(optimal_weight - 0.1, optimal_weight + 0.1), 2)

        return temp, humidity, weight, optimal_temp, optimal_humidity, optimal_weight

    # Streamlit UI setup
    st.title("Product Anomaly Detection Dashboard")
    st.write("Select the product to monitor:")

    # Input for product name
    product_name = st.selectbox("Select a product:", df['product_name'].unique())

    # Create session state for monitoring status, anomaly logs, and counts
    if 'monitoring' not in st.session_state:
        st.session_state.monitoring = False
    if 'normal_count' not in st.session_state:
        st.session_state.normal_count = 0
    if 'anomaly_count' not in st.session_state:
        st.session_state.anomaly_count = 0
    if 'anomalies_log' not in st.session_state:
        st.session_state.anomalies_log = []  # List to store all anomalies

    # Function to generate a unique product ID
    def generate_product_id():
        return random.randint(1000, 9999)  # Generates a random product ID between 1000 and 9999

    # Function to update readings and display results
    def update_readings():
        # Generate random values
        random_values = generate_random_values(product_name)
        if random_values is None:
            return  # Exit if no data found for the product

        temp, humidity, weight, optimal_temp, optimal_humidity, optimal_weight = random_values

        # Check for anomalies
        anomalies = []
        if temp < (optimal_temp - 5) or temp > (optimal_temp + 5):
            anomalies.append("Temperature anomaly")
        if humidity < (optimal_humidity - 10) or humidity > (optimal_humidity + 10):
            anomalies.append("Humidity anomaly")
        if weight < (optimal_weight - 0.1) or weight > (optimal_weight + 0.1):
            anomalies.append("Weight anomaly")

        # Log anomalies if detected
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        product_id = generate_product_id()  # Generate a unique product ID for this reading

        if anomalies:
            anomaly_message = f"Product ID: {product_id} | Timestamp: {timestamp} | Anomalies: {', '.join(anomalies)}"
            st.session_state.anomalies_log.append(anomaly_message)  # Store the message in the log
            st.session_state.anomaly_count += 1

            # Print the detected anomalies to the console
            print(anomaly_message)  # This will print anomalies in the console
        else:
            st.session_state.normal_count += 1  # Increment normal count if no anomalies

    # Start monitoring button
    if st.button("Start Monitoring"):
        # Reset all counts and logs each time monitoring starts
        st.session_state.normal_count = 0
        st.session_state.anomaly_count = 0
        st.session_state.anomalies_log = []  # Reset the anomaly log
        st.session_state.monitoring = True

    # Stop monitoring button
    if st.button("Stop Monitoring"):
        st.session_state.monitoring = False

    # Display the counts and logs on the dashboard
    st.sidebar.header("Dashboard")
    normal_count_display = st.sidebar.empty()
    anomaly_count_display = st.sidebar.empty()
    anomaly_log_display = st.empty()

    # Continuous monitoring
    if st.session_state.monitoring:
        while True:
            update_readings()  # Call the function to update readings

            # Update the sidebar displays
            normal_count_display.write(f"Normal Products: {st.session_state.normal_count}")
            anomaly_count_display.write(f"Anomalous Products: {st.session_state.anomaly_count}")

            # Build the formatted anomalies string
            if st.session_state.anomalies_log:
                formatted_anomalies = "### Detected Anomalies:\n"
                for anomaly in st.session_state.anomalies_log:
                    # Append each anomaly on a new line
                    formatted_anomalies += "\n" + anomaly + "\n"  # Add a newline for each anomaly

                # Display all detected anomalies
                anomaly_log_display.markdown(formatted_anomalies)  # Display the complete log at once

            time.sleep(1)  # Update every 2 seconds
