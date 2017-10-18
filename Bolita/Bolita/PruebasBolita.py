from pygame import *
from Bolita import *
from pygame.locals import *
import pygame,sys

def main():
    pygame.init()
    pygame.display.set_caption("Programa Bolita")

mibolita = Bolita(100,0,472)

mibolita.salto(0)
mibolita.desplazamientoBolita(5)
