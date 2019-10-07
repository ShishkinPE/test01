from graphics import *
from math import *
win= GraphWin("Food", 1000, 500)

def sky():
    sk=Rectangle(Point(0,0),Point(1500,1500))
    sk.setFill('blue')
    sk.draw(win)

def house(x,y,n,beta,c_wall,c_roof,window_is_on_the_left,c_window,c_door,c_chimney,smoke_is_here,c_smoke,c_ruchka):

    wall=Polygon(Point(x+10*n*cos(beta)-10*n*sin(beta), y+10*n*sin(beta)+10*n*cos(beta)), Point(x-10*n*cos(beta)-10*n*sin(beta)
            ,y-10*n*sin(beta)+10*n*cos(beta)), Point(x-10*n*cos(beta)+10*n*sin(beta),y-10*n*sin(beta)-10*n*cos(beta)), Point(x+10*n*cos(beta)+10*n*sin(beta), y+10*n*sin(beta)-10*n*cos(beta)))
    wall.setFill(c_wall)
    wall.draw(win)

    roof=Polygon(Point(x-15*n*cos(beta)+10*n*sin(beta),y-15*n*sin(beta)-10*n*cos(beta) ), Point(x+15*n*cos(beta)+10*n*sin(beta),
            y+15*n*sin(beta)-10*n*cos(beta)), Point(x-0*n*cos(beta)+20*n*sin(beta),y-0*n*sin(beta)-20*n*cos(beta)))
    roof.setFill(c_roof)
    roof.draw(win)
    
    
    if window_is_on_the_left==True:
        window = Polygon(Point(x-8*n*cos(beta)+8*n*sin(beta),y-8*n*sin(beta)-8*n*cos(beta)), Point(x-2*n*cos(beta)+8*n*sin(beta),
                y-2*n*sin(beta)-8*n*cos(beta)),Point(x-2*n*cos(beta)+2*n*sin(beta),y-2*n*sin(beta)-2*n*cos(beta)),Point(x-8*n*cos(beta)+2*n*sin(beta),y-8*n*sin(beta)-2*n*cos(beta)))
    else:
        window = Polygon(Point(x+8*n*cos(beta)+8*n*sin(beta),y+8*n*sin(beta)-8*n*cos(beta)),
        Point(x+2*n*cos(beta)+8*n*sin(beta),y+2*n*sin(beta)-8*n*cos(beta)),Point(x+2*n*cos(beta)+2*n*sin(beta),y+2*n*sin(beta)-2*n*cos(beta)),Point(x+8*n*cos(beta)+2*n*sin(beta),y+8*n*sin(beta)-2*n*cos(beta)))
    
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
        door = Polygon(Point(x+0*n*cos(beta)+8*n*sin(beta),y+0*n*sin(beta)-8*n*cos(beta)),Point(x+8*n*cos(beta)+8*n*sin(beta),y+8*n*sin(beta)-8*n*cos(beta)), Point(x+8*n*cos(beta)-8*n*sin(beta),
                    y+8*n*sin(beta)+8*n*cos(beta)),Point(x+0*n*cos(beta)-8*n*sin(beta),y-0*n*sin(beta)+8*n*cos(beta)))
        door.setFill(c_door)
        door.draw(win)
    else:
        door = Polygon(Point(x+0*n*cos(beta)+8*n*sin(beta),y+0*n*sin(beta)-8*n*cos(beta)),
        Point(x-8*n*cos(beta)+8*n*sin(beta),y-8*n*sin(beta)-8*n*cos(beta)), Point(x-8*n*cos(beta)-8*n*sin(beta),
                y-8*n*sin(beta)+8*n*cos(beta)),Point(x+0*n*cos(beta)-8*n*sin(beta),y-0*n*sin(beta)+8*n*cos(beta)))
        door.setFill(c_door)
        door.draw(win)
    
    chimney=Polygon(Point(x-10*n*cos(beta)+13*n*sin(beta),y-10*n*sin(beta)-13*n*cos(beta)),Point(x-10*n*cos(beta)+17*n*sin(beta),
      y-10*n*sin(beta)-17*n*cos(beta)),Point(x-12*n*cos(beta)+17*n*sin(beta),y-12*n*sin(beta)-17*n*cos(beta)),Point(x-12*n*cos(beta)+19*n*sin(beta),
            y-12*n*sin(beta)-19*n*cos(beta)),Point(x-4*n*cos(beta)+19*n*sin(beta),y-4*n*sin(beta)-19*n*cos(beta)),Point(x-4*n*cos(beta)+17*n*sin(beta),
                y-4*n*sin(beta)-17*n*cos(beta)),Point(x-6*n*cos(beta)+17*n*sin(beta),y-6*n*sin(beta)-17*n*cos(beta)),Point(x-6*n*cos(beta)+16*n*sin(beta),
                    y-6*n*sin(beta)-16*n*cos(beta)),Point(x-10*n*cos(beta)+13*n*sin(beta),y-10*n*sin(beta)-13*n*cos(beta)))
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
    sun = Circle(Point(x, y), r)
    sun.setFill(c_sun)
    sun.setOutline(c_sun)
    sun.draw(win)

