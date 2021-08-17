# Marketplaces-update-crawler

Um web crawler que indexa informação de atualizações dos principais marketplaces brasileiros. <br/>

## Requisitos
- [Python 3.9 ou superior](https://www.python.org/downloads/ "Download Python")

## Introdução

Clone o repositório para uma pasta local e configure como descrito nos tópicos seguintes

## Configurando o ambiente

Para que não seja necessário instalar as bibliotecas diretamente no computador e que o projeto seja executado de maneira local, é necessário as seguintes etapas.

- **Criação de ambiente virtual:**

    Nessa etapa será necessário executar os seguintes comandos no terminal (dentro da pasta do projeto):

    Instalar o módulo de ambiente virtual (caso ainda não o tenha)

        pip install virtualenv

    Checar instalação

        virtualenv --version

    Os seguintes passos são diferentes no Linux e no Windows

    **Exemplo para Linux**    

    Criar um ambiente virtual com o nome 'env'
            
        virtualenv env

    Ativar ambiente virtual

        source env/bin/activate

    Instalar as dependências do projeto

        pip install -r requirements.txt

    **Exemplo para Windows**
    
    Criar um ambiente virtual com o nome 'env'

        python -m venv env

    Ativar ambiente virtual

        ./env/Scripts/activate

    Instalar as dependências do projeto

        pip install -r requirements.txt

## Inserindo as variáveis

Modificar as variáveis no arquivo **'GlobalVariables.py'** para o correto funcionamento dos meios de mensagem e do banco de dados do arquivo de texto.

    DATABASE_FILE_DIRECTORY = "DB_FOLDER_DIRECTORY"

    SLACK_BOT = "SLACK_BOT_TOKEN"
