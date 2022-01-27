# Conversor de base numéricas
num = int(input('Digite um número inteiro: '))
print('Escolha um das bases para conversão:'
      '\n[ 1 ] converter para BINÁRIO'
      '\n[ 2 ] converter para OCTAL'
      '\n[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para BINÁRIO é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente')