import pygame,sys
import time
from random import randint
from pygame.locals import *


class Bolita():
    def __init__(self, vidaInicial, posX, posY):
        self.vida = vidaInicial
        self.puntaje = 0
        self.imagen = pygame.transform.scale(pygame.image.load('Imagenes/bolita1.png'), (70, 70))
        self.rectangulo = self.imagen.get_rect()
        self.imagenrect = self.imagen.get_rect()
        self.aceleGrave = 0.3
        self.rectangulo.centerx = posX
        self.rectangulo.centery = posY
        self.gravedad = True
        self.direccionMovimiento = True
        self.ancho = 800
        self.alto = 600
        self.ventana = pygame.display.set_mode((self.ancho, self.alto),0,32)

    def salto(self):
        velocidadVertical = [0, 0]
        clock = pygame.time.Clock()
        blanco = (255, 255, 255)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        velocidadVertical[0] = 0
                        velocidadVertical[1] = -10

            velocidadVertical[0] = self.aceleGrave + velocidadVertical[1]
            self.rectangulo.centery += velocidadVertical[0]
            velocidadVertical[1] = velocidadVertical[0]

            if self.rectangulo.centery < 0:
                self.rectangulo.centery = 0
                velocidadVertical = [0, 0]
            if self.rectangulo.centery > (self.alto - self.imagenrect.bottom):
                self.rectangulo.centery = self.alto - self.imagenrect.bottom


            clock.tick(60)
            self.ventana.fill(blanco)
            self.ventana.blit(self.imagen, (self.rectangulo.centerx, self.rectangulo.centery))
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




