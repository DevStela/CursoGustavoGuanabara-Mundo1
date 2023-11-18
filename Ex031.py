#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
Distancia = float(input('Informe a distância da viagem: '))

if Distancia <= 200:
    Calc = Distancia * 0,50
    print('Valor = {}'.format(Calc))
else:
    Calc2 = Distancia * 0,45
    print('Valor = {}'.format(Calc2))