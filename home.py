import streamlit as st

class HomePage:
    def __init__(self):
        pass

    def render(self):
        st.title("Home Page")
        st.write("### Welcome to the Cancer Cervix Indicator!")
        st.markdown("##### WIA1006 (LATORIANS)")
        st.markdown("##### Team Member:")
        table_md = """
        |No.|Name|Matrix No.|
        |--|--|--|
        |1.|Nor Farhan Fitri bin Nor Effendi|22059364|
        |2.|Muhammad Daniel Bin Abd.Razak|U2101081|
        |3.|Muhammad Azhar Aizad Asfarizailin|U2100687|
        |4.|Abdul Azim Bin Abdul Salam|U2102134|
        |5.|Abdul Hanif Bin Abdul Aziz|U2101905|
        """
        st.markdown(table_md)
        st.markdown("### Introduction to Cancer Cervix Indicator")

        introduction = '''The Cancer Cervix Indicator is a web-based tool designed to assess the risk of cervix cancer in individuals. Cervix cancer is a significant health concern affecting women worldwide. Early detection and intervention play a crucial role in improving outcomes and reducing mortality rates.

The Cancer Cervix Indicator utilizes a machine learning model trained on relevant risk factors and medical data to predict an individual's risk of developing cervix cancer. By answering a series of questions related to smoking history, contraceptive use, previous diagnoses, and other relevant factors, the indicator provides an estimate of the probability of cervix cancer.

This tool aims to empower individuals by increasing awareness about cervix cancer and promoting early detection. It is not intended to replace medical advice or diagnosis but rather serves as an informative resource to encourage proactive health management.

Please note that the Cancer Cervix Indicator should be used in conjunction with regular medical check-ups and consultations with healthcare professionals for a comprehensive assessment of one's health status.'''

        st.markdown(
    "<div style='text-align: justify'>{}</div>".format(introduction),
    unsafe_allow_html=True
)

