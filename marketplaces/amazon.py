import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararAlteracoes
from utilities.GlobalVariables import AMAZON_CODE

def amazon():
    # Faz a requisição e transforma o site em um objeto analisável
    page = requests.get("https://sellercentral.amazon.com/forums/c/9/41")
    soup = BeautifulSoup(page.text, "html.parser")

    # Pega elementos específicos da página, nesse caso titulo, link e url da última postagem do fórum
    titulo_raw = soup.select(".topic-list span")
    titulo = titulo_raw[0].text
    link = soup.select(".topic-list a")
    url = link[0].get('href')  

    # Chama a função para comparar com o dado presente no banco de dados
    # Se confirmado que há alterações, uma mensagem no Slack é enviada, e o banco de dados
    # É atualizado com os novos valores
    compararAlteracoes(AMAZON_CODE, titulo, url, False)