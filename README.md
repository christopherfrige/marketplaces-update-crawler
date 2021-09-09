# Marketplaces-update-crawler

Um web crawler que indexa informação de atualizações dos principais marketplaces brasileiros, centralizando a informação em um chat do Slack. <br>

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

    </br>

- **Setando variáveis de ambiente:**

    O projeto atualmente utiliza as seguintes variáveis de ambiente:

        TABLE_NAME -> Nome da tabela que será usada no Amazon DynamoDB

        SLACK_BOT -> Token do bot do slack que será utilizado

    Para utilizar o Amazon DynamoDB é necessário ter uma conta na AWS e ter configurado suas credenciais no computador. Após isso, é preciso criar uma tabela, com um nome que posteriormente será utilizado.

    Para mais informações de como pegar o token de um Bot e utilizá-lo, crie um servidor no Slack para testes e leia o tópico **"Criando um bot no Slack"** [dessa publicação](https://medium.com/@gpiress/criando-um-bot-no-slack-dd1895cc6422) no Medium.

    **Exemplo para Linux**</br>

    No terminal, digitar:

        SLACK_TOKEN="TOKEN_DO_SLACK_BOT"
        TABLE_NAME="NOME_DA_TABELA_NO_DYNAMODB"

    Para validar as variáveis:

        set | grep SLACK_TOKEN
        set | grep TABLE_NAME

    Verificar se as variáveis foram criadas:

        echo $SLACK_TOKEN
        echo $TABLE_NAME

    **Exemplo para Windows** </br>

    No terminal, digitar:

        setx SLACK_TOKEN "Token_Do_Slack_Bot"
        setx TABLE_NAME "Nome_Da_Tabela_No_DynamoDB"

    Ou também pode ser feito também através de interface gráfica, no painel de controle do sistema.

## Execução local

Para ver o indexador em ação, após a devida configuração, digitar no terminal:

    python run.py

É possível fazer alterações para indexar e comparar apenas os marketplaces selecionados, para isso basta alterar a rotina da função **main** do mesmo arquivo. </br>
Como por exemplo:

    def main(event, context):
        amazon()
        # b2w()
        # magazine()
        # mercadolivre()
        # viavarejo()

Nesse caso, rodaria apenas a verificação de atualizações da Amazon.
