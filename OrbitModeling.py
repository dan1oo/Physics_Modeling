from vpython import *
#Web VPython 3.2

#Setup
from visual import * 
scene = display(width=600, height=600, center=vector(0,0,0), background=color.white) 
"""
This program models simple orbit of a mass(spacecraft, etc.) around a planet and as affected by the gravity of similarly orbiting moons.
"""



G= 6.67*10**(-11) #Gravitational Constant 

#Edit Variables

Prad=   3.0*10**6  #Radius of planet 
Pmass = 3.0*10**24 #Mass of planet

#Creating vector objects
planet=sphere(pos=vec(0,0,0), radius=Prad, color=color.yellow) 
ship=sphere(pos=vec(4.0*Prad,0,0), radius=Prad/3., color=color.green, make_trail=True, trail_type="points", interval=10000) 
moon = sphere(pos = vec(25.0*Prad, 0, 0), radius = Prad/2., color = color.blue, make_trail=True, trail_type="points", interval=10000)
moon2 = sphere(pos = vec(0,20*Prad , 0), radius = Prad/2., color = color.yellow, make_trail=True, trail_type="points", interval=10000)




dt=0.2
t=0.0


#Functions of motion
def uppos(lol):
    #update ship position and velocity
    lol.pos = lol.v*dt+lol.pos
    lol.v = lol.a*dt +lol.v 
    return lol

def upa(lol, lal):
    #update ship acceleration
    lol.a = -G* lal.m/(mag(lol.pos-lal.pos))**2 * (lol.pos-lal.pos)/mag(lol.pos-lal.pos)
    return lol.a

def trt(thrust, lol):
    a = thrust*lol.v/mag(lol.v)
    return a


#Misc object values
planet.m= Pmass  # Mass of planet 
moon.m = planet.m/60.0
moon2.m = planet.m/50.
moon.v = 1633.4*vec(0,1,0)
moon2.v = 1826.2*vec(1,0,0)
ship.m=10000  # Mass of ship 
ship.v= 3000*vec(0,1,0)  # initial velocity of ship
thrust = 3 #m/s^2


#Time function
while t<500000:  #loop to do the following indented code for 50,000 s 
    rate(5000000)   #executes at 1,000,000 Hz
     
    moon.a = upa(moon, planet)+upa(moon, moon2)
    moon = uppos(moon)
    moon2.a = upa(moon2, planet)+ upa(moon2, moon)
    moon2 = uppos(moon2)
    
    ship.a = upa(ship, planet) + upa(ship,moon) + upa(ship, moon2)
    if 1000< t <1500:  #set the on variable to 1.0 between 1000s and 2000s 
      ship.a = ship.a + trt(thrust, ship)
    
    ship = uppos(ship)
    
    dt=100.0/mag(ship.v) 
    t = t+dt
    



