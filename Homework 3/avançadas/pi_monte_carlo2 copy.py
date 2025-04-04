import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import curve_fit

def pi_monte_carlo(N):
    dentro_circulo = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            dentro_circulo += 1
    return 4 * dentro_circulo / N

def erro_relativo(N_values):
    pi = np.pi
    erros = np.zeros(len(N_values))

    for i, N in enumerate(N_values):
        pi_estimado = pi_monte_carlo(N)
        erros[i] = abs(pi - pi_estimado)/pi

    return erros

def ajuste_erros(N, a, b):
    return a*N**b

N_values = np.logspace(1, 6, num=10)
N_values = np.round(N_values).astype(int)
erros = erro_relativo(N_values)

params, _ = curve_fit(ajuste_erros, N_values, erros)
ajuste_erro_fit = ajuste_erros(N_values, *params)
 

plt.figure(figsize=(10,6))
plt.plot(N_values, erros, label='Erro relativo', marker='o', color='purple')
plt.plot(N_values, ajuste_erro_fit, label='Ajuste', linestyle='--', color = 'pink')
plt.xlabel('N')
plt.ylabel("Erro")
plt.title('Escala linear', fontdict={'fontsize': 16,'fontname': 'Georgia'}, color = 'purple')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.loglog(N_values, erros, label='Erro relativo', marker='o', color='purple')
plt.loglog(N_values, ajuste_erro_fit, label='Ajuste', linestyle='--', color = 'pink')
plt.xlabel('N')
plt.ylabel("Erro")
plt.title('Escala loglog', fontdict={'fontsize': 16,'fontname': 'Georgia'}, color = 'purple')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.semilogx(N_values, erros, label='Erro relativo', marker='o', color='purple')
plt.semilogx(N_values, ajuste_erro_fit, label='Ajuste', linestyle='--', color = 'pink')
plt.xlabel('N')
plt.ylabel("Erro")
plt.title('Escala semilog x', fontdict={'fontsize': 16,'fontname': 'Georgia'}, color = 'purple')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.semilogy(N_values, erros, label='Erro relativo', marker='o', color='purple')
plt.semilogy(N_values, ajuste_erro_fit, label='Ajuste', linestyle='--', color = 'pink')
plt.xlabel('N')
plt.ylabel("Erro")
plt.title('Escala semilog-y', fontdict={'fontsize': 16,'fontname': 'Georgia'}, color = 'purple')
plt.legend()
plt.show()