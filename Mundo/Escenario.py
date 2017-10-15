import sys as s
from pygame import *
from pygame.locals import *
from random import randint
from Obstaculo import *
from Laser import *


# clase escenrario
class Escenario():

    # constructor
    def __init__(self, velocidad, ruta, orientacion, ventana):
        # atributos
        self.velocidad = velocidad
        self.fondo = image.load(ruta)
        self.orientacion = orientacion
        self.obstaculos = []
        self.rect = self.fondo.get_rect()
        self.ventana = ventana

    def generarObstaculos(self, puntaje, tiempo):
        self.tiempo = tiempo
        rand = randint(0, 1000)
        arriAba = randint(0,1)
        if rand % 250 == 0:
            laser = Laser("Imagenes/laserA.png","Imagenes/laserA.png",self.rect.width, 311, 10)
            self.obstaculos.append(laser)
        elif rand < 5:
            for x in range(2):
                if arriAba == 0:
                    posY = 40

                else:
                    posY = self.rect.height-40
            pared = Obstaculo("Imagenes/pared.png", self.rect.width, posY, 10)
            self.obstaculos.append(pared)








    def movimientoObstaculos(self):
        for obstaculo in self.obstaculos:
            if type(obstaculo) is Laser:
                if self.tiempo%5 == 0:
                    print("ntr")
                    obstaculo.activar(False)
                else:
                    obstaculo.activar(True)

            obstaculo.mover(self.velocidad)
            obstaculo.dibujar(self.ventana)






