import streamlit as st

st.set_page_config(layout="wide")


logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

st.title("☎️ 聯絡資訊")

markdown = """
感謝您使用朝聖者之路平台！<br>
雖然因為期末時間緊迫，目前尚未實現使用者自行標示地點與整合紀錄的功能 <br>
歡迎使用平台的朋友，將沿途探索到的美食店家、景點資訊分享給我們，<br>
我們將在後續更新納入您的寶貴建議，繼續優化平台
<br>
<br>
📧 **Email**: [example@domain.com](mailto:example@domain.com)  
📱 **聯絡電話**: +123-456-7890
<br>
<br>
<br>
~~~~期待在朝聖者之路與您相遇~~~~
"""
st.markdown(markdown, html =True)
