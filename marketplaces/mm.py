import requests
from bs4 import BeautifulSoup
from services.SlackBot import enviaMensagem, enviaMensagemAlteracao
from utilities.GlobalVariables import MM_CODE, DATABASE_FILE_DIRECTORY

# NAO FUNCIONANDO (ERRO 403 NA REQUEST)
# Provavelmente resolve-se com Selenium (como um operator bot)
def madeiramadeira():

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "cache-control": "max-age=0",
        "Content-Type": "text/html"
    }

    cookies = {
        "__cfruid": "6aa319aab0c110131f0901321a87e58e095b0b3e",
    }

    page = requests.get("https://madeiramadeira.zendesk.com/hc/pt-br/sections/360008709932-Coamunica%C3%A7%C3%A3o-Marketplace-", headers=headers, cookies=cookies)
    print(page)
    soup = BeautifulSoup(page.text, "html.parser")
    #print(soup)

    titulos = soup.find_all(class_="article-list-link")
    links = soup.find_all(class_="article-list-link")

    url = "https://madeiramadeira.zendesk.com/" + links[0].get('href')

    enviaMensagem(1, titulos[0].text.strip(), url, False)

madeiramadeira()