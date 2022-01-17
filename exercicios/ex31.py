# Custo da Viagem
dist_viagem = float(input('Qual é a distância da viagem: '))
print(f'Você está prestes a começar uma viagem de {dist_viagem}Km')
if dist_viagem <= 200:
    preco_passagem = dist_viagem * 0.50
else:
    preco_passagem = dist_viagem * 0.45
print(f'E o preço da passagem será de R${preco_passagem:.2f}')

