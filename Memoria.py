from random import *
from turtle import *

from freegames import path
# se importan las funciones de las bibliotecas para mezclar las tarjetas y un recurso de imagen

car = path('car.gif')  # imagen importada
tiles = list(range(32)) * 2 # 32 pares de tarjetas
state = {'mark': None}
hide = [True] * 64  # ayuda a saber si una tareta está oculta


def square(x, y):
# dibuja un cuadrado con el borde negro
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
# convierte las coordenadas en (x,y) en un índice de la lista de tiles
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
# convierte el índice de la tarjeta a (x,y)
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
# actualiza el estado de las tarjetas basado en clic
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
# dibuja la imagen de fondo así como las tarjetas
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)  #tamaño de la ventana
addshape(car)  # imagen de fondo como forma
hideturtle()
tracer(False)
onscreenclick(tap)  # indica que la función tap es un clic en pantalla
draw()
done()

