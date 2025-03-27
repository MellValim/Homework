def fatorial_while(n):
  
    assert isinstance(n, int)
    
    assert n >= 0
    
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado


print('Fatorial:', fatorial_while(5))