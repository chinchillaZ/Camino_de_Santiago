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


 
| 名稱              | 距離 (公里) | 天數 | 挑戰難度  | 適合季節                                |
|-------------------|------------|------|-----------|---------------------------------------|
| 法國之路          | 771        | 36   | ⭐⭐        | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |
| 葡萄牙之路        | 620        | 29   | ⭐         | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |
| 北方之路          | 481        | 23   | ⭐         | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |
| 原始之路          | 16         | 16   | ⭐⭐⭐⭐     | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |
| 銀之路            | 49         | 49   | ⭐⭐⭐⭐     | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |
| 英國之路          | 114        | 7    | ⭐⭐        | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |
| 世界盡頭之路      | 86         | 6    | ⭐⭐        | 1月  2月  3月  4月  5月  6月<br/>7月  8月  9月  10月  11月  12月 |

        
    st.markdown(markdown)

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


