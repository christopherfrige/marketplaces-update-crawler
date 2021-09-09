from services.SlackBot import enviaMensagem
from utilities.GlobalVariables import MARKETPLACES
from utilities.EnviromentVariables import TABLE_NAME
import boto3
from boto3.dynamodb.conditions import Key

def inicializaBanco():
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(TABLE_NAME)
    return table

def insereNoBanco(marketplaceID, texto, table):
    response = table.put_item(
                Item = {
                    "marketplace": marketplaceID,
                    "texto": texto
                }
            )
    return response

def procuraNoBanco(marketplaceID, table):
    response = table.get_item(
        Key={
            "marketplace": marketplaceID 
        }
    )
    return response

def compararAlteracoes(MKTPLACE_CODE, texto, url, versao=False):
    table = inicializaBanco()
    marketplaceID = MARKETPLACES.get(MKTPLACE_CODE)

    # Pega a linha do marketplace na tabela
    response = procuraNoBanco(marketplaceID, table)    

    # Se o dado do site diverge do contido no banco de dados
    try:
        if (texto != response['Item']['texto']):
            insereNoBanco(marketplaceID, texto, table)            
            print(f"Houveram mudanças em {marketplaceID}!")
            enviaMensagem(MKTPLACE_CODE, texto, url, versao)

    except KeyError:
        print(f"Marketplace {marketplaceID} não encontrado! Inserindo-o...")
        insereNoBanco(marketplaceID, texto, table)

if __name__ == "__main__":
    compararAlteracoes(0, "teste amazon", "random_url")
