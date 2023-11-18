#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt

Numero = float(input('Informe um número: '))

Dobro = Numero * 2
print('Dobro = {}'.format(Dobro))

Triplo = Numero * 3
print('Triplo = {}'.format(Triplo))

RaizQ = sqrt(Numero) 
print('Raiz quadrada = {}'.format(RaizQ))

