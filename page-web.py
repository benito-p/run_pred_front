import streamlit as st
import datetime
import requests

# Définir le titre et la sous-titre de la page
st.markdown("## *Estimez le temps de votre prochain trail !*")

# Ajouter une image de trail
from PIL import Image
image = Image.open("images/trail.jpeg")
st.image(image, use_column_width=True)

st.sidebar.title("Options de course")

# Créer les champs de saisie pour les informations de la séance de trail
distance = st.sidebar.slider("Distance (km)", min_value=0.0, max_value=45.0, value=10.0, step=0.1)
elevation_gain = st.sidebar.slider("Dénivelé positif total (m)", min_value=0, max_value=1000, value=200, step=10)
average_heart_rate = st.sidebar.slider("Fréquence cardiaque moyenne (bpm)", min_value=100, max_value=200, value=150, step=1)
gender = st.sidebar.selectbox("Genre", options=["M", "F"])

default_datetime = datetime.datetime(2023, 4, 1, 10, 0, 0)
selected_datetime = st.sidebar.date_input("Date de la course", value=default_datetime.date(), min_value=None, max_value=None)
selected_time = st.sidebar.time_input("Heure de la course", value=default_datetime.time())
timestamp = f'{selected_datetime} {selected_time}'

# Créer un bouton pour envoyer les informations à l'API
if st.button("**Prédire la durée de ma prochaine course/trail**"):
    # Créer le dictionnaire avec les informations saisies
    params = {
        'distance_km': distance,
        'elevation_gain_m': elevation_gain,
        'average_heart_rate': average_heart_rate,
        'timestamp': timestamp,
        'gender': gender
    }

    url = "http://localhost:8000/prediction"
    results_dict = requests.get(url=url, params=params).json()

    #st.markdown("**Résultats de la prédiction :**")

    if gender == 'M':
        st.write(f"- Coureur débutant : {results_dict.get('race_category_1_pred_time')}")
        st.write(f"- Coureur régulier : {results_dict.get('race_category_2_pred_time')}")
        st.write(f"- Coureur confirmé : {results_dict.get('race_category_3_pred_time')}")
        # st.write('')
        # st.write(f"- Coureur débutant : ")
        # st.write(f"- Coureur régulier : ")
        # st.write(f"- Coureur confirmé : ")

    else:
        st.write(f"- Coureuse débutante : {results_dict.get('race_category_1_pred_time')}")
        st.write(f"- Coureuse régulière : {results_dict.get('race_category_2_pred_time')}")
        st.write(f"- Coureuse confirmée : {results_dict.get('race_category_3_pred_time')}")
        # st.write('')
        # st.write(f"- Coureuse débutante : ")
        # st.write(f"- Coureuse régulière : ")
        # st.write(f"- Coureuse confirmée : ")
