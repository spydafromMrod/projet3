import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.header("Scraping et telechargement")


# Fonction de scraping pour voitures
def scrape_car_data(url, pages_to_scrape):
    data = []

    for page in range(1, pages_to_scrape + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        containers = soup.find_all('div', class_='listings-cards__list-item mb-md-3 mb-3')

        for container in containers:
            marque = container.find('h2').get_text(strip=True) if container.find('h2') else None
            details = container.find_all('li')
            annee = marque.split()[-1] if marque else None
            prix = container.find('h3').get_text(strip=True) if container.find('h3') else None
            kilometrage = details[1].get_text(strip=True) if len(details) > 1 else None
            boite_vitesse = details[2].get_text(strip=True) if len(details) > 2 else None
            carburant = details[3].get_text(strip=True) if len(details) > 3 else None
            proprietaire = container.find('p', class_='time-author m-0').get_text(strip=True) if container.find('p') else None

            data.append({
                'marque': marque,
                'annee': annee,
                'prix': prix,
                'kilometrage': kilometrage,
                'boite_vitesse': boite_vitesse,
                'carburant': carburant,
                'proprietaire': proprietaire
            })

    columns = ['marque', 'annee', 'prix', 'kilometrage', 'boite_vitesse', 'carburant', 'proprietaire']
    df = pd.DataFrame(data, columns=columns)
    return df

# Fonction de scraping pour location de voitures
def scrape_rental_data(url, pages_to_scrape):
    data = []

    for page in range(1, pages_to_scrape + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        containers = soup.find_all('div', class_='listings-cards__list-item mb-md-3 mb-3')

        for container in containers:
            marque = container.find('h2').get_text(strip=True) if container.find('h2') else None
            details = container.find_all('li')
            annee = marque.split()[-1] if marque else None
            prix = container.find('h3').get_text(strip=True) if container.find('h3') else None
            adresse = container.find('span', class_='town-suburb').get_text(strip=True) if container.find('span', class_='town-suburb') else None
            proprietaire = container.find('p', class_='time-author m-0').get_text(strip=True) if container.find('p') else None

            data.append({
                'marque': marque,
                'annee': annee,
                'prix': prix,
                'adresse': adresse,
                'proprietaire': proprietaire
            })

    columns = ['marque', 'annee', 'prix', 'adresse', 'proprietaire']
    df = pd.DataFrame(data, columns=columns)
    return df

# Fonction de scraping pour motos et scooters
def scrape_motorcycle_data(url, pages_to_scrape):
    data = []

    for page in range(1, pages_to_scrape + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        containers = soup.find_all('div', class_='listings-cards__list-item mb-md-3 mb-3')

        for container in containers:
            marque = container.find('h2').get_text(strip=True) if container.find('h2') else None
            annee = marque.split()[-1] if marque else None
            prix = container.find('h3').get_text(strip=True) if container.find('h3') else None
            adresse = container.find('span', class_='town-suburb').get_text(strip=True) if container.find('span', class_='town-suburb') else None
            kilometrage = container.find('li', class_='listing-item__attribute list-inline-item').get_text(strip=True) if container.find('li', class_='listing-item__attribute list-inline-item') else None
            proprietaire = container.find('p', class_='time-author m-0').get_text(strip=True) if container.find('p') else None

            data.append({
                'marque': marque,
                'annee': annee,
                'prix': prix,
                'adresse': adresse,
                'kilometrage': kilometrage,
                'proprietaire': proprietaire
            })

    columns = ['marque', 'annee', 'prix', 'adresse', 'kilometrage', 'proprietaire']
    df = pd.DataFrame(data, columns=columns)
    
    return df



# Streamlit app
st.title("Web Scraping des Annonces de Véhicules")

# Option de choix du lien
option = st.selectbox("Choisissez le lien à scrapper", 
                      ["Vente de voitures - Dakar Auto", 
                       "Location de voitures - Dakar Auto",
                       "Motos et scooters - Dakar Auto"])

if option == "Vente de voitures - Dakar Auto":
    base_url = 'https://dakar-auto.com/senegal/voitures-4'
    scrape_function = scrape_car_data
elif option == "Location de voitures - Dakar Auto":
    base_url = 'https://dakar-auto.com/senegal/location-de-voitures-19'
    scrape_function = scrape_rental_data
else:
    base_url = 'https://dakar-auto.com/senegal/motos-and-scooters-3'
    scrape_function = scrape_motorcycle_data

# Nombre de pages à scrapper
pages = st.number_input("Nombre de pages à scrapper", min_value=1, max_value=10, value=1, step=1)
scrape_button = st.button("Scrapper les données")

if scrape_button:
    with st.spinner("Scrapping en cours..."):
        data_frame = scrape_function(base_url, pages)
        st.success("Scraping terminé!")
        st.dataframe(data_frame)
#        st.write("Aperçu des données scrappées:")
#        st.write(data_frame)


if scrape_button:
    with st.spinner("Scrapping en cours...pour telechargement"):
        data_frame = scrape_function(base_url, pages)
        st.success("Scraping terminé!")
        
        # Télécharger les données
        st.download_button(
            label="Télécharger les données scrappées",
            data=data_frame.to_csv(index=False).encode('utf-8'),
            file_name=f'{option.replace(" ", "_").lower()}.csv',
            mime='text/csv'
        )


