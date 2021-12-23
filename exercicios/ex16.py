# Quebrando um número
''' # Outra forma de fazer
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}') '''

from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')



