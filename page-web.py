import streamlit as st
import datetime
from PIL import Image
import requests

#background : '#5fb54e'
#text : '#343536'

# Définit la configuration de la page avec l'image en fond d'écran
st.set_page_config(page_title='Trail Predictor', page_icon='🏃‍♂️🏃‍♀️', layout='wide')

st.sidebar.title(':orange[Données de course]')

ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(1 1 1 / 0%); } </style>''', unsafe_allow_html = True)


Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: #439c9a; box-shadow:  0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)


Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: #ffffff ; } </style>''', unsafe_allow_html = True)


col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: #439c9a; }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True)





# Créer les champs de saisie pour les informations de la séance de trail
distance = st.sidebar.slider("Distance (km)", min_value=0.0, max_value=45.0, value=10.0, step=0.1)
elevation_gain = st.sidebar.slider("Dénivelé positif total (m)", min_value=0, max_value=2000, value=200, step=10)
average_heart_rate = st.sidebar.slider("Fréquence cardiaque moyenne (bpm)", min_value=100, max_value=200, value=150, step=1)
gender = st.sidebar.selectbox("Genre", options=["M", "F"])
default_datetime = datetime.datetime(2023, 4, 1, 10, 0)
selected_datetime = st.sidebar.date_input("Date de la séance", value=default_datetime.date(), min_value=None, max_value=None)
selected_time = st.sidebar.time_input("Heure de la séance", value=default_datetime.time())
timestamp = f'{selected_datetime} {selected_time}'

#source image https://media.gettyimages.com/id/687968520/fr/photo/pov-dun-sentier-de-lhomme-en-cours-dex%C3%A9cution-sur-une-voie-unique-sur-la-haute-falaise.jpg?s=2048x2048&w=gi&k=20&c=7--hI-9pvyguq8xBN7AqNAqB8-Ojl9MyA7f2g22EOpA=
# https://images.unsplash.com/photo-1456613820599-bfe244172af5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1474&q=80

##438e9c;

CSS = """
h1 {
    color: black;
}
.stApp {
    background-image: url(https://images.unsplash.com/photo-1498581444814-7e44d2fbe0e2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2898&q=80);
    background-size: cover;
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)



# Définir le titre et la sous-titre de la page
st.title(':orange[Estimez le temps de votre prochain trail !]')

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
            st.write(f"<div style='background-color :    #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color : #white;'> Coureur débutant   🐭   : {results_dict.get('race_category_1_pred_time')} </h6>"
                f"</div>",
                unsafe_allow_html=True)
            st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'> Coureur régulier   🐰   : {results_dict.get('race_category_2_pred_time')} </h6>"
                f"</div>",
                unsafe_allow_html=True)
            st.write(f"<div style='background-color :    #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'> Coureur confirmé   🦊   : {results_dict.get('race_category_3_pred_time')} </h6>"
                f"</div>",
                unsafe_allow_html=True)
            # st.write('')
            # st.write(f"- Coureur débutant : ")
            # st.write(f"- Coureur régulier : ")
            # st.write(f"- Coureur confirmé : ")

        else:
            st.write(f"<div style='background-color :    #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'> Coureuse débutante   🐭   : {results_dict.get('race_category_1_pred_time')} </h6>"
                f"</div>",
                unsafe_allow_html=True)
            st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'> Coureuse régulière   🐰   : {results_dict.get('race_category_2_pred_time')} </h6>"
                f"</div>",
                unsafe_allow_html=True)
            st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'> Coureuse confirmée   🦊   : {results_dict.get('race_category_3_pred_time')} </h6>"
                f"</div>",
                unsafe_allow_html=True)
            # st.write('')
            # st.write(f"- Coureuse débutante : ")
            # st.write(f"- Coureuse régulière : ")
            # st.write(f"- Coureuse confirmée : ")





# Afficher les encarts dans la deuxième colonne
with col2:
    st.markdown(f"<div style='background-color :  #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h2 style= 'color :#white;'>Méthodologie </h2>"
                f"</div>",
                unsafe_allow_html=True
            )
    st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h7 style= 'color :#white;'>La méthodologie repose sur une estimation du temps de course par un modèle entrainé sur un dataset kaggle de différentes courses enregistrées dans la région de Pau https://www.kaggle.com/datasets/olegoaer/running-races-strava. </h7>"
                f"</div>",
                unsafe_allow_html=True
            )


    st.markdown("---")

    st.markdown(f"<div style='background-color :  #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h2 style= 'color :#white;'>L'équipe </h2>"
                f"</div>",
                unsafe_allow_html=True)
    st.write(f"<div style='background-color : #439c9a ; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'>Voici l'équipe qui a développé cette application : </h6>"
                f"</div>",
                unsafe_allow_html=True)

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        st.image("https://ca.slack-edge.com/T02NE0241-U04NG5700HW-494d59d5d15a-512",width=100)
        st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'>Simon </h6>"
                f"</div>",
                unsafe_allow_html=True)

    with col4:
        st.image("https://ca.slack-edge.com/T02NE0241-U04LX13GJET-195f2395ae0a-512", width=100)
        st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'>Thomas </h6>"
                f"</div>",
                unsafe_allow_html=True)

    with col5:
        st.image("https://ca.slack-edge.com/T02NE0241-U04M84VJQPQ-6f717977e3e8-512", width=100)
        st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'>Eryk </h6>"
                f"</div>",
                unsafe_allow_html=True)

    with col6:
        st.image("https://media.licdn.com/dms/image/C4D03AQHZUfunPYygDQ/profile-displayphoto-shrink_400_400/0/1631292675152?e=1686182400&v=beta&t=i5SwZ0z7PpgDLOc-SzaNmOfkTYaICMblpj7fcFWg498", width=100)
        st.write(f"<div style='background-color :   #439c9a; padding: 5px; border-radius: 5px; text-align: center;'>"
                f"<h6 style= 'color :#white;'>Benoit </h6>"
                f"</div>",
                unsafe_allow_html=True)
