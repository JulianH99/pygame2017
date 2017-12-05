
import pygame,sys
from pygame.locals import *

from Menu import Menu
pygame.init()
pygame.font.init()
size = width, height = 800, 500




def juego():

    #salir = True



    ventana = pygame.display.set_mode((100, 100))

    pygame.display.set_caption("Juego")

    while 'true':
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def creditos():
    print(" Funcion que muestra los creditos del programa.")


def salir():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)


if __name__ == '__main__':

    salir = False

    screen = pygame.display.set_mode(size)

    opciones = [
        ("Jugar", juego),
        ("Creditos", creditos),
        ("Salir", salir)
    ]



    fondo = pygame.image.load("fondo.jpg").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)
