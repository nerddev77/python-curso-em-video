larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print(f'Sua parede tem a dimensão de {larg} X {alt} e sua área é de {área}m²')
tinta = área / 2
print(f'Para pintar essa parede você vai precisar de {tinta :.2f}l de tinta')
