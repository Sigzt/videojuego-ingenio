from graphics import *

def linea (x1, y1, x2, y2):
    return Line(Point(x1,y1),Point(x2,y2))
def prin(): 
    x1= 200
    y1= 150
    x2= 400
    y2= 400
    p = Point(200, 200)
    p1 = Point(250, 100)
    lin = linea(x1,y1,x2,y2)
    midx = (x1+x2)/2
    midy = (y1+y2)/2
    mid = Point(midx, midy)
    lin.setOutline(color_rgb(100,100,200))
    mid.setOutline(color_rgb(0,0,0))
    lin.draw(win)
    mid.draw(win)
    win.getMouse()
win = GraphWin("gaming",500, 500)

print("xd")