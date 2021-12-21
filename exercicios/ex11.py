# Pintando parede
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
pintura = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.3f}m²')
print(f'Para pintar essa parede, você precisará de {pintura:.2f}l de tinta')
