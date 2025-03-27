def fibonacci(n, lista_completa=True):

    
    assert isinstance(n, int)
    
    assert n >= 0
    
    assert isinstance(lista_completa, bool)
    
    if n == 0:
        return [] if lista_completa else 0
    elif n == 1:
        return [0] if lista_completa else 0
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence if lista_completa else fib_sequence[-1]

print(fibonacci(5))
print(fibonacci(5, lista_completa=False))