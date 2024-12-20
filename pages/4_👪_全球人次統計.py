import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.express as px
import requests

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

st.title("全球人次統計 👪")


def show_map():
    # Load the GeoJSON data
    data = "https://chinchillaz.github.io/streamlit-hw/Camino/1_Frances_travelers.geojson"
    chart_data = gpd.read_file(data)

    # Filter data for the year 2024
    chart_data = chart_data[chart_data["year"] == 2024]
    
    # Extract the X (longitude) and Y (latitude) coordinates
    chart_data['X'] = chart_data['geometry'].apply(lambda x: x.coords[0][0])  # Longitude
    chart_data['Y'] = chart_data['geometry'].apply(lambda x: x.coords[0][1])  # Latitude

    # Render the map using Pydeck
    deck = pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=20,  # Centering the map on the general location
            longitude=0,  # Adjust based on your map area
            zoom=1,       # Adjust zoom to fit the global map
            pitch=50,     # Angle for 3D effect
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position=["X", "Y"],  # Corrected syntax for accessing the columns
                radius=1000,  # Size of the hexagons, adjust based on data density
                elevation_scale=4,
                elevation_range=[0, 1000],
                get_elevation="Number",  # Use the 'Number' column for height (this adds 3D bars)
                get_fill_color="[0, 0, 255, 255]",  # Color for the hexagons (blue)
                pickable=True,
                extruded=True,  # This makes the bars 3D
            ),
        ],
    )

    # Display the map in Streamlit using `st.pydeck_chart`
    st.pydeck_chart(deck)

# Create two rows using columns
upper_row = st.columns(3)  # Upper row with 3 buttons
lower_row = st.columns(4)  # Lower row with 4 buttons

# Upper row buttons
if upper_row[0].button("法國之路", use_container_width=True):
    show_map()
    
if upper_row[1].button("葡萄牙之路", use_container_width=True):
    upper_row[1].markdown("You clicked 葡萄牙之路")
if upper_row[2].button("北方之路", use_container_width=True):
    upper_row[2].markdown("You clicked 北方之路")

# Lower row buttons
if lower_row[0].button("原始之路", use_container_width=True):
    lower_row[0].markdown("You clicked 原始之路")
if lower_row[1].button("銀之路", use_container_width=True):
    lower_row[1].markdown("You clicked 銀之路")
if lower_row[2].button("英國之路", use_container_width=True):
    lower_row[2].markdown("You clicked 英國之路")
if lower_row[3].button("世界盡頭之路", use_container_width=True):
    lower_row[3].markdown("You clicked 世界盡頭之路")




st.markdown("#### 全部路線 遊客遊客數量統計 🔍")
# URL for JSON data
json_url = "https://chinchillaz.github.io/streamlit-hw/Camino/all_travelers.json"
response = requests.get(json_url)
json_data = response.json()

labels = json_data["pie_chart"]["labels"]
sizes = json_data["pie_chart"]["sizes"]
# Pie chart using Plotly
fig = px.pie(values=sizes, names=labels, title="Pie Chart from JSON Data")
st.plotly_chart(fig)




