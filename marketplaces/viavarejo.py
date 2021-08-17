import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararVersoes
from utilities.GlobalVariables import VIAVAREJO_CODE

def viavarejo():
    page = requests.get("https://desenvolvedores.viavarejo.com.br/api-portal/swagger")
    soup = BeautifulSoup(page.text, "html.parser")

    titulo = "Nova versão de API"
    url = "https://desenvolvedores.viavarejo.com.br/api-portal/swagger"

    # Pega as versões do site e coloca numa lista
    versaoDoDia = []
    for linha in soup.select("table tbody tr"):
        # Seleciona cada linha individualmente
        temp = linha.select("td")
        versaoDoDia.append(temp[1].text)     

    compararVersoes(VIAVAREJO_CODE, versaoDoDia, url)
