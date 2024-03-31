import streamlit as st
import pandas as pd


st.title('Book collection')

data = pd.read_csv("goodreads_library_export.csv")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Books ratings')

hist_values = data.groupby("My Rating")["Title"].count()
st.bar_chart(hist_values, color="#ffaa00")

st.subheader('Year Published')

hist_values = data.groupby("Year Published")["Title"].count()
st.bar_chart(hist_values)

st.subheader('Binding type')

hist_values = data.groupby("Binding")["Title"].count()
st.bar_chart(hist_values)


