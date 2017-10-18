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

        # elementos plataforma abajo
        self.plataforma = [image.load("Imagenes/plataforma.png"),image.load("Imagenes/plataforma.png")]
        self.rectPlataforma = [self.plataforma[0].get_rect(),self.plataforma[1].get_rect()]
        self.rectPlataforma[0].left = 0  # posicion izquierda del fondo
        self.rectPlataforma[0].bottom = alto  # posicion de arriba del fondo
        self.rectPlataforma[1].left = ancho  # posicion izquierda del fondo
        self.rectPlataforma[1].bottom = alto  # posicion de arriba del fondo

        # elementos plataforma arriba
        self.plataformaA = [image.load("Imagenes/plataforma.png"), image.load("Imagenes/plataforma.png")]
        self.rectPlataformaA = [self.plataformaA[0].get_rect(), self.plataformaA[1].get_rect()]
        self.rectPlataformaA[0].left = 0  # posicion izquierda del fondo
        self.rectPlataformaA[0].top = 0  # posicion de arriba del fondo
        self.rectPlataformaA[1].left = ancho  # posicion izquierda del fondo
        self.rectPlataformaA[1].top = 0  # posicion de arriba del fondo

        self.ventana = ventana  # ventan donde se colocara el escenario

    # generador aleatorio de obstaculos
    def generarObstaculos(self, puntaje, tiempo):
        self.tiempo = tiempo
        if tiempo%30 == 0:
           self.velocidad += 1
        rand = randint(0, 1000)
        arriba = randint(0,1)
        # genera lasers
        if rand % 250 == 0:
            laser = Laser("Imagenes/laserA.png","Imagenes/laserD.png",self.ancho, 311, 10)
            self.obstaculos.append(laser)
        # genera paredes
        elif rand < 80:
            for x in range(2):
                if arriba == 0:
                    posY = 40 + self.rectPlataformaA[0].height

                else:
                    posY = self.alto-40-self.rectPlataforma[0].height
            pared = Obstaculo("Imagenes/pared.png", self.ancho, posY, 10)
            self.obstaculos.append(pared)
        # genera chuzos
        elif 1<rand<50:
            for x in range(1):
                if arriAba == 0:
                    posY = 40 + self.rectPlataformaA[0].height

                else:
                    posY = self.alto-40-self.rectPlataforma[0].height
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

    # remover obstaculos fuera de area
    def removerObstaculo(self):
        for obstaculo in self.obstaculos:
            if obstaculo.rect.right<0:
                self.obstaculos.remove(obstaculo)

    # comprobacion de la colision de la bolita con algun obstaculo
    def colisionBolita(self, rect):

        i=rect.collidelis(self.obstaculos)
        return self.obstaculos[i].getValorDanio

    # dibujar fondo infinito
    def dibujarFondo(self, ventana):

        ventana.blit(self.fondo[0],self.rect[0])
        ventana.blit(self.fondo[1],self.rect[1])
        # plataformas
        ventana.blit(self.plataforma[0],self.rectPlataforma[0])
        ventana.blit(self.plataforma[1], self.rectPlataforma[1])
        ventana.blit(self.plataformaA[0], self.rectPlataformaA[0])
        ventana.blit(self.plataformaA[1], self.rectPlataformaA[1])


    # movimeinto del fondo
    def moverFondo(self):

        self.__restriccionFondo(self.rect)
        self.__restriccionPlataforma(self.rectPlataforma, self.rectPlataformaA)
        # fondo
        self.rect[0].left -= self.velocidadFondo
        self.rect[1].left -= self.velocidadFondo
        # plataformas
        self.rectPlataforma[1].left -= int(self.velocidad)
        self.rectPlataforma[0].left -= int(self.velocidad)
        self.rectPlataformaA[1].left -= int(self.velocidad)
        self.rectPlataformaA[0].left -= int(self.velocidad)


    # metodo para hacer movimientoinfinito fondo
    def __restriccionFondo(self, fondoRect):

        if fondoRect[0].left == -self.velocidadFondo:
            fondoRect[1].left = self.ancho-self.velocidadFondo
        elif fondoRect[1].left == -self.velocidadFondo:
            fondoRect[0].left = self.ancho-self.velocidadFondo

    # metodo para hacer movimientoinfinito pltaforma
    def __restriccionPlataforma(self, fondoRect, rect2):

       #print(fondoRect[0].right,"-",fondoRect[1].right)
        if fondoRect[0].right < 0:
            print("fondo 1")
            # plataforma abajo
            fondoRect[0].left = int(self.ancho - self.velocidad)
            fondoRect[1].right = fondoRect[0].left
            # plataforma arriba
            rect2[0].left = int(self.ancho - self.velocidad)
            rect2[1].right = rect2[0].left

        elif fondoRect[1].right < 0:
            print("fondo 2")
            # plataforma abajo
            fondoRect[1].left = int(self.ancho-self.velocidad)
            fondoRect[0].right = fondoRect[1].left
            # plataforma arriba
            rect2[1].left = int(self.ancho - self.velocidad)
            rect2[0].right = rect2[1].left













