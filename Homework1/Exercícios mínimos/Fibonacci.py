def fibonacci(n):
    
    # Inicializa a lista com os dois primeiros números da sequênci
    fib_sequence = [0, 1]
    
    # Verifica se o valor de n é 0 ou 1 e retornando uma lista
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    # gerar os próximos números da sequência
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    # Retorna a lista 
    return fib_sequence

print('5 primeiros termos', fibonacci(5))

# Armazena a sequência dos 20 primeiros números de Fibonacci na variável f
f = fibonacci(20)
print('20 primeiros termos:', f)

# Define um número e armazena a sequência dos 30 primeiros números de Fibonacci na variável f
numero = 30
f = fibonacci(numero)
print(f'Sequência dos {numero} primeiros números de Fibonacci: {f}')