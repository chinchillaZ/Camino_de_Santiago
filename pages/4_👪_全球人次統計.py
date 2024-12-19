import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
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

st.title("全球人次統計 👪")


# Create two rows using columns
upper_row = st.columns(3)  # Upper row with 3 buttons
lower_row = st.columns(4)  # Lower row with 4 buttons

# Upper row buttons
if upper_row[0].button("法國之路", use_container_width=True):
    upper_row[0].markdown("You clicked 法國之路")
if upper_row[1].button("葡萄牙之路", use_container_width=True):
    upper_row[1].markdown("You clicked 葡萄牙之路")
if upper_row[2].button("北方之路", use_container_width=True):
    upper_row[2].markdown("You clicked 北方之路")

# Lower row buttons
if lower_row[0].button("原始之路", use_container_width=True):
    lower_row[0].markdown("You clicked 原始之路")
if lower_row[1].button("銀之路", use_container_width=True):
    lower_row[1].markdown("You clicked 銀之路")
if lower_row[2].button("英國之路", use_container_width=True):
    lower_row[2].markdown("You clicked 英國之路")
if lower_row[3].button("世界盡頭之路", use_container_width=True):
    lower_row[3].markdown("You clicked 世界盡頭之路")


chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

m.to_streamlit(height=700)
