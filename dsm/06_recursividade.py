# O fatorial de um numero n inteiro > 1 pode ser definido.
#recursivamente, como:
#n! = n * (n - 1)!
#ja o fatorial de n = 1 é definido como 
#1! = 1

#implementação interativa de um fatorial
def fatorial_iter(n):
    resultado = 1
    # range começa em n e  vai descendo até 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado

#implementação recursiva de um fatorial
def fatorial_req(n):
    if n == 1: 
        return 1
    else: 
        return n * fatorial_req(n - 1)
    
    
    _
    ################################
print(f'6! é igual a {fatorial_req(6)}')


####################
def fatorial_overflow(n):
    return n * fatorial_overflow(n - 1)

###aumentando limite maximo de recursao

import sys
sys.setrecursionlimit(1000000)

print(f'-->6! é igual a {fatorial_overflow(5)}')
