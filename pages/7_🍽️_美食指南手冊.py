import streamlit as st

logo = "https://chinchillaz.github.io/streamlit-hw/logo_sun-removebg-preview.png"
st.sidebar.image(logo)

st.title("美食指南手冊 🍽️")

st.markdown(
    """
在Camino de Santiago朝聖之路上，美食不僅是一頓填飽肚子的餐點，更是對當地文化、傳統和人情味的深刻體驗。這片土地孕育了無數令人垂涎的美味，而每一道佳餚都訴說著當地有趣的故事。

無論您是漫步在西班牙的葡萄園之間，還是在葡萄牙的漁村享用新鮮海味，這份指南將帶您走進Camino之路的味蕾旅程。

你，準備好踏上這段飽含美食與文化的朝聖之路了嗎？
    """
)

# List of image URLs
image_urls = [
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/1_F.jpeg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/2_Paella.png",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/3_.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/4_.png",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/5_F.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/6_.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/7_F.png",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/8_F.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/9_.png",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/12_F.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/22_F.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/3_F.jpg",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/4_F.png",
    "https://chinchillaz.github.io/streamlit-hw/Camino/food/52_F.jpeg",
]

cols = 5  # 5 columns
rows = 3  # 3 rows
max_images = cols * rows  # Display up to 15 images

# Truncate the list to fit the table
image_urls = image_urls[:max_images]

for i in range(rows):
    # Create a row of 5 columns
    columns = st.columns(cols)
    for j in range(cols):
        index = i * cols + j
        if index < len(image_urls):
            # Display the image in the respective column
            with columns[j]:
                st.image(image_urls[index], use_container_width=True)





st.title("西班牙")

# First Dish: Pulpo a la Gallega
st.subheader("1. 炭烤香料馬鈴薯章魚腳 Pulpo a la Gallega")
markdown = """
源自西班牙西北部的加利西亞（Galicia）地區，加利西亞有著悠久的海鮮捕撈歷史，尤其是章魚，這使得章魚成為當地餐桌上的重要食材之一。這道菜的主要特色是將章魚腳和馬鈴薯結合，經過燒烤和香料調味，口感鮮嫩且極具層次感，通常作為前菜或共享菜品來享用，搭配著一杯清爽的白葡萄酒。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/1_F.jpeg"
st.image(image_url, caption="Pulpo a la Gallega", use_container_width=True)

# Second Dish: Paella de Marisco
st.subheader("2. 西班牙海鮮大鍋飯 Paella de Marisco")
markdown = """
Paella（帕埃利亞）這個名字來自西班牙瓦倫西亞（Valencia）。香料中的藏紅花賦予飯菜金黃顏色和特有香氣，海鮮口感鮮嫩多汁，搭配香脆的米飯底部（socarrat），深受食客喜愛。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/2_Paella.png"
st.image(image_url, caption="Paella de Marisco", use_container_width=True)

# Third Dish: Secreto de Cerdo a la Plancha
st.subheader("3. 秘密西班牙松阪豬 Secreto de Cerdo a la Plancha")
markdown = """
Secreto de Cerdo是一道來自西班牙的豬肉菜肴，名稱中的“Secreto”意指豬肉的「秘密部位」，豬肩部的嫩肉，煎烤後外脆內嫩。搭配橄欖油和鹽調味，肉香十足且不油膩，是一道簡單卻極美味的料理。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/3_.jpg"
st.image(image_url, caption="Secreto de Cerdo a la Plancha", use_container_width=True)

# Fourth Dish: Tortilla Espanola
st.subheader("4. 西班牙馬鈴薯烘蛋 Tortilla Espanola")
markdown = """
Tortilla Española 可以在西班牙的每個家庭、酒吧和餐廳中找到。它不僅是家常菜，還是西班牙的街頭小吃。很多西班牙人在午餐和晚餐時會享用這道菜，甚至會把它當作Tapas（小吃）來分享。

