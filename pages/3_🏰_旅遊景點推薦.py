import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

st.title("景點推薦 🏰")

# Initialize the map with center coordinates and zoom level
m = leafmap.Map(center=[42.5, -4.0], zoom=7, minimap_control=True)


cities_url = "https://chinchillaz.github.io/streamlit-hw/country_interest.geojson"
m.add_geojson(cities_url, layer_name="Intersect towns")

geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
style = {"color": "black", "weight": 3, "opacity": 0.8}
m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)

data = "https://chinchillaz.github.io/streamlit-hw/Camino/Caminos_attraction3.csv"
m.add_points_from_xy(data, x="Y", y="X")

# Display the map
m.to_streamlit(height=700)




st.markdown("#### 🎇推薦景點清點🎇")
df = pd.read_csv(data)
df['I wanna go!!!!!!!'] = False
# st.dataframe(df)

st.data_editor(
    df,
    column_config={
        "I wanna go!!!!!!!": st.column_config.CheckboxColumn(
            "I wanna go!!!!!!!",
            help="Select if you want to visit this place",
            default=False,
        )
    },
    disabled=[],  # You can disable other columns if needed
    hide_index=True,  # Hide the index if you want
)

# Add custom HTML to change the checkbox color (if HTML support is allowed in this context)
st.markdown(
    """
    <style>
        .streamlit-checkbox input[type=checkbox]:checked {
            background-color: red !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)




# with st.expander("See source code"):
#     with st.echo():

#         # m = leafmap.Map(center=[40, -100], zoom=4)
#         # cities = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
#         # regions = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson"

#         # m.add_geojson(regions, layer_name="US Regions")
#         # m.add_points_from_xy(
#         #     cities,
#         #     x="longitude",
#         #     y="latitude",
#         #     color_column="region",
#         #     icon_names=["gear", "map", "leaf", "globe"],
#         #     spin=True,
#         #     add_legend=True,
#        # Initialize the map with center coordinates and zoom level
#         m = leafmap.Map(center=[42.5, -4.0], zoom=7, minimap_control=True)
        
#         # URL for the cities GeoJSON
#         cities_url = "https://chinchillaz.github.io/streamlit-hw/country_interest.geojson"
#         # URL for the Camino de Santiago GeoJSON
#         geojson_url = "https://chinchillaz.github.io/streamlit-hw/all_Camino_route.geojson"
        
#         # Style for the Camino de Santiago routes
#         style = {"color": "navy", "weight": 3, "opacity": 0.8}
        
#         # Add the cities layer (Intersect towns)
#         m.add_geojson(cities_url, layer_name="Intersect towns")
        
#         # Add the Camino de Santiago routes layer with style
#         m.add_geojson(geojson_url, layer_name="Camino de Santiago Route", style=style)
        
#         # Display the map
#         m.to_streamlit(height=700)


