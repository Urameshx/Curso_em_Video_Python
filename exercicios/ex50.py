soma = 0
cont = 0
for i in range(1,7):
    num = int(input(f'Digite o {i}ºvalor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} número(s) e a soma dele(s) é igual a {soma}')