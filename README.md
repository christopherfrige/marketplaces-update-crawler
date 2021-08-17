# Marketplaces-update-crawler

Um web crawler que indexa informação de atualizações dos principais marketplaces brasileiros. [WIP] <br/>

## Requisitos
- [Python 3.9 ou superior](https://www.python.org/downloads/ "Download Python")

## Introdução

Após

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

## Executar

Para ver o indexador em ação, após a devida configuração, rodar o arquivo **run.py**. </br>
É possível fazer alterações para indexar e comparar marketplaces específicos, para isso só alterar a rotina da função **main** do mesmo arquivo. </br>
Como por exemplo:

    def main():
        amazon()
        #b2w()
        #magazine()
        #mercadolivre()
        #viavarejo()

Nesse caso, rodaria apenas a verificação de atualizações da amazon.