def fatorial(n):
   
    # verificar se n é um número inteiro
    assert isinstance(n, int)
    
    # Verifica se n é não negativo
    assert n >= 0
    
    if n == 0 or n == 1: 
        return 1
    else:
        return n * fatorial(n - 1)


print('Fatorial :', fatorial(5))