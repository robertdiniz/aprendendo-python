#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura da sua parede: '))
altura = float(input('Altura da sua parede: '))
print(f'Sua parede tem a dimensão de {largura}x{altura}\n sua área é de {largura*altura:.3f}m²')
print(f'Para pintar essa parede, você precisará de {(largura*altura)/2}l de tinta.')