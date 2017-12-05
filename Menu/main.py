
import pygame,sys
from pygame.locals import *

from Menu import Menu

def juego():
    pygame.font.init()

    size = width, height = 640, 400
    orientacion = top, buttom, left, right = 0, height, 0, width
    score = 0
    speed = [1, 1]
    ventana = pygame.display.set_mode(size)
    pygame.display.set_caption("Juego")
    # fondo y bolita
    ball = pygame.image.load("ball.png")
    ballrect = ball.get_rect()
    ballrect.left = left
    ballrect.top = top
    court = pygame.image.load("fondo.jpg")
    courtrect = court.get_rect()

    while 'true':
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        ballrect = ballrect.move(speed)

        if ballrect.top < top or ballrect.bottom > buttom:
            speed[1] = -speed[1]
        if ballrect.left < left or ballrect.right > right:
            speed[0] = -speed[0]

        ventana.blit(court, courtrect)
        ventana.blit(ball, ballrect)

def creditos():
    print ("Creditos")


def salir():
    import sys
    print (" se salio")
    sys.exit(0)


if __name__ == '__main__':
    salir = False
    opciones = [
        ("Jugar", juego),
        ("Creditos", creditos),
        ("Salir", salir)
    ]

    pygame.font.init()
    screen = pygame.display.set_mode((320, 240))
    fondo = pygame.image.load("fondo1.jpg").convert()
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
