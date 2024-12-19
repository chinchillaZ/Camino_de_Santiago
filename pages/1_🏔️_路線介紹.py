import streamlit as st
import leafmap.foliumap as leafmap
# import leafmap
import plotly.graph_objects as go
import pandas as pd
import pandas as pd
import numpy as np
import plotly.express as px

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)


st.title("路線介紹🎅")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:
    m = leafmap.Map(center = [42.5, -4.0], zoom = 6)
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
    m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style_callback=style_by_route)

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
    m.to_streamlit(height=500)  # Set height and width

   
#  藍色是適合的時間 #76d3ea
# 綠色是熱門的時間 #85cdb6
# 黃色是淡季  #f1aa3b
    
    markdown = """
        | 路線名稱             | 公里數  | 天數  | 挑戰難度  | 季節  (<span style="color:blue">適合月份</span> 、 <span style="color:green">熱門月份</span> 、<span style="color:orange"> 淡季</span>) |
        |-------------------|---------|-------|-----------|-------------------------------------------------------------------------------------------------------------|
        | 法國之路          | 771     | 36    | ⭐⭐        | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:orange">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:blue">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
        | 葡萄牙之路        | 620     | 29    | ⭐         | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
        | 北方之路          | 481     | 23    | ⭐         | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:green">7月</span>&nbsp;&nbsp;<span style="color:green">8月</span>&nbsp;&nbsp;<span style="color:blue">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
        | 原始之路          | 16      | 16    | ⭐⭐⭐⭐     | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:green">7月</span>&nbsp;&nbsp;<span style="color:green">8月</span>&nbsp;&nbsp;<span style="color:blue">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
        | 銀之路            | 49      | 49    | ⭐⭐⭐⭐     | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:orange">4月</span>&nbsp;&nbsp;<span style="color:orange">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
        | 英國之路          | 114     | 7     | ⭐⭐        | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:orange">4月</span>&nbsp;&nbsp;<span style="color:orange">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
        | 世界盡頭之路      | 86      | 6     | ⭐⭐        | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:orange">4月</span>&nbsp;&nbsp;<span style="color:orange">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    """



    
    st.markdown(markdown, unsafe_allow_html=True)


        
    # Create the DataFrame
    df = pd.DataFrame({
        "Name": ["法國之路", "葡萄牙之路", "北方之路", 
                 "原始之路", "銀之路", "英國之路", 
                 "世界盡頭之路"],
        "Distance (km)": [771, 620, 481, 16, 49, 114, 86],
        "Days": [36, 29, 23, 16, 49, 7, 6],
        "Challenge": ["Moderate", "Easy", "Easy", "Moderate Plus", "Moderate Plus", "Moderate", "Moderate"]
    })
    
    # Plot the bar chart
    fig = px.bar(
        data_frame=df,
        x="Name",
        y=["Distance (km)", "Days"],
        title="Distance and Days for Different Camino Routes",
        opacity=0.9,
        orientation="v",  # Vertical bars
        barmode='group',  # Grouped bar mode
    )
    
    fig.update_layout(
        xaxis_title="Camino Route",
        yaxis_title="Value",
        xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
    )
    
    # Show the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)


