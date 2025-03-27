import numpy as np

def fatorial(n):

    x = 1
    for i in range(1, n + 1):
        x *= i

    return x

f10 = fatorial(10)
print(f'O fatorial de 10 é {f10}')

f0 = fatorial(0)
print('O fatorial de 0 é', f0)