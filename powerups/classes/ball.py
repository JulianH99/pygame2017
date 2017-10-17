import pygame


class Ball(pygame.sprite.Sprite):

    life_points = 100
    score = 0
    speed = 5

    def __init__(self, limit):
        self.limit = limit
        self.image = pygame.image.load('./img/ball.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (30, self.limit - 20)
        self.goes_up = True
        pygame.sprite.Sprite.__init__(self)

    def update(self):

        if self.goes_up:
            if self.rect.top >= 20:
                self.rect.y -= self.speed

            else:
                self.goes_up = False
        else:
            if self.rect.bottom <= self.limit:
                self.rect.y += self.speed
            else:
                self.goes_up = True


