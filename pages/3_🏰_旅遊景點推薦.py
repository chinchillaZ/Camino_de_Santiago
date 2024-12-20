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


st.title("旅遊景點推薦 🏰")

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



st.markdown("<br><br>", unsafe_allow_html=True)  # Adds three line breaks
st.markdown("#### 🎇推薦景點清點🎇")
markdown = """
    精心蒐集各大平台上的熱門景點，讓您不再為選擇目的地煩惱。從歷史名勝到自然奇觀，為您推薦最值得一遊的地方。<br>
    歡迎勾選有興趣的目的地，按「確認」按鈕後，會在下方顯示清單~
"""
st.markdown(markdown, unsafe_allow_html=True)


df = pd.read_csv(data)
df['I wanna go!!!!!!!'] = False
# st.dataframe(df)

edited_df = st.data_editor(
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



 #Display the "我有興趣的景點" section title
st.markdown("#### 🎇我有興趣的景點🎇")

# Add a "確認" button just below the table
if st.button('確認'):
    # Extract the selected rows where 'I wanna go!!!!!!!' is True
    selected_attractions = edited_df[edited_df['I wanna go!!!!!!!'] == True]
    
    # Check if there are any selected attractions
    if not selected_attractions.empty:
        # Create a formatted list with both the 'id' and 'Attractions' columns
        attractions_text = "<br>".join([f'<span style="color:orange;"> {row["id"]} - {row["Attractions"]}</span>' 
                                       for index, row in selected_attractions.iterrows()])
        # Display the selected attractions in orange, each on a new line
        st.markdown(f'<br>{attractions_text}', unsafe_allow_html=True)
    else:
        st.markdown('<span style="color:orange;">還沒有選擇任何景點</span>', unsafe_allow_html=True)



