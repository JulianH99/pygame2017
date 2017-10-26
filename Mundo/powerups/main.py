from modules.powerup_generator import PowerupGenerator, POWERUP_INTERVAL
from modules.ball import Ball
from modules.effects import EFFECT_EVENT
import pygame

import time as deftime

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
effect_triggered = False


def main():
    running = True
    dt = clock.tick() # provisional
    while running:
        clock.tick(30)
        for event in pygame.event. get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == PUEVENT:
                global power_up
                power_up = powerup_generator.generate()
                sprite_group.add(power_up)
            if event.type == EFFECT_EVENT:
                print("Effect activated")
                power_up.effect.triggered = True

        # update sprites
        sprite_group.update()

        if power_up is not None:
            power_up.check_collide(ball)

            if power_up.effect.triggered:
                power_up.effect.start_reset_countdown(ball, dt)

        screen.fill((0, 0, 0))

        sprite_group.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
