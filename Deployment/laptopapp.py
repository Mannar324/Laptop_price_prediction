import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
with open('D:\Scraping_tasks\classifer.pkl','rb') as file:
    model=pickle.load(file)
st.set_page_config(
    page_title="laptop price predictor App",
    layout="centered"
)

#side bar
with st.sidebar:
    selected=  option_menu(
    "Main Menu",  # required
    ['Overview','EDA', 'Prediction'],  # required
    icons=[ 'card-list','graph-up-arrow','search'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
)

if( selected == 'Overview'):
   st.title('Laptop Price Prediction')
   st.image("laptop.jpeg",width=600)
   st.markdown('#### This project aims to predict the prices of noon store laptops in SAR currency ')


#.....................................................................................................................        


if selected == 'Prediction':
    st.title("Price Prediction")
    col1, col2 = st.columns(2)
    with col1:
        Category = st.selectbox('Category',options=['HUAWEI', 'Apple', 'ASUS', 'MSI', 'Lenovo', 'HP', 'Acer',
       'Microsoft', 'DELL'])
    with col2:
        Core = st.selectbox('Core', options=['Core i5', 'Core i7', 'Core i9', 'Core i3'])
    col3, col4 = st.columns(2)
    with col3:
        Ram = st.selectbox('Ram', options=['8GB', '16GB', '4GB', '256GB', '512GB', '32GB', '18GB', '36GB',
       '64GB', '2GB', '48GB', '12GB'])
    with col4:
        Memory = st.selectbox('Memory', options=['256GB', '512GB', '1TB', '128GB', '2TB'])

    st.markdown("<br><br>", unsafe_allow_html=True)
    col5, col6, col7 = st.columns([1,2,1])

    with col6:
        prediction = st.button('Predict the price 🔍')
    categories=['HUAWEI', 'Apple', 'ASUS', 'MSI', 'Lenovo', 'HP', 'Acer',
       'Microsoft', 'DELL']
    cores=['Core i5', 'Core i7', 'Core i9', 'Core i3']
    rams=['8GB', '16GB', '4GB', '256GB', '512GB', '32GB', '18GB', '36GB',
       '64GB', '2GB', '48GB', '12GB']
    memories=['256GB', '512GB', '1TB', '128GB', '2TB']     
    enc_cat={cat:i for i,cat in enumerate(categories)}
    enc_core={core:i for i,core in enumerate(cores)}
    enc_ram={ram:i for i,ram in enumerate(rams)}
    enc_memory={memory:i for i,memory in enumerate(memories)}
    #make dataframe to predict the price
    df=pd.DataFrame({ 'Category': [enc_cat[Category]],  # Wrap scalar values in lists
    'Core': [enc_core[Core]],
    'Ram': [enc_ram[Ram]],
    'Memory': [enc_memory[Memory]]})
    
    if prediction:
       result=model.predict(df) 
       st.write('The predicted price is:',round(result[0],2),' SAR') 
#.....................................................................................................................        
   
if selected=='EDA':
    #st.title('EDA Analysis')
    page_bg_css = """
    <style>
    body {
        background-color: #E88D67;  /* Change the background color here */
    }
    </style>
    """

# Apply the custom CSS
    st.markdown(page_bg_css, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>EDA Analysis</h1>", unsafe_allow_html=True)
    df=pd.read_csv('Modified laptops.csv')
    categories=df.groupby('Category')['price'].mean()
    categories=categories.sort_values(ascending=False)
    Ram=df['Ram'].value_counts().sort_values(ascending=False)
    fig1 = px.bar(categories, x=categories.index, y=categories.values, title="Top Companies by avgarge price",color_discrete_sequence=['#FF6347'])
    fig2 = px.bar(Ram, x=Ram.index, y=Ram.values, title="Top Rams")
    fig3 = px.histogram(df, x='price', title='Distribution of Price', nbins=5,color_discrete_sequence=['purple'])
    fig4 = px.scatter(df, x='Core', y='price', title='Price vs Core')
    fig5 = px.box(df, x='Category', y='price', title='Price vs Category')
    col1, col_space, col2 = st.columns([1, 18, 1])

    with col1:
        st.plotly_chart(fig1)

    with col_space:
        st.write(" ")  # This column acts as a spacer

    with col2:
        st.plotly_chart(fig2)

    col3,space_col,col4=st.columns([1, 18, 1])        
    with col3:
         st.plotly_chart(fig3) 
    with col4:
         st.plotly_chart(fig4)    
    col5,col6=st.columns([1,4.5])
    with col6:
        fig5.update_layout(width=1000, height=700)
        st.plotly_chart(fig5)
    
        
        