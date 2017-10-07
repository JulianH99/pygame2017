import pygame


class PowerUp(pygame.sprite.Sprite):
    """
        La clase PowerUp representa las mejoras o fallas que puede experimentar la pelota
    """
    def __init__(self, picture, type):
        """
            picture(string) : ruta de la imagen del powerUp
            type(obj) : tipo del powerUp
        """
        pygame.sprite.Sprite.__init__(self)

        #self.picture = pygame.image.load(picture).convert()
        #self.picture.set_colorkey((0, 0, 0))
        #self.rect = self.picture.get_rect()

        print "Hello from the powerup"


    def update(self):
        print "updating power up"

    