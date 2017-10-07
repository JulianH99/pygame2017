import pygame
import os
from classes.ball import Ball
from classes.powerup import PowerUp 

# dimensiones de la ventana
WIDTH = 500
HEIGHT = 500

# inicializar pygame
pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PowerUps")


# creación de Sprites
ball = Ball()
power_up = PowerUp("", 5)

# grupo de sprites
sprite_group = pygame.sprite.Group()
sprite_group.add(ball)
sprite_group.add(power_up)


def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        screen.fill((0, 0, 0))
    
        # update sprites
        sprite_group.update()

        #sprite_group.draw(screen)
    
    

if __name__ == '__main__':
    main()