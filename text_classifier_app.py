import streamlit as st
import joblib

# Load the saved model and vectorizer
classifier = joblib.load('text_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Streamlit app title and description
st.title("Text Emotion Classifier")
st.write("Enter a comment to predict its associated emotion!")

# Text input from the user
user_input = st.text_area("Your Comment", "")

if st.button("Predict Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter a valid comment!")
    else:
        # Transform the input using the loaded vectorizer
        input_vectorized = vectorizer.transform([user_input])
        # Predict emotion
        prediction = classifier.predict(input_vectorized)[0]
        # Display the prediction
        st.success(f"The predicted emotion is: **{prediction}**")
