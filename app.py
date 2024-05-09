# app.py
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model('food_freshness_model.h5')

# Define the classes
classes = ['Fresh', 'Rotten']

# Define the app
def main():
    st.title('Food Freshness Detection')

    # User uploads an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Preprocess the image
        img = image.load_img(uploaded_file, target_size=(100, 100))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        prediction = model.predict(img_array)
        result = classes[np.argmax(prediction)]

        # Display the result
        st.write(f"Prediction: {result}")

if __name__ == '__main__':
    main()