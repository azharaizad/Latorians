import streamlit as st
import joblib
import numpy as np

class CancerCervixPage:
    def __init__(self):
        pass
    
    def load_model(self):
            model = joblib.load('CC.pkl')
            return model
    
    def predict(self, input_vector):
            predicted_proba = self.model.predict(input_vector)
            prob = predicted_proba[0]
            # Convert probability to percentage
            percentage = float(prob) * 100
            return percentage
    
    def render(self):   
        st.title('Cervix Cancer Questionnaire')
        # Load the model
        with st.spinner("Loading Model..."):
            model = CancerCervixUI.load_model()
            CancerCervixUI.model = model
            st.write("Model successfully loaded")

        # Create dictionary to save responses
        responses = {}
        yes_no_mapping = {'Yes': 1, 'No': 0}

        # Questionnaire
        Q1 = st.number_input("How long have you been smoking?", min_value=0)
        responses['Smoke_years'] = Q1
        Q2 = st.number_input("If you have used hormonal contraceptives before. How many years have you used hormonal contraceptives?", min_value=0)
        responses['Hormonal_Contraceptives'] = Q2
        Q3 = st.radio("Have you used IUD (Intrauterine Device)?", ["No", "Yes"])
        responses['IUD_years'] = yes_no_mapping[Q3]
        Q4 = st.radio("Have you been infected by any STDs?", ["No", "Yes"])
        responses['STDs'] = yes_no_mapping[Q4]
        Q6 = st.number_input("How many STDs diagnoses have you had?", min_value=0)
        responses['STDs:Number_of_diagnosis'] = Q6
        Q7 = st.radio("Have you been diagnosed with cancer?", ["No", "Yes"])
        responses['Dx:Cancer'] = yes_no_mapping[Q7]
        Q8 = st.radio("Have you been diagnosed with HPV?", ["No", "Yes"])
        responses['Dx:HPV'] = yes_no_mapping[Q8]
        Q9 = st.radio("Have you been diagnosed with any other disease?", ["No", "Yes"])
        responses['Dx'] = yes_no_mapping[Q9]

        input_vector = np.array([[Q1, Q2, responses['IUD_years'], responses['STDs'],
                          Q6, responses['Dx:Cancer'],
                          responses['Dx:HPV'],
                          responses['Dx']]])

        input_vector = input_vector.astype('float32')
        input_vector = np.reshape(input_vector, (1, input_vector.shape[1]))

        # Display prediction result
        st.subheader('Prediction Result')

        if st.button('Show Probability'):
            percentage = CancerCervixUI.predict(input_vector)
            prediction_text = f'Based on the provided information, you are predicted to have a {percentage:.2f}% risk of cervix cancer.'
            st.write(prediction_text)


# Create UI
CancerCervixUI = CancerCervixPage()

