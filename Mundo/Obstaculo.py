import sys as s
from pygame import *
from pygame.locals import *

class Obstaculo():
    PARED = -2
    PUAS = -1

    # constructor
    def __init__(self, ruta, X, Y, danio, sonido):

        self.imagen = image.load(ruta)  # imagen que representa el obstaculo
        self.rect = self.imagen.get_rect()  # rectangulo creado apartir de la iamgen del obstaculo
        self.valorDanio = danio  # daño que hace el obstaculo si daño vale -2 es una pared si es -1 es un chuzo
        self.valorDanioAux = danio
        self.rect.centerx = X  # centro en x del obstaculo
        self.rect.centery = Y  # centro en y del obstaculo
        self.sonido = mixer.Sound(sonido)  # cargar sonido


    # mueve el obstaculo dependiendo de la velocidad
    def mover(self, velocidad):
        self.rect.centerx -= velocidad

    # dibuja el obstaculo en la ventana
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

    # obtenemos el valor de año del obstaculo

    def getValorDanio(self):
        return self.valorDanio

    # poner daño en 0
    def sinDanio(self):
        self.valorDanioAux = self.valorDanio
        self.valorDanio = 0

    # restablecer danio
    def restablecerDanio(self):
        self.valorDanio = self.valorDanioAux
