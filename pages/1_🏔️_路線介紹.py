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


st.title("各路線介紹")

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

    
    # markdown = """
    #     | 路線名稱            | 公里數  | 天數  | 挑戰難度  | 季節  (<span style="color:blue">適合月份</span> 、 <span style="color:green">熱門月份</span> 、<span style="color:orange"> 淡季</span>) |
    #     |-------------------|---------|-------|-----------|-------------------------------------------------------------------------------------------------------------|
    #     | 法國之路          | 771     | 36    | ⭐⭐        | &nbsp;<span style="color:orange">1月</span>&nbsp;&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;&nbsp;<span style="color:green">6月</span><br/> &nbsp;<span style="color:blue">7月</span>&nbsp;&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:blue">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    #     | 葡萄牙之路        | 620     | 29    | ⭐         | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    #     | 北方之路          | 481     | 23    | ⭐         | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:green">7月</span>&nbsp;&nbsp;<span style="color:green">8月</span>&nbsp;&nbsp;<span style="color:blue">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    #     | 原始之路          | 16      | 16    | ⭐⭐⭐⭐     | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:green">7月</span>&nbsp;&nbsp;<span style="color:green">8月</span>&nbsp;&nbsp;<span style="color:blue">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    #     | 銀之路            | 49      | 49    | ⭐⭐⭐⭐     | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:orange">4月</span>&nbsp;&nbsp;<span style="color:orange">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    #     | 英國之路          | 114     | 7     | ⭐⭐        | <span style="color:grey">1月</span>&nbsp;&nbsp;<span style="color:grey">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:blue">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:grey">12月</span> |
    #     | 世界盡頭之路      | 86      | 6     | ⭐⭐        | <span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:blue">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:blue">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span> |
    # """  
    # st.markdown(markdown, unsafe_allow_html=True)

    markdown = """
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <th>路線名稱</th>
            <th>公里數</th>
            <th>天數</th>
            <th>挑戰難度</th>
            <th>季節 (<span style="color:blue">適合月份</span> 、 <span style="color:green">熱門月份</span> 、<span style="color:orange"> 淡季</span>)</th>
        </tr>
        <tr>
            <td>法國之路</td>
            <td>771</td>
            <td>36</td>
            <td>⭐⭐</td>
            <td>&nbsp;<span style="color:orange">1月</span>&nbsp;&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;&nbsp;<span style="color:green">6月</span><br/> &nbsp;<span style="color:blue">7月</span>&nbsp;&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:blue">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span></td>
        </tr>
        <tr>
            <td>葡萄牙之路</td>
            <td>620</td>
            <td>29</td>
            <td>⭐</td>
            <td><span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span></td>
        </tr>
        <tr>
            <td>北方之路</td>
            <td>481</td>
            <td>23</td>
            <td>⭐</td>
            <td><span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:green">7月</span>&nbsp;&nbsp;<span style="color:green">8月</span>&nbsp;&nbsp;<span style="color:blue">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span></td>
        </tr>
        <tr>
            <td>原始之路</td>
            <td>16</td>
            <td>16</td>
            <td>⭐⭐⭐⭐</td>
            <td><span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:blue">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:green">7月</span>&nbsp;&nbsp;<span style="color:green">8月</span>&nbsp;&nbsp;<span style="color:blue">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span></td>
        </tr>
        <tr>
            <td>銀之路</td>
            <td>49</td>
            <td>49</td>
            <td>⭐⭐⭐⭐</td>
            <td><span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:orange">4月</span>&nbsp;&nbsp;<span style="color:orange">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:orange">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span></td>
        </tr>
        <tr>
            <td>英國之路</td>
            <td>114</td>
            <td>7</td>
            <td>⭐⭐</td>
            <td><span style="color:grey">1月</span>&nbsp;&nbsp;<span style="color:grey">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:green">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:blue">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:grey">12月</span></td>
        </tr>
        <tr>
            <td>世界盡頭之路</td>
            <td>86</td>
            <td>6</td>
            <td>⭐⭐</td>
            <td><span style="color:orange">1月</span>&nbsp;&nbsp;<span style="color:orange">2月</span>&nbsp;&nbsp;<span style="color:orange">3月</span>&nbsp;&nbsp;<span style="color:blue">4月</span>&nbsp;&nbsp;<span style="color:green">5月</span>&nbsp;&nbsp;<span style="color:blue">6月</span><br/> <span style="color:blue">7月</span>&nbsp;&nbsp;<span style="color:blue">8月</span>&nbsp;&nbsp;<span style="color:green">9月</span>&nbsp;&nbsp;<span style="color:blue">10月</span>&nbsp;&nbsp;<span style="color:orange">11月</span>&nbsp;&nbsp;<span style="color:orange">12月</span></td>
        </tr>
    </table>
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
        y=["Distance (km)", "Days"],  # Update with correct column names
        title="天數、距離比一比🔍",
        opacity=0.9,
        orientation="v",  # Vertical bars
        barmode='group',  # Grouped bar mode
    )
    
    fig.update_layout(
        #xaxis_title="路線",
        yaxis_title="數值",
        xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
    )
    
    # Show the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    markdown = """
            ### 法國之路 (Camino Francés)
        
        聖讓皮德波特（Saint-Jean-Pied-de-Port）位於法國，是這條路的起點，沿途經過的城市，如：潘普洛納（Pamplona）、布爾戈斯（Burgos）、萊昂（Leon）和龐費拉達（Ponferrada）等城鎮，  
        不僅有豐富的歷史文化，這條路線的地形還很多變，從庇里牛斯山脈的高山到北部平原的平坦地帶，再到加利西亞的起伏丘陵，相當考驗朝聖者的體能。  
        ![1](https://chinchillaz.github.io/streamlit-hw//Camino/photos/1_frances.png)
        
        ---
        
        ### 葡萄牙之路 (Camino Portugués)
        
        葡萄牙的首都里斯本（Lisbon）是這條路的主要出發點，沿途會經過「古老的道路」、「森林」、「農田」、「橄欖樹林」、「葡萄園」和「歷史城鎮」，這些自然景觀不僅提供了美麗的視覺享受，還能讓朝聖者與大自然親密接觸。  
        ![Image Description](https://chinchillaz.github.io/streamlit-hw//Camino/photos/2_portugal.jpg)

        
        ---
        
        ### 北方之路 (Camino del Norte)
        
        起點是位於西班牙北部的海濱城市聖塞巴斯蒂安（San Sebastien），沿途會穿越西班牙北部的海灘，再進入到寧靜的森林，於行走過程放鬆地享受大自然的魅力。  
        ![Image Description](https://chinchillaz.github.io/streamlit-hw//Camino/photos/3_Norte.jpg)
        
        ---
        
        ### 原始之路 (Camino Primitivo)
        
        這條路線是朝聖者前往聖雅各的最早路徑之一，起點位於西班牙的奧維多（Oviedo），沿途會經過坎塔布里亞山脈（Cantabrian Mountains），  
        以壯麗的自然景觀和豐富的文化聞名，但同時朝聖者也必須面對高達 1,100 米的山脈和險峻的地形，因此，也被描述為「美麗且最具挑戰性」的選擇。  
        ![Image Description](https://chinchillaz.github.io/streamlit-hw//Camino/photos/4_primitivo.jpg)
        
        ---
        
        ### 銀之路 (Via de la Plata)
        
        這條路線的起點位於南部的城市塞維利亞（Seville），其起源可以追溯到羅馬時代，當時它是塞維利亞和阿斯托爾加（Astorga）之間的重要貿易路線。  
        隨著時間的推移，這條路線逐漸成為朝聖者前往聖地亞哥·德·孔波斯特拉的主要路徑，並在阿斯托爾加與主要的「Camino Francés」（法國之路）相連。  
        沿途向朝聖者展示了西班牙豐富的文化遺產和自然美景，以及羅馬遺跡、中世紀橋樑和壯觀的教堂。  
        ![Image Description](https://chinchillaz.github.io/streamlit-hw//Camino/photos/5_Plata.jpg)
        
        ---
        
        ### 英國之路 (Camino Inglés)
        
        這條路線的歷史悠久，且與海洋有著密切的聯繫，從崎嶇的丘陵海岸線開始，再往內陸移動到郁郁蔥蔥的森林鄉村，不僅展現了自然景觀的美麗，也暗示了這條路線的多樣性，讓朝聖者能體驗不同的環境變化。  
        此外，這條路線也相較於其他路線安靜，朝聖者可以在一周內從費羅爾（Ferrol）或拉科魯尼亞（A Coruna）到達聖地亞哥（Santiago de Compostela）。  
        對於那些想要遠離更受歡迎的法國之路，並獲得朝聖證書的朝聖者來說，「英國之路」是一個很好的選擇。  
        ![Image Description](https://chinchillaz.github.io/streamlit-hw//Camino/photos/5_ingles.jpg)
        
        ---
        
        ### 世界盡頭之路 (Camino Finisterre-Muxía)
        
        許多朝聖者在抵達終點後，會決定將他們的旅程延伸到死亡之海（Costa da Morte）– 菲尼斯特雷（Finisterre），並在西班牙最西端的陡峭懸崖為這趟旅程畫下句點。  
        <img src="https://chinchillaz.github.io/streamlit-hw//Camino/photos/6_muxia.jpg" width="1200"/>

    """
    st.markdown(markdown, unsafe_allow_html=True)
   




