from graphics import *
from perspectiva import *
from deshacer import *

update()

win = GraphWin("test",600,600)
punto = [Point(200.0, 342.0),
         Point(272.0, 217.0),
         Point(366.0, 228.0),
         Point(516.0, 307.0),
         Point(576.0, 202.0),
         Point(723.0, 391.0)]

puntos = perspectiva(deshacer(punto,450))

for line in puntos:
    line.draw(win)

win.getMouse()

