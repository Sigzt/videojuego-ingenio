from graphics import *
mapa = [Point(30,50),Point(560,10),Point(420,570),Point(69,420),Point(69,300),Point(30,50)]

def lin(x1,y1,x2,y2):
    a = Point(x1,y1)
    b = Point(x2,y2)
    lin = Line(a,b)
    
    return lin


def planta(t):
    ven = GraphWin("xsd", 600, 600)
    i = 0
    while i < t:
        li = Line(mapa[i],mapa[i+1])
        li.draw(ven)
        i = i + 1   
    
    ven.getMouse()

planta(len(mapa)-1)
