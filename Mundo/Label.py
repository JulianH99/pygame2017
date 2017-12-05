import pygame,sys
from pygame.locals import *

class Label:
    pygame.init()
    myfont = pygame.font.SysFont("Century gothic", 23)
    text = ""
    x = 0
    y = 0
    rgb = (239, 239, 239)

    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y
        #self.rgb = color
        pass
    def setText(self,text):
        self.text = text
        pass
    def getLabel(self):
        return self.myfont.render(self.text, 0 , self.rgb)

    def getPos(self):
        pos = (self.x, self.y)
        return pos