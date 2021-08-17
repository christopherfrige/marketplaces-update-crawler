# Rodar as funções de cada um dos marketplaces aqui

from marketplaces.amazon import amazon
from marketplaces.b2w import b2w
from marketplaces.magazine import magazine
from marketplaces.mercadolivre import mercadolivre
from marketplaces.viavarejo import viavarejo

def main():
    print("Procurando por alterações...")
    #Marketplaces que serão investigados
    amazon()
    b2w()
    magazine()
    mercadolivre()
    viavarejo()

main()