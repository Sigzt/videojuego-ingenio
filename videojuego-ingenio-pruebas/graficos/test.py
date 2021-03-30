from graphics import *
from perspectiva import *
from deshacer import *

update()

win = GraphWin("test",600,600)
punto = [Point(176.0, 274.0),
         Point(216.0, 136.0),
         Point(336.0, 135.0),
         Point(411.0, 251.0),
         Point(422.0, 133.0),
         Point(580.0, 127.0),
         Point(668.0, 189.0),
         Point(708.0, 261.0)]

puntos = perspectiva(deshacer(punto,450))

for line in puntos:
    line.draw(win)

win.getMouse()

