# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title = 'Sigma Task by Tanmay')
st.title('Forbes Analysis')
st.subheader('List of year 2022')

st.markdown('---')
df = pd.read_csv('/Users/tanmay/Downloads/Forbes Global 2000 (Year 2022).csv')
st.title('Forbes Top 2000' )
st.dataframe(df)


# -- Feature 1
grouby_column = st.selectbox(
    'What would you like to analyse?',
    ('Sales', 'Profits', 'Assets', 'Market_Value'),)
output_columns = ['Company', 'Industry', 'Country']
df_grouped = df.groupby(by = [grouby_column], sort=True, as_index= False)[output_columns].sum()
st.dataframe(df_grouped)

industry=df.groupby('Industry').mean()

# -- Feature 2
#if st.button('Sector Wise Analysis'):
    

# -- Feature 3
if st.button('Plots for Industries with all attributes'):
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data =df, x = 'Market_Value', y = 'Industry')
    st.pyplot(fig)
    
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data =df, x = 'Assets', y = 'Industry')
    st.pyplot(fig)
    
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data =df, x = 'Profits', y = 'Industry')
    st.pyplot(fig)
    
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(data =df, x = 'Sales', y = 'Industry')
    st.pyplot(fig)


# -- Feature 4
if st.button('Correlation Analysis of Attributes'):
    fig = plt.figure(figsize=(10,4))
    sns.heatmap(df.corr())
    st.pyplot(fig)

if st.button('Comparative Analysis of Attributes'):
    fig = sns.pairplot(df,hue="Sales") 
    st.pyplot(fig)
    
    fig = sns.pairplot(df,hue="Profits") 
    st.pyplot(fig)
    
     
    fig =  sns.pairplot(df,hue="Assets") 
    st.pyplot(fig)
    
     
    fig = sns.pairplot(df,hue="Market_Value") 
    st.pyplot(fig)
    

