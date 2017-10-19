import sys as s
from pygame import *
from Obstaculo import *
from Escenario import *
from pygame.locals import *

def main():
    ancho = 700
    alto = 622
    imagenFondo = image.load("Imagenes/fondo.jpg")
    init()
    ventana = display.set_mode([ancho, alto])
    escenario = Escenario(2,1, "Imagenes/fondo.jpg", 0, ventana, ancho, alto)

    reloj = time.Clock()
    while True:
        #print(escenario.velocidad)
        reloj.tick(60)  # frames
        tiempo = int(time.get_ticks()/100)

        ventana.blit(imagenFondo, (0, 0))
        escenario.moverFondo()
        escenario.dibujarFondo(ventana)


        for evento in event.get():
            if evento.type == QUIT:
                quit()
                s.exit()
        escenario.generarObstaculos(21,tiempo)
        escenario.movimientoObstaculos()
        escenario.removerObstaculo()
        display.update()


main()