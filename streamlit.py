#import std libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Write a title
st.write('Penguin Explorer')
# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write('**Little** *app*')
# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')
# Write heading for Data
st.header('Data')
# Read csv file and output a sample of 20 data points
df = pd.read_csv('penguins_extra.csv')
st.write('Display a sample of 20 data points according to the species selected with corresponding title')

# Add a selectbox for species
species = st.selectbox('Choose the species:', df.species.unique())
# Display a sample of 20 data points according to the species selected with corresponding title
# Plotting seaborn
# Plotting plotly
# Bar chart count of species per island
# Maps
# Reference https://deckgl.readthedocs.io/en/latest/
# sidebar comment

