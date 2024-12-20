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

markdown = """
    這份資料整理至Camino官方網站，詳細記錄每年全球各地朝聖者人數。這些數據反映了不同國家的人們對朝聖者之路的熱情，從西班牙到美國，從亞洲到南美洲，每一筆數據不僅代表著一位位旅客的足跡，更是對信仰、歷史與文化的一次深刻體驗。

    以下統理2024年各國人數數據，繪製成3D柱狀圖:
"""

st.markdown(markdown, unsafe_allow_html=True)
# def show_map():
#     # Load the GeoJSON data
#     data = "https://chinchillaz.github.io/streamlit-hw/Camino/1_Frances_travelers.geojson"
#     chart_data = gpd.read_file(data)

#     # Filter data for the year 2024
#     chart_data = chart_data[chart_data["year"] == 2024]
    
#     # Extract the X (longitude) and Y (latitude) coordinates
#     chart_data['X'] = chart_data['geometry'].apply(lambda x: x.coords[0][0])  # Longitude
#     chart_data['Y'] = chart_data['geometry'].apply(lambda x: x.coords[0][1])  # Latitude

#     # Render the map using Pydeck
#     deck = pdk.Deck(
#         map_style=None,
#         initial_view_state=pdk.ViewState(
#             latitude=20,  # Centering the map on the general location
#             longitude=0,  # Adjust based on your map area
#             zoom=1,       # Adjust zoom to fit the global map
#             pitch=50,     # Angle for 3D effect
#         ),
#         layers=[
#             pdk.Layer(
#                 "HexagonLayer",
#                 data=chart_data,
#                 get_position=["X", "Y"],  # Corrected syntax for accessing the columns
#                 radius=1000,  # Size of the hexagons, adjust based on data density
#                 elevation_scale=4,
#                 elevation_range=[0, 1000],
#                 get_elevation="Number",  # Use the 'Number' column for height (this adds 3D bars)
#                 get_fill_color="[0, 0, 255, 255]",  # Color for the hexagons (blue)
#                 pickable=True,
#                 extruded=True,  # This makes the bars 3D
#             ),
#         ],
#     )

#     # Display the map in Streamlit using `st.pydeck_chart`
#     st.pydeck_chart(deck)
def show_map():
    # Generate some random chart data (latitude and longitude)
    chart_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"],
    )

    # Create a pydeck map with two layers: HexagonLayer and ScatterplotLayer
    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=37.76,
                longitude=-122.4,
                zoom=11,
                pitch=70,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=chart_data,
                    get_position="[lon, lat]",
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
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












st.markdown("<br><br><br>", unsafe_allow_html=True)  # Adds three line breaks


st.markdown("#### 全部路線 遊客遊客數量統計 🔍")
json_data = {
    "pie_chart": {
        "labels": [
            "Spain", "USA", "Italy", "Germany", "Portugal", "United Kingdom",
            "France", "Ireland", "Mexico", "Korea", "Canada", "Australia", "Poland",
            "Brazil", "Holland", "Republic Czech", "Argentina", "Colombia", "Denmark", "Taiwan",
            "Belgium", "China", "Austria", "Swiss", "Hungary", "South Africa", "Slovakia",
            "Romania", "Nea Zeeland", "Japan", "Ukraine", "Venezuela", "Sweden", "Russia",
            "Philippines", "Bulgaria", "Puerto Rico", "Chili", "Uruguay", "Norway", "Slovenia",
            "Singapore", "Ecuador", "Lithuania", "Finland", "Costa Rica", "Peru", "Latvia",
            "Hong Kong", "Malaysia", "Iran", "Indonesia", "Malta", "Estonia", "Guatemala",
            "Greece", "Israel", "Rep.Dominican", "Andorra", "El Salvador", "Belarus", "India",
            "Paraguay", "Luxembourg", "Bolivia", "Cuba", "Serbia", "Iceland", "Turkey",
            "Panama", "Iraq", "Nicaragua"
        ],
        "sizes": [
            43.71, 7.99, 6, 4.93, 4.59, 2.75,
            2.15, 2.15, 1.99, 1.65, 1.63, 1.61, 1.57,
            1.49, 1.33, 1.67, 1.01, 0.95, 0.8, 0.78,
            0.73, 0.53, 0.52, 0.4, 0.38, 0.35, 0.34,
            0.33, 0.31, 0.31, 0.3, 0.3, 0.29, 0.29,
            0.27, 0.23, 0.23, 0.21, 0.2, 0.18, 0.17,
            0.17, 0.17, 0.17, 0.16, 0.15, 0.14, 0.12,
            0.12, 0.11, 0.09, 0.09, 0.08, 0.07, 0.07,
            0.06, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05,
            0.04, 0.04, 0.03, 0.03, 0.03, 0.03, 0.03,
            0.03, 0.02, 0.02
        ]
    }
}

# Extract data for the pie chart
labels = json_data["pie_chart"]["labels"]
sizes = json_data["pie_chart"]["sizes"]

# Streamlit app

# Pie chart using Plotly
fig = px.pie(
    values=sizes,
    names=labels,
    #color_discrete_sequence=px.colors.qualitative.Paired,  # Use the 'Paired' color sequence
    #title="Traveler Distribution by Country",
)


st.plotly_chart(fig)


