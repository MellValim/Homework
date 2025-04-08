import random
import matplotlib.pyplot as plt
import numpy as np

def randomwalk(n):
    
    x = [0]
    y = [0]
    a = 0.6
    b = -0.6

    for i in range(1, n + 1):
        step = a+(b-a)*np.random.rand()
        xposition = x[-1]+step

        x.append(xposition)
        y.append(i)

    plt.plot(y, x, c='magenta')
    plt.title('O andar do bêbado', fontdict={'fontsize': 15,'fontname': 'Georgia'})
    plt.xlabel('Número de passos', fontdict={'fontsize': 16,'fontname': 'Georgia'})
    plt.ylabel('Posição', fontdict={'fontsize': 16,'fontname': 'Georgia'})
    plt.grid(True)
    plt.show()

    return x, y

print(randomwalk(1000))
    
    
    