def bhaskara(a, b, c):

    #para casos especiais onde a=b=c=0, o output é um erro
    if a == 0:
        if b == 0:
            if c == 0:
                return (0, 0)
            else:
                raise ValueError("A equação não possui solução.")

    #caso haja apenas um valor possível para x
        else:
            x = -c / b
            return (x, x)
    
  
    delta = b**2 - 4 * a * c
    
    #para raízes complexas
    if delta < 0:
        real_part = -b / (2 * a)
        imaginary_part = (-delta) ** 0.5 / (2 * a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)

    #raízes reais
    else:
    
        sqrt_delta = delta**0.5
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
    
    return x1, x2


print('Raízes:', bhaskara(1, 2, 3))  # Raízes complexas
