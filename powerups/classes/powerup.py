import pygame


class PowerUp(pygame.sprite.Sprite):
    """
        La clase PowerUp representa las mejoras o fallas que puede experimentar la pelota
    """

    x_speed = -5

    def __init__(self, image, ptype, limits):
        """
            picture(string) : ruta de la imagen del powerUp
            type(obj) : tipo del powerUp
        """

        self.ptype = ptype
        pygame.sprite.Sprite.__init__(self)
        self.y_limit = limits[1] - 200
        self.x_limit = limits[0] + 100          

        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_limit, self.y_limit)

        print "Hello from the powerup"

    def getEffect(self, ball):
        if self.ptype == 1:
            self.applyEffect()

    def update(self):
        self.rect.x += self.x_speed