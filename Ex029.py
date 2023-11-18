# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
Velocidade = float(input('Informe a velociade do carro: '))

if Velocidade <= 80:
    print('Você está na velocidade certa! Parabéns')
elif Velocidade > 80:
    print('vôce foi multado!')
    Multa = (Velocidade - 80) * 7
    print('Multa = {}'.format(Multa))

