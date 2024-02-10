import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/webtoon"
res = requests.get(url, headers=headers)
res.raise_for_status()

#print(res.text)

soup = BeautifulSoup(res.text, "lxml")

print(soup.a)
cartoons = soup.find_all("div")
print(cartoons)
# print(soup.title)
# print(soup.)

# cartoons = soup.find_all("span", attrs={"class": "text"})

# for cartoon in cartoons:
#     print(cartoon.get_text())