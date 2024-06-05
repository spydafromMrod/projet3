from fonctions.functions import display_data
import streamlit as st
import pandas as pd

st.header("fichiers CSV")


# Load the CSV data into DataFrames
df_cars = pd.read_csv('data/url1nettoyer.csv')
df_motorcycles = pd.read_csv('data/url2nettoyer.csv')
df_locations = pd.read_csv('data/url3nettoyer.csv')


# Clean the 'prix' column
df_cars['prix'] = df_cars['prix'].str.replace(' F CFA', '').str.replace(' ', '')
df_cars['prix'] = pd.to_numeric(df_cars['prix'], errors='coerce')

df_motorcycles['prix'] = df_motorcycles['prix'].str.replace(' F CFA', '').str.replace(' ', '')
df_motorcycles['prix'] = pd.to_numeric(df_motorcycles['prix'], errors='coerce')

df_locations['prix'] = df_locations['prix'].str.replace(' F CFA', '').str.replace(' ', '')
df_locations['prix'] = pd.to_numeric(df_locations['prix'], errors='coerce')

 

display_data(df_cars, df_motorcycles, df_locations)




