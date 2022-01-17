# Radar eletrônico
velocidade = float(input('Qual é a velocidade atual do carro? '))
limite = 80
if velocidade > limite:
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h' 
          f'\nVocê deve pagar uma multa de {multa}')
else:
    print('Tenha um bom dia! Dirija com segurança')
