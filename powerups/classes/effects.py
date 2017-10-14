#!usr/bin/env python

from abc import ABCMeta, abstractmethod

# definicion de la clase Effect
class Effect:
    """
        La clase abstacta Effect sirve como guia para realizar otros efectos bajo el mismo
        esqueleto, de manera que todos sean lo mas parecido posibles en terminos de
        definicion
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_over(self, ball):
        """
        El metodo apply_over define la accion que tendra el efecto sobre la bola.
        Es especifico de cada efecto, por esa razon se encuentra vacio en la clase base
        :param ball: la bola a la que se va a aplicar el efecto
        :return: None
        """
        pass
# fin clase


# Definicion clase ReduceOrAddEffect
class ReduceOrAddEffect(Effect):
    """
        La clase ReduceOrAddEffect define propiedades, o bueno, una propiedad en comun
        que tienen los efectos que se encargan de sumar o reducir una proporcion determinada
        de la bola, como los puntos de vida o el puntaje
    """
    def __init__(self, proportion=10):
        """
        El constructor recibe como parametro una proporcion opcional, que sera la proporcion
        con la cual la propiedad de la bola, sea cual sea, aumenta o disminuye
        :param proportion:  la proporcion para reducir o aumentar dicha propiedad
        """
        self.proportion = proportion

    def apply_over(self, ball):
        """
            En este caso, solamente se sobreescribe el metodo con el fin de que no haya
            errores al implementar la clase abstracta Effect
        :param ball:
        :return:
        """
        pass
# fin clase ReduceOrAddEffect


# definicion MoreLifeEffect
class MoreLifeEffect(ReduceOrAddEffect):
    """
        Representa el efecto encargado de sumar puntos de vida a la pelota
    """
    def apply_over(self, ball):
        # si existe el atributo 'life_points' en la calse bola...
        if hasattr(ball, 'life_points'):
            # se suma a sus puntos de vida la proporcion definida en el constructor
            ball.life_points += self.proportion
        else:
            # en case de que no exista dicha propiedad, se lanza un error
            raise AttributeError("La pelota no tiene vida we .-.")

# fin clase MoreLifeEffect


# definicion LessLifeEffect
class LessLifeEffect(ReduceOrAddEffect):
    """
        Representa el efecto encargado de restar puntos de vida a la pelota
    """
    def apply_over(self, ball):
        if hasattr(ball, 'life_points'):
            ball.life_points -= self.proportion

# fin clase LessLifeEffect


# definicion MoreScorePointsEffect
class MoreScorePointsEffect(ReduceOrAddEffect):
    """
        Representa la case encargada de sumar valor al puntaje de la bola
    """
    def apply_over(self, ball):
        if hasattr(ball, 'score'):
            ball.score += self.proportion
        else:
            raise AttributeError("La bola no tiene puntaje we u.u")

# fin clase MoreScorePointsEffect


# definicion LessScorePointsEffect
class LessScorePointsEffect(ReduceOrAddEffect):
    """
        Representa la clase encargada de restar valor al puntaje de la bola
    """
    def apply_over(self, ball):
        if hasattr(ball, 'score'):
            ball.score -= self.proportion
        else:
            raise AttributeError("La bola no tiene puntaje we u.u")

# fin clase LessScorePointsEffect


