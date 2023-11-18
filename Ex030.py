#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
Numero = int(input('Informe um nnúmero inteiro: '))

Calc = Numero % 2
if Calc == 0:
    print('É par!')
else: 
    print('É impar')
    