import requests
from bs4 import BeautifulSoup

#https://www.youtube.com/watch?v=87Gx3U0BDlo
# result = requests.get("https://www.google.com/")
# https://www.google.com/search?q=vodka&uact=5
result = requests.get("https://www.google.com/search?q=canada+history")


print(result.status_code)

if result.status_code == 200:
    src = result.content
    soup = BeautifulSoup(src,features="html.parser")
    #fina all the links
    links = soup.find_all("a")
    for link in links:
        if "canada" in link.text:
            print(link.attrs['href'])