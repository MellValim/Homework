import matplotlib.pyplot as plt
import numpy as np

def caminhadas(steps, simulations, p):
    all_simulations = []

    for _ in range(simulations):
        pos = [0]
        for _ in range(steps):
            passo = 1 if np.random.rand() < p else -1
            pos.append(pos[-1] + passo)
        all_simulations.append(pos)

    return np.array(all_simulations)

steps = 100
simulations = 100

trajetorias_05 = caminhadas(steps, simulations, p=0.5)
trajetorias_06 = caminhadas(steps, simulations, p=0.6)

passos = np.arange(steps + 1)

plt.figure(figsize=(10, 6))
for traj in trajetorias_05:
    plt.plot(passos, traj, color='magenta', alpha=0.2)
plt.title('100 passeios aleatórios (p=0.5)')
plt.xlabel('Número de passos')
plt.ylabel('Posição')
plt.show()

plt.figure(figsize=(10, 6))
for traj in trajetorias_06:
    plt.plot(passos, traj, color='cyan', alpha=0.2)
plt.title('100 passeios aleatórios (p=0.6)')
plt.xlabel('Número de passos')
plt.ylabel('Posição')
plt.show()
