import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararAlteracoes
from utilities.GlobalVariables import MAGAZINE_CODE

def magazine():
    headers = {"User-Agent": 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    # Necessário o header acima para autorizar a requisição
    page = requests.get("https://marketplace-faq.magazineluiza.com.br/", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    titulo_raw = soup.find(class_="hkb-category__title")
    titulo = titulo_raw.text.strip()

    link = soup.find(class_="hkb-category__link")
    url = link.get('href')

    compararAlteracoes(MAGAZINE_CODE, titulo, url)


