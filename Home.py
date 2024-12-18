import streamlit as st
import leafmap.foliumap as leafmap
import matplotlib.pyplot as plt
import folium

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
style = {"color": "yellow", "weight": 1.5, "opacity": 0.9}
m.add_geojson(country_url, layer_name="Country", style=style)

# Add GeoJSON line to the map
# geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
# style = {"color": "navy", "weight": 3, "opacity": 0.8}
# m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)

# Get the colors from the 'Paired' colormap
# Get the colors from the 'Paired' colormap
route_colors_hsv = {
    "法國之路": (0.702, 1.0, 0.271),  # Camino_Frances (HSV)
    "北方之路": (0.750, 1.0, 0.533),  # Camino_Ingles (HSV)
    "葡萄牙之路": (0.667, 1.0, 0.537),  # Camino_Portugues_central (HSV)
    "銀之路": (0.607, 1.0, 0.553),  # Camino_Primitivo (HSV)
    "原始之路": (0.528, 1.0, 0.553),  # Camino_del_Norte (HSV)
    "英格蘭之路": (0.425, 1.0, 0.553),  # Portugues_Coastal (HSV)
    "聖雅各海岸之路": (0.143, 1.0, 0.941)  # Via_de_la_Plata (HSV)
}


# List of GeoJSON URLs
geojson_urls = [
    "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Frances.geojson",
    "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Ingles.geojson",
    "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Portugues_central.geojson",
    "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_Primitivo.geojson",
    "https://chinchillaz.github.io/streamlit-hw/Camino/Camino_del_Norte.geojson",
    "https://chinchillaz.github.io/streamlit-hw/Camino/Portugues_Coastal.geojson",
    "https://chinchillaz.github.io/streamlit-hw/Camino/Via_de_la_Plata.geojson"
]


geojson_url = geojson_urls[0]
style = {"color": "navy", "weight": 3, "opacity": 0.8}
m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)


m.to_streamlit(height=500)