馬鈴薯的軟嫩與雞蛋的綿密相互交織，而橄欖油為整道菜增添了濃郁的風味，洋蔥則使得味道更加圓潤和甜美。這道菜的外層微微金黃，而內部保持濕潤且柔滑，具有豐富的家常感覺。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/4_.png"
st.image(image_url, caption="Tortilla Espanola", use_container_width=True)




st.subheader("5.塔帕斯 Tapas")
markdown = """
最早出現於西班牙的酒吧或餐館，當時酒吧的主人會用一片麵包或薄片肉類（例如火腿或香腸）來蓋住酒杯，防止灰塵或蚊子進入酒中。這片小食就被稱為 "tapa"（蓋子之意）。
隨著時間的推移，這些小吃變得越來越豐富，逐漸演變成各式各樣的小盤美食，現已成為一種社交文化的象徵。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/5_F.jpg"
st.image(image_url, caption="Tapas", use_container_width=True)



st.subheader("6.伊比利火腿 Jamon Iberico")
markdown = """
在西班牙，品嚐伊比利火腿是一種傳統的儀式，無論是在家庭聚會、節慶還是與朋友聚餐時，伊比利火腿都是必不可少的佳餚。其也成為了國際間推崇的高端食材，許多高端餐廳和美食愛好者都將它視為頂級享受，是西班牙其中一個國際名片。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/6_.jpg"
st.image(image_url, caption="Jamon Iberico", use_container_width=True)



st.subheader("7.燉牛肚 Callos a la Madrileña")
markdown = """
源自西班牙首都馬德里，這道菜由牛肚與各種香料、番茄和其他食材燉煮而成，風味濃郁，口感豐富。它在寒冷的季節中尤其受歡迎，常常出現在西班牙的家庭聚餐和餐廳菜單上。

這道菜也是西班牙社會中“共享”的象徵，常常會在大家聚集的餐桌上一起享用，傳遞著西班牙人對家庭和朋友聚會的重視。此外，燉牛肚也有著強烈的地方性特徵，是馬德里市民飲食文化的重要一環。雖然西班牙其他地區也有類似的燉菜，但這道菜在馬德里的獨特做法和風味，使其成為當地的代表性美食。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/7_F.png"
st.image(image_url, caption="Callos a la Madrileña", use_container_width=True)



st.subheader("8.安達盧西亞冷湯 Gazpacho")
markdown = """
Gazpacho 是安達盧西亞的經典料理，起源於西班牙南部的安達盧西亞地區，這裡氣候炎熱且乾燥，它不僅清涼解暑，還能提供充足的水分和維他命，是一道非常健康且既能解渴又能提供營養的夏季菜餚。

這道湯以新鮮的番茄、黃瓜、紅椒等蔬菜為基礎，搭配橄欖油和紅酒醋，風味獨特，讓人在炎熱的夏季中感到清涼和舒適。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/8_F.jpg"
st.image(image_url, caption="Gazpacho", use_container_width=True)



st.subheader("9.巧克力吉拿棒 Churros con Chocolate")
markdown = """
由香脆的吉拿棒（Churros）搭配濃郁的熱巧克力醬（Chocolate）一起食用，通常作為早餐或下午茶的點心。這道甜點在西班牙以及拉丁美洲地區都非常受歡迎，無論是街頭小攤還是餐廳中都可以看到它的身影。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/9_.png"
st.image(image_url, caption="Churros con Chocolate", use_container_width=True)



st.title("葡萄牙")
st.subheader("1.葡式蛋塔 Pastéis de nata")
markdown = """
Pastéis de nata 起源於葡萄牙的貝倫（Belém），這裡有著著名的貝倫蛋塔（Pastéis de Belém），被認為是葡萄牙最經典的版本。據說，這道甜點的起源可以追溯到18世紀的修道院，當時修道士使用剩餘的蛋黃和糖漿來製作這道甜點。隨著時間的推移，這款甜點逐漸流行開來，並在葡萄牙各地及全世界廣泛傳播。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/12_F.jpg"
st.image(image_url, caption="Pastéis de nata", use_container_width=True)



