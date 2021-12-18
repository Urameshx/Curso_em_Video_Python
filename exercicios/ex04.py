#Dissecando uma variável
palavra = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(palavra)}')
print('Só tem espaços?', palavra.isspace())
print('É um número?', palavra.isnumeric())
print('É alfabético?', palavra.isalpha())
print('É alfanumérico?', palavra.isalnum())
print('Está em letras maiúsculas?', palavra.isupper())
print('Está em letras minúsculas?', palavra.islower())
print('Está capitalizada?', palavra.istitle())


