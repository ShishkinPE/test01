from graphics import *
from math import *
win= GraphWin("Food", 3000, 3000)

def sky():
    sk=Rectangle(Point(0,0),Point(1500,1500))
    sk.setFill('blue')
    sk.draw(win)

def house(x,y,n,beta,c_wall,c_roof,window_is_on_the_left,c_window,c_door,c_chimney,smoke_is_here,c_smoke,c_ruchka):

    wall=Polygon(Point(x+10*n*cos(beta)-10*n*sin(beta), y+10*n*sin(beta)+10*n*cos(beta)), Point(x-10*n*cos(beta)-10*n*sin(beta),y-10*n*sin(beta)+10*n*cos(beta)), Point(x-10*n*cos(beta)+10*n*sin(beta),y-10*n*sin(beta)-10*n*cos(beta)), Point(x+10*n*cos(beta)+10*n*sin(beta), y+10*n*sin(beta)-10*n*cos(beta)))
    wall.setFill(c_wall)
    wall.draw(win)

    roof=Polygon(Point(x-15*n*cos(beta)+10*n*sin(beta),y-15*n*sin(beta)-10*n*cos(beta) ), Point(x+15*n*cos(beta)+10*n*sin(beta), y+15*n*sin(beta)-10*n*cos(beta)), Point(x-0*n*cos(beta)+20*n*sin(beta),y-0*n*sin(beta)-20*n*cos(beta)))
    roof.setFill(c_roof)
    roof.draw(win)
    
    
    if window_is_on_the_left==True:
        window = Polygon(Point(x-8*n*cos(beta)+8*n*sin(beta),y-8*n*sin(beta)-8*n*cos(beta)), Point(x-2*n*cos(beta)+8*n*sin(beta),y-2*n*sin(beta)-8*n*cos(beta)),Point(x-2*n*cos(beta)+2*n*sin(beta),y-2*n*sin(beta)-2*n*cos(beta)),Point(x-8*n*cos(beta)+2*n*sin(beta),y-8*n*sin(beta)-2*n*cos(beta)))
    else:
        window = Polygon(Point(x+8*n*cos(beta)+8*n*sin(beta),y+8*n*sin(beta)-8*n*cos(beta)), Point(x+2*n*cos(beta)+8*n*sin(beta),y+2*n*sin(beta)-8*n*cos(beta)),Point(x+2*n*cos(beta)+2*n*sin(beta),y+2*n*sin(beta)-2*n*cos(beta)),Point(x+8*n*cos(beta)+2*n*sin(beta),y+8*n*sin(beta)-2*n*cos(beta)))
    
    window.setFill(c_window)
    window.draw(win)
    
    if window_is_on_the_left==True:
        l1=Line(Point(x-5*n*cos(beta)+8*n*sin(beta),y-5*n*sin(beta)-8*n*cos(beta)), Point(x-5*n*cos(beta)+2*n*sin(beta),y-5*n*sin(beta)-2*n*cos(beta)))
        l1.draw(win)
        l2=Line(Point(x-8*n*cos(beta)+5*n*sin(beta),y-8*n*sin(beta)-5*n*cos(beta)), Point(x-2*n*cos(beta)+5*n*sin(beta),y-2*n*sin(beta)-5*n*cos(beta)))
        l2.draw(win)
    else:
        l1=Line(Point(x+5*n*cos(beta)+8*n*sin(beta),y+5*n*sin(beta)-8*n*cos(beta)), Point(x+5*n*cos(beta)+2*n*sin(beta),y+5*n*sin(beta)-2*n*cos(beta)))
        l1.draw(win)
        l2=Line(Point(x+8*n*cos(beta)+5*n*sin(beta),y+8*n*sin(beta)-5*n*cos(beta)), Point(x+2*n*cos(beta)+5*n*sin(beta),y+2*n*sin(beta)-5*n*cos(beta)))
        l2.draw(win)
    if window_is_on_the_left==True:
        door = Polygon(Point(x+0*n*cos(beta)+8*n*sin(beta),y+0*n*sin(beta)-8*n*cos(beta)),Point(x+8*n*cos(beta)+8*n*sin(beta),y+8*n*sin(beta)-8*n*cos(beta)), Point(x+8*n*cos(beta)-8*n*sin(beta),y+8*n*sin(beta)+8*n*cos(beta)),Point(x+0*n*cos(beta)-8*n*sin(beta),y-0*n*sin(beta)+8*n*cos(beta)))
        door.setFill(c_door)
        door.draw(win)
    else:
        door = Polygon(Point(x+0*n*cos(beta)+8*n*sin(beta),y+0*n*sin(beta)-8*n*cos(beta)),Point(x-8*n*cos(beta)+8*n*sin(beta),y-8*n*sin(beta)-8*n*cos(beta)), Point(x-8*n*cos(beta)-8*n*sin(beta),y-8*n*sin(beta)+8*n*cos(beta)),Point(x+0*n*cos(beta)-8*n*sin(beta),y-0*n*sin(beta)+8*n*cos(beta)))
        door.setFill(c_door)
        door.draw(win)
    
    chimney=Polygon(Point(x-10*n*cos(beta)+13*n*sin(beta),y-10*n*sin(beta)-13*n*cos(beta)),Point(x-10*n*cos(beta)+17*n*sin(beta),y-10*n*sin(beta)-17*n*cos(beta)),Point(x-12*n*cos(beta)+17*n*sin(beta),y-12*n*sin(beta)-17*n*cos(beta)),Point(x-12*n*cos(beta)+19*n*sin(beta),y-12*n*sin(beta)-19*n*cos(beta)),Point(x-4*n*cos(beta)+19*n*sin(beta),y-4*n*sin(beta)-19*n*cos(beta)),Point(x-4*n*cos(beta)+17*n*sin(beta),y-4*n*sin(beta)-17*n*cos(beta)),Point(x-6*n*cos(beta)+17*n*sin(beta),y-6*n*sin(beta)-17*n*cos(beta)),Point(x-6*n*cos(beta)+16*n*sin(beta),y-6*n*sin(beta)-16*n*cos(beta)),Point(x-10*n*cos(beta)+13*n*sin(beta),y-10*n*sin(beta)-13*n*cos(beta)))
    chimney.setFill(c_chimney)
    chimney.draw(win)
    
    if window_is_on_the_left==True:
         ruchka=Circle(Point(x+7*n*cos(beta)+0*n*sin(beta),y+7*n*sin(beta)-0*n*cos(beta)),n)
         ruchka.setFill(c_ruchka)
         ruchka.draw(win)  
    else:
         ruchka=Circle(Point(x-7*n*cos(beta)+0*n*sin(beta),y-7*n*sin(beta)-0*n*cos(beta)),n)
         ruchka.setFill(c_ruchka)
         ruchka.draw(win)
    
    smoke1=Oval(Point(x-10*n*cos(beta)+19*n*sin(beta),y-10*n*sin(beta)-19*n*cos(beta)),Point(x-6*n*cos(beta)+22*n*sin(beta),y-6*n*sin(beta)-22*n*cos(beta)))
    smoke1.setFill(c_smoke)
    smoke2=Oval(Point(x-12*n*cos(beta)+23*n*sin(beta),y-12*n*sin(beta)-23*n*cos(beta)),Point(x-8*n*cos(beta)+25*n*sin(beta),y-8*n*sin(beta)-25*n*cos(beta)))
    smoke2.setFill(c_smoke)
    if smoke_is_here==True:
        smoke1.draw(win)
        smoke2.draw(win)
        

