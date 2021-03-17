from graphics import *
import math  
mapa = [Point(30,200),Point(560,10),]   #importar del creador de mapas puntos extra: Point(420,570),Point(69,420),Point(30,50) 
x0 = 300.0
y0 = 300.0
camara = Point(0,300)
fovy = 1.8675
fovx = 3.49066
def perspectiva(t):
    cam = GraphWin("1", 600, 600)
    i = 0
    pmedio = Point(300,300)
    while i < t:

        dx = mapa[i].x - x0
        dy = mapa[i].y - y0
        dx2 = dx**2
        dy2 = dy**2
        d2x = mapa[i+1].x - x0
        d2y = mapa[i+1].y - y0
        d2x2 = d2x**2
        d2y2 = d2y**2
        p = math.sqrt(dx2 + dy2) #Pitágoras
        d = Point(dx,dy)
        p2 = math.sqrt(d2x2 + d2y2) #Pitágoras
        d2 = Point(d2x,d2y)
        alfa = abs(math.atan(dy/dx))
        beta = abs(math.atan(d2y/d2x))
        h = math.tan(alfa)/(math.tan(fovy))
        h2 = math.tan(beta)/(math.tan(fovy))
        a = camara.y + 300*h
        b = camara.y - 300*h
        c= camara.y + 300*h2
        d = camara.y -300*h2
        a1= Point(mapa[i]. x, a)
        a2= Point(mapa[i]. x, b)
        a3= Point(mapa[i+1]. x, c)
        a4= Point(mapa[i+1]. x, d)
        c = Polygon(a1,a2,a4,a3)
        c.draw(cam)
        #xd
        #li.draw(cam)
        i = i + 1   
    
    cam.getMouse()

perspectiva(len(mapa)-1)
