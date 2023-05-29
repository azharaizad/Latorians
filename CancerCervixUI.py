import streamlit as st
import h5py
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Assuming you have your dataset of factors affecting cervical cancer in a CSV file
DATA_FILE = 'risk_factors_cervical_cancer.csv'
# Assuming you have your trained FNN model saved in a file
MODEL_FILE = 'CervixCancerDetector.ipynb'

# Load and preprocess the dataset
def load_dataset():
    df = pd.read_csv(DATA_FILE)
    # Perform any necessary preprocessing steps (e.g., handling missing values, encoding categorical variables)
    return df

df = load_dataset()

# Perform any necessary preprocessing steps on the features (e.g., scaling)
scaler = StandardScaler()

# Load the trained FNN model
model = tf.keras.models.load_model(MODEL_FILE)

# Configure the Streamlit app
st.title('Cervical Cancer Predictor Questionnaire')

# Create input widgets for each feature in the dataset
feature_columns = df.columns[:-1]  # Exclude the target column
answers = []

for column in feature_columns:
    answer = st.selectbox(f"Select {column}", df[column].unique())
    answers.append(answer)

# Preprocess the answers
answers = scaler.transform([answers])

# Predict the probability of getting cervical cancer based on the user's answers
prediction = model.predict(answers)[0][0]

# Display the prediction
st.subheader("Cervical Cancer Probability")
st.write(f"The predicted probability of getting cervical cancer is: {prediction:.4f}")
