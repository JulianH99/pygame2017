from pygame import *
from ClaseBolita import *
import sys as s

def main():
    pygame.init()


    mibolita = Bolita(100, 0, 472, 300, 100)
    ventana = display.set_mode([mibolita.ancho,mibolita.alto])
    pygame.display.set_caption("Programa Bolita")
    blanco = (255, 255, 255)
    reloj = pygame.time.Clock()
    while True:
        reloj.tick(60)
        ventana.fill(blanco)


        mibolita.salto(ventana,5)
        mibolita.saltoDoble= True

        pygame.display.update()


main()

