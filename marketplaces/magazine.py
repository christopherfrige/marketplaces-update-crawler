import requests
from bs4 import BeautifulSoup
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao
from utilities.GlobalVariables import MAGAZINE_CODE, DATABASE_FILE_DIRECTORY

def magazine():
    headers = {"User-Agent": 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    # Necessário o header acima para autorizar a requisição
    page = requests.get("https://marketplace-faq.magazineluiza.com.br/", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    titulo_raw = soup.find(class_="hkb-category__title")
    titulo = titulo_raw.text.strip()
    descricao_raw = soup.find(class_="hkb-category__description")
    descricao = descricao_raw.text
    link = soup.find(class_="hkb-category__link")
    url = link.get('href')

    # Consulta no mini banco de dados para ver se houveram alterações
    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt") as db:
        linhas = db.readlines()
        tituloDB = linhas[MAGAZINE_CODE].strip()
        #print(titulo)
        #print(tituloDB)
        if titulo != tituloDB:
            temMudancas = True

    if temMudancas:
        enviaMensagem(MAGAZINE_CODE, titulo, url, descricao)
        print("Tiveram mudanças Magazine Luiza")
        
        linhas[MAGAZINE_CODE] = titulo + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", "w") as db:
            db.writelines(linhas)

magazine()