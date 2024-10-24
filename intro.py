import streamlit as st

def intro_page():
    st.title("DETECT-O-MATIC")

    # Main page with project introduction
    st.write("## Welcome to our project DETECT-O-MATIC")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write("Welcome to the forefront of innovation in food safety management!")
        st.write(
            "Our project, **DETECT-O-MATIC**, is designed to revolutionize the way food safety audits are conducted, making them more efficient, accurate, and secure.")
        st.write(
            "In an era where the integrity of food supply chains is paramount, we leverage cutting-edge technologies such as **Artificial Intelligence**, **Big Data**, and **Blockchain** to transform the labor-intensive auditing process into a streamlined, automated system. Using **computer vision**, our system detects defective products with unparalleled precision, ensuring that only the highest quality food reaches consumers. Coupled with advanced **AI models**, we identify products exhibiting anomalous sensor values—providing an early warning system that safeguards against potential safety risks.")

    with col2:
        # Add the image
        st.image(r'C:\Users\Dell\Downloads\he-modified.png', caption='Food Safety Innovation',
                 width=200)  # Update with your image path

    st.write(
        "Imagine a world where food safety audits are not just a periodic check, but a continuous, real-time process.")
    st.write(
        "But that’s not all! Our integration of **Blockchain technology** guarantees secure audit trails, enhancing transparency and accountability throughout the food production and distribution lifecycle. Each transaction, each audit, each data point is recorded immutably, providing a trust layer that enhances consumer confidence.")
    st.write(
        "Join us on this exciting journey as we harness the power of technology to create a safer, more reliable food ecosystem. Together, we are setting new standards in food safety auditing—ensuring that what we eat is not just safe, but also produced and distributed with integrity. Let’s dive into this innovative project and discover how we can make a difference in food safety today!")
    st.write("Ready to explore? Click the button below to embark on this transformative journey with us!")

