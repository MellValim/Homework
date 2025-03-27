import numpy as np
import matplotlib.pyplot as plt
import random

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
    erros = []
    
    for N in N_values:
        pi_estimado = pi_monte_carlo(N)
        erro = abs(pi - pi_estimado) / pi
        erros.append(erro)
    
    return erros

N_values = [10, 100, 1000, 10000, 100000, 1000000]

erros = erro_relativo(N_values)

plt.figure(figsize=(10, 6))
plt.plot(N_values, erros, label='Erro Relativo', marker='o')
plt.xlabel('Número de Pontos (N)')
plt.ylabel('Erro Relativo (E_N)')
plt.title('Erro Relativo em Função de N (Escala Linear)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.loglog(N_values, erros, label='Erro Relativo', marker='o')
plt.xlabel('Número de Pontos (N)')
plt.ylabel('Erro Relativo (E_N)')
plt.title('Erro Relativo em Função de N (Escala Log-Log)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.semilogx(N_values, erros, label='Erro Relativo', marker='o')
plt.xlabel('Número de Pontos (N)')
plt.ylabel('Erro Relativo (E_N)')
plt.title('Erro Relativo em Função de N (Escala Semi-Log X)')
plt.grid(True)
plt.legend()
plt.show()

coeffs = np.polyfit(np.log10(N_values), np.log10(erros), 1)
erro_ajustado = 10**(coeffs[1]) * (np.array(N_values) ** coeffs[0])

plt.figure(figsize=(10, 6))
plt.loglog(N_values, erros, label='Erro Relativo', marker='o')
plt.loglog(N_values, erro_ajustado, label='Ajuste', linestyle='--')
plt.xlabel('Número de Pontos (N)')
plt.ylabel('Erro Relativo (E_N)')
plt.title('Erro Relativo com Ajuste Log-Log')
plt.grid(True)
plt.legend()
plt.show()
