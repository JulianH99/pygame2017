import sys as s
from pygame import *
from pygame.locals import *
from Obstaculo import *

class Laser(Obstaculo):

    def __init__(self, ruta, ruta2, X, Y, danio):
        super().__init__(ruta, X, Y, danio)
        self.horizontal = False  # laser horizontal o vertical
        self.activo = False  # activo o no
        self.ruta2 = ruta2
        self.ruta1 = ruta

    def activar(self, estado):
        self.activo = estado
        if self.activo:
            self.imagen = image.load(self.ruta2)
        else:
            self.imagen = image.load(self.ruta1)



