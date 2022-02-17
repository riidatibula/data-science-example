import joblib
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='white', font_scale=1, rc = {'figure.figsize':(10,5)})

# load the model from disk
loaded_model = joblib.load('final_diamonds_regression.sav')

#####################################Data Frame#####################################

# Load DataFrame
@st.cache
def load_data():
    return pd.read_csv('diamonds_regression.csv')

if st.sidebar.checkbox('Show DataFrame'):
    st.header('Data Frame')
    data = load_data().head(20)
    data
    
#################################Correlation Heatmap#################################

if st.sidebar.checkbox('Show Correlation Heatmap'):
    data = load_data()
    fig, ax = plt.subplots()
    sns.heatmap(data.corr(), annot=True)
    
    st.header('Correlation Heatmap')
    st.pyplot(fig)
    st.write("Based on the correlation heatmap, the price is highly " +
             "correlated with the attributes Carat, x, y, and z — and less correlated with the attributes " +
             "Table and Depth.")

    
####################################Scatter Plot#####################################

if st.sidebar.checkbox('Show Scatter Plot'):
    data = load_data()
    fig2, ax = plt.subplots()
    sns.scatterplot(data=data, x='carat', y='x', hue='price')
    
    st.header('Scatter Plot')
    st.pyplot(fig2)
    st.write("Price is directly proportional to the attributes Carat and x")

####################################Scatter Plot#####################################

if st.sidebar.checkbox('Show Line Plot'):
    data = load_data()
    fig3, ax = plt.subplots()
    sns.lineplot(data=data, x='carat', y='price')
    
    st.header('Line Plot of Carat and Price')
    st.pyplot(fig3)

##################################Price Prediction##################################

st.header('Estimate Diamond Price')
st.write("A model was trained with the attributes: Carat, Cut, Depth, Table, and Price (having Price as the target)")
st.write("However, based on the correlation heatmap, Price is not highly correlated with Table and Depth but with attributes x, y, and z.")

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
