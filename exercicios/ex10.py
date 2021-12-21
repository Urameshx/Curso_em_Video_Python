#Conversor de moedas
real = float(input('Quanto dinheiro você tem na carteira? R$'))
real_dolar = real / 6
print(f'Com R${real:.2f} você pode comprar US${real_dolar:.2f} ')