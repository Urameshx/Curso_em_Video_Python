# Aluguel de carros
dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
preço_aluguel = (dias_alugados * 60) + (km_rodados * 0.15)
print(f'O total a pagar é de R${preço_aluguel:.2f}')

'''
Outra forma de fazer
dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
preço_dia = dias_alugados * 60
preço_km = km_rodados * 0.15
preço_aluguel = preço_km + preço_dia
print(f'O total a pagar é de R${preço_aluguel:.2f}')
'''

