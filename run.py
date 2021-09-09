# Rodar as funções de cada um dos marketplaces aqui

from marketplaces.amazon import amazon
from marketplaces.b2w import b2w
from marketplaces.magazine import magazine
from marketplaces.mercadolivre import mercadolivre
from marketplaces.viavarejo import viavarejo

def main(event, context):
    print("Procurando por alterações...")

    amazon()
    b2w()
    magazine()
    mercadolivre()
    viavarejo()

    print("Verificação finalizada!")

    return {
        "status_code": 200,
        "status": "OK"
    }


if __name__ == '__main__':
    main(None, None)