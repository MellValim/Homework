import random
import matplotlib.pyplot as plt

def pi_monte_carlo(N, retorna_pontos=False):
    dentro_circulo = 0
    dentro = []
    fora = []

    for _ in range(N):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            dentro_circulo += 1
            dentro.append((x, y))
        else:
            fora.append((x, y))

    pi = 4 * dentro_circulo / N

    if retorna_pontos:
        return pi, dentro, fora
    else:
        return pi

N = 10000
aprox_pi, dentro, fora = pi_monte_carlo(N, retorna_pontos=True)

x_dentro, y_dentro = zip(*dentro)
x_fora, y_fora = zip(*fora)

plt.figure(figsize=(7,7))
plt.scatter(x_dentro, y_dentro, color='green', s=1, label='Dentro do círculo')
plt.scatter(x_fora, y_fora, color='purple', s=1, label='Fora do círculo')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title(f"Valor de pi: {aprox_pi:.5f}")
plt.show()

print("O valor de pi é", aprox_pi)