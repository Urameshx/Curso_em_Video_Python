# Sorteando um item na lista
from random import choice
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
todos_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = choice(todos_alunos)
print(f'O aluno escolhido foi {aluno_escolhido}')





