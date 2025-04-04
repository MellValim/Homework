import numpy as np
import matplotlib.pyplot as plt

def logisticmap(r, x0, N):
    xn = np.zeros(N)
    xn[0] = x0
    for n in range(1, N):
        xn[n] = r * xn[n-1] * (1 - xn[n-1])
    return xn

plt.ion()  # Ativar modo interativo

M = 20000
N = M + 1000
x0 = 0.5
r_values = np.arange(1, 4, 0.1)

plt.figure(figsize=(10,6))

for r in r_values:
    xn = logisticmap(r, x0, N)
    plt.plot(r * np.ones(M), xn[-M:], 'k.', markersize=0.5)
    plt.pause(0.01)  # Atualiza o gráfico dinamicamente

plt.xlabel("r", color = 'purple')
plt.ylabel("$x_n$", color = 'purple')
plt.title("Mapa Logístico", fontdict={'fontsize': 16,'fontname': 'Georgia'}, color = 'purple')
plt.grid(True)
plt.show(block=True)

logisticmap()