from graphics import *
from math import *
win= GraphWin("Food", 1000, 500)

def sky():
    sk=Rectangle(Point(0,0),Point(1000,900))
    sk.setFill('blue')
    sk.draw(win)

def house():

    whall=Polygon(Point(900, 450), Point(700,450), Point(700, 300), Point(900,300))
    whall.setFill('gray')
    whall.draw(win)

    roof=Polygon(Point(650, 300), Point(800, 200), Point(950,300))
    roof.setFill('gray')
    roof.draw(win)

    grass = Polygon(Point(1000,450), Point(0,450), Point(0,500), Point(1000,500))
    grass.setFill('green')
    grass.draw(win)

    window = Polygon(Point(740,330), Point(740,390), Point(790,390), Point(790,330))
    window.setFill('#ffffff')
    window.draw(win)

    l1=Line(Point(765,330), Point(765,390))
    l1.draw(win)
    l2=Line(Point(740,360),Point(790,360))
    l2.draw(win)
    
    door = Rectangle(Point(820,350), Point(870,450))
    door.setFill('#000000')
    door.draw(win)

def sun(n):
    sun = Circle(Point(150,110), 50)
    sun.setFill('yellow')
    sun.draw(win)
    for i in range(n):
        x = 150 + int(100*(sin(2*i*pi/n)))
        y = 110 + int(100*(cos(2*i*pi/n)))
        l=Line(Point(150, 110), Point(x,y))
        l.setWidth(10)
        l.setFill('yellow')
        l.draw(win)


sky()
sun(10) 
house()
win.getMouse()
win.close()

