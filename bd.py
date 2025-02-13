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
    top5_plus_proches = df.nsmallest(5, 'distance')  # <-- Modification ici

    # Affichage des résultats
    return top5_plus_proches


def afficher_carte_static(df, address, top_n=5):
    ref_lat, ref_lon = get_coordinates(address)
    # Filtrer les top N adresses
    top = df.nsmallest(top_n, 'distance')

    # Créer la figure
    fig, ax = plt.subplots(figsize=(10, 10))

    # Afficher les points
    ax.scatter(top['longitude'], top['latitude'], c='blue', s=100, label='Top 5')
    ax.scatter(ref_lon, ref_lat, c='red', s=200, marker='*', label='Référence')

    # Ajouter la carte en arrière-plan (OpenStreetMap)
    ctx.add_basemap(
        ax,
        crs="EPSG:4326",  # WGS84 (coordonnées GPS standard)
        source=ctx.providers.OpenStreetMap.Mapnik
    )

    # Personnalisations
    ax.set_title('Top 5 des salles les plus proches')
    ax.legend()
    plt.savefig('carte_top5.png')
    plt.show()



def afficher_carte_simple(df, address):
    ref_lat, ref_lon = get_coordinates(address)
    top = df.nsmallest(5, 'distance')

    plt.figure(figsize=(10, 8))
    plt.scatter(top['longitude'], top['latitude'], c='blue', s=50, label='Salles')
    plt.scatter(ref_lon, ref_lat, c='red', s=100, marker='*', label='Référence')

    # Ajouter les annotations
    for idx, row in top.iterrows():
        plt.annotate(f"{row['distance']:.2f} km", (row['longitude'], row['latitude']))

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid()
    plt.savefig('carte_simple.png')
    plt.show()


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
        popup_text = f"{row['name']}"  # Ajouter un texte descriptif pour chaque point

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
address = "15 rue Génin 93200 Saint-Denis France"

df = get_best_address(address, df)

print(df)

map_html = add_markers_from_dataframe(df, address)

with gr.Blocks() as demo:
    gr.HTML(map_html._repr_html_())

demo.launch()
