# Aumento múltiplos
sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    novo_sal = sal + (sal * 0.15)
else:
    novo_sal = sal + (sal * 0.10)
print(f'Quem ganhava R${sal} passa a ganhar R${novo_sal:.2f}')
