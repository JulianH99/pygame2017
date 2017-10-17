import sys as s
from pygame import *
from pygame.locals import *
from random import randint
from Obstaculo import *
from Laser import *


# clase escenrario
class Escenario():

    # constructor
    def __init__(self, velocidad,velocidadFondo, rutaFondo, orientacion, ventana, ancho, alto):
        # atributos
        self.ancho = ancho  # ancho de la ventana
        self.alto = alto  # alto de la ventana
        self.velocidadFondo = velocidadFondo  # velocidad del fondo
        self.velocidad = velocidad  # velocidad que tendra el escenario y sus obstaculos
        self.fondo = [image.load(rutaFondo),image.load(rutaFondo)]  # imagen del fondo del escenario
        self.orientacion = orientacion  # orientacion del escenario
        self.obstaculos = []  # lista de obstaculos que van apareciendo
        self.rect = [self.fondo[0].get_rect(),self.fondo[1].get_rect()]  # obtencion de un retcnagulo del fondo
        self.rect[0].left = 0  # posicion izquierda del fondo
        self.rect[0].top = 0  # posicion de arriba del fondo
        self.rect[1].left = ancho  # posicion izquierda del fondo
        self.rect[1].top = 0  # posicion de arriba del fondo
        self.ventana = ventana  # ventan donde se colocara el escenario

    # generador aleatorio de obstaculos
    def generarObstaculos(self, puntaje, tiempo):
        self.tiempo = tiempo
        rand = randint(0, 1000)
        arriAba = randint(0,1)
        # genera lasers
        if rand % 250 == 0:
            laser = Laser("Imagenes/laserA.png","Imagenes/laserD.png",self.ancho, 311, 10)
            self.obstaculos.append(laser)
        # genera paredes
        elif rand < 5:
            for x in range(2):
                if arriAba == 0:
                    posY = 40

                else:
                    posY = self.alto-40
            pared = Obstaculo("Imagenes/pared.png", self.ancho, posY, 10)
            self.obstaculos.append(pared)
        elif 1<rand<4:
            for x in range(1):
                if arriAba == 0:
                    posY = 40

                else:
                    posY = self.alto-40
            chuzo = Obstaculo("Imagenes/pared.png", self.ancho, posY, 10)
            self.obstaculos.append(pared)


    # movimiento de los obstaculos
    def movimientoObstaculos(self):
        for obstaculo in self.obstaculos:
            if type(obstaculo) is Laser:
                if self.tiempo%3 == 0:
                    obstaculo.activar(True)
                else:
                    obstaculo.activar(False)

            obstaculo.mover(self.velocidad)
            obstaculo.dibujar(self.ventana)

    # restriccion obstaculos pantalla
    def restriccionObstaculo(self, rectObs):
        pass


    # comprobacion de la colision de la bolita con algun obstaculo
    def colisionBolita(self, rect):
        i=rect.collidelis(self.obstaculos)
        return self.obstaculos[i].getValorDanio

    # dibujar fondo infinito
    def dibujarFondo(self, ventana):
        ventana.blit(self.fondo[0],self.rect[0])
        ventana.blit(self.fondo[1],self.rect[1])

    # movimeinto del fondo
    def moverFondo(self):
        self.__restriccionFondo(self.rect)
        self.rect[0].left -= self.velocidadFondo
        self.rect[1].left -= self.velocidadFondo

    # metodo para hacer movimientoinfinito fondo
    def __restriccionFondo(self, fondoRect):
        print(fondoRect[0].left,"-",fondoRect[1].left)
        if fondoRect[0].left == -self.velocidadFondo:
            print("fondo 1")
            fondoRect[1].left = self.ancho-self.velocidadFondo
        elif fondoRect[1].left == -self.velocidadFondo:
            print("fondo 2")
            fondoRect[0].left = self.ancho-self.velocidadFondo














