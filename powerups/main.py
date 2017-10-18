import pygame


from classes.ball import Ball
from classes.powerup import PowerUp
from classes.effects import MoreLifeEffect, MoreScorePointsEffect

# dimensiones de la ventana
WIDTH = 800
HEIGHT = 500

# inicializar pygame
pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PowerUps")


# creacion de Sprites
ball = Ball(HEIGHT - 50)
power_up = PowerUp("./img/morescore.png", MoreScorePointsEffect(), (WIDTH, HEIGHT))

# grupo de sprites
sprite_group = pygame.sprite.Group()
sprite_group.add(ball)
sprite_group.add(power_up)

clock = pygame.time.Clock()


def main():
    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update sprites
        sprite_group.update()

        if ball.rect.colliderect(power_up.rect):
            power_up.execute(ball)
            power_up.disappear()
            print "Puntos de vida aumentados: {0}".format(ball.life_points)

        screen.fill((0, 0, 0))

        sprite_group.draw(screen)
    
        pygame.display.flip()


if __name__ == '__main__':
    main()
