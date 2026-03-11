import os
import json
from PIL import Image

import numpy as np
import tensorflow as tf
import streamlit as st  
from tensorflow.keras import layers, models

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/Plant_Disease_Prediction_model.keras"
# Load the pre-trained model
model = tf.keras.models.load_model(model_path)

# loading the class names
class_indices = json.load(open(f"{working_dir}/class_indices.json"))

# Function to Load and Preprocess the Image using PIL
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # load the image
    image = Image.open(image_path)
    # Resize the image
    image = image.resize(target_size)  
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    # scale the image values to [0, 1]
    image_array = image_array.astype('float32') / 255.
    return image_array

# Function to Predict the Class of the Image
def predict_image_class(model, image_path, class_indices):
    # Load and preprocess the image
    preprocessed_image = load_and_preprocess_image(image_path)
    # Make a prediction using the model
    predictions = model.predict(preprocessed_image)
    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    # Get the class name from the class indices
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name

# Streamlit App
st.title("🌿Plant Disease Classifier")

uploaded_image = st.file_uploader("Upload an image of a plant leaf", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1:
        resized_image = image.resize((150, 150))
        st.image(resized_image)
    
    with col2:
        if st.button("Classify"):
            # Preprocess the uploaded image and predict the class
            prediction = predict_image_class(model, uploaded_image, class_indices)
            st.success(f"**Prediction:** {prediction}")