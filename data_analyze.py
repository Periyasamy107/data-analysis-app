import streamlit as st
import pandas as pd 
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

# Title and subheader
st.title('Simple Data Analyze App')
st.subheader('We are going to analyse the csv files')

# Upload a dataset
upload = st.file_uploader('Upload a dataset(csv format)')
if upload is not None:
    data = pd.read_csv(upload)

# Showing sample dataset
if upload is not None:
    if st.checkbox('Preview'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())

# Check the datatypes 
if upload is not None:
    if st.checkbox('Datatypes of each column'):
        st.text('Datatypes')
        st.write(data.dtypes)

# Find number of Rows and Columns
if upload is not None:
    data_shape = st.radio('Rows or Columns : ',('Rows','Columns'))
    if data_shape == 'Rows':
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.write(data.shape[1])

# Find the missing values
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox('Null values present in the dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success('Congrats!! No null values present')

# Remove the duplicates 
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        # if st.button('Show the warning message'):
        #     st.warning('This file contains some duplicate values')
        dup = st.selectbox('Do you want to remove the duplicate values',\
                        ('select one', 'yes', 'no'))
        if dup == 'yes':
            data = data.drop_duplicates()
            st.text('Duplicates are removed')
        if dup == 'no':
            st.text('No problem')
    else:
        st.success('congrats!! No duplicates are there in this file')

# Get overall statistics
if upload is not None:
    if st.checkbox('Summary of the dataset'):
        st.write(data.describe(include='all'))

# About section
if st.button('About App'):
    st.text('Build with Streamlit')
    st.text('Thanks to Streamlit')

# by 
if st.checkbox('By'):
    st.success('Biggod is always with you')





