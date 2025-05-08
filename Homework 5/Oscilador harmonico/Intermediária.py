import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

omega0 = 2 * np.pi
T = 1 
t_span = (0, 5) 
y0 = [1.0, 0.0]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

b_vals = [0.5, 4 * np.pi, 10.0] 
labels = ['Subcrítico', 'Crítico', 'Supercrítico']

plt.figure(figsize=(12, 5))

for i, b in enumerate(b_vals):
    def f(t, y):
        x, v = y
        return [v, -omega0**2 * x - b * v]

    sol = solve_ivp(f, t_span, y0, t_eval=t_eval, method='RK45')

    plt.subplot(1, 2, 1)
    plt.plot(sol.t, sol.y[0], label=f'{labels[i]} (b={b})')
    plt.title('x(t)')
    plt.xlabel('t')
    plt.ylabel('x')

    plt.subplot(1, 2, 2)
    plt.plot(sol.t, sol.y[1], label=f'{labels[i]} (b={b})')
    plt.title('v(t)')
    plt.xlabel('t')
    plt.ylabel('v')

plt.subplot(1, 2, 1)
plt.legend()

plt.subplot(1, 2, 2)
plt.legend()

plt.tight_layout()
plt.show()
