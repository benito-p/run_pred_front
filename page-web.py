import streamlit as st
import datetime


# Définir le titre et la sous-titre de la page
st.title("Estimez le temps de votre prochain trail !")

# Ajouter une image de trail
from PIL import Image
image = Image.open("images/trail.jpeg")
st.image(image, use_column_width=True)


st.sidebar.title("Options de séance")

# Créer les champs de saisie pour les informations de la séance de trail
distance = st.sidebar.slider("Distance (en mètres)", min_value=0, max_value=45000, value=10000, step=100)
elevation_gain = st.sidebar.slider("Dénivelé (en mètres)", min_value=0, max_value=1000, value=200, step=10)
average_heart_rate = st.sidebar.slider("Fréquence cardiaque moyenne", min_value=100, max_value=200, value=150, step=1)

gender = st.sidebar.selectbox("Genre", options=["M", "F"])


default_datetime = datetime.datetime(2023, 4, 1, 10, 0)
selected_datetime = st.sidebar.date_input("Date de la séance", value=default_datetime.date(), min_value=None, max_value=None)
selected_time = st.sidebar.time_input("Heure de la séance", value=default_datetime.time())

# Créer un bouton pour envoyer les informations à l'API
if st.button("Prédire la durée de mon prochain trail"):
    # Créer le dictionnaire avec les informations saisies
    test_dict = {
        'distance': distance,
        'elevation_gain': elevation_gain,
        'average_heart_rate': average_heart_rate,
        'timestamp': timestamp,
        'gender': gender
    }


# Affichage des résultats de l'API
results_dict = {'race_category_1_pred_time': 3800.0, 'race_category_2_pred_time': 3570.0, 'race_category_3_pred_time': 3200.0}



new_results_dict = {}
for key, value in results_dict.items():
    if 'time' in key:
        time_delta = datetime.timedelta(seconds=value)
        time_string = f"{time_delta.seconds // 3600}h {(time_delta.seconds % 3600) // 60}min {time_delta.seconds % 60}s"
        new_results_dict[key] = str(time_string)
    else:
        new_results_dict[key] = value






st.write("Résultats de la prédiction :")

for category, time in new_results_dict.items():
    st.write(f"- {category} : {time}")
