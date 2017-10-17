import pygame,sys
import time
from random import randint
from pygame.locals import *



pygame.init()
pygame.display.set_caption("Programa Bolita")


class Bolita():
    def __init__(self, vidaInicial, posX, posY):
        self.vida = vidaInicial
        self.puntaje = 0
        self.imagen = pygame.image.load("Imagenes/bolita1.png")
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.centerx = posX
        self.rectangulo.centery = posY
        self.gravedad = True
        self.direccionMovimiento = True
        self.ventana = pygame.display.set_mode((800, 600))

    def salto(self, aumento):
        blanco = (255, 255, 255)
        velocidad = 180


        while True:
            self.ventana.fill(blanco)
            self.ventana.blit(self.imagen, (self.rectangulo.centerx, self.rectangulo.centery))
            self.Tiempo = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        self.rectangulo.centery -= velocidad + aumento

                        #self.rectangulo.centery += velocidad + aumento
                elif event.type == pygame.KEYUP:
                    if event.key == K_UP:
                        print("Tecla arriba presionada")
            pygame.display.update()

    def acumularPuntos(self, puntos):
        self.puntaje += puntos

    def obtenerPuntos(self):

        return self.puntaje

    def obtenerVida(self):

        return self.vida

    def modificarVida(self, cambioVida):
        self.vida += cambioVida

    def desplazamientoBolita(self, velocidad):


        blanco = (255, 255, 255)

        while True:
            self.ventana.fill(blanco)
            self.ventana.blit(self.imagen,(self.rectangulo.centerx, self.rectangulo.centery))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        self.rectangulo.centerx -= velocidad
                    elif event.key == K_RIGHT:
                        self.rectangulo.centerx += velocidad
                elif event.type == pygame.KEYUP:
                    if event.key == K_RIGHT:
                        print("Tecla derecha presionada")
                    elif event.key == K_LEFT:
                        print("Tecla izquierda presionada")
            pygame.display.update()

    def obtenerRectangulo(self):
        return self.rectangulo

    def restriccionMovimiento(self):
        pass


mibolita = Bolita(100,0,472)

mibolita.salto(0)
mibolita.desplazamientoBolita(5)

