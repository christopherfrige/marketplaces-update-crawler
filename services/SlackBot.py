from slack_sdk import WebClient
from utilities.GlobalVariables import MARKETPLACES
from utilities.EnviromentVariables import SLACK_TOKEN

# Envio de mensagens no canal do slack, havendo descrição ou não
def enviaMensagem(MKTPLACE_CODE, title, url, versao = False):
    slack_client = WebClient(SLACK_TOKEN)
    marketplaceID = MARKETPLACES.get(MKTPLACE_CODE)
    if versao:
        response = slack_client.chat_postMessage(
            channel="sls-change-tracker",
            text=f"Há uma nova alteração no *{marketplaceID}*:\n"
            f"*<{url}|Nova versão da API!>*",
            )
    else:
        response = slack_client.chat_postMessage(
            channel="sls-change-tracker",
            text=f"Há uma nova alteração no *{marketplaceID}*:\n"
            f"*<{url}|{title}>*",
            )
    return response