def luchiki(n,x,y,r,c_sun):
    v=(5,5)
    k=[1,1,1,1,1,1,1,1,1,1]
    g=[1,1,1,1,1,1,1,1,1,1]
    for i in range(n):
        z = x + 100*(sin(2*i*pi/n))
        d = y + 100*(cos(2*i*pi/n))
        l = Line(Point(x, y), Point(z,d))
        l.setWidth(4)
        l.setFill(c_sun)
        k[i] = l

    for i in range(n):
         z = x + 100 * (sin(2 * i * pi / n + pi/n))
         d = y + 100 * (cos(2 * i * pi / n + pi/n))
         l = Line(Point(x, y), Point(z, d))
         l.setWidth(4)
         l.setFill(c_sun)
         g[i] = l

    for i in range(n):
        k[i].draw(win)
    for i in range(n):
        k[i].undraw()
        g[i].draw(win)
        time.sleep(0.01)
    for i in range(n):
        g[i].undraw()
    time.sleep(0.001)




def add(point_1,point_2):
    new_point=Point(point_1.x+point_2.x,point_1.y+point_2.y)
    return(new_point)
        
 



def tree(r,c_krona,c_trunk,coords1_x,coords1_y):
    
    trunk=Rectangle(Point(coords1_x-r/4,coords1_y+r/2),Point(coords1_x+r/4,coords1_y+3*r))
    trunk.setFill(c_trunk)
    trunk.draw(win)

    krona=Circle(Point(coords1_x,coords1_y), r)
    krona.setFill(c_krona)
    krona.draw(win)

    return(trunk,krona,r,coords1_x,coords1_y)

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




house(x=800,y=250,n=10,beta=pi,c_wall='grey',c_roof='red',window_is_on_the_left=True,c_window='blue',c_door='brown',c_chimney='red',smoke_is_here=False,c_smoke='white',c_ruchka='blue')

human(500,400,20,'blue','red','green','yellow','white')
for i in range(4):
    oblako(10+100*i,100+20*i,10,'white')
    oblako(400+100*i,100+20*i,10,'white')
    z=Point(20,20)

    #начало алгоритма движения деревьев
a=[1,1,1]
b=[1,1,1]
coords_x=[1,1,1]
coords_y=[1,1,1]
for i in range(2):
    a[i], b[i], r, coords_x[i],coords_y[i] = tree( r=20, c_krona='green', c_trunk='yellow', coords1_x=300+100*i, coords1_y=400+100*i)


v_x=[5,5,5]  #на i-том месте стоит проекция скорости i-ого дерева
v_y=[5,5,5]  #на i-том месте стоит проекция скорости i-ого дерева
def check_coords(i):
    if coords_x[i]-r<0 or coords_x[i]+r>1000:
        v_x[i]=-v_x[i]
    if (coords_y[i]+3*r < 455 and v_y[i]<0)  or (coords_y[i]+3*r > 500 and v_y[i]>0):
        v_y[i] = -v_y[i]
    return(v_x[i],v_y[i])

sun(10,100,150,50,'violet')
while  True:
    for i in range(2):
        check_coords(i)
        a[i].move(v_x[i], v_y[i])
        b[i].move(v_x[i], v_y[i])
        coords_x[i] += v_x[i]
        coords_y[i] += v_y[i]
    luchiki(10, 100, 150, 50, 'violet')
    time.sleep(0.001)








win.getMouse()
win.close()

