import pandas as pd
import paths
import tqdm
import numpy as np
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import contextily as ctx
import folium
import gradio as gr

# data load
def load_df(filepath=paths.location_path):
    try:
        # On essaie d'accéder à la variable 'location_path' dans le module 'paths'
        file_path = filepath

        # Lecture du fichier CSV
        df_location = pd.read_csv(file_path)

    except AttributeError:
        print("Le chemin du fichier est introuvable.")
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
    return df_location

def get_coordinates(address):
    geolocator = Nominatim(user_agent="my_geocoder", timeout=10)  # Timeout de 10 secondes
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Erreur pour l'adresse '{address}': {e}")
        return None, None

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en km
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat/2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

# get best addresses
def get_best_address(ref_address, df):
    ref_lat, ref_lon = get_coordinates(ref_address)

    # Calcul des distances
    df['distance'] = df.apply(lambda row: haversine(ref_lat, ref_lon, row['latitude'], row['longitude']), axis=1)

    # Sélection des 5 adresses les plus proches
    top5_plus_proches = df.nsmallest(10, 'distance')  # <-- Modification ici

    # Affichage des résultats
    return top5_plus_proches


def convertir_en_entier(s):
    # Remplacer les virgules par des points
    s = s.replace(',', '.')

    # Convertir en flottant
    nombre_flottant = float(s)

    # Convertir en entier (arrondi vers le bas)
    nombre_entier = int(nombre_flottant)

    return nombre_entier

def add_markers_from_dataframe(df, address):
    lat, lon = get_coordinates(address)

    # Nouvelle position centrale de la carte
    map_center = [lat, lon]  # Paris, par exemple
    map = folium.Map(location=map_center, zoom_start=12)

    # Ajouter le calque OpenStreetMap avec attribution correcte
    folium.TileLayer(
    'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    ).add_to(map)

    latitude_ref, longitude_ref = get_coordinates(address)

    folium.Marker(
        [latitude_ref, longitude_ref],
                icon=folium.Icon(color='red')
                ).add_to(map)

    for idx, row in df.iterrows():
        latitude = row['latitude']
        longitude = row['longitude']
        name = row['name']
        phone_number = row['phone_number']
        rating = convertir_en_entier(row['rating'])*'* '
        distance = round(row['distance'], 2)

        popup_text = (f"name : {name}\nphone : {phone_number}\nrating : {rating}\ndistance"
                      f" : {distance}")  # Ajouter un texte descriptif pour chaque point

        # Ajouter un marqueur avec les coordonnées du dataframe
        folium.Marker(
        [latitude, longitude],
        popup=popup_text,
        icon=folium.Icon(color='blue')
        ).add_to(map)

    # Retourner la carte pour l'affichage
    return map

# Chargement des données
df = load_df('preprocessed_data/clean_data_salles.csv')

def get_html(address):
    new_df = get_best_address(address, df)
    print(f"result \n : {new_df}")
    map = add_markers_from_dataframe(new_df, address)
    return map._repr_html_()


# CSS personnalisé pour l'image de fond
custom_css = """
div {
    background-image: url('https://static.vecteezy.com/system/resources/previews/006/965/779/non_2x/empty-top-wooden-table-and-sakura-flower-with-fog-and-morning-light-background-photo.jpg');
    background-size: cover;
    background-position: center;
}
"""


with gr.Blocks() as demo:
    gr.Markdown("## Carte des salles les plus proches")
    text_area = gr.Textbox(placeholder="Entrez une adresse")
    search_btn = gr.Button("Afficher la carte")
    carte_area = gr.HTML()

    search_btn.click(
        fn=get_html,
        inputs=text_area,
        outputs=carte_area
    )

demo.launch()