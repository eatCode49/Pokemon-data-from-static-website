import os
import requests
from bs4 import BeautifulSoup

directory = os.makedirs("data")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"}
for i in range(1,38):
    request = requests.get(f"https://scrapeme.live/page/{i}/?s=pokemon", headers=header)
    soup = BeautifulSoup(request.content, "html.parser")
    with open(f"data/Pokemon_{i}.html","w",encoding='utf-8') as file:
        file.write(str(soup))
        