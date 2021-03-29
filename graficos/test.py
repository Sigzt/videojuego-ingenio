from graphics import *
from perspectiva import *


update()

win = GraphWin("test",600,600)
punto = []

puntos = perspectiva(punto)

for line in puntos:
    line.draw(win)

win.getMouse()

