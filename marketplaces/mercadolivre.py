import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararAlteracoes
from utilities.GlobalVariables import MERCADOLIVRE_CODE

# Mercado Pago
def mercadolivre():
    page = requests.get("https://www.mercadopago.com.br/developers/pt/guides/resources/changelog/current-year")
    soup = BeautifulSoup(page.text, "html.parser")

    # Pega o primeiro título do changelog
    titulo_raw = soup.find(class_="changelog-label-container")
    titulo = titulo_raw.text
    url = "https://www.mercadopago.com.br/developers/pt/guides/resources/changelog/current-year"

    compararAlteracoes(MERCADOLIVRE_CODE, titulo, url, False)

