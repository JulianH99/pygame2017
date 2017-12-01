import pygame
import sys as s
import time
from random import randint
from pygame.locals import *
from Obstaculo import *

#Clase Bolita
class Bolita():
    #Metodo Constructor
    def __init__(self, vidaInicial, posX, posY, ancho, alto, tamanoPlatPiso, techo):
        self.vida = vidaInicial
        self.puntaje = 0
        self.imagen = pygame.transform.scale(pygame.image.load('Imagenes/bolita1.png'), (70, 70))
        self.rectangulo = self.imagen.get_rect()
        self.imagenrect = self.imagen.get_rect()
        self.aceleGrave = 0.3
        self.rectangulo.left = posX
        self.rectangulo.centery = posY
        self.gravedad = True
        self.ancho = ancho
        self.alto = alto
        self.techo = techo
        self.tamanoPlatPiso = tamanoPlatPiso
        self.velocidadVertical = [0, 0]
        self.vivoMuerto = True
        self.saltoDoble = False
        self.invertirDireccion = False
        self.saltos =0
        self.cont=0
        self.cont2=0
        self.cont3=0
        self.cont4=0
        self.cont5=0
    #Metodo para el salto de la bolita, incluyendo el doble y el desplazamiento
    def salto(self,velocidad,tecla,estado):

        if self.gravedad:

            self.aceleGrave = 0.3
            if self.cont4<1:
                self.rectangulo.centery = self.alto - (self.imagenrect.height / 2) - self.tamanoPlatPiso + 10 - .5
                print("entra a piso")
                self.cont4+=1
            signo = 1
            self.cont3=0
            self.cont5=0
            #self.velocidadVertical[1]=0

        else:

            self.aceleGrave = -0.3
            signo = -1
            if self.cont3<1:
                self.rectangulo.top = self.techo
                print("-------------------------------------------------------")

                self.cont3+=1
            self.cont4=0




        # Algoritmo salto doble
        if self.saltoDoble:

            if self.saltos<1:
                if tecla == K_UP:
                    self.velocidadVertical[0] = 0
                    self.velocidadVertical[1] = (-10) *signo
                    self.saltos = self.saltos + 1

            if (self.rectangulo.centery == self.alto - (self.imagenrect.height / 2) - self.tamanoPlatPiso + 10 - .5) and self.gravedad:

                self.saltos = 0

            elif (self.rectangulo.centery==self.techo) and (self.gravedad==False):

                self.saltos = 0

            if estado==False:
                self.__movHorizontal(velocidad, tecla)

        # Algoritmo salto simple
        else:


            if self.rectangulo.centery == self.alto - (self.imagenrect.height / 2) - self.tamanoPlatPiso + 10 - .5 and self.gravedad:
                if tecla == K_UP:
                    self.velocidadVertical[0] = 0
                    self.velocidadVertical[1] = (-10)*signo
                if estado == False:
                    self.__movHorizontal(velocidad, tecla)

            if self.rectangulo.centery == self.techo and self.gravedad==False:
                if tecla == K_UP:
                    self.velocidadVertical[0] = 0
                    self.velocidadVertical[1] = (-10)*signo
                if estado == False:
                    self.__movHorizontal(velocidad, tecla)


            if estado==False:
                self.__movHorizontal(velocidad, tecla)



        if self.gravedad==False and self.cont5<1:
            self.velocidadVertical[1] = 0
            self.cont5+=1




        self.velocidadVertical[0] = self.aceleGrave + self.velocidadVertical[1]

        self.rectangulo.centery += (self.velocidadVertical[0])
        #print(self.rectangulo.centery,"---",self.velocidadVertical[1])
        self.velocidadVertical[1] = self.velocidadVertical[0]


        #Ubica la bolita deacuerdo a si se invierte la direccion o no
        if self.invertirDireccion and self.cont<1:
            self.rectangulo.left=self.ancho
            self.cont+=1
            cont2=0
        elif self.invertirDireccion==False and self.cont2<1:
            self.rectangulo.left=0
            self.cont2+=1
            cont=0

        self.restriccionMovimiento()



    #Metodo para dibujar la bolita
    def dibujarBolita(self,ventana):
        ventana.blit(self.imagen, (self.rectangulo.left, self.rectangulo.centery))


    #Se van guardando los puntos de la bolita
    def acumularPuntos(self, puntos):
        self.puntaje += puntos


    #Se obtiene el puntaje de la bolita
    def obtenerPuntos(self):
        return self.puntaje


    #Se obtiene la vida de la bolita
    def obtenerVida(self):
        return self.vida




    #Se modifica la vida de la bolita según los obstáculos y powerUps
    #Se determina si la bolita tiene vida o no
    def modificarVida(self, cambioVida,escenario):
        estado=False
        signo=-1

        if escenario.getOrientacion()==escenario.ORIENT_DER_IZQ:
            signo=1



        if cambioVida==Obstaculo.PARED:

            self.rectangulo.centerx -=escenario.velocidad*signo
            estado=True
        elif cambioVida==Obstaculo.PUAS:
            self.rectangulo.centerx -=escenario.velocidad*signo
            self.vida += cambioVida
            estado=True
        else:
            self.vida += cambioVida
            estado=False
        print("Vida Actual: ",self.vida)

        if self.vida>0:
            self.vivoMuerto=True
        else:
            self.vivoMuerto=False


        return estado



    #Metodo para el doble salto
    def activarSaltoDoble(self, estado):
        self.saltoDoble=estado


    #Metodo para invertir dirección
    def invertirDireccion(self,estado):
        self.invertirDireccion = estado

    #Metodo para invertir gravedad
    def invertirGravedad(self):
        self.gravedad = not self.gravedad


    #Metodo para obtener el rectangulo
    def obtenerRectangulo(self):
        return self.rectangulo


    #Se restringe el movimiento que debe hacer la bolita
    def restriccionMovimiento(self):

        if self.rectangulo.centery < self.techo:
            self.rectangulo.centery = self.techo
            self.velocidadVertical = [0, 0]
        if self.rectangulo.centery > (self.alto - (self.imagenrect.height/2)-self.tamanoPlatPiso+10):
            self.rectangulo.centery = self.alto - (self.imagenrect.height/2)-self.tamanoPlatPiso+10

        if self.rectangulo.right > self.ancho:
            self.rectangulo.right = self.ancho

        if self.rectangulo.left < 0:
            self.rectangulo.left = 0
    def __movHorizontal(self,velocidad,tecla):
        if tecla == K_LEFT:
            self.rectangulo.centerx -= velocidad
        elif tecla == K_RIGHT:
            self.rectangulo.centerx += velocidad
    def getVivoMuerto(self):
        return self.vivoMuerto


