import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

images = soup.find_all("img",attrs={"class": "thumb_img"})

# print(images[0])
for index,image in enumerate(images):
    try:
        image_url = image["data-original-src"]
    except KeyError:
        break

    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open(f"movie{index+1}.jpg","wb")as f:
        f.write(image_res.content)