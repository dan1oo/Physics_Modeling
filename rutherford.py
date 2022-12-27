from vpython import *
#Web VPython 3.2

#Setu-p
from visual import * 
scene = display(width=600, height=600, center=vector(0,0,0), background=color.white) 
G=6.67*10**(-11) # Gravitational Constant 
k=8.987552e9 # Coulomb Constant 
goldrad=7.e-15  # Radius of gold nucleus 
alpharad=7.e-15  # Radius of alpha particle 
gold= sphere(pos=vec(0,0,0), radius=goldrad, color=color.green, make_trail=True, 
trail_type="points",interval=100) 
 
alpha= sphere(pos=vec(-200*goldrad,0,0), radius=alpharad, color=color.red, 
make_trail=True, trail_type="points",interval=100) 
 
gold.m=197.*1.67e-27  # Mass of gold nucleus 
alpha.m=4.*1.67e-27  # Mass of alpha 
gold.q=79.*1.6e-19  # Charge of gold 
alpha.q=2.0*1.6e-19  # Charge of alpha 
alpha.v=vec(1e7,0,0)  # velocity of alpha particle 

dt=10**(-23)
t=0.0



def colaw(lol, lal):
    return (K * (lol.q) * (lal.q)*(lol.pos-lal.pos)/((mag(lol.pos-lal.pos))**2))
    
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

j=0 
while j < 101:   #outer loop which sets initial positions, velocities of the alpha particles 
    j=j+1 # counter for the number of the alpha particle, e.g. 1st, 2nd, 3rd, ... 
    alpha.pos=vec(-200*goldrad,-(200-4*j)*goldrad,0)  # different for each alpha 
    r=alpha.pos-gold.pos  # initial relative position vector 
    alpha.v=vec(1e7,0,0)   # resets it to same initial value for each alpha 
    alpha.a= k*gold.q*alpha.q/alpha.m/mag(r)/mag(r)*r/mag(r) #initial alpha acceleration 
    t=0  # start time at zero seconds for each alpha particle 
    while t<29e-20:  #inner time loop for collision of one alpha particle with gold atom 
        rate(100000000)     
        alpha.pos=alpha.pos+alpha.v*dt  #update the alpha position after dt has passed 
        alpha.v=alpha.v+alpha.a*dt  #update the alpha velocity after dt has passed 
        r=alpha.pos-gold.pos  # new relative position vector 
        alpha.a= k*gold.q*alpha.q/alpha.m/mag(r)/mag(r)*r/mag(r) #new alpha acceleration 
        t=t+dt  #increase time by dt








