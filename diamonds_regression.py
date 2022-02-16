import numpy as np
import pandas as pd
import os
from sklearn.externals import joblib
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white', font_scale=5)

# load the model from disk
loaded_model = joblib.load('final_diamonds_regression.sav')

st.header('Estimate Diamond Price')

# Carat
carat = st.slider('Carat', 0.0, 5.0, 0.1)

# Cut
cut = st.radio('Cut', ('Fair', 'Good', 'Ideal', 'Premium', 'Very Good'))

if cut == 'Fair':
    cut_list = [1, 0, 0, 0, 0]
elif cut == 'Good':
    cut_list = [0, 1, 0, 0, 0]
elif cut == 'Ideal':
    cut_list = [0, 0, 1, 0, 0]
elif cut == 'Premium':
    cut_list = [0, 0, 0, 1, 0]
elif cut == 'Very Good':
    cut_list = [0, 0, 0, 0, 1]

# Depth
depth = st.slider('Depth', 0.0, 100.0, 50.0)

# Table
table = st.slider('Table', 0.0, 100.0, 50.0)

data = [carat] + cut_list + [depth, table]
prediction = round (loaded_model.predict([data])[0])

st.subheader(f"Suggested Price: {prediction}")
