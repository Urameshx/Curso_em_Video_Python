# Aprovando Empréstimo
val_casa = float(input('Valor da casa: R$'))
sal_comprador = float(input('Salário do comprador: R$'))
anos_financ = int(input('Quantos anos de financiamento? '))
parc_mensal = val_casa / (anos_financ * 12)
minimo = sal_comprador * 0.3
print(f'Para pagar uma casa de R${val_casa:.2f} em {anos_financ} anos, '
      f'a prestação será de R${parc_mensal:.2f}')
if parc_mensal <= minimo:
    print('Empréstimo aceito')
else:
    print('Empréstimo negado')