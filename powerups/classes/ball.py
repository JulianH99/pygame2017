import pygame


class Ball(pygame.sprite.Sprite):

    __life_points = 100
    __score = 0
    __speed = 5

    def __init__(self, limit):
        self.__limit = limit
        self.__image = pygame.image.load('./img/ball.png').convert()
        self.__rect = self.__image.get_rect()
        self.__rect.center = (30, self.__limit - 20)
        self.__goes_up = True
        pygame.sprite.Sprite.__init__(self)

    def update(self):

        if self.__goes_up:
            if self.__rect.top >= 20:
                self.__rect.y -= self.__speed

            else:
                self.__goes_up = False
        else:
            if self.__rect.bottom <= self.__limit:
                self.__rect.y += self.__speed
            else:
                self.__goes_up = True

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def life_points(self):
        return self.__life_points

    @life_points.setter
    def life_points(self, value):
        self.__life_points = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


