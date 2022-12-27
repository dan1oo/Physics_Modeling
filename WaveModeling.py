from vpython import *
#Web VPython 3.2
from visual import * 
N = 101 # N of atoms in set 
spacing = 1 # distance between atoms 
atom_radius = 0.25*spacing  # radius of atom 
scene.center = 0.5*(N-1)*vector(1,0,0)  # center the scene on the middle atom 
mass = 1
K = 1
 
class set:   # define a class of objects to represent set of atoms;  
         
    def __init__(self,  N, atom_radius, spacing ):  
# self is the variable that is equal to the class set, N, radius, spacing 
 
        self.atoms = [ ]  #defines list storing the objects 
        for x in range(0,N,1):  #loop defining objects ... spheres as atoms 
            atom = sphere(radius=atom_radius, color = color.red) # all atoms same radius and color  
            atom.pos=vector(x,0,0)*spacing  #initial position of an atom on x-axis 
            atom.v = vec(0,0,0)  # give each atom a random velocity 
            atom.force = vec(0,0,0)
            self.atoms.append( atom )  #add each atom to list 
 
c = set(N, atom_radius, spacing) # the variable c is assigned to the set; in the class it is self 
def y(t,A,f):
    return vec(0, A*sin(2*pi*t/(f)),0)
    
    
dt=.005  #time step 
t=0  #time 
while t<1000:  #time loop 
      c.atoms[0].pos =  y(t, 5, 2*N)
      i=1 
      while i<N-1: 
            c.atoms[i].force=  -K*(c.atoms[i].pos-c.atoms[i-1].pos)-K*(c.atoms[i].pos-c.atoms[i+1].pos)
            i=i+1 
 
      i=0  #list position for first atom 
      rate(10000) 
      
      while i<N:     #updating position for each atom
            c.atoms[i].v = c.atoms[i].v + c.atoms[i].force*dt/mass
            c.atoms[i].pos=c.atoms[i].pos+c.atoms[i].v*dt 
            i=i+1     
      t=t+dt 
      
      
      
      
      