from graphics import *
def deshacer (pp,hs):
    t = len(pp)
    i = 0
    while i < t:
        pp[i].x = pp[i].x - hs
        pp[i].y = -pp[i].y + hs
        i = i + 1
    return pp

