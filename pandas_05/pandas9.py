# Beautifulsoup 객체를 이용한 웹문서 처리
import requests
from bs4 import BeautifulSoup

baseurl = "https://www.naver.com"
headers = {"User-Agent":"Mozilla/5.0"}

source = requests.get(baseurl, headers=headers)
print(source)

conv_data = BeautifulSoup(source.text, "lxml")
print(conv_data, type(conv_data))

for atag in conv_data.find_all("a"):
    href = atag.get("href")
    title = atag.get_text(strip=True)
    if title:
        print(href)
        print(title)
        print("-----------")
