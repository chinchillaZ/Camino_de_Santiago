import streamlit as st

st.set_page_config(layout="wide")


logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

st.title("☎️ 聯絡資訊")

markdown = """
感謝您使用朝聖者之路平台！<br>  
由於期末時間緊迫，目前尚未實現使用者自行標示地點與整合紀錄的功能。<br>  
我們誠摯邀請使用平台的朋友，將沿途探索到的美食店家與景點資訊分享給我們。<br>  
您的寶貴建議將有助於我們在後續更新中，繼續優化平台內容，服務更多的朝聖者。<br>  
<br>  
期待在朝聖者之路與您相遇！

<br>  
📧 **Email**: [example@domain.com](mailto:example@domain.com)  
📱 **聯絡電話**: +123-456-7890  
<br>  
"""

st.markdown(markdown, unsafe_allow_html=True)

