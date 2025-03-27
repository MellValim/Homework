def fibonacci(n, lista_completa=True):
  
    #verificar se n é um número inteiro
    assert isinstance(n, int) 
    
    #verificar se lista_completa é booleano
    assert isinstance(lista_completa, bool) 
    
    #verificar se n é não negativo
    assert n >= 0
    
    if n == 0:
        return [] if lista_completa else 0
    elif n == 1:
        return [0] if lista_completa else 0
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence if lista_completa else fib_sequence[-1]

print('Sequência de Fibonacci é:', fibonacci(5))
