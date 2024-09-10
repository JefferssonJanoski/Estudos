def pertence_fibonacci(num):
    a, b = 0, 1 #inicio da sequencia
    
    if num == 0 or num == 1:
        return True
    
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

numero = int(input('Informe um número: '))

if pertence_fibonacci(numero):
    print('\nO número {} pertence à sequência de Fibonacci.'.format(numero))
else:
    print('\nO número {} não pertence à sequência de Fibonacci.'.format(numero))
