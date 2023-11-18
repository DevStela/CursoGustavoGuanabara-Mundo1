#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
Largura = float(input('Informe a largura da parede: '))
Altura = float(input('Informe a altura da parede: '))

Area = Largura * Altura
Tinta = Area / 2

print('Quantidade de tinta = {}'.format(Tinta))
