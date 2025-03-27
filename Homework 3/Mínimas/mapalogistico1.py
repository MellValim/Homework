import numpy as np
import matplotlib.pyplot as plt

def mapa_logistico(r, x0, N):
    xn = np.zeros(N + 1) 
    xn[0] = x0 
    
    for n in range(1, N + 1): #N+1 para incluir o x0
        xn[n] = r * xn[n-1] * (1 - xn[n-1])  
    
    return xn.tolist() 

x0 = 0.5 
N = 1000  
r_values = [2, 3.3, 3.5, 3.9]

plt.figure(figsize=(10, 6))

for r in r_values:
    xn = mapa_logistico(r, x0, N)
    n_values = np.arange(N + 1)

    if r == 2:
        plt.plot(n_values, xn, label=f"r = {r}") 
    else:
        plt.scatter(n_values, xn, s=0.5, label=f"r = {r}")

plt.xlabel("n")
plt.ylabel("x_n")
plt.title("Mapa Logístico")
plt.legend()
plt.show()

