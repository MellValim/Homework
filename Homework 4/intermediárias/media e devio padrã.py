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


plt.plot(passos, media_05, label='Média (p=0.5)', color='magenta')
plt.plot(passos, media_06, label='Média (p=0.6)', color='purple')
plt.xlabel('Número de passos')
plt.ylabel('Média da posição')
plt.title('Média da posição em função dos passos')
plt.show()

plt.plot(passos, desvio_05, label='Desvio (p=0.5)', color='magenta')
plt.plot(passos, desvio_06, label='Desvio (p=0.6)', color='purple')
plt.xlabel('Número de passos')
plt.ylabel('Desvio padrão da posição')
plt.title('Desvio padrão da posição em função dos passos')
plt.show()



    
