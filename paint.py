"""
Paint, for drawing shapes

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circulo(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    radius = abs(end.x - start.x)

    circle(radius)


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    
    length = end.x - start.x
    width = end.y - start.y

    for _ in range(2):  # El bucle para dibujar 2 lados de longitud y 2 de anchura
        forward(length)  # Dibuja el lado más largo
        left(90)
        forward(width)   # Dibuja el lado más corto
        left(90)

    end_fill()


def triangle(start, end):
    """Draw a triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        forward(end.x - start.x)  # Dibuja el lado del triángulo
        left(120)  # Gira 120 grados para formar los ángulos del triángulo equilátero

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
dot()
