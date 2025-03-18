import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("predictive_maintenance_model.pkl")

# Define feature labels
feature_labels = [
    "Air Temperature [K]", 
    "Process Temperature [K]", 
    "Rotational Speed [rpm]", 
    "Torque [Nm]", 
    "Tool Wear [min]"
]

# Define labels for predictions (failure types)
FAILURE_LABELS = {
    0: "✅ No Failure",
    1: "🔥 Heat Failure",
    2: "⚡ Power Failure",
    3: "🛠️ Tool Wear Failure",
    4: "🏋️‍♂️ Overstrain Failure"
}

# Streamlit page settings
st.set_page_config(page_title="Predictive Maintenance", page_icon="🔧", layout="centered")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/476/476863.png", width=100)  # Maintenance Icon
st.sidebar.title("🔧 Predictive Maintenance Classifier")
st.sidebar.markdown("Enter machine sensor readings to predict if maintenance is needed.")

# Main title
st.title("🔍 Predictive Maintenance System")
st.markdown("**Fill in the equipment's operating data below:**")

# User input fields
user_inputs = []
for label in feature_labels:
    value = st.number_input(f"🔹 {label}", value=0.0, step=0.1, format="%.2f")
    user_inputs.append(value)

# Predict button
if st.button("🚀 Predict"):
    try:
        # Convert inputs to numpy array and reshape
        features = np.array(user_inputs).reshape(1, -1)
        
        # Model prediction
        prediction = model.predict(features)[0]

        # Display result with styling
        if prediction == 0:
            st.success(f"✅ **Prediction:** {FAILURE_LABELS[0]}")
            st.balloons()
        else:
            st.error(f"⚠️ **Failure Detected:** {FAILURE_LABELS[prediction]}")
            st.warning("Immediate maintenance is recommended!")

    except Exception as e:
        st.error("❌ An error occurred! Please enter valid numerical values.")

# Footer
st.markdown("---")
st.markdown("🚀 Developed with ❤️ using **Streamlit & Machine Learning**")
