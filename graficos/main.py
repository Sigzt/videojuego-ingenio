from graphics import *
from mapc import *
from perspectiva import *
#sonido???


pantalla =[Point(25.0, 97.0),
Point(25.0, 242.0),
Point(100.0, 196.0),
Point(94.0, 90.0),
Point(73.0, 66.0),
Point(6.0, 72.0),
Point(25.0, 97.0),
0,
Point(114.0, 195.0),
Point(112.0, 89.0),
Point(134.0, 69.0),
Point(180.0, 70.0),
Point(196.0, 90.0),
Point(201.0, 198.0),
Point(156.0, 240.0),
Point(114.0, 195.0),
0,
Point(219.0, 198.0),
Point(212.0, 88.0),
Point(236.0, 67.0),
Point(291.0, 67.0),
Point(309.0, 91.0),
Point(310.0, 199.0),
Point(258.0, 240.0),
Point(219.0, 198.0),
0,
Point(328.0,87.0),
Point(351.0, 64.0),
Point(405.0, 57.0),
Point(427.0, 84.0),
Point(431.0, 193.0),
Point(396.0, 242.0),
Point(338.0, 199.0),
Point(328.0,87.0),
0,
Point(449.0, 80.0),
Point(447.0, 193.0),
Point(473.0, 207.0),
Point(477.0, 137.0),
Point(494.0, 172.0),
Point(511.0, 136.0),
Point(517.0, 242.0),
Point(552.0, 277.0),
Point(542.0, 67.0),
Point(507.0, 67.0),
Point(493.0, 98.0),
Point(477.0, 66.0),
Point(457.0, 60.0),
Point(449.0, 80.0),
0,
Point(40.0, 98.0),
Point(42.0, 198.0),
Point(81.0, 179.0),
Point(75.0, 96.0),
Point(40.0, 98.0),
0,
Point(129.0, 95.0),
Point(131.0, 182.0),
Point(170.0, 215.0),
Point(167.0, 94.0),
Point(129.0, 95.0),
0,
Point(232.0, 94.0),
Point(234.0, 184.0),
Point(258.0, 217.0),
Point(286.0, 192.0),
Point(281.0, 95.0),
Point(232.0, 94.0),
0,
Point(404.0, 91.0),
Point(405.0, 191.0),
Point(372.0, 212.0),
Point(360.0, 94.0),
Point(404.0, 91.0),
0,
Point(207.0, 226.0),
Point(177.0, 251.0),
Point(177.0, 307.0),
Point(203.0, 333.0),
Point(229.0, 309.0),
Point(226.0, 274.0),
Point(201.0, 270.0),
Point(207.0, 226.0),
0,
Point(191.0, 290.0),
Point(206.0, 307.0),
Point(216.0, 289.0),
Point(191.0, 290.0),
0,
Point(320.0, 222.0),
Point(283.0, 253.0),
Point(282.0, 273.0),
Point(316.0, 271.0),
Point(311.0, 310.0),
Point(344.0, 291.0),
Point(344.0, 252.0),
Point(320.0, 222.0),
0,
Point(315.0, 241.0),
Point(300.0, 256.0),
Point(329.0, 258.0),
Point(315.0, 241.0),
0,
Point(27.0, 286.0),
Point(98.0, 238.0),
Point(136.0, 280.0),
Point(136.0, 280.0),
0,
Point(230.0, 248.0),
Point(249.0, 271.0),
Point(279.0, 236.0),
Point(279.0, 236.0),
0,
Point(373.0, 250.0),
Point(404.0, 280.0),
Point(435.0, 234.0),
Point(525.0, 290.0),
Point(525.0, 290.0),
0,
Point(180.0, 340.0),
Point(220.0, 363.0),
Point(259.0, 333.0),
Point(282.0, 362.0),
Point(342.0, 334.0),
Point(342.0, 334.0),
0,
Point(206.0, 422.0),
Point(203.0, 372.0),
Point(337.0, 372.0),
Point(338.0, 421.0),
Point(206.0, 422.0),
0, 
Point(207.0, 443.0),
Point(205.0, 491.0),
Point(333.0, 493.0),
Point(334.0, 448.0),
Point(207.0, 443.0),
0,
Point(207.0, 515.0),
Point(213.0, 565.0),
Point(333.0, 568.0),
Point(330.0, 519.0),
Point(207.0, 515.0)]

def pintar(puntos, win):
    i = 0
    t = len(puntos) - 1
    while i < t:
        if puntos[i + 1] == 0:
            i = i + 2
        else:
            c = Line(puntos[i],puntos[i+1])
            c.draw(win)
            i = i+1
def main():
    win = GraphWin("DOOOM 64 + 5",600,600)
    pintar(pantalla,win)
    a = win.getMouse()
    if(a.x - 203 > 0 and a.x -330<0):
        if(a.y - 300 > 0 and a.y < 420):
            print(1)
        if(a.y - 430 > 0 and a.y < 490):
            print(2)
            win.close()
            i = crear()
        if(a.y - 510 > 0 and a.y < 570):
            print(3)

while True:
    main()

win.getMouse()
