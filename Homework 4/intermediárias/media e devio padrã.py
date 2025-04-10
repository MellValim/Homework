import matplotlib.pyplot as plt
import numpy as np

def randomwalk(steps, simulations, p):
    positions = np.zeros((simulations, steps+1))

    for s in range (simulations):
        pos = [0]

        for _ in range (steps):
            step = 1 if np.random.rand() < p  else -1

            pos.append(pos[-1] + step)

        positions[s] = pos
    media = np.mean(positions, axis = 0)
    desvpad = np.std(positions, axis =0)
                     
    return media, desvpad
    
steps = 100
simulations = 500

media_05, desvio_05 = randomwalk(steps, simulations, p=0.5)
media_06, desvio_06 = randomwalk(steps, simulations, p=0.6)

passos = np.arange(steps + 1)


plt.figure(figsize=(10, 6))

plt.plot(passos, media_05, label='Média (p=0.5)', color='magenta')
plt.fill_between(passos, media_05 - desvio_05, media_05 + desvio_05, color='magenta', alpha=0.2, label='±1σ (p=0.5)')

plt.plot(passos, media_06, label='Média (p=0.6)', color='blue')
plt.fill_between(passos, media_06 - desvio_06, media_06 + desvio_06, color='blue', alpha=0.2, label='±1σ (p=0.6)')

plt.xlabel('Número de passos')
plt.ylabel('Posição média')
plt.title('Média e desvio padrão da posição em função dos passos')
plt.tight_layout()
plt.show()



    
