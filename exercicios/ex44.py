# Gerenciador de Pagamentos
preco_compra = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
      preco_com_desconto = preco_compra - (preco_compra * 0.1 )
      print(f'Sua compra de R${preco_compra:.2f} vai custar R${preco_com_desconto:.2f} no final.')
elif opcao == 2:
     preco_com_desconto = preco_compra - (preco_compra * 0.05 )
     print(f'Sua compra de R${preco_compra:.2f} vai custar R${preco_com_desconto:.2f} no final.')
elif opcao == 3:
      parcela = preco_compra / 2
      print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.'
            f'\nA compra de R${preco_compra} vai custar R${preco_compra:.2f} no final. ')
elif opcao == 4:
      preco_com_juros = preco_compra + (preco_compra * 0.2 )
      total_parcela = int(input('Quantas parcelas? '))
      parcela = preco_com_juros / total_parcela
      print(f'Sua compra será parcelada em {total_parcela}x de R${parcela:.2f} COM JUROS.'
            f'\nA compra de R${preco_compra:.2f} vai custar R${preco_com_juros:.2f} no final.')
else:
      print('Escolha uma opção válida')

