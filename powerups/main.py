import pygame
import os
from classes.ball import Ball
from classes.powerup import PowerUp 

# window dimensions
WIDTH = 500
HEIGHT = 500

# initialize pygame
pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PowerUps")


# sprites creation
ball = Ball()
power_up = PowerUp("", 5)

# sprite group
sprite_group = pygame.sprite.Group()

# adding sprites to group
sprite_group.add(ball)
sprite_group.add(power_up)


def main():
    running = True
    while running:

        # loo through events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill screen
        screen.fill((0, 0, 0))
    
        # update sprites
        sprite_group.update()

        # draw sprites
        #sprite_group.draw(screen)
    
    

if __name__ == '__main__':
    main()