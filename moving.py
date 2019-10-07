import graphics as gr
from math import *
import random
N=100
SIZE_X=1300
SIZE_Y=700
METRIC_SIZE=100
dt=0.0001
g=9.81*METRIC_SIZE
def writing_traectory(t,ttt,n,x,y):
    if (int(t/dt)% n == 0):
        tt=gr.Text(gr.Point(int(x),int(y)),ttt)
        tt.draw(win)

def dima_mokeev_petuh():
    return('true')
        
def field_B(x,y,t):
    x0=SIZE_X//2
    y0=SIZE_Y//2
    b=-90 * sin(5 * t)  + 0* ((x - x0) ** 2 + (y - y0) ** 2) / 1000 
    if (x > SIZE_X) or (x < 0) or (y < 0) or (y > SIZE_Y):
        b=1000
    return(b)

def magnetic_x(vx,vy,x,y,t,e):
    new_vx=vx-field_B(x,y,t)*vy*dt*e
    return(new_vx)

def magnetic_y(vx,vy,x,y,t,e):
    new_vy=vy+field_B(x,y,t)*vx*dt*e
    return(new_vy)

def gravity_y(vx,vy,x,y):
    new_vy=vy+g*dt
    return(new_vy)

def gravity_x(vx,vy,x,y):
    new_vx=vx
    return(new_vx)

def force_x(vx,vy,x,y,t,e):
    vx = gravity_x(vx,vy,x,y)
    vx = magnetic_x(vx,vy,x,y,t,e)
    return(vx)

def force_y(vx,vy,x,y,t,e):
    vy = gravity_y(vx,vy,x,y)
    vy = magnetic_y(vx,vy,x,y,t,e)
    return(vy)

def draw_lines():
    for i in range(SIZE_X//METRIC_SIZE):
        l=gr.Line(gr.Point(i*METRIC_SIZE,0),gr.Point(i*METRIC_SIZE,SIZE_Y))
        l.draw(win)
    for i in range(SIZE_Y//METRIC_SIZE):
        l=gr.Line(gr.Point(0,i*METRIC_SIZE),gr.Point(SIZE_X,i*METRIC_SIZE))
        l.draw(win)
    
    
win=gr.GraphWin("something",SIZE_X, SIZE_Y)

t=0
vx=0*METRIC_SIZE
vy=0*METRIC_SIZE
x=SIZE_X//2
y=SIZE_Y//2
draw_lines()
x0=x
y0=y
circle = gr.Circle(gr.Point(x, y), 5)
circle.setFill('blue')
circle.draw(win)
e=1

while dima_mokeev_petuh():
    for i in range(N):
        t=t+dt
        vx=force_x(vx,vy,x,y,t,e)
        vy=force_y(vx,vy,x,y,t,e)
        x=x+vx*dt
        y=y+vy*dt
        writing_traectory(t,'.',100,x,y)
    gr.time.sleep(dt*N*0)    
    circle.move(x-x0,y-y0)
    y0=y
    x0=x
