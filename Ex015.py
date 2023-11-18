#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
Dias = int(input('Informe quantos dias foi alugado: '))
Km = float(input('Informe a quantidade de km rodados: '))

PreçoD = Dias * 60
PreçoK = Km * 0,15
PreçoT = PreçoD + PreçoK

print('Preço = {}'.format(PreçoT))

