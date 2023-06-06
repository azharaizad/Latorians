import streamlit as st
import joblib
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from tensorflow import keras 

#load our model
model_3 = joblib.load('CC.pkl')

#create UI
st.title('Cervix Cancer Questionnaire')

# create dictionary to save response
responses = {}
yes_no_mapping = {'Yes': 1, 'No': 0}

#question
Q1 = st.number_input("How long have you been smoking?",min_value=0)
responses['Smoke_years'] = Q1
Q2 = st.number_input("Have you used hormonal contraceptives? For how many years have you used hormonal contraceptives?",min_value=0)
responses['Hormonal_Contraceptives'] = Q2
Q3 = st.radio("Have you used IUD (Intrauterine Device)?",["Yes","No"])
responses['IUD_years'] = yes_no_mapping[Q3]
Q4 = st.radio("Have you been infected by any STDs",["Yes","No"])
responses['STDs'] = yes_no_mapping[Q4]
Q5 = st.number_input("How many STDs have been infected?",min_value=0)
responses['STDs_number'] = Q5
Q6 = st.number_input("Have many STDs diagnosis have you taken?",min_value=0)
responses['STDs:Number_of_diagnosis'] = Q6
Q7 = st.radio("Have you been diagnosed with cancer?",["Yes","No"])
responses['Dx:Cancer'] = yes_no_mapping[Q7]
Q8 = st.radio("Have you been diagnosed with HPV?",["Yes","No"])
responses['Dx:HPV'] = yes_no_mapping[Q8]
Q9 = st.radio("Have you been diagnosed with any other disease?",["Yes","No"])
responses['Dx'] = yes_no_mapping[Q9]




# Perform prediction
# Perform prediction
input_vector = np.array([[Q1, Q2, responses['IUD_years'], responses['STDs'],
                          Q5, Q6, responses['Dx:Cancer'],
                          responses['Dx:HPV'],
                          responses['Dx']]])

input_vector = input_vector.astype('float32')

input_vector = input_vector.astype('float32')
input_vector = np.reshape(input_vector, (1, input_vector.shape[1]))
predicted_proba = model_3.predict(input_vector)
prob = predicted_proba[0]
# Convert probability to percentage
percentage = float(prob) * 100

# Display prediction result
st.subheader('Prediction Result')
st.write(f'Based on the provided information, you are predicted to have a {percentage:.2f}% risk of cervix cancer.')

