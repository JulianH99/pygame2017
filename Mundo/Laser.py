import sys as s
from pygame import *
from pygame.locals import *
from Obstaculo import *


# clase laser hereda de la calse obstaculo
class Laser(Obstaculo):

    # constructor
    def __init__(self, ruta, ruta2, X, Y, danio):
        super().__init__(ruta, X, Y, danio) # paso de valores para los atributos de la superclase
        self.horizontal = False  # laser horizontal o vertical
        self.activo = False  # activo o no
        self.ruta2 = ruta2  # ruta de la imagen del laser apagado
        self.ruta1 = ruta  # ruta de la imagen del laser encendido

    # activacion o desactivacion del laser
    def activar(self, estado):
        self.activo = estado
        if self.activo:
            self.imagen = image.load(self.ruta2)
        else:
            self.imagen = image.load(self.ruta1)




