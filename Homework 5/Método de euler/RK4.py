import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    
    for i in range(len(t) - 1):
        h = t[i+1] - t[i]
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/2, y[i] + h/2 * k1)
        k3 = f(t[i] + h/2, y[i] + h/2 * k2)
        k4 = f(t[i] + h, y[i] + h * k3)
        
        y[i+1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return y

g = 9.8  
b = 0.1 
m = 1.0 

v0 = 0.0 

dt = 0.1  
t_max = 10.0 
n_steps = int(t_max / dt) + 1
t = np.linspace(0, t_max, n_steps)

def dvdt(t, v):
    return -g - (b/m) * v

v_rk4 = runge_kutta4(dvdt, v0, t)

dts = [0.1, 0.05, 0.01]
plt.figure(figsize=(12, 8))

for dt in dts:
    n_steps = int(t_max / dt) + 1
    t_temp = np.linspace(0, t_max, n_steps)
    
    v_euler_temp = np.zeros(n_steps)
    v_euler_temp[0] = v0
    for i in range(n_steps - 1):
        dvdt_euler = -g - (b/m) * v_euler_temp[i]
        v_euler_temp[i+1] = v_euler_temp[i] + dvdt_euler * dt
    
    v_rk4_temp = runge_kutta4(dvdt, v0, t_temp)
    
    plt.plot(t_temp, v_euler_temp, '--', label=f'Euler, dt={dt}')
    plt.plot(t_temp, v_rk4_temp, '-', label=f'RK4, dt={dt}')

v_terminal = - (m * g) / b

plt.axhline(y=v_terminal, color='blue', linestyle=':', label='Velocidade terminal')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Comparação entre Método de Euler e RK4 para diferentes passos de tempo')
plt.legend()
plt.show()