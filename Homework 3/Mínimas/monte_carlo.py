import random

def monte_carlo_pi(n):
  dentro_circulo = 0
  for i in range(n):

    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2+y**2<=1:
      dentro_circulo +=1
  return 4*dentro_circulo/n

N = 1000000
aprox_pi = monte_carlo_pi(N)

print("o valor aproximado de pi é", aprox_pi)