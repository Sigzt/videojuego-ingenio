from graphics import *
from lineas import *
import math  
eñe = True
mapaa = [Point(-270,250),Point(120,290),Point(200,100),Point(60,10)]   #importar del creador de mapas puntos extra: Point(420,570),Point(69,420),Point(30,50) 
x0 = 300.0
y0 = 300.0
camara = Point(0,300)
fovy = 1.8675
fovx = 3.49066
cam = GraphWin("1", 600, 600)
cuadrado = Polygon()
def perspectiva(t, mapa):
    
    i = 0
    pmedio = Point(300,300)
    while i < t:
        dx = mapa[i].x 
        dy = mapa[i].y 
        dx2 = dx**2
        dy2 = dy**2
        d2x = mapa[i+1].x 
        d2y = mapa[i+1].y 
        d2x2 = d2x**2
        d2y2 = d2y**2
        p = math.sqrt(dx2 + dy2) #Pitágoras
        d = Point(dx,dy)
        p2 = math.sqrt(d2x2 + d2y2) #Pitágoras
        d2 = Point(d2x,d2y)
        alfa = abs(math.atan(300/p))
        beta = abs(math.atan(300/p2))
        h = math.tan(alfa)/(math.tan(fovy))
        h2 = math.tan(beta)/(math.tan(fovy))
        a = camara.y + 300*h
        b = camara.y - 300*h
        c= camara.y + 300*h2
        d = camara.y -300*h2
        a1= Point(mapa[i].x+300, a)
        a2= Point(mapa[i].x+300, b)
        a3= Point(mapa[i+1].x+300, c)
        a4= Point(mapa[i+1].x+300, d)
        cuadrado = Polygon(a1,a2,a4,a3)
        cuadrado.draw(cam)
        planta(len(mapa)-1,mapa)
        
        #xd
        #li.draw(cam)
        i = i + 1   
mapa = mapaa
perspectiva(len(mapaa)-1,mapa)

while eñe == True:  
    
    i= 0
    mov = input("xd")
    if(mov == "w"):
        while i < len(mapaa):
            mapa[i].y = mapa[i].y - 30
            print()
            i = i+1
        
        perspectiva(len(mapaa)-1,mapa)
        mov = "no"
    if(mov == "s"):
        while i < len(mapaa):
            mapa[i].y = mapa[i].y + 30
            i = i+1
        
        perspectiva(len(mapaa)-1,mapa)
        mov = "no"
     if(mov == "a"):
        while i < len(mapaa):
            mapa[i].x = mapa[i].x - 30
            print()
            i = i+1
        
        perspectiva(len(mapaa)-1,mapa)
        mov = "no"
    if(mov == "d"):
        while i < len(mapaa):
            mapa[i].x = mapa[i].x + 30
            i = i+1
        
        perspectiva(len(mapaa)-1,mapa)
        mov = "no"
