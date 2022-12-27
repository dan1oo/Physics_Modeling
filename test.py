from vpython import *
#Web VPython 3.2
from visual import * 
scene = display(width=600, height=600, center=vector(0,0,0), background=color.white) 
# The origin and tips of vectors A and B 
origin=vector(0,0,0) 
A=vector(1,1,0) 
B=vector(1.5,-1.5,0) 
Aarrow=arrow(pos=origin, axis=A, color=color.blue, shaftwidth = 0.1) 
Barrow=arrow(pos=origin, axis=B, color=color.green, shaftwidth = 0.1) 
r = A-B
rarrow = arrow(pos = origin, axis = r, color = color.red, shaftwidth = 0.1)
ball=sphere(pos=B, radius=0.2, color=color.yellow) 
unitr=r/mag(r) 
ball.v=0.1*unitr 
#Making the ball move from B to A 
dt=0.005    # a small time step i.e. 0.005 s 
tend=mag(r)/mag(ball.v)    # tend is the time it takes for a ball to travel the distance from B to A 
t=0.0          # start time t at zero seconds 
ball.a= 0.1*unitr  #vector for acceleration of ball  
while t<tend:  #loop to do the following indented code over and over until t > tend 

     rate(1000)   #executes code only at 1000Hz (slows the motion enough to be seen) 
     ball.pos=ball.pos+ball.v*dt  #updates the ball position after dt has passed 
     ball.v=ball.v+ball.a*dt  #update the ball velocity after dt has passed
     t=t+dt  #increase time t by dt 

