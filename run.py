# Rodar as funções de cada um dos marketplaces aqui
# Definir um schedule pra rodar (diariamente ou semanalmente)

from marketplaces.amazon import amazon
from marketplaces.b2w import b2w
from marketplaces.magazine import magazine
from marketplaces.mercadolivre import mercadolivre
from marketplaces.viavarejo import viavarejo

def main():
    amazon()
    b2w()
    magazine()
    mercadolivre()
    viavarejo()

main()