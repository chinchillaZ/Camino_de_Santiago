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





markdown = """
        <br><br><br>
        相關連結<br>
        [► Camino七大路線介紹⛰️: 這些路線充滿歷史與挑戰，帶你走過美麗的景點與文化的精髓](https://camino.streamlit.app/%E8%B7%AF%E7%B7%9A%E4%BB%8B%E7%B4%B9)  
        [► Camino沿路旅遊景點推薦🏰: 從壯麗的古堡到浪漫的海岸線，發現不容錯過的必遊景點！](https://camino.streamlit.app/%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6)  
        [► Camino全球人次統計👪: 全球朝聖者的足跡！快來看看哪個國家的旅客最多](https://camino.streamlit.app/%E5%85%A8%E7%90%83%E4%BA%BA%E6%AC%A1%E7%B5%B1%E8%A8%88)  
        [► Camino美食指南手冊🍽️: 品味Camino沿途的美味，從地道的小吃到高端餐廳一網打盡！](https://camino.streamlit.app/%E7%BE%8E%E9%A3%9F%E6%8C%87%E5%8D%97%E6%89%8B%E5%86%8A)      
    """
st.markdown(markdown, unsafe_allow_html=True)


