import pygame


class PowerUp(pygame.sprite.Sprite):
    """
        La clase PowerUp representa las mejoras o fallas que puede experimentar la pelota
    """

    __x_speed = -5

    def __init__(self, effect, limits):
        """
            picture(string) : ruta de la imagen del powerUp
            type(obj) : tipo del powerUp
        """

        self.__effect = effect
        pygame.sprite.Sprite.__init__(self)
        self.__y_limit = limits[1]
        self.__x_limit = limits[0]

        self.__image = pygame.image.load(effect.image).convert()
        self.__image.set_colorkey((255, 255, 255))
        self.__rect = self.__image.get_rect()
        self.__rect.center = (self.__x_limit, self.__y_limit)

    def execute(self, ball):
        """
            Este metodo se encarga de ejecutar el efecto sobre la bola una vez que este es tocado
            por la bola
        :param ball: objeto de tipo Ball que es tocado por el powerUp
        :return:
        """
        self.__effect.apply_over(ball)

    def disappear(self):
        """
            Este metodo se encarga de hacer desaparecer visualmente el powerUp cuando la pelota lo toca,
            ademas de moverlo fuera de la pantalla, puesto que a pesar de que desaparece visualmente,
            el objeto sigue en su ultima posicion
        :return:
        """
        self.kill()
        self.__rect.center = (-100, -100)

    def update(self):
        self.__rect.x += self.__x_speed

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

