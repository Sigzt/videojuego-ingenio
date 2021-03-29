from graphics import *
from mapc import *
import guardar
from perspectiva import *
import mapas_niveles
#sonido???


pantalla = mapas_niveles.inicio
nivel_1 = mapas_niveles.escena_1

def main():
    win = GraphWin("DOOOM 64 + 5",600,600)
    pintar(pantalla,win)
    a = win.getMouse()
    if(a.x - 203 > 0 and a.x -330<0):
        if(a.y - 300 > 0 and a.y < 420):
            win.close()
            win = GraphWin("DOOOM 64 + 5", 600, 600)
            pintar(nivel_1, win)
            win.getMouse()
            print(1)
        if(a.y - 430 > 0 and a.y < 490):
            print(2)
            win.close()
            i = crear()
        if(a.y - 510 > 0 and a.y < 570):
            print(3)

main()


