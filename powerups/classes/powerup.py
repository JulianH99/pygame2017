import pygame


class PowerUp(pygame.sprite.Sprite):
    """
        La clase PowerUp representa las mejoras o fallas que puede experimentar la pelota
    """

    x_speed = -5

    def __init__(self, image, effect, limits):
        """
            picture(string) : ruta de la imagen del powerUp
            type(obj) : tipo del powerUp
        """

        self.effect = effect
        pygame.sprite.Sprite.__init__(self)
        self.y_limit = limits[1] - 200
        self.x_limit = limits[0] + 100          

        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_limit, self.y_limit)

        print "Hello from the powerup"

    def execute(self, ball):
        """
            Este metodo se encarga de ejecutar el efecto sobre la bola una vez que este es tocado
            por la bola
        :param ball: objeto de tipo Ball que es tocado por el powerUp
        :return:
        """
        self.effect.apply_over(ball)

    def disappear(self):
        """
            Este metodo se encarga de hacer desaparecer visualmente el powerUp cuando la pelota lo toca,
            ademas de moverlo fuera de la pantalla, puesto que a pesar de que desaparece visualmente,
            el objeto sigue en su ultima posicion
        :return:
        """
        self.kill()
        self.rect.center = (-100, -100)

    def update(self):
        self.rect.x += self.x_speed
