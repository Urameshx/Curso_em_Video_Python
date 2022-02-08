# GAME: Pedra, Papel e Tesoura
import random as rd
import time as tm
itens = ('Pedra', 'Papel', 'Tesoura')
computador = rd.choice(itens)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
tm.sleep(0.5)
print('KEN')
tm.sleep(0.5)
print('PO!!!')
tm.sleep(0.5)
print('-=' * 11)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 'Pedra':
    if jogador == 0:      # jogador jogou PEDRA
        print('EMPATE')
    elif jogador == 1:    # jogador jogou PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2:    # jogador jogou TESOURA
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 'Papel':
    if jogador == 0:  # jogador jogou PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1:  # jogador jogou PAPEL
        print('EMPATE')
    elif jogador == 2:  # jogador jogou TESOURA
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 'Tesoura':
    if jogador == 0:  # jogador jogou PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1:  # jogador jogou PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2:  # jogador jogou TESOURA
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')