import streamlit as st
import leafmap.foliumap as leafmap
#import leafmap
import matplotlib.pyplot as plt
import folium
from branca.element import Template, MacroElement

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
st.title("Camino de Santiago")

st.markdown(
    """
    朝聖者之路（Camino de Santiago）是歐洲著名的朝聖路線，終點位於西班牙北部加利西亞的聖地亞哥-德孔波斯特拉大教堂（Santiago de Compostela），據說是聖雅各的長眠之地。這條路線自中世紀起便吸引無數朝聖者徒步前往，途中穿越山脈、河谷與村莊，既是一場身心挑戰，也是文化與自然的體驗。今天，無論是出於宗教、文化探索或運動目的，每年都有數十萬人踏上這段富有意義的旅程，感受道路上的和平與反思。
    """
)


# st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
#m.add_basemap("OpenTopoMap")
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
labels = [
    "Camino Frances",
    "Camino Ingles",
    "Camino Portugues Central",
    "Camino Primitivo",
    "Camino del Norte",
    "Portugues Coastal",
    "Via de la Plata",
    "Default",
]
colors = ["red", "blue", "orange", "green", "purple", "yellow", "brown", "black"]

# Add the legend to the map
Map.add_legend(title="Camino de Santiago Routes", labels=labels, colors=colors)



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
