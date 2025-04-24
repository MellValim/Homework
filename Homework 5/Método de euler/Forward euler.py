import numpy as np

g = -9.8
a = 0.1 # onde a = b/m
def func(t, v):
    return(g-a*v)

def euler (t0, v, h, t):
    temp = -0

    while t0<t:
        temp = t
        v = v+h*func(t0,v)
        t0 = t0+h

    print("Valor aproximado da solução em v= ", v, "é","%.6f"% v)
    
v0 = 1
t0 = 0
h = 0.5 #stepsize
t = 0.1

euler (t0, v0, h, t)