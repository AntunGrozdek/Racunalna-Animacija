import pyglet
from pyglet.gl import *
import random
import time
import numpy as np
import math
import pyglet
from pyglet import window
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
from pyglet import clock

sub_width = 512
sub_height = 512

window = pyglet.window.Window()
print(window.height, window.width)

flag_x = 0
flag_y = 0
counter = 0
move = 0
# global x, y, x2, y2, x3, y3, x4, y4, x5, y5


def koord():
    x = random.randint(100, 530)
    y = random.randint(100, 370)
    x2 = random.randint(100, 530)
    y2 = random.randint(100, 370)
    x3 = random.randint(100, 530)
    y3 = random.randint(100, 370)
    x4 = random.randint(100, 530)
    y4 = random.randint(100, 370)
    x5 = random.randint(100, 530)
    y5 = random.randint(100, 370)
    size = random.randint(10, 15)
    size2 = random.randint(10, 15)
    size3 = random.randint(10, 15)
    size4 = random.randint(10, 15)
    size5 = random.randint(10, 20)
    return x, y, x2, y2, x3, y3, x4, y4, x5, y5, size, size2, size3, size4, size5


x, y, x2, y2, x3, y3, x4, y4, x5, y5, size, size2, size3, size4, size5 = koord()


@window.event
def on_key_press(symbol, modifiers):
    global flag_x, flag_y, counter, x, y, x2, y2, x3, y3, x4, y4, x5, y5, size
    if counter < 19:
        if symbol == key.UP:
            flag_y += 5
            counter += 1
        if symbol == key.RIGHT:
            flag_x += 5
            counter += 1
        if symbol == key.LEFT:
            flag_x -= 5
            counter += 1
        if symbol == key.DOWN:
            flag_y -= 5
            counter += 1
    else:
        x, y, x2, y2, x3, y3, x4, y4, x5, y5, size, size2, size3, size4, size5 = koord()
        flag_x = 0
        flag_y = 0
        counter = 0


@window.event
def on_draw():
    global x, y, x2, y2, x3, y3, x4, y4, x5, y5, size
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1-counter/20, 0.0, 0.0)

    pyglet.graphics.draw(4, GL_QUADS, ('v3f', [x + flag_x + move, y + flag_y + move, 0, x + flag_x + move, y + flag_y + size + move, 0, x + flag_x + size + move, y + flag_y + size + move, 0, x + flag_x + size + move, y + flag_y + move, 0]))
    pyglet.graphics.draw(4, GL_QUADS, ('v3f', [x2 + flag_x + move, y2 + flag_y + move, 0, x2 + flag_x + move, y2 + flag_y + size2 + move, 0, x2 + flag_x + size2 + move, y2 + flag_y + size2 + move, 0, x2 + flag_x + size2 + move, y2 + flag_y + move, 0]))
    pyglet.graphics.draw(4, GL_QUADS, ('v3f', [x3 + flag_x + move, y3 + flag_y + move, 0, x3 + flag_x + move, y3 + flag_y + size3 + move, 0, x3 + flag_x + size3 + move, y3 + flag_y + size3 + move, 0, x3 + flag_x + size3 + move, y3 + flag_y + move, 0]))
    pyglet.graphics.draw(4, GL_QUADS, ('v3f', [x4 + flag_x + move, y4 + flag_y + move, 0, x4 + flag_x + move, y4 + flag_y + size4 + move, 0, x4 + flag_x + size4 + move, y4 + flag_y + size4 + move, 0, x4 + flag_x + size4 + move, y4 + flag_y + move, 0]))
    pyglet.graphics.draw(4, GL_QUADS, ('v3f', [x5 + flag_x + move, y5 + flag_y + move, 0, x5 + flag_x + move, y5 + flag_y + size5 + move, 0, x5 + flag_x + size5 + move, y5 + flag_y + size5 + move, 0, x5 + flag_x + size5 + move, y5 + flag_y + move, 0]))


def callback(dt):
    global move, counter, flag_x, flag_y, x, y, x2, y2, x3, y3, x4, y4, x5, y5, size
    move += 1
    if counter < 19:
        counter += 1
    else:
        x, y, x2, y2, x3, y3, x4, y4, x5, y5, size, size2, size3, size4, size5 = koord()
        flag_x = 0
        flag_y = 0
        counter = 0
    return


clock.schedule_interval(callback, 0.016)

pyglet.app.run()
