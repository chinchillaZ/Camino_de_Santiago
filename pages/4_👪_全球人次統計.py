import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np

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

# Function to generate and display the map
def show_map():
    # Prepare the chart data for the map
    data = "https://chinchillaz.github.io/streamlit-hw/Camino/1_Frances_travelers.csv"
    chart_data = pd.read_csv(data)
    chart_data = chart_data[chart_data["year"]==2024] # plot 2024 only

    # Render the map using Pydeck
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=20,  # Centering the map on the general location
                longitude=0,  # Adjust based on your map area
                zoom=2,       # Adjust zoom to fit the global map
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=chart_data,
                    get_position="[Y, X]",  # Using Y (longitude) and X (latitude) for positions
                    radius=200,  # Size of the hexagons, adjust based on data density
                    elevation_scale=10000,
                    elevation_range=[0, 5000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=chart_data,
                    get_position="[Y, X]",  # Using Y (longitude) and X (latitude) for positions
                    get_color="[200, 30, 0, 160]",  # Color for points
                    get_radius=200000,  # Size of scatterplot points
                ),
            ],
        )
    )


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





