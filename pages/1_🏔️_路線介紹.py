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

    # m = leafmap.Map(
    #     locate_control=True, latlon_control=True, draw_export=True, minimap_control=True, center = [42.5, -4.0], zoom = 8 
    # )
    # m.add_basemap(basemap)

    # geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
    # # Define a style function to set line color to navy
    # style = {"color": "navy", "weight": 3, "opacity": 0.8}
    # m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)
    
    # m.to_streamlit(height=700)
    # Define route colors based on the dictionary
   

    # Define route colors based on the dictionary
    route_colors = {
        "法國之路": "#440154",  # Camino_Frances
        "北方之路": "#482878",  # Camino_Ingles
        "葡萄牙之路": "#3e4a89",  # Camino_Portugues_central
        "銀之路": "#31688e",  # Camino_Primitivo
        "原始之路": "#21908d",  # Camino_del_Norte
        "英格蘭之路": "#5dc963",  # Portugues_Coastal
        "聖雅各海岸之路": "#f0f921",  # Via_de_la_Plata
    }
    
    # Initialize the map
    m = leafmap.Map(center=[42.5, -4.0], zoom=7, minimap_control=True)
    
    # GeoJSON URL for the Camino de Santiago route
    geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
    
    # Define a style function that uses route_colors based on feature properties
    def style_function(feature):
        # Get the route name from the feature properties
        route_name = feature['properties'].get('route', '')
    
        # Get the color for the route, default to navy if not found
        color = route_colors.get(route_name, 'navy')
        return {
            "color": color,
            "weight": 3,
            "opacity": 0.8
        }
    
    # Add the GeoJSON with dynamic colors based on route name
    m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style_function=style_function)
    
    # Display the map in Streamlit
    m.to_streamlit(height=700)



    st.header("intro")
    
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


    
    # 路線資料
    data = {
        "name": [
            "法國之路 (Camino Francés)",
            "葡萄牙之路 (Camino Portugués)",
            "北方之路 (Camino del Norte)",
            "原始之路 (Camino Primitivo)",
            "銀之路 (Via de la Plata)",
            "英國之路 (Camino Inglés)",
            "世界盡頭之路 (Camino Finisterre-Muxía)"
        ],
        "Distance": [771, 620, 481, 16, 49, 114, 86],
        "Days": [36, 29, 23, 16, 49, 7, 6]
    }
    
    route_colors = {
        "法國之路 (Camino Francés)": "#440154",
        "葡萄牙之路 (Camino Portugués)": "#3e4a89",
        "北方之路 (Camino del Norte)": "#482878",
        "原始之路 (Camino Primitivo)": "#21908d",
        "銀之路 (Via de la Plata)": "#31688e",
        "英國之路 (Camino Inglés)": "#5dc963",
        "世界盡頭之路 (Camino Finisterre-Muxía)": "#f0f921",
    }
    
    df = pd.DataFrame(data)
    
    # 繪圖
    fig = go.Figure()
    
    for index, row in df.iterrows():
        fig.add_trace(go.Bar(
            name=row["name"],
            x=["Distance", "Days"],
            y=[row["Distance"], row["Days"]],
            marker_color=route_colors[row["name"]]
        ))
    
    fig.update_layout(
        barmode="group",
        title="Camino de Santiago Routes",
        xaxis_title="Metrics",
        yaxis_title="Values",
        legend_title="Routes"
    )
    
    fig.show()







    #     # Data for the routes
    # routes = ["法國之路", "北方之路", "葡萄牙之路", "銀之路", "原始之路", "英格蘭之路", "聖雅各海岸之路"]
    # distances_km = [780, 825, 620, 1000, 321, 120, 825]
    
    # # Create an interactive bar chart using Plotly
    # # fig = go.Figure(go.Bar(
    # #     x=distances_km,
    # #     y=routes,
    # #     orientation='h',  # Horizontal bar chart
    # #     marker=dict(color='skyblue'),
    # # ))
    
    # # fig.update_layout(
    # #     title='朝聖者之路 路線長度分布',
    # #     xaxis_title='距離 (公里)',
    # #     yaxis_title='路線名稱',
    # #     template='plotly_white'
    # # )
    # # Colors for each route
    # route_colors = {
    #     "法國之路": "#440154",  # Camino_Frances
    #     "北方之路": "#482878",  # Camino_Ingles
    #     "葡萄牙之路": "#3e4a89",  # Camino_Portugues_central
    #     "銀之路": "#31688e",  # Camino_Primitivo
    #     "原始之路": "#21908d",  # Camino_del_Norte
    #     "英格蘭之路": "#5dc963",  # Portugues_Coastal
    #     "聖雅各海岸之路": "#f0f921",  # Via_de_la_Plata
    # }


    # # Create a list of colors for the bars based on the routes
    # bar_colors = [route_colors[route] for route in routes]
    
    # # Create an interactive bar chart using Plotly
    # fig = go.Figure(go.Bar(
    #     x=distances_km,
    #     y=routes,
    #     orientation='h',  # Horizontal bar chart
    #     marker=dict(color=bar_colors),
    # ))
    
    # fig.update_layout(
    #     title='朝聖者之路 路線長度分布',
    #     xaxis_title='距離 (公里)',
    #     yaxis_title='路線名稱',
    #     template='plotly_white'
    # )
        
    # # Display the interactive plot in Streamlit
    # st.plotly_chart(fig)


