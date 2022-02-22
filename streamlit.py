# import std libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Write a title
st.write('Penguin Explorer')
# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write('**Little** *app* for exploring `penguin` [dataset](https://allisonhorst.github.io/palmerpenguins/)')
# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')
# Write heading for Data
st.header('Data')
# Read csv file and output a sample of 20 data points
df = pd.read_csv('penguins_extra.csv')
st.write('Display a sample of data points from `penguins` dataset', df.sample(20))
# Add a selectbox for species
species = st.selectbox('Choose the species:',df.species.unique())
# Display a sample of 20 data points according to the species selected with corresponding title
df_species = df.loc[df.species==species]
st.write(f'Subset of data for {species} penguins',df_species)
# Plotting seaborn
st.subheader('Plotting')
fig,ax = plt.subplots()
ax = sns.scatterplot(data = df, x='bill_length_mm',y='flipper_length_mm',hue='species',size='sex')
st.pyplot(fig)
# Plotting plotly
fig = px.scatter(df,x='bill_length_mm',y='flipper_length_mm',color='species',animation_frame='species',hover_name='name',range_x=[30,70],range_y=[150,250])
st.plotly_chart(fig)
# Bar chart count of species per island
st.bar_chart(df.groupby('species')['island'].count())
# Maps
st.map(df)
# Reference https://deckgl.readthedocs.io/en/latest/
st.write('If you are intersted to further explore mapping check out [pydeck](https://deckgl.readthedocs.io/en/latest/)')
# sidebar comment
choice = st.sidebar.radio('Hope this was interesting',['yes','no'])
name = st.text_input('First name')
st.write(name)