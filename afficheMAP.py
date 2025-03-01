# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kY8qV6cLmX6nXFys-DYCpjQb7NjFsxSV
"""

import gradio as gr
import folium
from geopy.geocoders import Nominatim

def get_coordinates(address):
    geolocator = Nominatim(user_agent="geo_converter")
    location = geolocator.geocode(address)

    if location:
        return location.latitude, location.longitude
    else:
        return None

def create_map(address):
    coordinates = get_coordinates(address)

    if coordinates:
        latitude, longitude = coordinates
        my_map = folium.Map(location=[latitude, longitude], zoom_start=15)
        folium.Marker([latitude, longitude], popup=address, tooltip="Cliquez pour voir").add_to(my_map)

        # Sauvegarde et affichage de la carte
        #map_filename = "map.html"
        #my_map.save(map_filename) # We save to a variable instead
        #print(f"Carte enregistrée sous '{map_filename}'. Ouvrez ce fichier pour voir la carte.")
        return my_map._repr_html_() # This will return the HTML representation of the map
    else:
        print("Adresse non trouvée.")
        return "" # Return empty string if address is not found

# Exemple d'utilisation
address = "66 rue camille desmoulins 94230 cachan"
map_html = create_map(address) # Change variable name to map_html

with gr.Blocks() as demo:
    gr.HTML(value=map_html) # Use map_html

demo.launch()

