#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
Ano = int(float('Informe o número que quer analizar: '))

if Ano % 4 and Ano % 100 != 0 or Ano % 400 == 0: 
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')