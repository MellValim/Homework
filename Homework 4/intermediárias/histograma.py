import matplotlib.pyplot as plt
import numpy as np
import random

def random_walks(steps, simulations, p):
    positions = np.zeros((simulations, steps + 1))

    for s in range(simulations):
        pos = [0]

        for _ in range(steps):
            step = 1 if np.random.rand() < p else -1
            pos.append(pos[-1] + step)
        positions[s] = pos

    media = np.mean(positions, axis=0)
    desvio = np.std(positions, axis=0)

    return positions, media, desvio

steps = 100
simulations = 100

positions_05, media_05, desvio_05 = random_walks(steps, simulations, p=0.5)
positions_06, media_06, desvio_06 = random_walks(steps, simulations, p=0.6)

passos = np.arange(steps + 1)

plt.figure(figsize=(10, 6))

plt.plot(passos, media_05, label='Média (p=0.5)', color='blue')
plt.fill_between(passos, media_05 - desvio_05, media_05 + desvio_05, color='blue', alpha=0.2)

plt.plot(passos, media_06, label='Média (p=0.6)', color='magenta')
plt.fill_between(passos, media_06 - desvio_06, media_06 + desvio_06, color='magenta', alpha=0.2)

plt.title('Média e desvio padrão da posição ao longo do tempo')
plt.xlabel('Número de passos')
plt.ylabel('Posição média')
plt.tight_layout()
plt.show()

def plot_histogramas(positions, titulo, cor):
    plt.figure(figsize=(10, 6))

    plt.hist(positions[:, 0], bins=30, alpha=0.5, label='Início', color='gray')
    plt.hist(positions[:, steps // 2], bins=30, alpha=0.5, label='Meio', color=cor)
    plt.hist(positions[:, -1], bins=30, alpha=0.5, label='Final', color='black')

    plt.title(titulo)
    plt.xlabel('Posição')
    plt.ylabel('Número de caminhantes')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_histogramas(positions_05, 'Histogramas da posição (p=0.5)', 'blue')

plot_histogramas(positions_06, 'Histogramas da posição (p=0.6)', 'green')
