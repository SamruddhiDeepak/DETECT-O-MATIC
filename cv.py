
def canned_page():
    import streamlit as st
    import cv2
    import numpy as np
    from inference_sdk import InferenceHTTPClient
    import tempfile
    import os

    # Initialize the Roboflow client
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="k1imImlLCAG8jOgDRxjM"
    )

    # Streamlit UI setup
    st.title("Canned Food Defect Detection in Selected Video")
    st.write("Select a video to detect defects.")

    # Predefined video options
    video_options = {
        "Video 1": r"C:\Users\Dell\Desktop\VIDEO 1.mp4",  # Update with actual path
        "Video 2": r"C:\Users\Dell\Desktop\VIDEO 2.mp4"  # Update with actual path
    }

    # Video selection
    selected_video = st.selectbox("Choose a video", list(video_options.keys()))

    # Start processing when a video is selected
    if selected_video:
        st.write(f"Processing **{selected_video}**...")  # Inform the user that processing is starting
        video_path = video_options[selected_video]

        # Use OpenCV to capture video from the selected file
        cap = cv2.VideoCapture(video_path)

        # Get total number of frames in the video
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Process video frame by frame
        for frame_count in range(total_frames):
            ret, frame = cap.read()
            if not ret:
                st.write("Finished processing the video.")
                break

            if frame_count == 0:
                continue

            # Convert the frame to JPG format
            img_encoded = cv2.imencode('.jpg', frame)[1]
            img_bytes = img_encoded.tobytes()

            # Create a temporary file for the current frame
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_frame_file:
                temp_frame_file.write(img_bytes)
                temp_frame_file.flush()  # Ensure the data is written to disk

                # Perform inference
                try:
                    result = CLIENT.infer(temp_frame_file.name, model_id="canned-food-surface-defect/1")
                except Exception as e:
                    st.write(f"Error during inference: {str(e)}")
                    continue

                # Streamlit columns to display the image and the results side by side
                col1, col2 = st.columns(2)

                with col1:
                    # Resize the frame to make it smaller (e.g., 20% of the original size)
                    resized_frame = cv2.resize(frame, (int(frame.shape[1] * 0.2), int(frame.shape[0] * 0.2)))

                    # Display the resized frame in the Streamlit app (left column)
                    st.image(resized_frame, channels="BGR", use_column_width=True)

                with col2:
                    # Display the detection results in the right column
                    if result['predictions']:
                        for prediction in result['predictions']:
                            confidence = prediction['confidence']
                            defect_class = prediction['class']

                            if confidence > 0.68:  # Only process if confidence is above 68%
                                st.write(f"**Defect Detected:** {defect_class}")
                                st.write(f"**Confidence:** {confidence * 100:.2f}%")
                            else:
                                st.write("No defect detected.")

        # Release the video capture object
        cap.release()
        cv2.destroyAllWindows()
