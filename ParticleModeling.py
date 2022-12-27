from vpython import *
#Web VPython 3.2

#Setu-p
from visual import * 
scene = display(width=600, height=600, center=vector(0,0,0), background=color.white) 
G=6.67*10**(-11) # Gravitational Constant 
K=8.987552e9 # Coulomb Constant 
ball1rad=.1  # Radius of ball one 
ball2rad=.1  # Radius of ball two 
 
ball1= sphere(pos=vec(0,0,0), radius=ball1rad, color=color.green, make_trail=True, 
trail_type="points", interval=100)  # position is the origin 
ball2= sphere(pos=vec(-4,0.1,0), radius=ball2rad, color=color.red, make_trail=True, 
trail_type="points", interval=100) # position is -5 meters on the x-axis 
 
ball1.m=3.0  # Mass of ball 1 
ball2.m=3.0  # Mass of ball 2 
ball1.q=5*10**(-6)  # Charge of ball 1 in Coulombs 
ball2.q=5*10**(-6)  # Charge of ball 2 in Coulombs 
ball2.v = vec(0.5,0.1,0.2)
ball1.v = vec(-0.2,0.1,-0.5)
ball1.a = vec(0,0,0)
ball2.a = vec(0,0,0)

dt=0.09
t=0.0

def colaw(lol, lal):
    r= lol.pos-lal.pos
    return (K * (lol.q) * (lal.q)*(r/mag(r))/((mag(lol.pos-lal.pos))**2))
    
def uppos(lol):
    #update ship position and velocity
    lol.pos = lol.v * dt+lol.pos
    lol.v = lol.a*dt +lol.v 
    return lol
#def upa2(lol, lal, lel):
#    lol.a = -G* lal.m/(mag(lol.pos-lal.pos))**2 * (lol.pos-lal.pos)/mag(lol.pos-lal.pos)+-G* lel.m/(mag(lol.pos-lel.pos))**2 * (lol.pos-lel.pos)/mag(lol.pos-lel.pos)
#    return lol
def upa(lol, lal):
    lol.a = colaw(lol, lal)/lol.m
    return lol.a



label( pos= vec(-3,4,0), text= ("P1xi: " +str(ball1.m*ball1.v.x )))  ## prints above origin
label( pos= vec(0,4,0), text= ("P1yi: " +str(ball1.m*ball1.v.y )))  ## prints above origin
label( pos= vec(-3,3.5,0), text= "P2xi: " +str(ball2.m*ball2.v.x ))  ## prints above origin
label( pos= vec(0,3.5,0), text= "P2yi: " +str(ball2.m*ball2.v.y ))  ## prints above origin
label( pos= vec(3,4,0), text= "E1i: " +str((ball1.m*ball1.v.x)**2/(2*ball1.m) ))  ## prints above origin
label( pos= vec(3,3.5,0), text= "E2i: " +str((ball2.m*ball2.v.x)**2/(2*ball2.m) ))  ## prints above origin

while mag(ball1.pos-ball2.pos)<=5:   
    rate(50)   #executes at 1,000,000 Hz
    
    ball1.a = upa(ball1, ball2)
    ball2.a = upa(ball2, ball1)
    
    
    ball1 = uppos(ball1)
    ball2 = uppos(ball2)
    
    
    
    
    
  
    t = t+dt



label( pos= vec(-3,-4,0), text= ("P1xf: " +str(ball1.m*ball1.v.x )))  ## prints above origin
label( pos= vec(0,-4,0), text= ("P1yf: " +str(ball1.m*ball1.v.y )))  ## prints above origin
label( pos= vec(-3,-3.5,0), text= "P2xf: " +str(ball2.m*ball2.v.x ))  ## prints above origin
label( pos= vec(0,-3.5,0), text= "P2yf: " +str(ball2.m*ball2.v.y ))  ## prints above origin
label( pos= vec(3,-4,0), text= "E1f: " +str((ball1.m*ball1.v.x)**2/(2*ball1.m) ))  ## prints above origin
label( pos= vec(3,-3.5,0), text= "E2f: " +str((ball2.m*ball2.v.x)**2/(2*ball2.m) ))  ## prints above origin




