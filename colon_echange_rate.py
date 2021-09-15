import requests
from bs4 import BeautifulSoup

result = requests.get("https://fx-rate.net/CRC/USD/")


print(result.status_code)

if result.status_code == 200:
    src = result.content
    soup = BeautifulSoup(src,features="html.parser")
    #fina all the links
    div_tags = soup.find_all('div')
    exchange = ""
    for div in div_tags:
        ID = div.get('id')
        if ID == "pair_today":
            algos = div.find_all('div')
            for algo in algos:
                texts = algo.find_all('h1')
                for ts in texts:
                    if "Costa Rican" in ts.text:
                        exchange = ts.text
                        break
    split = exchange.split()
    textNum = split[5]
    intValue = float(textNum)
    tasa = round(intValue, 4)
    print(tasa)