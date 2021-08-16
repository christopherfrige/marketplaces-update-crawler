import requests
from bs4 import BeautifulSoup
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao
from utilities.GlobalVariables import AMAZON_CODE, DATABASE_FILE_DIRECTORY

def amazon():
    page = requests.get("https://sellercentral.amazon.com/forums/c/9/41")
    soup = BeautifulSoup(page.text, "html.parser")

    titulo_raw = soup.select(".topic-list span")
    titulo = titulo_raw[0].text
    link = soup.select(".topic-list a")
    url = link[0].get('href')

    # Consulta no mini banco de dados para ver se houveram alterações
    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt", "r") as db:
        linhas = db.readlines()
        tituloDB = linhas[AMAZON_CODE].strip()
        #print(titulo)
        #print(tituloDB)
        if titulo != tituloDB:
            temMudancas = True

    if temMudancas:
        enviaMensagem(AMAZON_CODE, titulo, url, False)
        print("Tiveram mudanças Amazon")
        
        linhas[AMAZON_CODE] = titulo + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", "w") as db:
            db.writelines(linhas)

amazon()