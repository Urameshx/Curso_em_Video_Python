# Maior e menor valores
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))
# Verificando quem é menor
if valor1 < valor2 and valor3:
    print(f'O menor valor digitado foi {valor1}')
elif valor2 < valor1 and valor3:
    print(f'O menor valor digitado foi {valor2}')
else:
    print(f'O menor valor digitado foi {valor3}')
# Verificando quem é maior
if valor1 > valor2 and valor3:
    print(f'O maior valor digitado foi {valor1}')
elif valor2 > valor1 and valor3:
    print(f'O maior valor digitado foi {valor2}')
else:
    print(f'O maior valor digitado foi {valor3}')

'''
# outra possibilidade de fazer
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
# verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
'''
