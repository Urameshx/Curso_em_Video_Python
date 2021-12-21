# Calculando descontos
preço_produto = float(input('Qual é o preço do produto? R$'))
preço_promoção = preço_produto - (preço_produto * 0.05)
print(f'O produto que custava R${preço_produto}, na promoção com desconto de 5% vai custar R${preço_promoção:.2f}')
