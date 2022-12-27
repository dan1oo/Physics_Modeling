from vpython import *
#Web VPython 3.2
from visual import * 
scene = display(width=600, height=600, center=vector(0,0,0), background=color.white) 
# The origin and tips of vectors A and B 
surface= box(pos=vec(0,0,0), length=12, height=0.1, width=0) 
origin=vector(0,0,0) 


ball=sphere(pos=origin, radius=0.1, color=color.yellow, make_trail=True, trail_type="points") 

v =20
theta= 0.5
ball.v=vector(v*cos(theta),v*sin(theta),0)
#Making the ball move from B to A 
dt=0.0005    # a small time step i.e. 0.005 s 
   # tend is the time it takes for a ball to travel the distance from B to A 
t=0.0          # start time t at zero seconds 
b = -0.15
c =0.075
ball.a= vector(0, -9.8, 0)+ b*ball.v + c*mag(ball.v)* cross(ball.v, vector(0,0,-1))  #vector for acceleration of ball
varrow = arrow(pos = ball.pos, axis = ball.v, color = color.purple, shaftwidth = 0.05)
aarrow = arrow(pos = ball.pos, axis = ball.a, color = color.yellow, shaftwidth =0.05)

while ball.pos.y >= 0.0:  #loop to do the following indented code over and over until t > tend 

     rate(2000)   #executes code only at 1000Hz (slows the motion enough to be seen) 
     ball.pos=ball.pos+ball.v*dt  #updates the ball position after dt has passed 
     ball.v=ball.v+ball.a*dt  #update the ball velocity after dt has passed
     varrow.pos = ball.pos
     varrow.axis = ball.v
     aarrow.pos = ball.pos
     
     ball.a = vector(0, -9.8,0) + b*ball.v+ c*mag(ball.v)* cross(ball.v, vector(0,0,-1))
     aarrow.axis = ball.a
     t=t+dt  #increase time t by dt 
     
range= str(ball.pos.x)  ## converts variable to string for printing in label 
label( pos=ball.pos+vec(0,-1.0,0), text=range )  ## prints range 
     
