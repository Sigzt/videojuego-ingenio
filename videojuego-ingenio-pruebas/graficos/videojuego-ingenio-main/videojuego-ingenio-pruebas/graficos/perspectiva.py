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
    c = Line(puntos[i], puntos[i+1])
    c.draw(win)
    c.undraw
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
        fuera = False
        tg = abs(math.atan(mapa[i].x/mapa[i].y))
        tg2 = abs(math.atan(mapa[i+1].x/mapa[i+1].y))
        print(fovx, tg, tg2)
        if (tg > fovx or mapa[i].y < 0) and (tg2 > fovx or mapa[i+1].y < 0):
            print("fuera")
            fuera = True
        #py = 110*(100/mapa[i].y)  # cálculo de la altura        se calcula antes porque (de momento) no varía respecto la posición en x (no puede superar el fov)
        #py2 = 110*(100/mapa[i+1].y)            soy tontísimo. si calculo la altura antes, la intersección no sirve para nada y utiliza la altura (eje z, simulado) calculada previamente respecto al punto absoluto(valor y del punto(x,y)) y no calcula la altura a partir del punto de intersección.
        if fuera == False:
            if mapa[i].x == 0.0:
                mapa[i].x = 1
            if mapa[i].y == 0.0:
                mapa[i].y = 1
            print(fovx, tg , tg2)
            if tg < fovx and tg2 < fovx:    
                print("dentro")
                py = 110*(100/mapa[i].y)
                py2 = 110*(100/mapa[i+1].y)
                px = 170*(mapa[i].x/mapa[i].y) # desplazamiento de x respecto al foco
                px2 = 170*(mapa[i+1].x/mapa[i+1].y)
                a = Point(300 + px, 300 - py)  #puntos de perspectiva
                b = Point(300 + px, 300 + py) 
                c = Point(300 + px2, 300 - py2) 
                d = Point(300 + px2, 300 + py2)  
                pp.append(Line(a, b))
                pp.append(Line(a, c))
                pp.append(Line(b, d))
                pp.append(Line(c, d))
            if tg > fovx or tg2 > fovx:
                print("si")
                #hacer magia
                vd = [mapa[i+1].x - mapa[i].x, mapa[i+1].y - mapa[i].y]
                vdf = [3,1]
                if mapa[i].x < 0 or  mapa[i+1].x < 0:
                    vdf[0] = -vdf[0]
                det = (vd[0]*vdf[1])-(vd[1]*vdf[0])
                c = -vd[0]*mapa[i].x - vd[1]*mapa[i].y
                interseccion = (c+vdf[1])/det  #GASTAR EL PUNTO DE INTERSECCIÓN PARA CALULAR LA ALTURA , POR FAVOR
                if tg > tg2:#punto 1 está fuera
                    print(1)
                    py = 110*(100/interseccion)  
                    py2 =  110*(100/mapa[i+1].y)
                    px = abs(mapa[i].x)/mapa[i].x #si x es negativo, el resultado es -1 y por tanto x está a la izda
                    px2 = 170*(mapa[i+1].x/mapa[i+1].y)
                    a = Point(300 + (300*px), 300 - py)     #mitad +- mitad = 0  o máx
                    b = Point(300 + (300*px), 300 + py)
                    c = Point(300 + px2, 300 - py2)
                    d = Point(300 + px2, 300 + py2)
                if tg < tg2:  #punto 2 está fuera   (copypaste del de arriba)
                    print(2)
                    px2 = abs(mapa[i+1].x)/mapa[i+1].x
                    px = 170*(mapa[i].x/mapa[i].y)
                    py2 = 110*(100/interseccion)
                    py = 110*(100/mapa[i].y)
                    c = Point(300 + (300*px2), 300 - py2)     
                    d = Point(300 + (300*px2), 300 + py2)
                    a = Point(300 + px, 300 - py)
                    b = Point(300 + px, 300 + py)
                pp.append(Line(a, b))
                pp.append(Line(a, c))
                pp.append(Line(b, d))
                pp.append(Line(c, d))
        i = i + 1
    return pp
