#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc 
NumeroR = float(input('Informe um número real: '))

PorcaoInt = trunc(NumeroR)

print('Porção inteira = {}'.format(PorcaoInt))