def sun(n,x,y,r,c_sun):
    sun = Circle(Point(x,y), r)
    sun.setFill(c_sun)
    sun.setOutline(c_sun)
    sun.draw(win)
    for i in range(n):
        z = x + int(100*(sin(2*i*pi/n)))
        d = y + int(100*(cos(2*i*pi/n)))
        l=Line(Point(x, y), Point(z,d))
        l.setWidth(10)
        l.setFill(c_sun)
        l.draw(win)
        
 


    
def tree(x,y,r,c_krona,c_trunk):
    
    trunk=Rectangle(Point(x-r/4,y+r/2),Point(x+r/4,y+3*r))
    trunk.setFill(c_trunk)
    trunk.draw(win)
    krona=Circle(Point(x,y), r)
    krona.setFill(c_krona)
    krona.draw(win)
def human(x,y,r,c_head,c_telo,c_nogi,c_ruki,c_eyes):
   
    
    noga_left=Polygon(Point(x-r/4,y+r/4),Point(x-3*r/2,y+3*r/2),Point(x-4*r,y+3*r/2))
    noga_left.setFill(c_nogi)
    noga_left.draw(win)
    
    noga_right=Polygon(Point(x+r/4,y+r/4),Point(x+3*r/2,y+3*r/2),Point(x+4*r,y+3*r/2))
    noga_right.setFill(c_nogi)
    noga_right.draw(win)
    
    ruka_right=Polygon(Point(x+r/4,y+r/4),Point(x+3*r/2,y-r/2),Point(x+4*r,y-r/2))
    ruka_right.setFill(c_ruki)
    ruka_right.draw(win)
    
    ruka_left=Polygon(Point(x-r/4,y+r/4),Point(x-3*r/2,y-r/2),Point(x-4*r,y-r/2))
    ruka_left.setFill(c_ruki)
    ruka_left.draw(win)
    
    telo=Circle(Point(x,y),3*r/2)
    telo.setFill(c_telo)
    telo.draw(win)
    
    head=Circle(Point(x,y-5*r/2),r)
    head.setFill(c_head)
    head.draw(win)
    
    eye1=Circle(Point(x-r/4,y-5*r/2),r/8)
    eye1.setFill(c_eyes)
    eye1.draw(win)
    
    eye2=Circle(Point(x+r/4,y-5*r/2),r/8)
    eye2.setFill(c_eyes)
    eye2.draw(win)
    
def oblako(x,y,r,c_oblako):
    o=Oval(Point(x,y),Point(x+20*r,y+50))
    o.setFill(c_oblako)
    o.setOutline(c_oblako)
    o.draw(win)
sky()
grass = Polygon(Point(1000,450), Point(0,450), Point(0,500), Point(1000,500))
grass.setFill('green')
grass.draw(win)
sun(20,100,150,50,'violet') 
house(900,450,6,pi/2,'grey','red',True,'blue','violet','red',True,'white','blue')
tree(300,300,100,'green','black')
human(200,200,40,'blue','red','green','yellow','white')
for i in range(4):
    oblako(10+100*i,100+20*i,10,'white')
win.getMouse()
win.close()

