from random import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt 

x=[absc for absc in range(0,1001,100)]

    
def somme(tableau):
    s=0
    for i in range(len(tableau)):
        s = s + tableau[i]

    return s

def double_somme(tableau):
    s=[]
    somme=0
    for i in range(len(tableau)):
        s.append(tableau[i])
        for j in range(len(s)):
            somme=somme + s[j]
    return somme
            
        

z=[]
for i in range(1,1002,100):
    a = timer()
    maliste2=somme([ randint(0,100000) for k in range(i)])
    b=timer()
    z.append(b-a)


t=[]


    
plt.plot(x,y,":",color="red",lw=2,label="le_premier")



plt.title("cout des tris")
plt.legend()
plt.show()
