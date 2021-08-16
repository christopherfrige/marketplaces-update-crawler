import requests
from bs4 import BeautifulSoup
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao
from utilities.GlobalVariables import MERCADOLIVRE_CODE, DATABASE_FILE_DIRECTORY

# Mercado Pago
def mercadolivre():
    page = requests.get("https://www.mercadopago.com.br/developers/pt/guides/resources/changelog/current-year")
    soup = BeautifulSoup(page.text, "html.parser")

    # Pega o primeiro título do changelog
    titulo_raw = soup.find(class_="changelog-label-container")
    titulo = titulo_raw.text
    url = "https://www.mercadopago.com.br/developers/pt/guides/resources/changelog/current-year"

    # Consulta no mini banco de dados para ver se houveram alterações
    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt", "r") as db:
        linhas = db.readlines()
        tituloDB = linhas[MERCADOLIVRE_CODE].strip()
        #print(titulo)
        #print(tituloDB)
        if titulo != tituloDB:
            temMudancas = True

    if temMudancas:
        enviaMensagem(MERCADOLIVRE_CODE, titulo, url, False)
        print("Tiveram mudanças Mercado Livre")
        
        linhas[MERCADOLIVRE_CODE] = titulo + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", "w") as db:
            db.writelines(linhas)


mercadolivre()