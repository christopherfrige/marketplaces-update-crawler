import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararAlteracoes
from utilities.GlobalVariables import VIAVAREJO_CODE

def viavarejo():
    url = "https://desenvolvedores.viavarejo.com.br/api-portal/swagger"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    # Pega as versões do site e coloca numa lista
    versaoAtual = []
    for linha in soup.select("table tbody tr"):
        # Seleciona cada linha individualmente
        temp = linha.select("td")
        versaoAtual.append(temp[1].text)     

    compararAlteracoes(VIAVAREJO_CODE, versaoAtual, url , "Nova versão da API!")
