# Jogo da Adivinhação v.1.0
import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num_bet = int(input('Em que número eu pensei? ')) # número que o usuário aposta
print('PROCESSANDO...')
sleep(2)
num_random = random.randint(0,5) # número que o pc escolhe aleatoriamente
if num_bet == num_random:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num_random} e não no {num_bet}!')


