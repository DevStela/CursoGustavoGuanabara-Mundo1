#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
Reta1 = float(input('Informe a primeira reta: '))
Reta2 = float(input('Informe a segunda reta: '))
Reta3 = float(input('Informe a terceira reta: '))

if Reta1 < Reta2 + Reta3 and Reta2 < Reta1 + Reta3 and Reta3 < Reta1 + Reta2:
    print('OS seguimentos podem forma uma reta')
else: 
    ('Não podem formar uma reta')