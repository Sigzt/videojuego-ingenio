from graphics import *
mapaa = [Point(30,50),Point(420,10),Point(500,200),Point(560,290),Point(69,420),Point(69,300),Point(30,50)]
ven = GraphWin("xsd", 300, 300)
def lin(x1,y1,x2,y2):
    a = Point(x1,y1)
    b = Point(x2,y2)
    lin = Line(a,b)
    
    return lin


def planta(t, mapa):
    li = lin(2,2,2,2) 
    i = 0
    ps = 0
    while i < ps:
        li.undraw()
        p = p + 1
    while i < t:
        p = lin(0,150,300,150)
        p.draw(ven)
        x1 = mapa[i].x+300
        y1 = -mapa[i].y +300
        x2 = mapa[i+1].x+300
        y2 = -mapa[i+1].y +300
        li = lin(x1/2,y1/2,x2/2,y2)
        li.draw(ven)
        i = i + 1   
