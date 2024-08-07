import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('The purpose of this application is to experience the process of creating predictive models easily in Python and scikit-learn.')

with st.expander("Data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write("**X**")
  X = df.drop("species", axis=1)
  X
  
  st.write("**Y**")
  y = df.species
  y


with st.expander("Data visualization"):
  st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", color="species")

# Data preparations
with st.sidebar:
  st.header("Input features")
  # "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island = st.selectbox("Island", ("Biscoe", "Dream", "Torgersen",))
  gender = st.selectbox("Gendar", ("Male", "Female"))
  bill_length_mm = st.slider("Bill length (mm)", 32.1, 59.6, 43.9)
  
