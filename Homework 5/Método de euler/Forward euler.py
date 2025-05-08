import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # m/s²
b = 0.1  # kg/s
m = 1.0  # kg

# Condições iniciais
v0 = 0.0  # m/s

# Parâmetros numéricos
dt = 0.1  # s
t_max = 10.0  # s
n_steps = int(t_max / dt) + 1

# Arrays para armazenar resultados
t = np.linspace(0, t_max, n_steps)
v_euler = np.zeros(n_steps)
v_euler[0] = v0

# Método de Euler
for i in range(n_steps - 1):
    dvdt = -g - (b/m) * v_euler[i]
    v_euler[i+1] = v_euler[i] + dvdt * dt

# Velocidade terminal teórica
v_terminal = - (m * g) / b

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, v_euler, label='Método de Euler')
plt.axhline(y=v_terminal, color='r', linestyle='--', label='Velocidade terminal teórica')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Queda livre com resistência do ar - Método de Euler')
plt.legend()
plt.grid(True)
plt.show()

# Comparação com velocidade terminal
print(f"Velocidade terminal teórica: {v_terminal:.2f} m/s")
print(f"Velocidade final calculada: {v_euler[-1]:.2f} m/s")