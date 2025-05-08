import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da corda
L = 1.0       # comprimento
N = 100       # número de pontos
dx = L / (N - 1)
x = np.linspace(0, L, N)
c = 1.0       # velocidade da onda

# Matriz tridiagonal
main_diag = -2.0 * np.ones(N-2)
off_diag = np.ones(N-3)
A = (np.diag(main_diag) +
     np.diag(off_diag, k=1) +
     np.diag(off_diag, k=-1)) / dx**2

# Solução do problema de autovalores
lambdas, phis = np.linalg.eigh(A)

# Frequências naturais:
omega_squared = -c**2 * lambdas
omega = np.sqrt(omega_squared)

# Gráficos dos 4 primeiros modos
plt.figure(figsize=(10, 6))
colors = ['pink', 'magenta', 'blue', 'purple']  # <- aqui você muda as cores

for i in range(4):
    mode_shape = np.zeros(N)
    mode_shape[1:-1] = phis[:, i]  # bordas fixas (zero)
    plt.plot(x, mode_shape, label=f"Modo {i+1}, ω = {omega[i]:.2f}", color=colors[i])

plt.title("Primeiros 4 modos de vibração da corda")
plt.xlabel("x")
plt.ylabel("φ(x)")
plt.legend()
plt.tight_layout()
plt.show()
