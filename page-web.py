import streamlit as st
import datetime
from PIL import Image
import requests



# Définit la configuration de la page avec l'image en fond d'écran
st.set_page_config(page_title='Trail Predictor', page_icon='🏃‍♂️🏃‍♀️', layout='wide')

st.sidebar.title("Options de course")

# Créer les champs de saisie pour les informations de la séance de trail
distance = st.sidebar.slider("Distance (km)", min_value=0.0, max_value=45.0, value=10.0, step=0.1)
elevation_gain = st.sidebar.slider("Dénivelé positif total (m)", min_value=0, max_value=2000, value=200, step=10)
average_heart_rate = st.sidebar.slider("Fréquence cardiaque moyenne (bpm)", min_value=100, max_value=200, value=150, step=1)
gender = st.sidebar.selectbox("Genre", options=["M", "F"])
default_datetime = datetime.datetime(2023, 4, 1, 10, 0)
selected_datetime = st.sidebar.date_input("Date de la séance", value=default_datetime.date(), min_value=None, max_value=None)
selected_time = st.sidebar.time_input("Heure de la séance", value=default_datetime.time())
timestamp = f'{selected_datetime} {selected_time}'

CSS = """
h1 {
    color: black;
}
.stApp {
    background-image: url(https://media.gettyimages.com/id/687968520/fr/photo/pov-dun-sentier-de-lhomme-en-cours-dex%C3%A9cution-sur-une-voie-unique-sur-la-haute-falaise.jpg?s=2048x2048&w=gi&k=20&c=7--hI-9pvyguq8xBN7AqNAqB8-Ojl9MyA7f2g22EOpA=);
    background-size: cover;
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)



# Définir le titre et la sous-titre de la page
st.title("Estimez le temps de votre prochain trail !")

# Diviser l'écran en deux colonnes
col1, col2 = st.columns(2)


# Afficher l'encart de la méthodologie dans la colonne de gauche
with col1:
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

        url = st.secrets.get('url_live','http://localhost:8000')
        url = f'{url}/prediction'
        results_dict = requests.get(url=url, params=params).json()

        #st.markdown("**Résultats de la prédiction :**")

        if gender == 'M':
            st.write(f"- Coureur débutant 🐌 : {results_dict.get('race_category_1_pred_time')}")
            st.write(f"- Coureur régulier 🐰 : {results_dict.get('race_category_2_pred_time')}")
            st.write(f"- Coureur confirmé 🐆 : {results_dict.get('race_category_3_pred_time')}")
            # st.write('')
            # st.write(f"- Coureur débutant : ")
            # st.write(f"- Coureur régulier : ")
            # st.write(f"- Coureur confirmé : ")

        else:
            st.write(f"- Coureuse débutante 🐌 : {results_dict.get('race_category_1_pred_time')}")
            st.write(f"- Coureuse régulière 🐰 : {results_dict.get('race_category_2_pred_time')}")
            st.write(f"- Coureuse confirmée 🐆 : {results_dict.get('race_category_3_pred_time')}")
            # st.write('')
            # st.write(f"- Coureuse débutante : ")
            # st.write(f"- Coureuse régulière : ")
            # st.write(f"- Coureuse confirmée : ")





# Afficher les encarts dans la deuxième colonne
with col2:
    st.markdown("## Méthodologie")
    st.write("La méthodologie repose sur une estimation du temps de course par un modèle entrainé sur un dataset kaggle de différentes courses enregistrées dans la région de Pau https://www.kaggle.com/datasets/olegoaer/running-races-strava.")

    st.markdown("---")

    st.markdown("## L'équipe")
    st.write("Voici l'équipe qui a développé cette application :")

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        st.image("https://ca.slack-edge.com/T02NE0241-U04NG5700HW-494d59d5d15a-512", use_column_width=True)
        st.write("Simon")

    with col4:
        st.image("https://ca.slack-edge.com/T02NE0241-U04LX13GJET-195f2395ae0a-512", use_column_width=True)
        st.write("Thomas")

    with col5:
        st.image("https://ca.slack-edge.com/T02NE0241-U04M84VJQPQ-c61211e3448c-512", use_column_width=True)
        st.write("Eryk")

    with col6:
        st.image("https://media.licdn.com/dms/image/C4D03AQHZUfunPYygDQ/profile-displayphoto-shrink_400_400/0/1631292675152?e=1686182400&v=beta&t=i5SwZ0z7PpgDLOc-SzaNmOfkTYaICMblpj7fcFWg498", use_column_width=True)
        st.write("Benoit")
