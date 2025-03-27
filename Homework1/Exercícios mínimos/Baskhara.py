    import math 

    def bhaskara(a, b, c):
        
        delta = b**2 - 4 * a * c
        
        #definir uma condição para quando não há raízes reais
        if delta < 0:
            raise ValueError("A equação não possui raízes reais (delta < 0).")
        
        #calculo do delta e das raízes pela fórmula de baskhara
        sqrt_delta = math.sqrt(delta)
        
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        
        return x1, x2

        #testar se a é divisível por b
    def is_divisor(a, b):    

        if a % b == 0:
            return True
        else:
            return False

    x1, x2 = bhaskara(2, 12, -14)
    print('A primeira raiz é:', x1)
    print('A segunda raiz é:', x2)

    print('divisão', is_divisor(10, 2)) 
    print('divisão', is_divisor(15, 4)) 