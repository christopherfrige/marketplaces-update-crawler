import requests
from bs4 import BeautifulSoup
from services.DatabaseComparisons import compararAlteracoes
from utilities.GlobalVariables import B2W_CODE

def b2w():
    page = requests.get("https://desenvolvedores.skyhub.com.br/comunicados/comunicados-2021")
    soup = BeautifulSoup(page.text, "html.parser")

    titulo_raw = soup.find_all(class_="text-4505230f--UIH400-4e41e82a--textContentFamily-49a318e1")
    titulo = titulo_raw[3].text

    link = soup.find_all("a", class_="reset-3c756112--card-6570f064--whiteCard-fff091a4--card-5e635eb5")
    url = "https://desenvolvedores.skyhub.com.br/" + link[0].get('href')

    compararAlteracoes(B2W_CODE, titulo, url)
