#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Dinheiro =  float(input('Informe a quantidade de dinheiro que você tem: '))
Cotacao = float(input('Informe a cotação do dólar atualmente: '))

Quantidade = Dinheiro / Cotacao

print('Quantidade = {}'.format(Quantidade))

