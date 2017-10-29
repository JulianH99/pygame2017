import sys as s
from math import floor
from pygame import *
from pygame.locals import *
from random import randint
from Obstaculo import *
from Laser import *







# clase escenrario
class Escenario():
    # constantes
    ORIENT_IZQ_DER = 0
    ORIENT_DER_IZQ = 1
    ORIENT_G_NOR = 2
    ORIENT_G_INVER = 3
    FONDOS={'NORMAL': image.load("Imagenes/fondoMovil1.png"),
            'OBSTACULO': image.load("Imagenes/fondoObstaculo.png"),
            'POWERUP_BUENO': image.load("Imagenes/fondoPowerupBueno.png"),
            'POWERUP_MALO': image.load("Imagenes/fondoPowerupMalo.png"),
            'AUMENTO_VELOCIDAD': image.load("Imagenes/fondoVelocidad.png"),
            'PUNTAJE': image.load("Imagenes/fondoPuntaje.png")
            }

    # constructor
    def __init__(self, velocidad,velocidadFondo, orientacion, ventana, ancho, alto):
        # atributos
        self.ancho = ancho  # ancho de la ventana
        self.alto = alto  # alto de la ventana
        self.velocidadFondo = velocidadFondo  # velocidad del fondo
        self.velocidad = velocidad  # velocidad que tendra el escenario y sus obstaculos
        self.dirVel = 1 # direccion de la velocidad
        self.fondo = [self.FONDOS['NORMAL'],self.FONDOS['NORMAL']]  # imagen del fondo del escenario
        self.orientacion = orientacion  # orientacion del escenario
        self.obstaculos = []  # lista de obstaculos que van apareciendo
        self.rect = [self.fondo[0].get_rect(),self.fondo[1].get_rect()]  # obtencion de un retcnagulo del fondo
        self.rect[0].left = 0  # posicion izquierda del fondo
        self.rect[0].top = 0  # posicion de arriba del fondo
        self.rect[1].left = ancho  # posicion izquierda del fondo
        self.rect[1].top = 0  # posicion de arriba del fondo

        # elementos plataforma abajo
        self.plataforma = [image.load("Imagenes/plataformaA.png"),image.load("Imagenes/plataformaA.png")]
        self.rectPlataforma = [self.plataforma[0].get_rect(),self.plataforma[1].get_rect()]
        self.rectPlataforma[0].left = 0  # posicion izquierda de la plataforma
        self.rectPlataforma[0].bottom = alto-50  # posicion de arriba de la plataforma
        self.rectPlataforma[1].left = ancho  # posicion izquierda de la plataforma
        self.rectPlataforma[1].bottom = alto-50 # posicion de arriba de la plataforma

        # elementos plataforma arriba
        self.plataformaA = [image.load("Imagenes/plataforma.png"), image.load("Imagenes/plataforma.png")]
        self.rectPlataformaA = [self.plataformaA[0].get_rect(), self.plataformaA[1].get_rect()]
        self.rectPlataformaA[0].left = 0  # posicion izquierda del plataforma
        self.rectPlataformaA[0].top = 0  # posicion de arriba de la plataforma
        self.rectPlataformaA[1].left = ancho # posicion izquierda de la plataforma
        self.rectPlataformaA[1].top = 0  # posicion de arriba de la plataforma
        self.posX = 0  # posicion donde comienza a crerarse los obstaculos
        self.ventana = ventana  # ventan donde se colocara el escenario

        self.__aux1= 0
        self.__aux2 = 0
        self.__auxTiempoFondo = 0
        self.__cont=0

    # generador aleatorio de obstaculos
    def generarObstaculos(self, puntaje, tiempo):

        #self.cambiarFondo(self.FONDOS['NORMAL'])
        self.tiempo = tiempo

        self.__cambiarOrientacion()

        # velocidad varia cada 30 segundos
        if tiempo != self.__aux1 and tiempo % 300 == 0:
            self.__aux1 = tiempo
            self.velocidad += (self.dirVel*self.dirVel)
            trueno=mixer.Sound("Sonidos/rayo.wav")
            trueno.play()
            self.cambiarFondo(self.FONDOS['AUMENTO_VELOCIDAD'])


        r = randint(20,70)

        if tiempo!=self.__aux2 and tiempo % r  == 0:
            self.__aux2 = tiempo
            listObstaculos=[]
            o = randint(0,2)
            arriba = randint(0, 1)
            # creacion laser
            laser = Laser("Imagenes/laserA.png", "Imagenes/laserD.png", self.posX, 311, -10, "Sonidos/laser.wav")
            listObstaculos.append(laser)
            # creacion muro
            if arriba == 0:
                posY = 40 + self.rectPlataformaA[0].height

            else:
                posY = self.alto - 40 - self.rectPlataforma[0].height
            pared = Obstaculo("Imagenes/pared.png",self.posX, posY, Obstaculo.PARED, "Sonidos/pared.wav")
            listObstaculos.append(pared)
            # creacion puas
            if arriba == 0:
                posY = 40 + self.rectPlataformaA[0].height

            else:
                posY = self.alto - 40 - self.rectPlataforma[0].height
            puas = Obstaculo("Imagenes/pared.png", self.posX, posY, Obstaculo.PUAS,"Sonidos/shoot.wav")
            listObstaculos.append(pared)

            if self.__verificiacionObstaculos(listObstaculos[o]):
                self.obstaculos.append(listObstaculos[o])



                """self.obstaculos[len(self.obstaculos) - 1].rect.left -= 20
                self.obstaculos.append(listObstaculos[o])
                print("Entra 2")"""




        """
        if tiempo!=self.__aux2 and tiempo % (20 - self.cantidad) == 0:
            self.__aux2 = tiempo
            rand = randint(0, 1000)
            arriba = randint(0,1)
            # genera lasers
            if rand % 10 == 0:
                laser = Laser("Imagenes/laserA.png","Imagenes/laserD.png",self.ancho, 311, 10)
                self.obstaculos.append(laser)
            # genera paredes
            elif rand < 1000:
                for x in range(5):
                    if arriba == 0:
                        posY = 40 + self.rectPlataformaA[0].height

                    else:
                        posY = self.alto-40-self.rectPlataforma[0].height
                pared = Obstaculo("Imagenes/pared.png", self.ancho, posY, 10)
                self.obstaculos.append(pared)
            # genera chuzos
            elif 1<rand<50:
                for x in range(3):
                    if arriAba == 0:
                        posY = 40 + self.rectPlataformaA[0].height

                    else:
                        posY = self.alto-40-self.rectPlataforma[0].height
                chuzo = Obstaculo("Imagenes/pared.png", self.ancho, posY, 10)
                self.obstaculos.append(pared)
        """


    # verficacion espacio entrew obstaculos
    def __verificiacionObstaculos(self, obstaculo):

        if int(len(self.obstaculos))==0:
            #print(len(self.obstaculos))
            return True
        else:

            ultimoObstaculo = self.obstaculos[len(self.obstaculos)-1]


            if ultimoObstaculo.rect.top==self.obstaculos[len(self.obstaculos)-1].rect.top and (ultimoObstaculo.rect.left<=obstaculo.rect.left<=ultimoObstaculo.rect.right or ultimoObstaculo.rect.left<=obstaculo.rect.right<=ultimoObstaculo.rect.right):
                #print("entra 2")
                return False
            else:
                return True






    # movimiento de los obstaculos
    def movimientoObstaculos(self):
        # veriificaion orientacion movimeinto
        self.__cambiarOrientacion()

        for obstaculo in self.obstaculos:
            if type(obstaculo) is Laser:
                if self.tiempo%15 == 0:
                    obstaculo.activar(True)

                elif self.tiempo%3 == 0:
                    obstaculo.activar(False)

            obstaculo.mover(self.velocidad*self.dirVel)
            obstaculo.dibujar(self.ventana)

    # remover obstaculos fuera de area
    def removerObstaculo(self):
        if self.ORIENT_IZQ_DER==self.orientacion:
            for obstaculo in self.obstaculos:
                if obstaculo.rect.left > self.ancho:
                    self.obstaculos.remove(obstaculo)
        else:
            for obstaculo in self.obstaculos:
                if obstaculo.rect.right<0:
                    self.obstaculos.remove(obstaculo)

    # comprobacion de la colision de la bolita con algun obstaculo
    def colisionBolita(self, rect):
        if rect.collidelist(self.obstaculos)!=-1:
            i = rect.collidelist(self.obstaculos)
            if type(self.obstaculos[i]) is not Laser:
                self.cambiarFondo(self.FONDOS['OBSTACULO'])


            if type(self.obstaculos[i]) is Laser:
                if self.obstaculos[i].activo:
                    self.cambiarFondo(self.FONDOS['OBSTACULO'])

                    self.obstaculos[i].sonido.play()

                    return self.obstaculos[i].getValorDanio()
                else:
                    self.cambiarFondo(self.FONDOS['NORMAL'])
                    return 0

            else:
                if self.__cont < 1:
                    self.obstaculos[i].sonido.play()
                    self.__cont += 1
                return self.obstaculos[i].getValorDanio()
        else:
            self.cambiarFondo(self.FONDOS['NORMAL'])
            self.__cont=0

        return 0

    # dibujar fondo infinito
    def dibujarFondo(self, ventana):

        ventana.blit(self.fondo[0],self.rect[0])
        ventana.blit(self.fondo[1],self.rect[1])
        # plataformas
        ventana.blit(self.plataforma[0],self.rectPlataforma[0])
        ventana.blit(self.plataforma[1], self.rectPlataforma[1])
        #ventana.blit(self.plataformaA[0], self.rectPlataformaA[0])
        #ventana.blit(self.plataformaA[1], self.rectPlataformaA[1])


    # movimeinto del fondo
    def moverFondo(self):

        self.__cambiarOrientacion()
        self.__restriccionFondo(self.rect)
        self.__restriccionPlataforma(self.rectPlataforma, self.rectPlataformaA)

        # fondo
        self.rect[0].left -= (self.velocidadFondo*self.dirVel)
        self.rect[1].left -= (self.velocidadFondo*self.dirVel)

        # plataformas
        self.rectPlataforma[1].left -= int(self.velocidad*self.dirVel)
        self.rectPlataforma[0].left -= int(self.velocidad*self.dirVel)
        self.rectPlataformaA[1].left -= int(self.velocidad*self.dirVel)
        self.rectPlataformaA[0].left -= int(self.velocidad*self.dirVel)



    # metodo para hacer movimientoinfinito fondo
    def __restriccionFondo(self, fondoRect):
        # verificacion oreintacion
        if self.ORIENT_IZQ_DER == self.orientacion:
            if fondoRect[0].right == self.ancho :
                fondoRect[1].right = self.velocidadFondo
            elif fondoRect[1].right == self.ancho:
                fondoRect[0].right = self.velocidadFondo
        else:
            if fondoRect[0].left == -self.velocidadFondo:
                fondoRect[1].left = self.ancho - self.velocidadFondo
            elif fondoRect[1].left == -self.velocidadFondo:
                fondoRect[0].left = self.ancho - self.velocidadFondo



    # metodo para hacer movimientoinfinito pltaforma
    def __restriccionPlataforma(self, fondoRect, rect2):

       # verificacion oreintacion
       if self.ORIENT_IZQ_DER == self.orientacion:
            if fondoRect[0].left > self.ancho:

                # plataforma abajo
                fondoRect[0].right = 0
                fondoRect[1].left = fondoRect[0].right
                # plataforma arriba
                rect2[0].right = 0
                rect2[1].left = rect2[0].right


            elif fondoRect[1].left > self.ancho:
                # plataforma abajo
                fondoRect[1].right = 0
                fondoRect[0].left = fondoRect[1].right
                # plataforma arriba
                rect2[1].left = int(self.ancho - (self.velocidad*self.dirVel))
                rect2[0].right = rect2[1].left
                rect2[1].right = 0
                rect2[0].left = rect2[1].right

       else:
           if fondoRect[0].right < 0:

               # plataforma abajo
               fondoRect[0].left = int(self.ancho - (self.velocidad * self.dirVel))
               fondoRect[1].right = fondoRect[0].left
               # plataforma arriba
               rect2[0].left = int(self.ancho - (self.velocidad * self.dirVel))
               rect2[1].right = rect2[0].left


           elif fondoRect[1].right < 0:
               # plataforma abajo
               fondoRect[1].left = int(self.ancho - (self.velocidad * self.dirVel))
               fondoRect[0].right = fondoRect[1].left
               # plataforma arriba
               rect2[1].left = int(self.ancho - (self.velocidad * self.dirVel))
               rect2[0].right = rect2[1].left


    # cambair orientacion movimiento
    def __cambiarOrientacion(self):
        if self.orientacion == self.ORIENT_IZQ_DER:
            self.dirVel = -1
            self.posX=0

        else:
            self.dirVel = 1
            self.posX = self.ancho

    # cambiar fondo
    def cambiarFondo(self,fondo):
        self.fondo[0]=fondo
        self.fondo[1]=fondo





    # colocar danio en 0
    def sinDanio(self):
        for obstaculo in self.obstaculos:
            self.obstaculos.sinDanio()

    # restablecer danio
    def restablecerDanio(self):
        for obstaculo in self.obstaculos:
            self.obstaculos.restablecerDanio()

    # obtener valor velocidad
    def getVelocidad(self):
        return self.velocidad

    # colocar valor velocidad
    def setVeolcidad(self, velocidad):
        self.velocidad = velocidad

    # obtenerOrientacion
    def getOrientacion(self):
        return self.velocidad

    # colocarOrientacion
    def setOrientacion(self, orientacion):
        self.orientacion = orientacion












