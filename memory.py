"""Memorama, juego para encontrar parejas de autotas."""

from random import shuffle
from turtle import (
    up, goto, down, color, begin_fill, forward, left, end_fill, clear, shape,
    stamp, write, update, ontimer, setup, addshape, hideturtle, tracer,
    onscreenclick, done
)

from freegames import path

auto = path('car.gif')
fichas = list(range(32)) * 2
estado = {'marca': None}
oculto = [True] * 64


def cuadrado(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def indice(x, y):
    """Convierte las coordenadas (x, y) al índice de las fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(contador):
    """Convierte el conteo de fichas a coordenadas (x, y)."""
    return (contador % 8) * 50 - 200, (contador // 8) * 50 - 200


def clicar(x, y):
    """Actualiza la marca y las fichas ocultas basándose en los clicars."""
    ubicacion = indice(x, y)
    marca = estado['marca']

    if marca is None or marca == ubicacion or fichas[marca] != fichas[ubicacion]:
        estado['marca'] = ubicacion
    else:
        oculto[ubicacion] = False
        oculto[marca] = False
        estado['marca'] = None


def dibujar():
    """Dibuja la imagen y las fichas."""
    clear()
    goto(0, 0)
    shape(auto)
    stamp()

    for count in range(64):
        if oculto[count]:
            x, y = xy(count)
            cuadrado(x, y)

    marca = estado['marca']

    if marca is not None and oculto[marca]:
        x, y = xy(marca)
        up()
        goto(x + 2, y)
        color('black')
        write(fichas[marca], font=('Arial', 30, 'normal'))

    update()
    ontimer(dibujar, 100)


"""Inicializa el juego."""
shuffle(fichas)
setup(420, 420, 370, 0)
addshape(auto)
hideturtle()
tracer(False)
onscreenclick(clicar)
dibujar()
done()
