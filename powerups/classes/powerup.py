import pygame


class PowerUp(pygame.sprite.Sprite):
    """
        PowerUp class represents the powers or damages  that the ball can suffer
    """
    def __init__(self, picture, type):
        """
            picture(string) : path to the image to put in the sprite
            type(obj) : type of the power up
        """
        pygame.sprite.Sprite.__init__(self)

        #self.picture = pygame.image.load(picture).convert()
        #self.picture.set_colorkey((0, 0, 0))
        #self.rect = self.picture.get_rect()

        print "Hello from the powerup"


    def update(self):
        print "updating power up"

    