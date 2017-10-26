import pygame
import sys as s
import time
from random import randint
from pygame.locals import *


class Bolita():
    def __init__(self, vidaInicial, posX, posY, ancho, alto, tamanoPlat):
        self.vida = vidaInicial
        self.puntaje = 0
        self.imagen = pygame.transform.scale(pygame.image.load('Imagenes/bolita1.png'), (70, 70))
        self.rectangulo = self.imagen.get_rect()
        self.imagenrect = self.imagen.get_rect()
        self.aceleGrave = 0.3
        self.rectangulo.left = posX
        self.rectangulo.centery = posY
        self.gravedad = True
        self.direccionMovimiento = True
        self.ancho = ancho
        self.alto = alto
        self.techo =0
        self.tamanoPlat = tamanoPlat
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


        self.restriccionMovimiento()



    def dibujarBolita(self,ventana):
        ventana.blit(self.imagen, (self.rectangulo.left, self.rectangulo.centery))

    def acumularPuntos(self, puntos):
        self.puntaje += puntos

    def obtenerPuntos(self):

        return self.puntaje

    def obtenerVida(self):

        return self.vida

    def modificarVida(self, cambioVida):
        self.vida += cambioVida


    def activarSaltoDoble(self, estado):
        self.saltoDoble=estado



    def obtenerRectangulo(self):
        return self.rectangulo

    def restriccionMovimiento(self):

        if self.rectangulo.centery < self.techo:
            self.rectangulo.centery = self.techo
            self.velocidadVertical = [0, 0]
        if self.rectangulo.centery > (self.alto - (self.imagenrect.height/2)-self.tamanoPlat+10):
            self.rectangulo.centery = self.alto - (self.imagenrect.height/2)-self.tamanoPlat+10

        if self.rectangulo.right > self.ancho:
            self.rectangulo.right = self.ancho

        if self.rectangulo.left < 0:
            self.rectangulo.left = 0

