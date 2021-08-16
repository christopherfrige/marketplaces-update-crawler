import requests
from bs4 import BeautifulSoup
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao
from utilities.GlobalVariables import B2W_CODE, DATABASE_FILE_DIRECTORY

def b2w():
    page = requests.get("https://desenvolvedores.skyhub.com.br/comunicados/comunicados-2021")
    soup = BeautifulSoup(page.text, "html.parser")

    titulo_raw = soup.find_all(class_="text-4505230f--UIH400-4e41e82a--textContentFamily-49a318e1")
    titulo = titulo_raw[3].text
    descricao_raw = soup.find_all(class_="text-4505230f--TextH400-3033861f--textContentFamily-49a318e1")
    descricao = descricao_raw[2].text
    link = soup.find_all("a", class_="reset-3c756112--card-6570f064--whiteCard-fff091a4--card-5e635eb5")
    url = "https://desenvolvedores.skyhub.com.br/" + link[0].get('href')

    # Consulta no mini banco de dados para ver se houveram alterações
    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt", "r") as db:
        linhas = db.readlines()
        tituloDB = linhas[B2W_CODE].strip()
        #print(titulo)
        #print(tituloDB)
        if titulo != tituloDB:
            temMudancas = True

    if temMudancas:
        enviaMensagem(B2W_CODE, titulo, url, descricao)
        print("Tiveram mudanças B2W")
        
        linhas[B2W_CODE] = titulo + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", "w") as db:
            db.writelines(linhas)

b2w()