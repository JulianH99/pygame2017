# definicion de la clase powerup generator

from powerups.modules.effects import *
from powerups.modules.powerup import PowerUp
import random

POWERUP_INTERVAL = 10 * 1000  # intervalo en milisegundos


class PowerupGenerator:
    def __init__(self, scr_width, scr_heigth):
        self.__effects_list = [MoreScorePointsEffect,
                               MoreLifeEffect,
                               LessScorePointsEffect,
                               LessLifeEffect,
                               MoreSpeedEffect,
                               LessSpeedEffect,
                               ChangeStageDirectionEffect,
                               ChangeGravityEffect]

        self.__scr_width = scr_width + 100
        self.__scr_heigth = scr_heigth

    def generate(self):
        pos_x = self.__scr_width
        pos_y = random.randint(160, self.__scr_heigth)

        power_up = PowerUp(random.choice(self.__effects_list)(), (pos_x, pos_y))
        return power_up




