import math

def bhaskara(a, b, c):
   
    # Verifica se a é diferente de zero
    assert a != 0 
     
    delta = b**2 - 4 * a * c
     
    if delta < 0:
        raise ValueError(" não há raízes reais")
    
     
    sqrt_delta = math.sqrt(delta)
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    
    return x1, x2

 
try:
    x1, x2 = bhaskara(2, 12, -14)
    print('Raízes :', x1, x2)
except ValueError as e:
    print(e)