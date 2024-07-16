import streamlit as st
import pandas as pd
import plotly.express as px

def display_data(df_cars, df_motorcycles, df_locations):
    st.title('Donnees CSV')
    st.write('### Voitures en vente')
    st.dataframe(df_cars)

    st.write('### Motos et scooter en vente')
    st.dataframe(df_motorcycles)

    st.write('### donnee Location ')
    st.dataframe(df_locations)

def plot_data(df, title):
    st.write(f'### {title} Data')
    
    # Nombre de vehicule par an
    vehicle_counts_by_year = df['annee'].value_counts().reset_index()
    vehicle_counts_by_year.columns = ['Year', 'Count']
    vehicle_counts_by_year = vehicle_counts_by_year.sort_values(by='Year')

    # Plot number of vehicles by year
    fig = px.bar(vehicle_counts_by_year, x='Year', y='Count', title=f'Number of {title}s by Year')
    st.plotly_chart(fig)

    # Top 10 most expensive vehicles
    top_10_expensive = df.nlargest(10, 'prix')
    fig_expensive = px.bar(top_10_expensive, 
                           x='prix', 
                           y='marque', 
                           orientation='h', 
                           title=f'Top 10 most expensive {title}s', 
                           text='prix',
                           labels={'prix': 'Price (F CFA)', 'marque': 'Brand'},
                           color='prix',  
                           color_discrete_sequence=px.colors.sequential.Viridis)  # You can change this to any color sequence you prefer
    
    fig_expensive.update_layout(
        yaxis={'categoryorder':'total ascending'},
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Background color of the plot area
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Background color of the entire figure
        font=dict(color="white")  # Text color
    )
    st.plotly_chart(fig_expensive)

    # Number of vehicles by region
    # Calcul du nombre de véhicules par région
    vehicle_counts_by_region = df['adresse'].value_counts().reset_index()
    vehicle_counts_by_region.columns = ['Region', 'Count']
    vehicle_counts_by_region = vehicle_counts_by_region.sort_values(by='Count', ascending=False)

    # Couleurs personnalisées
    colors = px.colors.qualitative.Alphabet[:len(vehicle_counts_by_region)]

    # Création du graphique
    fig_region = px.bar(
        vehicle_counts_by_region, 
        x='Region', 
        y='Count', 
        title='Number of Vehicles by Region', 
        color='Region',
        color_discrete_sequence=colors
    )

    # Affichage du graphique avec Streamlit
    st.plotly_chart(fig_region)

    # Number of vehicles by brand
    vehicle_counts_by_brand = df['marque'].value_counts().reset_index()
    vehicle_counts_by_brand.columns = ['Brand', 'Count']
    vehicle_counts_by_brand = vehicle_counts_by_brand.sort_values(by='Count', ascending=False)

    # Plot number of vehicles by brand
    fig_brand = px.bar(vehicle_counts_by_brand, x='Brand', y='Count', title=f'Number of {title}s by Brand')
    st.plotly_chart(fig_brand)

def plot_comparative_data(df_cars, df_motorcycles, df_locations):
    st.title('Comparative Analysis')
    
    # Comparative Price Distribution
    df_cars['type'] = 'Car'
    df_motorcycles['type'] = 'Motorcycle'
    df_locations['type'] = 'Location'
    df_combined = pd.concat([df_cars, df_motorcycles, df_locations])

    fig_price_distribution = px.box(df_combined, x='type', y='prix', title='Comparative Price Distribution',
                                    labels={'prix': 'Price (F CFA)', 'type': 'Vehicle Type'})
    st.plotly_chart(fig_price_distribution)

    # Comparative Count by Year
    vehicle_counts_by_year = df_combined.groupby(['type', 'annee']).size().reset_index(name='Count')
    fig_count_by_year = px.line(vehicle_counts_by_year, x='annee', y='Count', color='type', 
                                title='Comparative Count by Year', labels={'annee': 'Year', 'Count': 'Count'})
    st.plotly_chart(fig_count_by_year)

    # Comparative Count by Region
    vehicle_counts_by_region = df_combined.groupby(['type', 'adresse']).size().reset_index(name='Count')
    fig_count_by_region = px.bar(vehicle_counts_by_region, x='adresse', y='Count', color='type', 
                                 title='Comparative Count by Region', labels={'adresse': 'Region', 'Count': 'Count'})
    st.plotly_chart(fig_count_by_region)

# Load the CSV data into DataFrames
df_cars = pd.read_csv('data/url1nettoyer.csv')
df_motorcycles = pd.read_csv('data/url2nettoyer.csv')
df_locations = pd.read_csv('data/url3nonnettoyer.csv')

# Clean the 'prix' column
def clean_prix(df):
    df['prix'] = df['prix'].str.replace(' F CFA', '').str.replace(' ', '')
    df['prix'] = pd.to_numeric(df['prix'], errors='coerce')
    return df