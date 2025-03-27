def fatorial_recursivo(n):
   
    assert isinstance(n, int)
    
    assert n >= 0
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)


print('Fatorial recursivo:', fatorial_recursivo(5))