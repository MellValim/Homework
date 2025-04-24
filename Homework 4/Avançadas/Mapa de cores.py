import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import Normalize

def random_walks(steps, simulations, p):
    positions = np.zeros((simulations, steps + 1))

    for s in range(simulations):
        pos = [0]

        for _ in range(steps):
            step = 1 if np.random.rand() < p else -1
            pos.append(pos[-1] + step)
        positions[s] = pos

    return positions

steps = 100
simulations = 100
p=0.6

positions = random_walks(steps, simulations, p)

#intervalo de posições
min_pos = int(np.min(positions))
max_pos = int(np.max(positions))
bins = np.arange(min_pos - 1, max_pos +2 )

histograma = []

for t in range(steps + 1):
    hist, _ = np.histogram(positions[:, t], bins=bins)
    histograma.append(hist)

    heatmap = np.array(histograma)

norm = Normalize(vmin=0, vmax=np.max(heatmap))

plt.figure(figsize=(12, 6))
plt.imshow(heatmap.T, aspect='auto', cmap='plasma', origin='lower', 
           extent=[0, steps, bins[0], bins[-1]], norm=norm)
plt.colorbar()
plt.title(f'Evolução do histograma das posições (p={p})')
plt.xlabel('Passo')
plt.ylabel('Posição')
plt.grid(False)
plt.tight_layout()
plt.show()