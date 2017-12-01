#!usr/bin/env python
# encoding: UTF-8

from abc import ABCMeta, abstractmethod
import pygame

IMAGES_PATH = "./img/"

EFFECT_DURATION = 5 * 1000

EFFECT_EVENT = pygame.USEREVENT + 2
reset_event_ins = pygame.event.Event(EFFECT_EVENT)


# definicion de la clase Effect
class Effect:
    """
        La clase Effect sirve como guia para realizar otros efectos bajo el mismo
        esqueleto, de manera que todos sean lo mas parecido posibles en terminos de
        definicion
    """

    __image = ""

    def __init__(self):
        self.__triggered = False
        self.__effect_time = 0
        self.before_effect_value = None

    def apply_over(self, obj,obj2):
        """
        El metodo apply_over define la accion que tendra el efecto sobre la bola.
        Es especifico de cada efecto, por esa razon se encuentra vacio en la clase base
        :param obj: el objeto al que se va a aplicar el efecto
        :return: None
        """
        pass

    def reset(self, obj):
        """
        El metodo reset sirve para devolver a la pelota a su estado inicial (es decir,
        el estado con el que contaba antes de que el powerup apareciera)luego del tiempo determinado
        :param obj:
        :return:
        """
        pass

    def start_reset_countdown(self, obj, dt):
        """
               Este metodo es usado para resetear la bola luego de que pase el tiempo definido de segundos
               que el efecto debe durar
               :param dt: cantidad de tiempo que cambia desde que se inicia el evento de reseteo
               :param obj: objeto al cual se aplicara el reseteo
               :return:
        """
        if self.__triggered:
            self.__effect_time += dt
            # print('{}'.format(dt))
            if self.__effect_time >= EFFECT_DURATION:
                self.reset(obj)
                self.__triggered = False

    @property
    def triggered(self):
        return self.__triggered

    @triggered.setter
    def triggered(self, value):
        self.__triggered = value

# fin clase


# Definicion clase ReduceOrAddEffect
class ReduceOrAddEffect(Effect):
    """
        La clase ReduceOrAddEffect define propiedades, o bueno, una propiedad en comun
        que tienen los efectos que se encargan de sumar o reducir una proporcion determinada
        de la bola, como los puntos de vida o el puntaje
    """
    __effect_time = 0

    def __init__(self, proportion=10):
        """
        El constructor recibe como parametro una proporcion opcional, que sera la proporcion
        con la cual la propiedad de la bola, sea cual sea, aumenta o disminuye
        :param proportion:  la proporcion para reducir o aumentar dicha propiedad
        """
        super().__init__()
        self.proportion = proportion

# fin clase ReduceOrAddEffect


# definicion clase ChangeStageDirectionEffect
class ChangeStageDirectionEffect(Effect):

    __image = IMAGES_PATH + "changedirection.png"

    def apply_over(self, obj,obj2):

        if obj2.getOrientacion()==obj2.ORIENT_IZQ_DER:
            obj2.setOrientacion(obj2.ORIENT_DER_IZQ)
        else:
            obj2.setOrientacion(obj2.ORIENT_IZQ_DER)

    def reset(self, obj):
        obj.setOrientacion(not obj.getOrientacion())

    @property
    def image(self):
        return self.__image
# fin clase ChangeStageDirectionEffect


# definicion MoreLifeEffect
class MoreLifeEffect(ReduceOrAddEffect):
    """
        Representa el efecto encargado de sumar puntos de vida a la pelota
    """
    __image = IMAGES_PATH + "morelife.png"

    def apply_over(self, obj,obj2):
        # si existe el atributo 'life_points' en la calse bola...
        if hasattr(obj, 'vida'):
            # se suma a sus puntos de vida la proporcion definida en el constructor
            obj.vida += self.proportion
        else:
            # en case de que no exista dicha propiedad, se lanza un error
            raise AttributeError("La pelota no tiene vida we .-.")

    @property
    def image(self):
        return self.__image

# fin clase MoreLifeEffect


# definicion LessLifeEffect
class LessLifeEffect(ReduceOrAddEffect):
    """
        Representa el efecto encargado de restar puntos de vida a la pelota
    """

    __image = IMAGES_PATH + "lesslife.png"

    def apply_over(self, obj, obj2):
        if hasattr(obj, 'vida'):
            obj.vida -= self.proportion

    @property
    def image(self):
        return self.__image

# fin clase LessLifeEffect


# definicion MoreScorePointsEffect
class MoreScorePointsEffect(ReduceOrAddEffect):
    """
        Representa la case encargada de sumar valor al puntaje de la bola
    """

    __image = IMAGES_PATH + "morescore.png"

    def apply_over(self, obj,obj2):
        if hasattr(obj, 'puntaje'):
            obj.puntaje += self.proportion
        else:
            raise AttributeError("La bola no tiene puntaje we u.u")

    @property
    def image(self):
        return self.__image
# fin clase MoreScorePointsEffect


# definicion LessScorePointsEffect
class LessScorePointsEffect(ReduceOrAddEffect):
    """
        Representa la clase encargada de restar valor al puntaje de la bola
    """

    __image = IMAGES_PATH + "lessscore.png"

    def apply_over(self, obj,obj2):
        if hasattr(obj, 'puntaje'):
            obj.puntaje -= self.proportion
        else:
            raise AttributeError("La bola no tiene puntaje we u.u")

    @property
    def image(self):
        return self.__image

# fin clase LessScorePointsEffect


# definicion clase MoreSpeedEffect
class MoreSpeedEffect(ReduceOrAddEffect):
    """
        Clase encargada de aumentar el valor de la velocidad en la pelota
    """

    __image = IMAGES_PATH + "morespeed.png"

    def __init__(self, proportion=1):
        super().__init__(proportion)

    def apply_over(self, obj, obj2):

            self.before_effect_value = obj2.getVelocidad()
            obj2.setVelocidad (obj2.getVelocidad()+self.proportion)



    def reset(self, obj):
        obj.speed = self.before_effect_value

    @property
    def image(self):
        return self.__image

# fin clase MoreSpeedEffect


# definicion clase LessSpeedEffect
class LessSpeedEffect(ReduceOrAddEffect):
    """
        clase encargada de reducir el valor de la velocidad de la bola
    """

    __image = IMAGES_PATH + "lessspeed.png"

    def __init__(self, proportion=1):
        super().__init__(proportion)

    def apply_over(self, obj,obj2):
        self.before_effect_value = obj2.getVelocidad()
        obj2.setVelocidad(obj2.getVelocidad() - self.proportion)

    def reset(self, obj):
        obj.speed = self.before_effect_value

    @property
    def image(self):
        return self.__image
# fin definicion clase LessSpeedEffect


