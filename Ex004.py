#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
Entrada = input('Informe alguma coisa: ')

print('O tipo primitivo é ', type(Entrada))
print('Só tem espaços? ', Entrada.isspace())
print('É um número? ', Entrada.isnumeric())
print('É alfabetico? ', Entrada.isalpha())
print('É alfanúmerico ', Entrada.isalnum())
print('Está maiuscula? ', Entrada.isupper())
print('Está minuscula? ', Entrada.islower())
print('Está capitalizada? ', Entrada.istitle())

