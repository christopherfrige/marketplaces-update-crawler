from slack_sdk import WebClient
from utilities.Tokens import SLACK_TOKEN
from utilities.GlobalVariables import MARKETPLACES

def enviaMensagem(mkt_code, title, url, descricao):
    slack_client = WebClient(SLACK_TOKEN)
    if descricao:
        slack_client.chat_postMessage(
            channel="atualizacoes", 
            text=f"Há uma nova alteração no *{MARKETPLACES.get(mkt_code)}*:\n"
            f"*<{url}|{title}>*\n"
            f"_{descricao}_"
            )
    else:
        slack_client.chat_postMessage(
            channel="atualizacoes", 
            text=f"Há uma nova alteração no *{MARKETPLACES.get(mkt_code)}*:\n"
            f"*<{url}|{title}>*"
            )


def enviaMensagemAlteracao(mkt_code, alteracao, url):
    slack_client = WebClient(SLACK_TOKEN)
    slack_client.chat_postMessage(
        channel="atualizacoes", 
        text=f"Há uma nova alteração no *{MARKETPLACES.get(mkt_code)}*:\n"
        f"*<{url}|{alteracao}>*"
        )