st.subheader("2.葡式烤雞 Frango assado")
markdown = """
Frango Assado 是葡萄牙的一道經典家庭料理，幾乎每個家庭都有自己獨特的烤雞製作方式，通常是將整隻雞用香料和橄欖油醃製後，再放入烤箱中烤製。這道菜風味獨特，外皮酥脆，肉質鮮嫩多汁，並且充滿了香料的香氣。

很多餐廳會提供搭配傳統葡萄牙飲品，如葡萄酒或啤酒。葡萄牙烤雞也在一些殖民地，如安哥拉和莫桑比克，甚至是巴西等地有著深遠的影響，當地的居民也深受其啟發，並發展出各自不同的烤雞風味。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/22_F.jpg"
st.image(image_url, caption="Frango assado", use_container_width=True)



st.subheader("3.豬扒包 Bifanas")
markdown = """
據說源自葡萄牙的金達（Vila de Fafe）地區，並在當地的酒吧和街頭市場中逐漸流行起來。隨著時間的推移，這道美味小吃成為了葡萄牙各地街頭的經典美食，經常出現在葡萄牙的節日集市和家庭聚會中。

這道美味的熱三明治以醃製過的豬肉為主角，豬肉經過香料和調味料的醃製後，煎炸至外焦內嫩，再夾入柔軟的麵包中食用，搭配上辣醬或其他配料，形成了獨特的風味。是葡萄牙街頭和酒吧裡常見的小吃。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/3_F.jpg"
st.image(image_url, caption="Bifanas", use_container_width=True)


st.subheader("4.胖三明治 Francesinha")
markdown = """
來自葡萄牙波爾圖地區的經典料理，Francesinha 的名稱意思是“小法國人”，但它的背景並不是來自法國，而是葡萄牙對法式三明治(Croque Monsieur)的獨特創新。這道菜由多層豐富的食材組成，並浸泡在濃郁的醬汁中，是一道非常有特色且令人滿足的美食。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/4_F.png"
st.image(image_url, caption="Francesinha", use_container_width=True)



st.subheader("5.炸鱈魚球 Bolinhos de Bacalhau")
markdown = """
葡萄牙有一句名言：“Deus fez o bacalhau e o diabo fez o resto” （“上帝創造了鱈魚，惡魔創造了其餘的”），這句話反映了鱈魚在葡萄牙料理中的重要地位。鱈魚不僅在葡萄牙的日常飲食中占有一席之地，也是葡萄牙傳統節日和家庭聚會的必備食材。

這道小吃由鹹鱈魚（Bacalhau）為主要食材，搭配土豆、洋蔥、香菜等調味料，製成小圓球狀後進行油炸。炸至金黃酥脆的鱈魚球，外脆內嫩，鮮美可口，特別適合作為開胃小吃。
"""
st.markdown(markdown)
image_url = "https://chinchillaz.github.io/streamlit-hw/Camino/food/52_F.jpeg"
st.image(image_url, caption="Bolinhos de Bacalhau", use_container_width=True)




markdown = """
        <br><br><br>
        相關連結<br>
        [► Camino七大路線介紹⛰️: 這些路線充滿歷史與挑戰，帶你走過美麗的景點與文化的精髓](https://camino.streamlit.app/%E8%B7%AF%E7%B7%9A%E4%BB%8B%E7%B4%B9)  
        [► Camino沿路旅遊景點推薦🏰: 從壯麗的古堡到浪漫的海岸線，發現不容錯過的必遊景點！](https://camino.streamlit.app/%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6)  
        [► Camino全球人次統計👪: 全球朝聖者的足跡！快來看看哪個國家的旅客最多](https://camino.streamlit.app/%E5%85%A8%E7%90%83%E4%BA%BA%E6%AC%A1%E7%B5%B1%E8%A8%88)  
        [► Camino美食指南手冊🍽️: 品味Camino沿途的美味，從地道的小吃到高級餐廳一網打盡！](https://camino.streamlit.app/%E7%BE%8E%E9%A3%9F%E6%8C%87%E5%8D%97%E6%89%8B%E5%86%8A)      
    """
st.markdown(markdown, unsafe_allow_html=True)
