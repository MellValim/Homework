import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L = 1.0
c = 1.0
N = 200
x = np.linspace(0, L, N)
t_max = 2
fps = 60
frames = t_max * fps
dt = t_max / frames

modes = 4
phi = [np.sin(n * np.pi * x / L) for n in range(1, modes+1)]
omega = [n * np.pi * c / L for n in range(1, modes+1)]
colors = ['red', 'green', 'blue', 'purple']

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
lines = []

for ax, n, color in zip(axs.flat, range(modes), colors):
    ax.set_xlim(0, L)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title(f'Modo {n+1}')
    line, = ax.plot([], [], color=color)
    lines.append(line)

fig2, ax2 = plt.subplots(figsize=(8, 4))
line_combo, = ax2.plot([], [], color='black')
ax2.set_xlim(0, L)
ax2.set_ylim(-1.5, 1.5)
ax2.set_title("Combinação dos modos (3f)")

def update(frame):
    t = frame * dt
    for n in range(modes):
        y = phi[n] * np.cos(omega[n] * t)
        lines[n].set_data(x, y)
    
    combo = sum((1 / (n+1)**2) * phi[n] * np.cos(omega[n] * t) for n in range(modes))
    line_combo.set_data(x, combo)

    return lines + [line_combo]

ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=1000/fps)
ani_combo = FuncAnimation(fig2, update, frames=frames, blit=True, interval=1000/fps)

plt.show()
