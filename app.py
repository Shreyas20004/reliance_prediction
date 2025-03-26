import streamlit as st
import pickle
# Streamlit UI
st.title("Reliance Stock Price Prediction")

# Load trained model
with open("./reliance_model.pkl", "rb") as f:
    model = pickle.load(f)

# User input for stock price prediction
ma_7 = st.number_input("Enter 7-day Moving Average:")
ma_30 = st.number_input("Enter 30-day Moving Average:")
lag_1 = st.number_input("Enter Previous Day's Price:")

if st.button("Predict Price"):
    input_data = [[ma_7, ma_30, lag_1]]
    prediction = model.predict(input_data)[0]
    st.write(f"### Predicted Reliance Stock Price: ₹{prediction:.2f}")