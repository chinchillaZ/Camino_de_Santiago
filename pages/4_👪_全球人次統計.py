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
    這份資料整理至Camino官方網站，詳細記錄每年全球各地朝聖者人數。這些數據反映了不同國家的人們對朝聖者之路的熱情，從西班牙到美國，從亞洲到南美洲，每一筆數據不僅代表著一位位旅客的足跡，更是對信仰、歷史與文化的一次深刻體驗。<br><br>
    以下統理2024年各國走朝聖者之路的人數，繪製成3D柱狀圖，歡迎點選「路線按鈕」觀看~!!
"""

st.markdown(markdown, unsafe_allow_html=True)

color_map = {
        "Camino_Frances": [255, 0, 0],           # Vibrant red
        "Camino_Ingles": [0, 0, 255],           # Strong blue
        "Camino_Portugues_central": [255, 165, 0],  # Bright orange
        "Camino_Primitivo": [0, 255, 0],        # Fresh green
        "Camino_del_Norte": [128, 0, 128],      # Deep purple
        "Portugues_Coastal": [255, 255, 0],     # Sunny yellow
        "Via_de_la_Plata": [139, 69, 19],       # Earthy brown
        "default": [0, 0, 0],                   # Default color if route not found
    }

data_urls_dict = {
    "Camino_Frances": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/1_Frances_travelers.csv",
    "Camino_Ingles": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/6_Ingles_travelers.csv",
    "Camino_Portugues_central": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/2_Portugues_travelers.csv",
    "Camino_Primitivo": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/4_Primitivo_travelers.csv",
    "Camino_del_Norte": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/3_Norte_travelers.csv",
    "Portugues_Coastal": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/7_Muxia_travelers.csv",
    "Via_de_la_Plata": "https://raw.githubusercontent.com/chinchillaZ/streamlit-hw/main/Camino/5_Plata_travelers.csv",
    "default": ""  # Default key if route is not found
}


# def show_map(csv_url, color):

#     # Read the CSV file
#     chart_data = pd.read_csv(csv_url)
#     chart_data = chart_data[chart_data["year"] == 2024]

#    # Load the GeoJSON data from the URL
#     geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
#     geojson_data = requests.get(geojson_url).json()

#     # Filter the GeoJSON features based on the route_name
#     filtered_geojson = {
#         "type": "FeatureCollection",
#         "features": [
#             feature for feature in geojson_data["features"]
#             if feature["properties"].get("route") == route_name
#         ]
#     }



#     st.pydeck_chart(
#         pdk.Deck(
#             map_style="mapbox://styles/mapbox/light-v10",
#             initial_view_state=pdk.ViewState(
#                 latitude=40.0,  # Center near Spain for better view
#                 longitude=0.0,
#                 zoom=1,
#                 pitch=45,
#             ),
#             layers=[
#                 pdk.Layer(
#                     "ColumnLayer",
#                     data=chart_data,
#                     get_position="[Y, X]",  # Note: Longitude is X, Latitude is Y
#                     get_elevation="Number / 10",  # Set the elevation (height of the column) proportional to 'Number'
#                     elevation_scale=800,  # Scale factor for elevation 誇張程度
#                     get_fill_color=f"[{color[0]}, {color[1]}, {color[2]}, 210]",  # Color of the columns RGBA
#                     radius=80000,  # Radius of the columns
#                     pickable=True,
#                 ),
#                 pdk.Layer(
#                     "GeoJsonLayer",  # Add GeoJSON layer
#                     filtered_geojson,  # Use the filtered GeoJSON
#                     get_fill_color=[255, 0, 0, 255],  # Color for the route line (red)
#                     get_line_color=[255, 0, 0],  # Line color for the route (red)
#                     line_width=4,  # Line width for the route
#                     pickable=True,
#                 )
#             ],
#         )
#     )
#     # Show the table of chart_data
#     st.table(chart_data)  # Display the chart data as a table

# Function to show the map
def show_map(csv_url, color, route_name):
    # Read the CSV file
    chart_data = pd.read_csv(csv_url)
    chart_data = chart_data[chart_data["year"] == 2024]
    
    # Load the GeoJSON data from the URL
    geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
    geojson_data = requests.get(geojson_url).json()

    # Filter the GeoJSON features based on the route_name
    filtered_geojson = {
        "type": "FeatureCollection",
        "features": [
            feature for feature in geojson_data["features"]
            if feature["properties"].get("route") == route_name
        ]
    }

    # Create the map using pydeck
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v10",  # Map style
            initial_view_state=pdk.ViewState(
                latitude=40.0,  # Center near Spain for better view
                longitude=0.0,
                zoom=1,
                pitch=45,
            ),
            layers=[
                pdk.Layer(
                    "ColumnLayer",
                    data=chart_data,
                    get_position="[Y, X]",  # Longitude is X, Latitude is Y
                    get_elevation="Number / 10",  # Set the elevation proportional to 'Number'
                    elevation_scale=800,  # Scale factor for elevation
                    get_fill_color=f"[{color[0]}, {color[1]}, {color[2]}, 210]",  # Color of the columns RGBA
                    radius=80000,  # Radius of the columns
                    pickable=True,  # Allow clicking on columns
                ),
                pdk.Layer(
                    "GeoJsonLayer",  # Add GeoJSON layer
                    filtered_geojson,  # Use the filtered GeoJSON
                    get_fill_color=[255, 0, 0, 255],  # Color for the route line (red)
                    get_line_color=[255, 0, 0],  # Line color for the route (red)
                    line_width=4,  # Line width for the route
                    pickable=True,
                )
            ],
        )
    )
    st.table(chart_data)  # Display the chart data as a table




# Create two rows using columns
upper_row = st.columns(3)  # Upper row with 3 buttons
lower_row = st.columns(4)  # Lower row with 4 buttons

# Upper row buttons
# Upper row buttons
if upper_row[0].button("法國之路", use_container_width=True):
    route_name = "Camino_Frances"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)
    
if upper_row[1].button("葡萄牙之路", use_container_width=True):
    route_name = "Camino_Portugues_central"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)

if upper_row[2].button("北方之路", use_container_width=True):
    route_name = "Camino_del_Norte"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)

# Lower row buttons
if lower_row[0].button("原始之路", use_container_width=True):
    route_name = "Camino_Primitivo"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)
    
if lower_row[1].button("銀之路", use_container_width=True):
    route_name = "Via_de_la_Plata"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)
    
if lower_row[2].button("英國之路", use_container_width=True):
    route_name = "Camino_Ingles"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)
    
if lower_row[3].button("世界盡頭之路", use_container_width=True):
    route_name = "Portugues_Coastal"
    data_url = data_urls_dict.get(route_name, data_urls_dict["default"])
    color = color_map.get(route_name, color_map["default"])
    show_map(data_url, color)




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


markdown = """
        <br><br><br>
        相關連結<br>
        [► Camino七大路線介紹⛰️: 這些路線充滿歷史與挑戰，帶你走過美麗的景點與文化的精髓](https://camino.streamlit.app/%E8%B7%AF%E7%B7%9A%E4%BB%8B%E7%B4%B9)  
        [► Camino沿路旅遊景點推薦🏰: 從壯麗的古堡到浪漫的海岸線，發現不容錯過的必遊景點！](https://camino.streamlit.app/%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6)  
        [► Camino全球人次統計👪: 全球朝聖者的足跡！快來看看哪個國家的旅客最多](https://camino.streamlit.app/%E5%85%A8%E7%90%83%E4%BA%BA%E6%AC%A1%E7%B5%B1%E8%A8%88)  
        [► Camino美食指南手冊🍽️: 品味Camino沿途的美味，從地道的小吃到高級餐廳一網打盡！](https://camino.streamlit.app/%E7%BE%8E%E9%A3%9F%E6%8C%87%E5%8D%97%E6%89%8B%E5%86%8A)      
    """
st.markdown(markdown, unsafe_allow_html=True)


