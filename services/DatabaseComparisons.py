from utilities.GlobalVariables import *
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao

# Consulta obanco de dados para ver se houveram alterações (novas postagens)
def compararAlteracoes(MKTPLACE_CODE, titulo, url, descricao):
    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt", mode="r", encoding='utf8') as db:
        linhas = db.readlines()
        tituloDB = linhas[MKTPLACE_CODE].strip()
    
        if titulo != tituloDB:
            temMudancas = True

    if temMudancas:
        enviaMensagem(MKTPLACE_CODE, titulo, url, descricao)
        print(f"Tiveram mudanças {MARKETPLACES.get(MKTPLACE_CODE)}")
        
        linhas[MKTPLACE_CODE] = titulo + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", mode="w", encoding='utf8') as db:
            db.writelines(linhas)

# Consulta o banco de dados em busca em busca de alterações (novas versões)
def compararVersoes(MKTPLACE_CODE, versaoDoDia, url):
    temMudancas = False
    with open(DATABASE_FILE_DIRECTORY + "\database.txt", mode="r", encoding='utf8') as db:
        linhas = db.readlines()
        versaoDB = linhas[MKTPLACE_CODE].strip()
        
        if str(versaoDoDia) != versaoDB:
            temMudancas = True

    if temMudancas:
        titulo = "Nova versão de API"
        enviaMensagemAlteracao(MKTPLACE_CODE, titulo, url)        
        print("Tiveram mudanças Via Varejo")

        linhas[MKTPLACE_CODE] = str(versaoDoDia) + "\n"
        with open (DATABASE_FILE_DIRECTORY + "\database.txt", mode="w", encoding='utf8') as db:
            db.writelines(linhas)

