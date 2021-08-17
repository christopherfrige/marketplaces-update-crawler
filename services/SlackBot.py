from slack_sdk import WebClient
from utilities.GlobalVariables import MARKETPLACES, SLACK_TOKEN

def enviaMensagem(MKTPLACE_CODE, title, url, descricao):
    slack_client = WebClient(SLACK_TOKEN)
    if descricao:
        slack_client.chat_postMessage(
            channel="atualizacoes", 
            text=f"Há uma nova alteração no *{MARKETPLACES.get(MKTPLACE_CODE)}*:\n"
            f"*<{url}|{title}>*\n"
            f"_{descricao}_"
            )
    else:
        slack_client.chat_postMessage(
            channel="atualizacoes", 
            text=f"Há uma nova alteração no *{MARKETPLACES.get(MKTPLACE_CODE)}*:\n"
            f"*<{url}|{title}>*"
            )


def enviaMensagemAlteracao(MKTPLACE_CODE, alteracao, url):
    slack_client = WebClient(SLACK_TOKEN)
    slack_client.chat_postMessage(
        channel="atualizacoes", 
        text=f"Há uma nova alteração no *{MARKETPLACES.get(MKTPLACE_CODE)}*:\n"
        f"*<{url}|{alteracao}>*"
        )
