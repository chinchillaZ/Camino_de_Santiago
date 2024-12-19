import streamlit as st
import leafmap.foliumap as leafmap
# import leafmap
import plotly.graph_objects as go
import pandas as pd

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)


st.title("路線介紹")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:
    m = leafmap.Map(center = [42.5, -4.0], zoom = 7)
    m.add_basemap(basemap)

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
    m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style_callback=style_by_rout

    
    m.to_streamlit(height=500)  # Set height and width


 
    # markdown = """
        
    #     | Name                          | Distance (km) | Days | Challenge      |
    # |-------------------------------|---------------|------|----------------|
    # | 法國之路 (Camino Francés)       | 771           | 36   | Moderate       |
    # | 葡萄牙之路 (Camino Portugués)   | 620           | 29   | Easy           |
    # | 北方之路 (Camino del Norte)     | 481           | 23   | Easy           |
    # | 原始之路 (Camino Primitivo)     | 16            | 16   | Moderate Plus  |
    # | 銀之路 (Via de la Plata)        | 49            | 49   | Moderate Plus  |
    # | 英國之路 (Camino Inglés)        | 114           | 7    | Moderate       |
    # | 世界盡頭之路 (Camino Finisterre-Muxía) | 86            | 6    | Moderate       |
    
    #     """
        
    # st.markdown(markdown)
