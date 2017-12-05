import pygame
from pygame.locals import *


class Menu:

    def __init__(self, opciones):
        self.opciones = opciones
        self.font = pygame.font.SysFont("Century gothic", 40)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False
        self.app_name = "Ball run"

    def actualizar(self):

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                titulo, funcion = self.opciones[self.seleccionado]
                funcion()

        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

    def imprimir(self, screen):

        total = self.total
        indice = 0
        altura_de_opcion = 50
        x = 105
        y = 105

        app_title = self.font.render(self.app_name, 1, (232, 232, 232))
        screen.blit(app_title, (50, 20))

        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (133, 63, 255)
            else:
                color = (255, 255, 255)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)