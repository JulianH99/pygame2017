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


    def salto(self,velocidad,tecla):
        if self.saltoDoble:
            if tecla == K_UP:
                self.velocidadVertical[0] = 0
                self.velocidadVertical[1] = -10
            elif tecla == K_LEFT:
                self.rectangulo.centerx -= velocidad
            elif tecla == K_RIGHT:
                self.rectangulo.centerx += velocidad


        else:
            if self.rectangulo.centery == self.alto - self.rectangulo.width:
                if tecla == K_UP:
                    self.velocidadVertical[0] = 0
                    self.velocidadVertical[1] = -10
                elif tecla == K_LEFT:
                    self.rectangulo.centerx -= velocidad
                elif tecla == K_RIGHT:
                    self.rectangulo.centerx += velocidad

            else:
                if tecla == K_LEFT:
                    self.rectangulo.centerx -= velocidad
                elif tecla == K_RIGHT:
                    self.rectangulo.centerx += velocidad







        self.velocidadVertical[0] = self.aceleGrave + self.velocidadVertical[1]
        self.rectangulo.centery += self.velocidadVertical[0]
        self.velocidadVertical[1] = self.velocidadVertical[0]

        if self.rectangulo.centery < self.piso:
            self.rectangulo.centery = self.piso
            self.velocidadVertical = [0, 0]
        if self.rectangulo.centery > (self.alto - self.imagenrect.bottom):
            self.rectangulo.centery = self.alto - self.imagenrect.bottom



    def dibujarBolita(self,ventana):
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





