import numpy as np
import matplotlib.pyplot as plt
import time

def pi_monte_carlo_vetorizado(N):
    x, y = np.random.uniform(-1, 1, (2, N))
    return 4 * np.sum(x**2 + y**2 <= 1) / N

def pi_monte_carlo_lento(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    cond = x**2 + y**2 <= 1
    return 4 * np.count_nonzero(cond) / N

def medir_tempo(func, N_array):
    tempos = []
    for N in N_array:
        inicio = time.time()
        func(N)
        fim = time.time()
        tempos.append(fim - inicio)
    return np.array(tempos)

N_values = np.logspace(1, 6, num=10, dtype=int)

tempos_vetorizado = medir_tempo(pi_monte_carlo_vetorizado, N_values)
tempos_lento = medir_tempo(pi_monte_carlo_lento, N_values)

plt.figure(figsize=(10, 5))
plt.loglog(N_values, tempos_vetorizado, 'o-', label='Vetorizado', color='blue')
plt.loglog(N_values, tempos_lento, 's--', label='Com loops', color='magenta')
plt.xlabel('N (Número de pontos)')
plt.ylabel('Tempo de execução (s)')
plt.title("Comparação de tempo de execução", fontdict={'fontsize': 16,'fontname': 'Georgia'})
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.show()
