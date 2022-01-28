# Alistamento militar
import datetime as dt
ano_atual = dt.date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade_atual = ano_atual - ano_nasc  # Calculo da idade atual
print(f'Quem nasceu em {ano_nasc} tem {idade_atual} anos em {dt.date.today().year}')
ano_de_alistamento = ano_nasc + 18  # Calculo do ano necessário para se alistar
if ano_de_alistamento > ano_atual:
    periodo_alistamento = ano_de_alistamento - ano_atual
else:
    periodo_alistamento = ano_atual - ano_de_alistamento
if idade_atual > 18:
    print(f'Você já deveria ter se alistado há {periodo_alistamento} anos'
          f'\nSeu alistamento foi em {ano_de_alistamento}')
elif idade_atual == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Ainda faltam {periodo_alistamento} ano(s) para o alistamento'
          f'\nSeu alistamento será em {ano_de_alistamento}')


