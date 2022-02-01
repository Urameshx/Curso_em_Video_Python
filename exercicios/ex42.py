# Analisando Triângulos v2.0
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Formam um triângulo equilátero')
    elif r1 != r2 != r3 != r1:
        print('Formam um triângulo escaleno')
    else:
        print('Formam um triângulo isósceles')
else:
    print('Não formam um triângulo!')
