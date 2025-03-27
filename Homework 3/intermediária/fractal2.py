import numpy as np
import matplotlib.pyplot as plt

#cria uma função para o mapa logístico (ja inclui os valores de x, N e M na inicialização da função)
def logisticmap(x0 = 0.5,N = 10000, M = 1000):
    valores_r = np.arange(1, 5, 0.01) # de 1 a 4 em passos de 0.01

    for r in valores_r:
        xn=np.zeros(N) #um array de zeros (para ser preenchido) de tamanho N
        xn[0]=x0 #valor inicial

        for n in range(1, N): #define os valores de xn de acordo com a quação
            xn[n]= r * xn[n-1] * (1 - xn[n-1])

        plt.plot(r*np.ones(M), xn[-M:], 'm.', markersize=0.5 ) #plota r em um array (por isso *np.ones), seleciona apenas os últimos valores de M

    #plotar o gráfico
    plt.xlabel("r")
    plt.ylabel("x")
    plt.title("Mapa logístico")
    plt.show()

#chamar a função
logisticmap()

