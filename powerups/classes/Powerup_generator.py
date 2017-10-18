# definicion de la clase powerup generator

from powerups.classes.effects import *
from powerups.classes.powerup import PowerUp
import random

POWERUP_INTERVAL = 7 * 1000  # intervalo en milisegundos


class PowerupGenerator:

    def __init__(self, scr_width, scr_heigth):
        self.effects_list = [MoreScorePointsEffect,
                             MoreLifeEffect,
                             LessScorePointsEffect,
                             LessLifeEffect,
                             MoreSpeedEffect,
                             LessSpeedEffect]
        self.scr_width = scr_width + 100
        self.scr_heigth = scr_heigth - 100

    def generate(self):

        pos_x = self.scr_width
        pos_y = random.randint(20, self.scr_heigth)

        power_up = PowerUp(random.choice(self.effects_list)(), (pos_x, pos_y))
        return power_up

