import streamlit as st
import streamlit.components.v1 as components  # Correct import


st.header("Avis")
st.title("Formulaire")
# URL du formulaire Kobo Toolbox
kobo_form_url = "https://ee.kobotoolbox.org/x/rX04pau9"




components.iframe(src=kobo_form_url, width=900, height=2000)  