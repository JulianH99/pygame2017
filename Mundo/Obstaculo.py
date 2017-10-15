import sys as s
from pygame import *
from pygame.locals import *

class Obstaculo():
    def __init__(self, ruta, X, Y, danio):
        self.imagen = image.load(ruta)
        self.rect = self.imagen.get_rect()  # rectangulo creado apartir de la iamgen del obstaculo
        self.valorDanio = danio  # daño que hace el obstaculo
        self.rect.centerx = X  # centro en x del obstaculo
        self.rect.centery = Y  # centro en y del obstaculo


    def mover(self, velocidad):
        self.rect.centerx -= velocidad


    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)