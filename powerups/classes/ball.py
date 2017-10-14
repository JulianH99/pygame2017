import pygame


class Ball(pygame.sprite.Sprite):

    life_points = 100
    score = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        print "updating ball"
