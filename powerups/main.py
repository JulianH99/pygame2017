import pygame
from pygame.locals import *
from classes.Powerup_generator import PowerupGenerator, POWERUP_INTERVAL
from classes.ball import Ball
from classes.effects import EFFECT_DURATION



# dimensiones de la ventana
WIDTH = 800
HEIGHT = 500

# evento para agregar un power_up a la pantalla cada x segundos
PUEVENT = pygame.USEREVENT + 1

pygame.time.set_timer(PUEVENT, POWERUP_INTERVAL)

# creacion del generador del powerup

powerup_generator = PowerupGenerator(WIDTH, HEIGHT)

# inicializar pygame
pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PowerUps")


# creacion de Sprites
ball = Ball(HEIGHT - 50)
power_up = None

# grupo de sprites
sprite_group = pygame.sprite.Group()
sprite_group.add(ball)

clock = pygame.time.Clock()

# configuracion para la duracion del efecto

effect_reset_ready = 0
dt = clock.tick()


def main():
    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == PUEVENT:
                global power_up
                power_up = powerup_generator.generate()
                sprite_group.add(power_up)


        # update sprites
        sprite_group.update()

        # pygame.set_interval(show_powerup, POWERUP_INTERVAL)
        if power_up is not None:
            if ball.rect.colliderect(power_up.rect):
                power_up.execute(ball)
                power_up.disappear()
                sprite_group.remove(power_up)
                print("Puntos de vida aumentados: {0}".format(ball.life_points))


        screen.fill((0, 0, 0))

        sprite_group.draw(screen)
    
        pygame.display.flip()


if __name__ == '__main__':
    main()
