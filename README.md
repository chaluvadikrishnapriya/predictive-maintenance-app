# predictive-maintenance-app
This Predictive Maintenance Classifier is a machine learning-based web application built using Streamlit. It predicts machine failure based on input sensor values, helping industries prevent breakdowns and optimize maintenance schedules.

The model is trained on industrial sensor data, considering key parameters like:

Air Temperature [K]
Process Temperature [K]
Rotational Speed [rpm]
Torque [Nm]
Tool Wear [min]
The application provides real-time predictions on whether the machine will fail, along with the failure type (e.g., Heat Failure, Power Failure, etc.).

To run:::
streamlit run app.py

