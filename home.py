import streamlit as st
from streamlit_option_menu import option_menu


def main():

    st.title("Projet Groupe#3")

    # Description du projet
    st.subheader("Groupe 3")
    st.markdown("""
    - **ANGUILET Joan-Yves Darys**
    - **KAMBOU Celestin**
    - **MBALLO Cheikh Abdou Khadre**
    - **TANI NOUR Amal**
    """)

    st.subheader("Objectif")
    st.markdown("""
    Créer une application de web scraping avec Streamlit et pouvoir y intégrer son programme.
    """)

    st.subheader("Sujet du Projet")
    st.markdown("""
    Scraper et nettoyer les données sur plusieurs pages en utilisant BeautifulSoup.

    - **URL 1** : [https://dakar-auto.com/senegal/voitures-4](https://dakar-auto.com/senegal/voitures-4)
      - V1: marque
      - V2: année
      - V3: prix
      - V4: adresse
      - V5: kilométrage
      - V6: boite vitesse
      - V7: carburant
      - V8: propriétaire

    - **URL 2** : [https://dakar-auto.com/senegal/motos-and-scooters-3](https://dakar-auto.com/senegal/motos-and-scooters-3)
      - V1: marque
      - V2: année
      - V3: prix
      - V4: adresse
      - V5: kilométrage
      - V6: propriétaire

    - **URL 3** : [https://dakar-auto.com/senegal/location-de-voitures-19](https://dakar-auto.com/senegal/location-de-voitures-19)
      - V1: marque
      - V2: année
      - V3: prix
      - V4: adresse
      - V5: propriétaire
    """)




if __name__ == '__main__':
    main()
