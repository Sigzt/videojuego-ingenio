from graphics import *

def crear():
    fin = False
    print("especifica las dimesiones del mapa")
    x = 900#input("x: ")
    y = 900#input("y: ")
    win = GraphWin("creador de mapas",x,y)
    
    p0 = Point(450,450)
    p1 = Point(150,340)
    p2 = Point(750, 340)
    l = Line(p0,p1)
    l.draw(win)
    l = Line(p1,p2)
    l.draw(win)
    l = Line(p0, p2)
    l.draw(win)
    a = win.getMouse()
    mapa = [a]
    print(a)
    while fin == False:
        c = Circle(a,10)
        c.draw(win)
        b = win.getMouse()
        for cord in mapa:
            ax = b.x
            ay = b.y
            if ax > 880 and ay >880:
                fin = True
            if cord == 0:
                chungus = 0
            else:
                dx = abs(cord.x - b.x)
                dy = abs(cord.y - b.y)
                if dx < 10 and dy < 10 :
                    b = cord
                    #fin = True
                    lin = Line(a,b)
                    lin.draw(win)
                    a1 = win.getMouse()
                    
                    mapa.append(b)
                    mapa.append(0)
                    break
                else:
                    a1 = b
        lin = Line(a,b)
        lin.draw(win)
        
        a = b
        a = a1
        print(a1)
        mapa.append(a1)
    print("fin")
    win.close()
    return mapa


