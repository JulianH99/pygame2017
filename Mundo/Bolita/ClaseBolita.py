import pygame
import sys as s
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
        self.alto = posY
        self.piso =0

        self.velocidadVertical = [0, 0]
        self.saltoDoble = False


    def salto(self,ventana,velocidad):



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.saltoDoble:
                    if event.key == K_UP:
                        self.velocidadVertical[0] = 0
                        self.velocidadVertical[1] = -10
                    elif event.key == K_LEFT:
                        self.rectangulo.centerx -= velocidad
                    elif event.key == K_RIGHT:
                        self.rectangulo.centerx += velocidad


                else:
                    if self.rectangulo.centery==self.alto-self.rectangulo.width:

                        if event.key == K_UP:
                            self.velocidadVertical[0] = 0
                            self.velocidadVertical[1] = -10
                        elif event.key == K_LEFT:
                            self.rectangulo.centerx -= velocidad
                        elif event.key == K_RIGHT:
                            self.rectangulo.centerx += velocidad

                    else:
                        if event.key == K_LEFT:
                            self.rectangulo.centerx -= velocidad
                        elif event.key == K_RIGHT:
                            self.rectangulo.centerx += velocidad
            elif event.type == pygame.QUIT:
                pygame.quit()
                s.exit()





        self.velocidadVertical[0] = self.aceleGrave + self.velocidadVertical[1]
        self.rectangulo.centery += self.velocidadVertical[0]
        self.velocidadVertical[1] = self.velocidadVertical[0]

        if self.rectangulo.centery < self.piso:
            self.rectangulo.centery = self.piso
            velocidadVertical = [0, 0]
        if self.rectangulo.centery > (self.alto - self.imagenrect.bottom):
            self.rectangulo.centery = self.alto - self.imagenrect.bottom

        ventana.blit(self.imagen, (self.rectangulo.centerx, self.rectangulo.centery))

    def acumularPuntos(self, puntos):
        self.puntaje += puntos

    def obtenerPuntos(self):

        return self.puntaje

    def obtenerVida(self):

        return self.vida

    def modificarVida(self, cambioVida):
        self.vida += cambioVida

    def desplazamientoBolita(self, velocidad):
        pass

    def activarSaltoDoble(self, estado):
        self.saltoDoble=estado




    def obtenerRectangulo(self):
        return self.rectangulo

    def restriccionMovimiento(self):
        pass




