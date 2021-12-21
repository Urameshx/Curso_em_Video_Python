# Reajuste Salarial
salario_funcionario = float(input('Qual é o salário do funcionário? R$'))
aumento_salario = (salario_funcionario * 0.15) + salario_funcionario
print(f'Um funcionário que ganhava R${salario_funcionario:.2f}, com 15% de aumento,'
      f' passa a receber R${aumento_salario:.2f}')
