from graphics import *
from perspectiva import *
from deshacer import *
import math
import time

update()
minimapa = GraphWin("s",900,900)

pps = [
    Point(208.0, 282.0),
    Point(568.0, 270.0),
    Point(719.0, 435.0),
    Point(460.0, 521.0),
    Point(163.0, 521.0),
    Point(208.0, 282.0)
]
i = 0

def main (line):
    win = GraphWin("test", 600, 600)
    for l in line:
        l.draw(win)



while i < len(pps) - 1:
    p  = Line(pps[i],pps[i+1])
    p.draw(minimapa)
    i = i + 1         
punto = deshacer(pps, 450)
puntos = perspectiva(punto)
main(puntos)
main(puntos)
while True:
    main(puntos)
    t = 0 
    while t < len(punto)-1:
        theta = math.atan(punto[t].y/punto[t].x)
        x2 = (punto[t].x**2)
        y2 = (punto[t].y**2)
        r = math.sqrt(x2 + y2)
        thetap = theta + 0.174533
        punto[t].x = r*math.cos(thetap)
        punto[t].y = r*math.sin(thetap)
        t = t + 1
    time.sleep(1)





