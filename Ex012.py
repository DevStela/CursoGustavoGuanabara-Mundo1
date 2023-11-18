#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Preco = float(input('Informe o preço: '))

Desconto = Preco - (Preco * 5 / 100)

print('Desconto = {}'.format(Desconto))

