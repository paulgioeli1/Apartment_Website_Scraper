#Trying to pull data off of Versailles Website

import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.equityapartments.com/los-angeles/koreatown/versailles-koreatown-apartments"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

prices = soup.find_all("span", class_ = "pricing")

price_list = []

for price in prices:
    price_list.append(price.text)


print(price_list)
df = pd.DataFrame(price_list)
print(df)
