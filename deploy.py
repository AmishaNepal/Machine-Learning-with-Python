import streamlit as st
import numpy as np
import joblib

#Load trained model
model=joblib.load('iris_model.pkl')

#Streamline UI
st.title("🌸 Iris Flower Species Prediction🌸")
st.write("Enter the flower measurements and get the prediction.")

#Input Fields
sepal_length = st.number_input("Sepal Length(cm)", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
sepal_width = st.number_input("Sepal Width(cm)", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
petal_length = st.number_input("Petal Length(cm)", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
petal_width = st.number_input("Petal width(cm)", min_value=0.0, max_value=10.0, step=0.1, value=0.0)

col1,col2=st.columns([2,2])

#Predict Button
with col1:
    if st.button("Predict",use_container_width=True):
        input_data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])
        prediction=model.predict(input_data)
        species=prediction[0]
        st.success(f"☘️ Predicted Species: **{species.capitalize()}**")


# Reset Button
with col2:
    if st.button("Reset", use_container_width=True):
        st.experimental_rerun()
    