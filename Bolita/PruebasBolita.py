from pygame import *
from Bolita.ClaseBolita import *

def main():
    pygame.init()
    pygame.display.set_caption("Programa Bolita")

mibolita = Bolita(100,0,472)

mibolita.salto()
#mibolita.desplazamientoBolita(5)
