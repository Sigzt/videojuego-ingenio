from graphics import *
import time


win = GraphWin("xd", 600, 600)
map = [Point(167.0, 137.0),
       Point(131.0, 346.0),
       Point(380.0, 324.0),
       Point(383.0, 139.0),
       Point(591.0, 133.0),
       Point(606.0, 314.0)]
t = len(map) - 4


if t < 0:
    print("no hay suficientes puntos")
else:
    p = Polygon(map[0], map[1], map[2], map[3])
    i = 0
    while True:
        p = Polygon(map[0], map[1], map[2], map[3])
        i = 0
        p.setFill("red")
        p.draw(win)
        time.sleep(0.01666666666)
        p.undraw()
        for puntos in map:
            puntos.x = puntos.x + 20
        p = Polygon(map[0], map[1], map[2], map[3])
        p.setFill("red")
        p.draw(win)
        time.sleep(0.01666666666)
        p.undraw()
        





        

