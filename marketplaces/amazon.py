import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararAlteracoes
from utilities.GlobalVariables import AMAZON_CODE

def amazon():
    page = requests.get("https://sellercentral.amazon.com/forums/c/9/41")
    soup = BeautifulSoup(page.text, "html.parser")

    titulo_raw = soup.select(".topic-list span")
    titulo = titulo_raw[0].text
    link = soup.select(".topic-list a")
    url = link[0].get('href')  

    compararAlteracoes(AMAZON_CODE, titulo, url, False)
