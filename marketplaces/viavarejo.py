import requests
from bs4 import BeautifulSoup
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao
from utilities.GlobalVariables import VIAVAREJO_CODE, DATABASE_FILE_DIRECTORY

def viavarejo():
    page = requests.get("https://desenvolvedores.viavarejo.com.br/api-portal/swagger")
    soup = BeautifulSoup(page.text, "html.parser")

    titulo = "Nova versão de API"
    url = "https://desenvolvedores.viavarejo.com.br/api-portal/swagger"

    # Pega as versões do site (há 3) e coloca numa lista
    versaoDoDia = []
    for linha in soup.select("table tbody tr"):
        # Seleciona cada linha individualmente
        temp = linha.select("td")
        versaoDoDia.append(temp[1].text)     

    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt", "r") as db:
        linhas = db.readlines()
        versaoDB = linhas[VIAVAREJO_CODE].strip()
        #print(versaoDoDia)
        #print(versaoDB)
        if str(versaoDoDia) != versaoDB:
            temMudancas = True

    if temMudancas:
        enviaMensagemAlteracao(VIAVAREJO_CODE, titulo, url)        
        print("Tiveram mudanças Via Varejo")

        linhas[VIAVAREJO_CODE] = str(versaoDoDia) + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", "w") as db:
            db.writelines(linhas)

viavarejo()