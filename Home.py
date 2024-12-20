import streamlit as st
import leafmap.foliumap as leafmap
import matplotlib.pyplot as plt
import folium
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

# Customize page title
st.title("Welcome to Camino de Santiago App")
# Display clickable links

st.markdown(
    """
    朝聖者之路（Camino de Santiago）是歐洲著名的朝聖路線，終點位於西班牙北部加利西亞的聖地亞哥-德孔波斯特拉大教堂（Santiago de Compostela），據說是聖雅各的長眠之地。這條路線自中世紀起便吸引無數朝聖者徒步前往，途中穿越山脈、河谷與村莊，既是一場身心挑戰，也是文化與自然的體驗。今天，無論是出於宗教、文化探索或運動目的，每年都有數十萬人踏上這段富有意義的旅程，感受道路上的和平與反思。
    """
)




m = leafmap.Map(center = [42.5, -4.0], zoom = 7 , minimap_control=True)

country_url = "https://chinchillaz.github.io/streamlit-hw/S_P_F_country_clear.geojson"
style = {
    "color": "grey",  # Outline color
    "weight": 1.5,      # Line thickness
    "opacity": 0.5,     # Line transparency
    "fillColor": "none" # No fill color
}
m.add_geojson(country_url, layer_name="Country", style=style)

# # Add GeoJSON line to the map
# geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
# style = {"color": "navy", "weight": 3, "opacity": 0.8}
# m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)

def style_by_route(feature):
    route = feature["properties"].get("route", "default")  # Get the "route" value
    # Define a color map for different routes
    color_map = {
        "Camino_Frances": "red",          # Vibrant red
        "Camino_Ingles": "blue",         # Strong blue
        "Camino_Portugues_central": "orange",  # Bright orange
        "Camino_Primitivo": "green",     # Fresh green
        "Camino_del_Norte": "purple",    # Deep purple
        "Portugues_Coastal": "yellow",   # Sunny yellow
        "Via_de_la_Plata": "brown",      # Earthy brown
        "default": "black",              # Default color if route not found
    }

    return {
        "color": color_map.get(route, "black"),  # Use the route value to get the color
        "weight": 3,
        "opacity": 0.8,
    }

# Add the GeoJSON with dynamic styling
geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style_callback=style_by_route)

# Define the legend details
# Define the legend dictionary
legend_dict = {
    "法國之路 (Camino Francés)": "red",
    "英國之路 (Camino Inglés)": "blue",
    "葡萄牙之路 (Camino Portugués)": "orange",
    "原始之路 (Camino Primitivo)": "green",
    "北方之路 (Camino del Norte)": "purple",
    "世界盡頭之路 (Camino Finisterre-Muxía)": "yellow",
    "銀之路 (Via de la Plata)": "brown",
    #"Default": "black",
}

# Add the legend to the map
m.add_legend(title="Camino de Santiago Routes", legend_dict=legend_dict)

st.markdown(
    """
    [► Camino七大路線介紹⛰️: 這些路線充滿歷史與挑戰，帶你走過美麗的景點與文化的精髓](https://camino.streamlit.app/%E8%B7%AF%E7%B7%9A%E4%BB%8B%E7%B4%B9)  
    [► Camino沿路旅遊景點推薦🏰: 從壯麗的古堡到浪漫的海岸線，發現不容錯過的必遊景點！](https://camino.streamlit.app/%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6)  
    [► Camino全球人次統計👪: 全球朝聖者的足跡！快來看看哪個國家的旅客最多](https://camino.streamlit.app/%E5%85%A8%E7%90%83%E4%BA%BA%E6%AC%A1%E7%B5%B1%E8%A8%88)  
    [► Camino美食指南手冊🍽️: 品味Camino沿途的美味，從地道的小吃到高端餐廳一網打盡！](https://camino.streamlit.app/%E7%BE%8E%E9%A3%9F%E6%8C%87%E5%8D%97%E6%89%8B%E5%86%8A)  
    """
)


# Title for the page







# def random_color(feature):
#     return {
#         "color": random.choice(["blue", "purple", "brown", "pink"]),
#          "weight": 2,
#     }

# m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style_callback=random_color)

# Get the colors from the 'Paired' colormap
# Get the colors from the 'Paired' colormap
# route_colors = [
#     "#b3ff44",  # 法國之路
#     "#bf8600",  # 北方之路
#     "#aa8800",  # 葡萄牙之路
#     "#9a8c8c",  # 銀之路
#     "#876e8c",  # 原始之路
#     "#6c8c8c",  # 英格蘭之路
#     "#24f0f0"   # 聖雅各海岸之路
# ]


# List of GeoJSON URLs
# geojson_urls = [
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Frances.geojson",
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Ingles.geojson",
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Portugues_central.geojson",
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Primitivo.geojson",
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_del_Norte.geojson",
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Portugues_Coastal.geojson",
#     "https://chinchillaz.github.io/streamlit-hw/Camino/Via_de_la_Plata.geojson"
# ]



# # Loop through the route_colors and geojson_urls to add them dynamically
# for i in range(4):   #
#     style = {"color": route_colors[i], "weight": 3, "opacity": 0.8}
#     m.add_geojson(geojson_urls[i], layer_name=f"Camino de Santiago Route {i+1}", style=style)

m.to_streamlit(height=500)
