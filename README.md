# DETECT-O-MATIC
## 🚀 Project Overview
Food safety is critical in ensuring public health and reducing foodborne illnesses. This project automates the food safety auditing process using **AI** and **sensor data** to detect anomalies in temperature, humidity, and weight parameters across multiple food product categories like dairy, meat, snacks, bread and fried snacks.

By leveraging **AI anomaly detection** and **real-time sensor monitoring**, our solution provides early warnings of food safety risks, allowing food production and storage facilities to take preventive action before spoilage or contamination occurs.

Additionally, we implemented a **video classification system** for canned goods. By leveraging a pre-trained model from **Roboflow**, we can assess whether the goods are defective or non-defective with high confidence based on input video data, making the auditing process more efficient.

## ✨ Key Features
- **Multi-product Monitoring**: Supports different food categories like dairy, meat, fresh produce, frozen foods, and baked goods, each with its own specific parameters.
- **AI-Powered Anomaly Detection**: Detects abnormal temperature, humidity, and pH levels using ""decision logic**.
- **Real-Time Alerts**: Provides a log of anomalous products when sensor data conditions have deviated from safe ranges.
- **Video Classification for Canned Goods**: Classifies canned goods as defective or non-defective using a Roboflow pre-trained model with high confidence.
- **Blockchain Integration**: Logs audit trails of detected anomalies for secure, immutable records, ensuring transparency in food safety compliance.
- **Scalable Solution**: Easily expandable to new types of food products or environmental conditions.

## 🛠️ Technology Stack
- **Python** for data generation, anomaly detection, and logging.
- **Pandas** is used for managing product data, and NumPy for generating random sensor values.
- **Roboflow** pre trained model for the package anomaly detection in canned food products.
- **Streamlit** serves as the front-end for real-time monitoring
- **OpenCV** handles image and video processing. 
- **InferenceHTTPClient API** is used for AI-based defect detection
- **Cv2** processes the uploaded media for detection. 

## ⚙️ How It Works
1. **Data Collection**: The system collects temperature, humidity, and pH data from a simulated dataset for various food products.
   
2. **AI-based Anomaly Detection**:
   - The AI model (with simple decision logic) analyzes the sensor data and checks for deviations outside the predefined safe range.
   - Each product type has its own specific safety thresholds for temperature and humidity (e.g., Dairy: 2°C-4°C, 50%-60% humidity).

3. **Real-time Alerts**: When an anomaly is detected, such as temperature spikes or humidity anomalies, the system takes a log of it and displays on the window.

4. **Dashboard Visualization**: An intuitive web-based dashboard updates in real-time, the number of normal and anomalous products.
5. **Video Classification of Canned Goods**: The system uses a pre-trained model from Roboflow to classify canned goods based on video inputs. It determines whether the goods are defective or non-defective with high confidence.


## 🎯 Project Goals
- **Improve Food Safety**: Ensure safe food handling by identifying potential risks early in the production/storage process.
- **Automate Auditing**: Reduce manual inspection errors and streamline the compliance process.
- **Enhance Defect Detection**: Leverage AI video classification to assess canned goods and improve quality control.
- **Promote Transparency**: With optional blockchain integration, provide secure and tamper-proof audit trails.

                                                                           

