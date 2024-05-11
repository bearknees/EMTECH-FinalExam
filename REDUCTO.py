import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.optimizers import Adam

model = load_model('Fruitsandveggies.h5')

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

classes = {0: 'Fresh Banana', 1: 'Fresh Cucumber', 2: 'Fresh Orange', 
           3: 'Rotten Banana', 4: 'Rotten Cucumber', 5: 'Rotten Orange'}

def analyze_image(image_file):
    try:
        image = Image.open(image_file)
        image = image.resize((150, 150))
        image = np.expand_dims(image, axis=0)
        image = np.array(image) / 255.0
        
        pred_probabilities = model.predict(image)
        pred_class_index = np.argmax(pred_probabilities, axis=1)[0]
    
        if pred_class_index in classes:
            predicted_class = classes[pred_class_index]
            return f"Result: {predicted_class}"
        else:
            return "Unknown Fruit"
    except Exception as e:
        return "Error Processing Image"

st.markdown("<h1 style='text-align: center; color: white; background-color: #F08080; padding: 20px; border-radius: 20px;'>REDUCTO: A Food Freshness Detector Web App for your Fruits and Vegetables</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green; background-color: #ffffff; padding: 10px; font-size: 16px; border-radius: 20px;'>Upload an image of a banana, orange, or cucumber to know if your food is fresh or rotten.</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: green; background-color: #ffffff; padding: 10px; font-size: 16px; border-radius: 20px;'>Discover the Future of Data Visualization</h2>", unsafe_allow_html=True)
st.image("https://www.graciemag.com/wp-content/uploads/2014/12/GM-White-Page-214.jpg", caption='Discover Freshness', use_column_width=True)
st.markdown("<p style='text-align: center; background-color: #ffffff; padding: 10px; border-radius: 20px;'>Join us in exploring innovative ways to interpret data and gain insights.</p>", unsafe_allow_html=True)

uploaded_image = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
    if st.button("Analyze Image", key="analyze_btn"):
        result = analyze_image(uploaded_image)
        st.write(result)

st.markdown("<div style='background-color: #F0F2F6; padding: 20px; border-radius: 20px; margin-bottom: 20px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black; margin-top: 10px;'>Who We Are</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: justify; padding: 10px;'>Welcome to Reducto Food Detect Web App, where we use cutting-edge technology to determine the freshness of your food specifically oranges, banana, and cucumber with just a click!<br>Our team is dedicated to providing you with accurate results, so you can say goodbye to guessing games when it comes to your food quality.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>Sign Up for Our Newsletter</h2>", unsafe_allow_html=True)
email = st.text_input("", placeholder="Your Email Address", key="newsletter_email")
if st.button("Sign Up", key="signup_btn"):
    with open("emails.txt", "a") as file:
        file.write(email + "\n")
    st.balloons()
    st.success("You have successfully signed up for our newsletter!")

st.markdown("<div style='background-color: #F0F2F6; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Contact Us</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Phone: +1 123-456-7890<br>WhatsApp: +1 123-456-7890<br>Email: reductofooddetect@gmail.com<br>Address: Marikina City, Philippines<br>Working Hours: Mon-Fri: 9am-5pm</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>About REDUCTO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>REDUCTO is a revolutionary web app designed to help you determine the freshness of your food using advanced image recognition technology. Simply upload an image of your food, and our AI-powered system will analyze it to tell you if it's fresh or rotten. This app is perfect for anyone looking to reduce food waste and ensure they're eating healthy, fresh food.</p>", unsafe_allow_html=True)
