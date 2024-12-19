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
    st.header("intro")
    
    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
 
    markdown = """
        
        | Name                          | Distance (km) | Days | Challenge      |
    |-------------------------------|---------------|------|----------------|
    | 法國之路 (Camino Francés)       | 771           | 36   | Moderate       |
    | 葡萄牙之路 (Camino Portugués)   | 620           | 29   | Easy           |
    | 北方之路 (Camino del Norte)     | 481           | 23   | Easy           |
    | 原始之路 (Camino Primitivo)     | 16            | 16   | Moderate Plus  |
    | 銀之路 (Via de la Plata)        | 49            | 49   | Moderate Plus  |
    | 英國之路 (Camino Inglés)        | 114           | 7    | Moderate       |
    | 世界盡頭之路 (Camino Finisterre-Muxía) | 86            | 6    | Moderate       |
    
        """
        
    st.markdown(markdown)
