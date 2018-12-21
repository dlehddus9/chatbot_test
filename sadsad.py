imgurl = soup2.find("div", class_="thmb c").find("img")["origin_src"]
atth = [{"title":"How does this look?","image_url": imgurl}]

img_title = []
img_url = []


for i in range():
    dic = [{"title": img_title[i], "image_url": img_url[i]}]

    sc.api_call(
       "chat.postMessage",
       channel=channel,
       text= "맛집이름",
       attachments = dic
     )