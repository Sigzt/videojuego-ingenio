from graphics import *
import time
import math
def normalizar(mapa):
    t = len(mapa)
    i=0 
    while i < t:
        px = mapa[i].x - 300
        py = -mapa[i].y + 300
        mapa[i] = Point(px, py)
        i = i + 1
    return mapa
def pintar(puntos, win):
    i = 0
    t = len(puntos) - 1
    while i < t:
        if puntos[i + 1] == 0:
            i = i + 2
        else:
            c = Line(puntos[i], puntos[i+1])
            c.draw(win)
            i = i+1

def lineas(a,b,c,d):
    x = Point(a,b)
    y = Point(c,d)
    lin = Line(x,y)
    return lin
def render(punto):
    se_renderiza = True
    return se_renderiza


def perspectiva(mapa):
    t = len(mapa)-1
    i = 0
    pp = [0]
    pp.clear()
    fovx = 1.22173
    fovz = 0.872665
    if mapa[i].x == 0.0:
        mapa[i].x = 1
    if mapa[i].y == 0.0:
        mapa[i].y = 1
    while i < t:
        if mapa[i].x == 0.0:
            mapa[i].x = 1
        if mapa[i].y == 0.0:
            mapa[i].y = 1
        if mapa[i].y < 0 and mapa[i].y < 0:
            g = None
        #if mapa[i].y >0 and mapa[i].y >0:
            # desplazamiento de x respecto al foco
        px = 110*(mapa[i].x/mapa[i].y)
        px2 = 110*(mapa[i+1].x/mapa[i+1].y)
        py = 110*(100/mapa[i].y)
        py2 = 110*(100/mapa[i+1].y)  # cálculo de la altura
        #if mapa[i].y < 0  or mapa[i].y < 0:
        #    g = None

        a = Point(300 + px, 300-py)
        b = Point(300 + px, 300 + py)
        c = Point(300 + px2, 300-py2)
        d = Point(300 + px2, 300 + py2)
        pp.append(Line(a, b))
        pp.append(Line(a, c))
        pp.append(Line(b, d))
        pp.append(Line(c, d))
        i = i + 1
    return pp
