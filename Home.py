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
paired_colors = plt.cm.Paired.colors

# Assign colors to each route
route_colors = {
    "法國之路": paired_colors[0],  # Camino_Frances
    "北方之路": paired_colors[1],  # Camino_Ingles
    "葡萄牙之路": paired_colors[2],  # Camino_Portugues_central
    "銀之路": paired_colors[3],  # Camino_Primitivo
    "原始之路": paired_colors[4],  # Camino_del_Norte
    "英格蘭之路": paired_colors[5],  # Portugues_Coastal
    "聖雅各海岸之路": paired_colors[6],  # Via_de_la_Plata
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

# Create a map centered on Spain
m = folium.Map(location=[42.5, -3.7], zoom_start=6)

# Loop through the GeoJSON URLs and add them to the map with the assigned colors
for geojson_url, (route_name, route_color) in zip(geojson_urls, route_colors.items()):
    # Add the GeoJSON layer to the map with the specified color
    folium.GeoJson(
        geojson_url,
        name=route_name,
        style_function=lambda x, color=route_color: {
            "color": color,
            "weight": 3,
            "opacity": 0.8
        }
    ).add_to(m)

# Add layer control to toggle layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save("camino_map.html")


m.to_streamlit(height=500)
