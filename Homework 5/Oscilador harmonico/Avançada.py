import numpy as np
import matplotlib.pyplot as plt

omega0 = 2 * np.pi
b = 0.5 
dt = 0.001
t_max = 5
n_steps = int(t_max / dt)
t = np.linspace(0, t_max, n_steps)

x0 = 1.0
v0 = 0.0

x = np.zeros(n_steps)
v = np.zeros(n_steps)
a = np.zeros(n_steps)

x[0] = x0
a[0] = -omega0**2 * x0 - b * v0

x[1] = x[0] + v0 * dt + 0.5 * a[0] * dt**2

for n in range(1, n_steps - 1):
    v[n] = (x[n] - x[n-1]) / dt
    a[n] = -omega0**2 * x[n] - b * v[n]
    x[n+1] = 2 * x[n] - x[n-1] + dt**2 * a[n]

v[-1] = (x[-1] - x[-2]) / dt

plt.figure(figsize=(10, 4))
plt.plot(t, x, label='x(t) - Verlet')
plt.plot(t, v, label='v(t) - derivada de x', linestyle='--')
plt.xlabel('t')
plt.title('Oscilador harmônico amortecido (Verlet)')
plt.legend()
plt.tight_layout()
plt.show()
