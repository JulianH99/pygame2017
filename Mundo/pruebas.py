from powerups.modules.powerup_generator import POWERUP_INTERVAL,PowerupGenerator
import sys as s

from Obstaculo import *
from Escenario import *
from pygame.locals import *
from Bolita.ClaseBolita import *

from pygame import *

# POWERUPS
PWEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PWEVENT, POWERUP_INTERVAL)
powerup = None
sprite_group = pygame.sprite.Group()
def generate():
    return PowerupGenerator(ancho, alto-150).generate()

def colisionBolita(power_up,ball,escen):
    if power_up is not None:
        power_up.check_collide(ball,escen)

        if power_up.effect.triggered:
            power_up.effect.start_reset_countdown(ball, 10)

# tamaño ventana
ancho = 800
alto = 600




def main():

    imagenFondo = image.load("Imagenes/fondoEstatico1.png")

    init()

    ventana = display.set_mode([ancho, alto])

    # escenario
    escenario = Escenario(2,1, Escenario.ORIENT_DER_IZQ, ventana, ancho, alto)

    # bolita
    bolita = Bolita(500,0,escenario.alto - 40 - escenario.rectPlataforma[0].height,ancho,alto,imagenFondo.get_height()+(escenario.rectPlataforma[0].height)/2,escenario.rectPlataformaA[0].height)
    reloj = time.Clock()
    cont=0
    cont2=0
    while True:
        dt = reloj.tick()  # provisional
        reloj.tick(60)  # frames
        tiempo = int(time.get_ticks()/100)
        #bolita.invertirDireccion=True
        #escenario.setOrientacion(escenario.ORIENT_IZQ_DER)
        """
        if tiempo == 50:
            bolita.gravedad = False
            escenario.setOrientacion(escenario.ORIENT_IZQ_DER)
            print("Gravedad inver y sentido escenario izq der y bolita iz y der")
        if tiempo == 100:
            bolita.gravedad = True
            escenario.setOrientacion(escenario.ORIENT_DER_IZQ)
            bolita.invertirDireccion = True
            print("Gravedad nor y sentido escenario der izq y bolita der iz")
        if tiempo == 150:
            bolita.gravedad = False
            escenario.setOrientacion(escenario.ORIENT_IZQ_DER)
            bolita.invertirDireccion = False
            print("Gravedad inver y sentido escenario izq der y bolita iz der")
        if tiempo == 200:
            bolita.gravedad = True
            escenario.setOrientacion(escenario.ORIENT_DER_IZQ)
            print("Gravedad nor y sentido escenario der izq y bolita iz der")
        if tiempo == 250:
            bolita.gravedad = False
            escenario.setOrientacion(escenario.ORIENT_IZQ_DER)
            bolita.invertirDireccion = False
            print("Gravedad inver y sentido escenario izq der y bolita iz der")
    """


        escenario.moverFondo()
        escenario.dibujarFondo(ventana)



        for evento in event.get():
            if evento.type==KEYDOWN:
                if evento.key==K_LEFT or evento.key==K_RIGHT or evento.key==K_UP:
                    bolita.salto(escenario.velocidad + 10, evento.key,bolita.modificarVida(escenario.colisionBolita(bolita.rectangulo),escenario))


            if evento.type == QUIT:
                quit()
                s.exit()
            if evento.type == PWEVENT:
                global powerup
                powerup=generate()
                sprite_group.add(powerup)

        # bolita
        bolita.salto(escenario.velocidad + 10, None,bolita.modificarVida(escenario.colisionBolita(bolita.rectangulo),escenario))
        bolita.dibujarBolita(ventana)

        bolita.saltoDoble = False

        if bolita.getVivoMuerto()==False:
            print("GameOver")
            quit()
            s.exit()


        # powerup
        sprite_group.update()
        #colisionBolita(powerup,bolita)
        sprite_group.draw(ventana)

        colisionBolita(powerup,bolita,escenario)
        # escneario y obstcaulos
        escenario.generarObstaculos(21,tiempo)
        escenario.movimientoObstaculos()
        escenario.removerObstaculo()
        ventana.blit(imagenFondo, (0, 466))
        display.update()


main()